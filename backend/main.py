from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from pydantic import BaseModel
import json
import uuid
import os
import shutil

from backend.langgraph_backend import workflow, checkpointer
import backend.rag_utils as rag_utils
from langchain_core.messages import HumanMessage, AIMessage

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    thread_id: str
    persona: str = "You are a helpful AI assistant."

@app.get("/")
def get_index():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(content=html)

@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    config = {"configurable": {"thread_id": req.thread_id, "persona": req.persona}}
    
    def event_generator():
        try:
            for msg, metadata in workflow.stream(
                {"messages": [HumanMessage(content=req.message)]}, 
                config=config,
                stream_mode="messages"
            ):
                if metadata.get("langgraph_node") == "agent":
                    if isinstance(msg, AIMessage) and msg.content:
                        content_str = ""
                        if isinstance(msg.content, list):
                            for item in msg.content:
                                if isinstance(item, dict) and "text" in item:
                                    content_str += item["text"]
                                elif isinstance(item, str):
                                    content_str += item
                        else:
                            content_str = str(msg.content)
                        
                        if content_str:
                            yield f"data: {json.dumps({'content': content_str})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.get("/history")
async def get_history():
    import sqlite3
    try:
        conn = sqlite3.connect("chats.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT thread_id FROM checkpoints ORDER BY checkpoint_id DESC")
        threads = [{"thread_id": row[0]} for row in cursor.fetchall()]
        conn.close()
        return {"history": threads}
    except Exception as e:
        return {"error": str(e), "history": []}

@app.get("/history/{thread_id}")
async def get_thread_history(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}
    tuple_data = checkpointer.get_tuple(config)
    if not tuple_data or "channel_values" not in tuple_data.checkpoint or "messages" not in tuple_data.checkpoint["channel_values"]:
        return {"messages": []}
    
    messages = tuple_data.checkpoint["channel_values"]["messages"]
    result = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            result.append({"role": "user", "content": msg.content})
        elif isinstance(msg, AIMessage):
            if isinstance(msg.content, list):
                content_str = ""
                for item in msg.content:
                    if isinstance(item, dict) and "text" in item:
                        content_str += item["text"]
                    elif isinstance(item, str):
                        content_str += item
                result.append({"role": "assistant", "content": content_str})
            else:
                result.append({"role": "assistant", "content": str(msg.content)})
    return {"messages": result}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Create a temporary directory if it doesn't exist
        os.makedirs("temp_uploads", exist_ok=True)
        file_path = os.path.join("temp_uploads", file.filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Ingest the document
        num_splits = rag_utils.ingest_document(file_path)
        
        return JSONResponse(content={"message": f"Successfully processed {file.filename} into {num_splits} chunks."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
