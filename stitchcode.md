<!-- Design System -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Nexa AI - New Chat</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "inverse-on-surface": "#2f3133",
                        "tertiary-container": "#b2b7be",
                        "outline-variant": "#524534",
                        "on-tertiary-fixed": "#171c21",
                        "on-secondary-fixed": "#251a00",
                        "on-surface": "#e2e2e5",
                        "surface-tint": "#ffb955",
                        "on-primary": "#452b00",
                        "secondary-fixed-dim": "#edc157",
                        "surface-container": "#1e2022",
                        "surface-container-low": "#1a1c1e",
                        "secondary": "#edc157",
                        "background": "#111416",
                        "tertiary-fixed": "#dee3ea",
                        "on-error": "#690005",
                        "on-primary-fixed-variant": "#633f00",
                        "primary": "#ffc880",
                        "on-error-container": "#ffdad6",
                        "error": "#ffb4ab",
                        "primary-fixed": "#ffddb4",
                        "tertiary-fixed-dim": "#c2c7ce",
                        "tertiary": "#ced2d9",
                        "surface-container-high": "#282a2c",
                        "on-tertiary-container": "#43484e",
                        "primary-fixed-dim": "#ffb955",
                        "secondary-container": "#906d00",
                        "on-surface-variant": "#d7c3ae",
                        "surface-container-highest": "#333537",
                        "outline": "#9f8e7a",
                        "inverse-surface": "#e2e2e5",
                        "on-secondary-fixed-variant": "#5b4300",
                        "on-secondary-container": "#fff7ee",
                        "inverse-primary": "#835500",
                        "surface-variant": "#333537",
                        "primary-container": "#f5a623",
                        "surface": "#111416",
                        "error-container": "#93000a",
                        "surface-container-lowest": "#0c0e10",
                        "on-tertiary": "#2c3136",
                        "on-primary-fixed": "#291800",
                        "on-background": "#e2e2e5",
                        "on-primary-container": "#644000",
                        "surface-bright": "#37393c",
                        "on-secondary": "#3f2e00",
                        "surface-dim": "#111416",
                        "on-tertiary-fixed-variant": "#42474d",
                        "secondary-fixed": "#ffdf9b"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "section-margin": "4rem",
                        "container-padding": "2rem",
                        "sidebar-width": "280px",
                        "element-gap": "1rem"
                    },
                    "fontFamily": {
                        "body-lg": ["Plus Jakarta Sans"],
                        "display-lg-mobile": ["Plus Jakarta Sans"],
                        "display-lg": ["Plus Jakarta Sans"],
                        "label-sm": ["Plus Jakarta Sans"],
                        "headline-md": ["Plus Jakarta Sans"],
                        "body-md": ["Plus Jakarta Sans"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                        "display-lg-mobile": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "label-sm": ["13px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                        "headline-md": ["24px", { "lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
                        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }]
                    }
                }
            }
        }
    </script>
<style>
        body {
            background-color: #080A0C;
            color: #e2e2e5;
        }
        .glow-border:hover {
            border-color: #F5A623;
            box-shadow: 0 0 8px 2px rgba(245, 166, 35, 0.2);
        }
        .bg-layer-1 { background-color: #080A0C; }
        .bg-layer-2 { background-color: #0D1013; }
        .bg-layer-3 { background-color: #161B20; }
        .border-base { border-color: #272D33; }
        .bg-gradient-card {
            background: linear-gradient(180deg, #161B20 0%, #111519 100%);
        }
    </style>
</head>
<body class="antialiased min-h-screen flex overflow-hidden">
<!-- SideNavBar -->
<aside class="fixed left-0 top-0 h-screen w-sidebar-width bg-surface-container dark:bg-surface-container border-r border-outline-variant dark:border-outline-variant shadow-none hidden md:flex flex-col h-full p-element-gap z-20">
<!-- Brand/Logo -->
<div class="mb-8 mt-2 px-2">
<h1 class="font-display-lg text-display-lg text-primary dark:text-primary tracking-tight">Nexa AI</h1>
<p class="font-label-sm text-label-sm text-on-surface-variant mt-1">Premium Concierge</p>
</div>
<!-- CTA Button -->
<button class="w-full bg-primary-container text-on-primary-container font-label-sm text-label-sm py-3 px-4 rounded-xl flex items-center justify-center gap-2 mb-8 hover:brightness-110 transition-all border-t border-[#ffdf9b]/30">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">add</span>
            New Chat
        </button>
<!-- Navigation Tabs -->
<nav class="flex-1 overflow-y-auto space-y-2 pr-2">
<div class="px-2 mb-2 font-label-sm text-label-sm text-on-surface-variant opacity-70 uppercase tracking-wider">History</div>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-primary font-bold border-r-2 border-primary bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined">history</span>
<span class="font-body-md text-body-md truncate">Today</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined">calendar_today</span>
<span class="font-body-md text-body-md truncate">Yesterday</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-body-md text-body-md truncate">Archive</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform mt-8" href="#">
<span class="material-symbols-outlined">settings</span>
<span class="font-body-md text-body-md truncate">Settings</span>
</a>
</nav>
<!-- Footer Profile -->
<div class="mt-auto pt-4 border-t border-outline-variant/30 px-2">
<a class="flex items-center gap-3 px-2 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200" href="#">
<div class="w-8 h-8 rounded-full bg-primary-container/20 flex items-center justify-center text-primary">
<span class="material-symbols-outlined">person</span>
</div>
<span class="font-body-md text-body-md truncate">Alex Mercer</span>
</a>
</div>
</aside>
<!-- Main Content Area -->
<div class="flex-1 flex flex-col md:ml-sidebar-width min-h-screen bg-layer-1">
<!-- TopNavBar -->
<header class="docked full-width top-0 bg-background/80 dark:bg-background/80 backdrop-blur-md border-b border-outline-variant dark:border-outline-variant shadow-sm flex justify-between items-center h-16 px-container-padding z-10">
<!-- Mobile Menu Toggle (Visible only on small screens) -->
<button class="md:hidden text-on-surface-variant hover:text-primary transition-all p-2 rounded-lg hover:bg-surface-container-high">
<span class="material-symbols-outlined">menu</span>
</button>
<!-- Product Name / Context -->
<div class="font-headline-md text-headline-md text-on-surface dark:text-on-surface truncate md:hidden">
                Nexa AI • Smart
            </div>
<!-- Top Nav Links (Desktop) -->
<nav class="hidden md:flex items-center gap-6 h-full">
<div class="font-headline-md text-headline-md text-on-surface dark:text-on-surface mr-6">Nexa AI • Smart</div>
<a class="text-primary font-bold border-b-2 border-primary pb-1 h-full flex items-center mt-1 active:opacity-80" href="#">
<span class="font-body-md text-body-md">Models</span>
</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-all h-full flex items-center mt-1 active:opacity-80" href="#">
<span class="font-body-md text-body-md">Settings</span>
</a>
</nav>
<!-- Trailing Actions -->
<div class="flex items-center gap-2">
<button class="p-2 text-on-surface-variant hover:text-primary transition-all rounded-lg hover:bg-surface-container-high" title="Favorite">
<span class="material-symbols-outlined">star</span>
</button>
<button class="p-2 text-on-surface-variant hover:text-primary transition-all rounded-lg hover:bg-surface-container-high" title="Share">
<span class="material-symbols-outlined">share</span>
</button>
</div>
</header>
<!-- Main Canvas -->
<main class="flex-1 overflow-y-auto px-4 md:px-container-padding py-section-margin flex flex-col items-center justify-center w-full max-w-5xl mx-auto">
<!-- Welcome Header -->
<div class="text-center mb-16 space-y-6">
<!-- Geometric Logo -->
<div class="w-20 h-20 mx-auto rounded-2xl bg-layer-3 border border-base shadow-sm flex items-center justify-center relative overflow-hidden group glow-border transition-all duration-300 cursor-pointer">
<!-- Subtle inner gradient -->
<div class="absolute inset-0 bg-gradient-to-br from-primary/10 to-transparent opacity-50"></div>
<svg class="relative z-10 text-primary" fill="none" height="40" viewBox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg">
<path d="M10 30V10H16L24 22V10H30V30H24L16 18V30H10Z" fill="currentColor"></path>
</svg>
</div>
<h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface tracking-tight">
                    How can I help you today?
                </h2>
</div>
<!-- Suggestion Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6 w-full max-w-4xl mb-12">
<!-- Card 1 -->
<button class="bg-gradient-card border border-base rounded-[22px] p-6 text-left transition-all duration-300 glow-border group relative overflow-hidden flex flex-col gap-3">
<div class="w-10 h-10 rounded-full bg-layer-2 border border-base flex items-center justify-center text-primary group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined">lightbulb</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md text-on-surface mb-1">Explain something</h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">Break down complex topics into simple, easy-to-understand terms.</p>
</div>
</button>
<!-- Card 2 -->
<button class="bg-gradient-card border border-base rounded-[22px] p-6 text-left transition-all duration-300 glow-border group relative overflow-hidden flex flex-col gap-3">
<div class="w-10 h-10 rounded-full bg-layer-2 border border-base flex items-center justify-center text-primary group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined">edit_document</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md text-on-surface mb-1">Write something</h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">Draft emails, essays, code, or creative stories with precision.</p>
</div>
</button>
<!-- Card 3 -->
<button class="bg-gradient-card border border-base rounded-[22px] p-6 text-left transition-all duration-300 glow-border group relative overflow-hidden flex flex-col gap-3">
<div class="w-10 h-10 rounded-full bg-layer-2 border border-base flex items-center justify-center text-primary group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined">analytics</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md text-on-surface mb-1">Analyze information</h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">Process data, summarize documents, or find patterns in text.</p>
</div>
</button>
<!-- Card 4 -->
<button class="bg-gradient-card border border-base rounded-[22px] p-6 text-left transition-all duration-300 glow-border group relative overflow-hidden flex flex-col gap-3">
<div class="w-10 h-10 rounded-full bg-layer-2 border border-base flex items-center justify-center text-primary group-hover:bg-primary/10 transition-colors">
<span class="material-symbols-outlined">psychology</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md text-on-surface mb-1">Brainstorm ideas</h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">Generate creative concepts, names, or strategies for your project.</p>
</div>
</button>
</div>
<!-- Input Area Placeholder -->
<div class="w-full max-w-4xl mt-auto relative group">
<div class="absolute -inset-0.5 bg-gradient-to-r from-primary/30 to-primary/0 rounded-xl blur opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 transition duration-500"></div>
<div class="relative flex items-center bg-layer-2 border border-base rounded-xl overflow-hidden glow-border p-2">
<button class="p-3 text-on-surface-variant hover:text-primary transition-colors">
<span class="material-symbols-outlined">add_circle</span>
</button>
<input class="flex-1 bg-transparent border-none outline-none focus:ring-0 font-body-md text-body-md text-on-surface placeholder:text-on-surface-variant/50 px-2 py-3" placeholder="Message Nexa AI..." type="text">
<button class="p-3 text-primary bg-primary/10 hover:bg-primary/20 rounded-lg transition-colors ml-2">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">send</span>
</button>
</div>
<p class="text-center font-label-sm text-label-sm text-on-surface-variant/60 mt-4">Nexa AI can make mistakes. Consider verifying important information.</p>
</div>
</main>
</div>
</body></html>

<!-- Welcome - Nexa AI (Obsidian Amber) -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Nexa AI - Chat</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "inverse-on-surface": "#2f3133",
                        "tertiary-container": "#b2b7be",
                        "outline-variant": "#524534",
                        "on-tertiary-fixed": "#171c21",
                        "on-secondary-fixed": "#251a00",
                        "on-surface": "#e2e2e5",
                        "surface-tint": "#ffb955",
                        "on-primary": "#452b00",
                        "secondary-fixed-dim": "#edc157",
                        "surface-container": "#1e2022",
                        "surface-container-low": "#1a1c1e",
                        "secondary": "#edc157",
                        "background": "#111416",
                        "tertiary-fixed": "#dee3ea",
                        "on-error": "#690005",
                        "on-primary-fixed-variant": "#633f00",
                        "primary": "#ffc880",
                        "on-error-container": "#ffdad6",
                        "error": "#ffb4ab",
                        "primary-fixed": "#ffddb4",
                        "tertiary-fixed-dim": "#c2c7ce",
                        "tertiary": "#ced2d9",
                        "surface-container-high": "#282a2c",
                        "on-tertiary-container": "#43484e",
                        "primary-fixed-dim": "#ffb955",
                        "secondary-container": "#906d00",
                        "on-surface-variant": "#d7c3ae",
                        "surface-container-highest": "#333537",
                        "outline": "#9f8e7a",
                        "inverse-surface": "#e2e2e5",
                        "on-secondary-fixed-variant": "#5b4300",
                        "on-secondary-container": "#fff7ee",
                        "inverse-primary": "#835500",
                        "surface-variant": "#333537",
                        "primary-container": "#f5a623",
                        "surface": "#111416",
                        "error-container": "#93000a",
                        "surface-container-lowest": "#0c0e10",
                        "on-tertiary": "#2c3136",
                        "on-primary-fixed": "#291800",
                        "on-background": "#e2e2e5",
                        "on-primary-container": "#644000",
                        "surface-bright": "#37393c",
                        "on-secondary": "#3f2e00",
                        "surface-dim": "#111416",
                        "on-tertiary-fixed-variant": "#42474d",
                        "secondary-fixed": "#ffdf9b"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "section-margin": "4rem",
                        "container-padding": "2rem",
                        "sidebar-width": "280px",
                        "element-gap": "1rem"
                    },
                    "fontFamily": {
                        "body-lg": ["Plus Jakarta Sans"],
                        "display-lg-mobile": ["Plus Jakarta Sans"],
                        "display-lg": ["Plus Jakarta Sans"],
                        "label-sm": ["Plus Jakarta Sans"],
                        "headline-md": ["Plus Jakarta Sans"],
                        "body-md": ["Plus Jakarta Sans"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                        "display-lg-mobile": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "label-sm": ["13px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                        "headline-md": ["24px", { "lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
                        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }]
                    }
                }
            }
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .code-keyword { color: #f5a623; }
        .code-string { color: #a3defe; }
        .code-comment { color: #6b7280; }
        .code-function { color: #818cf8; }
        .code-number { color: #34d399; }
    </style>
</head>
<body class="bg-background text-on-background font-body-md text-body-md min-h-screen flex overflow-hidden">
<!-- SideNavBar -->
<nav class="hidden md:flex bg-surface-container dark:bg-surface-container fixed left-0 top-0 h-screen w-sidebar-width border-r border-outline-variant dark:border-outline-variant shadow-none flex-col p-element-gap z-20">
<div class="mb-8 px-2 mt-4 flex items-center justify-between">
<span class="font-display-lg text-headline-md text-primary dark:text-primary tracking-tight">Nexa AI</span>
</div>
<button class="mb-6 w-full py-3 px-4 rounded-lg bg-primary-container text-[#080A0C] font-label-sm text-label-sm border-t border-[#f8e0a8] flex items-center justify-center gap-2 transition-transform active:scale-95">
<span class="material-symbols-outlined" data-icon="add">add</span>
            New Chat
        </button>
<div class="flex-1 overflow-y-auto">
<div class="mb-4">
<span class="px-3 text-xs font-semibold text-outline tracking-wider uppercase mb-2 block">History</span>
<ul class="space-y-1">
<li>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-primary font-bold border-r-2 border-primary bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined text-sm" data-icon="history">history</span>
<span class="truncate">Python Web Scraper</span>
</a>
</li>
<li>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined text-sm" data-icon="history">history</span>
<span class="truncate">Today</span>
</a>
</li>
<li>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined text-sm" data-icon="calendar_today">calendar_today</span>
<span class="truncate">Yesterday</span>
</a>
</li>
<li>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined text-sm" data-icon="inventory_2">inventory_2</span>
<span class="truncate">Archive</span>
</a>
</li>
</ul>
</div>
<div class="mt-8">
<ul class="space-y-1">
<li>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined text-sm" data-icon="settings">settings</span>
<span>Settings</span>
</a>
</li>
</ul>
</div>
</div>
<div class="mt-auto pt-4 border-t border-outline-variant/30 flex items-center gap-3 px-2">
<img alt="Alex Mercer" class="w-8 h-8 rounded-full object-cover border border-outline-variant" data-alt="A small, professional headshot avatar of a user in a dark mode UI. High quality, clear lighting, premium aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuA0x7UBeGiw0HlE4oiHDUW35fH44jbsF6zDdbPkECqRGZ-Oo-_gNOYsyBeM81HoPMtdWjrBA8PWwTrpttfteFu69v6mAyqeNhVC1W3nxnSeMBawmV3PxrpluZvnGvbShZnxYiygFju3VkJBfBDKWQQ8Snn6gw9ojlFCgTW2emTvmjmrApTGzwqqcglxYZNeGcyvdlr-f1K9A86hlPQiCZjjjY4tccRKgF-4Ge2l5lY2JkItMs5td4fO">
<span class="font-label-sm text-label-sm text-on-surface truncate">Alex Mercer</span>
</div>
</nav>
<!-- Main Content Area -->
<main class="flex-1 flex flex-col md:ml-sidebar-width h-screen bg-[#080A0C]">
<!-- TopNavBar -->
<header class="bg-background/80 dark:bg-background/80 backdrop-blur-md flex justify-between items-center h-16 px-container-padding border-b border-outline-variant dark:border-outline-variant shadow-sm docked full-width top-0 z-10 sticky">
<div class="flex items-center gap-4">
<button class="md:hidden text-on-surface">
<span class="material-symbols-outlined" data-icon="menu">menu</span>
</button>
<div class="flex items-center gap-2 bg-[#161B20] border border-[#272D33] rounded-lg px-3 py-1.5 cursor-pointer hover:border-outline-variant transition-colors">
<span class="font-headline-md text-body-md text-on-surface dark:text-on-surface font-semibold">Nexa AI • Pro</span>
<span class="material-symbols-outlined text-sm text-on-surface-variant" data-icon="expand_more">expand_more</span>
</div>
</div>
<div class="flex items-center gap-4">
<nav class="hidden lg:flex gap-6 mr-4">
<a class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80" href="#">Models</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80" href="#">Settings</a>
</nav>
<div class="flex items-center gap-3">
<button class="text-on-surface-variant hover:text-primary transition-colors p-2 rounded-full hover:bg-surface-container">
<span class="material-symbols-outlined" data-icon="star">star</span>
</button>
<button class="text-on-surface-variant hover:text-primary transition-colors p-2 rounded-full hover:bg-surface-container">
<span class="material-symbols-outlined" data-icon="share">share</span>
</button>
</div>
</div>
</header>
<!-- Chat Canvas -->
<div class="flex-1 overflow-y-auto px-4 py-8 md:px-8 scroll-smooth" id="chat-container">
<div class="max-w-[1000px] mx-auto space-y-8">
<!-- User Message -->
<div class="flex justify-end mb-6">
<div class="bg-[#161B20] border-l-2 border-primary text-on-surface px-5 py-4 rounded-2xl rounded-tr-sm max-w-[85%] shadow-sm">
<p class="font-body-md text-body-md">Can you provide a Python script for a simple quantum circuit using Qiskit? Include comments explaining the steps.</p>
</div>
</div>
<!-- AI Response -->
<div class="flex justify-start mb-6 gap-4">
<div class="flex-shrink-0 mt-1">
<div class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center border border-primary/30">
<span class="material-symbols-outlined text-primary text-sm" data-icon="memory">memory</span>
</div>
</div>
<div class="bg-[#111519] border border-[#272D33] text-on-surface px-5 py-5 rounded-2xl rounded-tl-sm w-full max-w-[90%]">
<p class="font-body-md text-body-md mb-4">Certainly. Here is a basic Python script using Qiskit to create and execute a simple quantum circuit that creates a Bell state (entangled pair).</p>
<!-- Code Block -->
<div class="bg-[#080A0C] rounded-xl border border-[#272D33] overflow-hidden my-4 group">
<div class="flex justify-between items-center px-4 py-2 bg-[#161B20] border-b border-[#272D33]">
<span class="font-label-sm text-label-sm text-on-surface-variant uppercase">Python</span>
<button class="text-on-surface-variant hover:text-primary transition-colors flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-sm" data-icon="content_copy">content_copy</span>
<span class="text-xs font-semibold">Copy</span>
</button>
</div>
<div class="p-4 overflow-x-auto flex text-sm font-mono leading-relaxed">
<div class="text-right pr-4 border-r border-[#272D33] text-outline-variant select-none mr-4 space-y-1">
<div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div><div>9</div><div>10</div><div>11</div><div>12</div><div>13</div><div>14</div><div>15</div><div>16</div>
</div>
<div class="space-y-1 text-on-surface">
<div><span class="code-keyword">from</span> qiskit <span class="code-keyword">import</span> QuantumCircuit, transpile</div>
<div><span class="code-keyword">from</span> qiskit_aer <span class="code-keyword">import</span> AerSimulator</div>
<div><span class="code-keyword">from</span> qiskit.visualization <span class="code-keyword">import</span> plot_histogram</div>
<div class="h-5"></div>
<div><span class="code-comment"># Create a Quantum Circuit acting on the q register (2 qubits, 2 classical bits)</span></div>
<div>circuit = QuantumCircuit(<span class="code-number">2</span>, <span class="code-number">2</span>)</div>
<div class="h-5"></div>
<div><span class="code-comment"># Add a H gate on qubit 0, putting this qubit in superposition.</span></div>
<div>circuit.h(<span class="code-number">0</span>)</div>
<div class="h-5"></div>
<div><span class="code-comment"># Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting them in a Bell state.</span></div>
<div>circuit.cx(<span class="code-number">0</span>, <span class="code-number">1</span>)</div>
<div class="h-5"></div>
<div><span class="code-comment"># Map the quantum measurement to the classical bits</span></div>
<div>circuit.measure([<span class="code-number">0</span>,<span class="code-number">1</span>], [<span class="code-number">0</span>,<span class="code-number">1</span>])</div>
<div class="h-5"></div>
<div><span class="code-keyword">print</span>(<span class="code-string">"Circuit created successfully."</span>)</div>
</div>
</div>
</div>
<p class="font-body-md text-body-md mt-4">This script sets up a 2-qubit circuit, applies a Hadamard gate to the first qubit to create superposition, and then a CNOT gate to entangle them. Finally, it measures the output.</p>
<div class="flex gap-2 mt-6">
<span class="bg-primary/10 text-primary font-label-sm text-[10px] px-2 py-1 rounded-full uppercase tracking-wider border border-primary/20">Qiskit</span>
<span class="bg-primary/10 text-primary font-label-sm text-[10px] px-2 py-1 rounded-full uppercase tracking-wider border border-primary/20">Quantum Computing</span>
</div>
</div>
</div>
</div>
</div>
<!-- Input Area -->
<div class="px-4 py-6 md:px-8 bg-gradient-to-t from-[#080A0C] via-[#080A0C]/90 to-transparent">
<div class="max-w-[1000px] mx-auto">
<div class="relative bg-[#0D1013] border border-[#272D33] rounded-2xl shadow-sm focus-within:border-primary/50 focus-within:shadow-[0_0_15px_rgba(245,166,35,0.1)] transition-all duration-300">
<textarea class="w-full bg-transparent text-on-surface font-body-md text-body-md p-4 pr-14 border-none focus:ring-0 resize-none max-h-32 placeholder-outline" placeholder="Ask Nexa AI a question..." rows="1"></textarea>
<button class="absolute right-3 bottom-3 p-2 bg-primary-container text-[#080A0C] rounded-lg hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined text-sm" data-icon="send">send</span>
</button>
</div>
<div class="text-center mt-3">
<span class="font-label-sm text-[11px] text-outline-variant">Nexa AI can make mistakes. Consider verifying important information.</span>
</div>
</div>
</div>
</main>
</body></html>

<!-- Code Assistant - Nexa AI (Obsidian Amber) -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Nexa AI - Chat</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<style>
        .material-symbols-outlined {
            font-family: 'Material Symbols Outlined';
            font-weight: normal;
            font-style: normal;
            font-size: 24px;
            display: inline-block;
            line-height: 1;
            text-transform: none;
            letter-spacing: normal;
            word-wrap: normal;
            white-space: nowrap;
            direction: ltr;
        }
        
        /* Inner glow effect for amber accents */
        .glow-amber-border {
            box-shadow: inset 0 1px 0 0 rgba(245, 166, 35, 0.3);
        }
        
        /* Subtle scrollbar for chat */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #272D33;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #333537;
        }
    </style>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "inverse-on-surface": "#2f3133",
                        "tertiary-container": "#b2b7be",
                        "outline-variant": "#524534",
                        "on-tertiary-fixed": "#171c21",
                        "on-secondary-fixed": "#251a00",
                        "on-surface": "#e2e2e5",
                        "surface-tint": "#ffb955",
                        "on-primary": "#452b00",
                        "secondary-fixed-dim": "#edc157",
                        "surface-container": "#1e2022",
                        "surface-container-low": "#1a1c1e",
                        "secondary": "#edc157",
                        "background": "#111416",
                        "tertiary-fixed": "#dee3ea",
                        "on-error": "#690005",
                        "on-primary-fixed-variant": "#633f00",
                        "primary": "#ffc880",
                        "on-error-container": "#ffdad6",
                        "error": "#ffb4ab",
                        "primary-fixed": "#ffddb4",
                        "tertiary-fixed-dim": "#c2c7ce",
                        "tertiary": "#ced2d9",
                        "surface-container-high": "#282a2c",
                        "on-tertiary-container": "#43484e",
                        "primary-fixed-dim": "#ffb955",
                        "secondary-container": "#906d00",
                        "on-surface-variant": "#d7c3ae",
                        "surface-container-highest": "#333537",
                        "outline": "#9f8e7a",
                        "inverse-surface": "#e2e2e5",
                        "on-secondary-fixed-variant": "#5b4300",
                        "on-secondary-container": "#fff7ee",
                        "inverse-primary": "#835500",
                        "surface-variant": "#333537",
                        "primary-container": "#f5a623",
                        "surface": "#111416",
                        "error-container": "#93000a",
                        "surface-container-lowest": "#0c0e10",
                        "on-tertiary": "#2c3136",
                        "on-primary-fixed": "#291800",
                        "on-background": "#e2e2e5",
                        "on-primary-container": "#644000",
                        "surface-bright": "#37393c",
                        "on-secondary": "#3f2e00",
                        "surface-dim": "#111416",
                        "on-tertiary-fixed-variant": "#42474d",
                        "secondary-fixed": "#ffdf9b"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "section-margin": "4rem",
                        "container-padding": "2rem",
                        "sidebar-width": "280px",
                        "element-gap": "1rem"
                    },
                    "fontFamily": {
                        "body-lg": ["Plus Jakarta Sans"],
                        "display-lg-mobile": ["Plus Jakarta Sans"],
                        "display-lg": ["Plus Jakarta Sans"],
                        "label-sm": ["Plus Jakarta Sans"],
                        "headline-md": ["Plus Jakarta Sans"],
                        "body-md": ["Plus Jakarta Sans"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                        "display-lg-mobile": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "label-sm": ["13px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                        "headline-md": ["24px", { "lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
                        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }]
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-[#080A0C] text-on-surface font-body-md min-h-screen overflow-hidden flex">
<!-- SideNavBar -->
<nav class="hidden md:flex flex-col h-screen w-sidebar-width fixed left-0 top-0 bg-[#0D1013] border-r border-[#272D33] shadow-none z-20">
<div class="p-element-gap flex flex-col h-full">
<!-- Brand -->
<div class="mb-8 px-4 flex items-center gap-3">
<div class="w-10 h-10 rounded-xl bg-gradient-to-br from-[#161B20] to-[#111519] border border-[#272D33] flex items-center justify-center glow-amber-border">
<span class="font-display-lg text-[24px] text-primary tracking-tight leading-none">N</span>
</div>
<div>
<h1 class="font-headline-md text-[18px] text-primary tracking-tight leading-none">Nexa AI</h1>
<p class="font-label-sm text-label-sm text-on-surface-variant mt-1">Premium Concierge</p>
</div>
</div>
<!-- CTA -->
<button class="mb-8 mx-4 bg-primary-container text-[#080A0C] hover:bg-primary-fixed transition-colors duration-200 rounded-lg py-3 px-4 font-label-sm flex items-center justify-center gap-2 glow-amber-border active:scale-95 transition-transform">
<span class="material-symbols-outlined text-[18px]">add</span>
                New Chat
            </button>
<!-- Navigation -->
<div class="flex-1 overflow-y-auto">
<ul class="space-y-1">
<li>
<a class="flex items-center gap-3 px-4 py-3 text-primary font-bold border-r-2 border-primary bg-surface-container-high transition-colors duration-200" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">history</span>
<span class="font-label-sm text-label-sm">Today</span>
</a>
</li>
<li>
<a class="flex items-center gap-3 px-4 py-3 text-on-surface-variant font-medium hover:bg-surface-container-high hover:text-on-surface transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined">calendar_today</span>
<span class="font-label-sm text-label-sm">Yesterday</span>
</a>
</li>
<li>
<a class="flex items-center gap-3 px-4 py-3 text-on-surface-variant font-medium hover:bg-surface-container-high hover:text-on-surface transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-label-sm text-label-sm">Archive</span>
</a>
</li>
</ul>
<div class="mt-8 px-4 font-label-sm text-xs text-outline mb-2">TOOLS</div>
<ul class="space-y-1">
<li>
<a class="flex items-center gap-3 px-4 py-3 text-on-surface-variant font-medium hover:bg-surface-container-high hover:text-on-surface transition-colors duration-200 active:scale-95 transition-transform" href="#">
<span class="material-symbols-outlined">settings</span>
<span class="font-label-sm text-label-sm">Settings</span>
</a>
</li>
</ul>
</div>
<!-- Footer -->
<div class="mt-auto pt-4 border-t border-[#272D33]">
<button class="w-full flex items-center gap-3 px-4 py-3 hover:bg-surface-container-high rounded-lg transition-colors duration-200">
<img alt="Alex Mercer" class="w-8 h-8 rounded-full border border-[#272D33] object-cover" data-alt="A small, circular avatar portrait of a professional individual in a minimalist studio setting, high quality, soft studio lighting, sharp focus, neutral dark background to fit a dark UI theme." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCqsiKUZ7QoanbYXGQcIuvu0fOX3Sv6W4cW17_QEQzwQN4Mv02jhjTIPcVMfH6bHfI95aw8Y5K4KH11w_knChSTu6VDKLgcBoTO0uQW0JQlO8J706_qQP-0A1AD0oPNMxyD7Gq2MoyY3vjjk82I8jsrfT0FsvBKZmsy233Oz0WRwqiyiNPiWdnxl4v8XNIILPqxAl0WZbLF5US5e60bOCmAZpqVHqzpcnncAe5Q9MUnEhNlp7jcoOe-">
<span class="font-label-sm text-label-sm text-on-surface flex-1 text-left">Alex Mercer</span>
<span class="material-symbols-outlined text-outline">more_horiz</span>
</button>
</div>
</div>
</nav>
<!-- Main Content Area -->
<div class="flex-1 flex flex-col md:ml-sidebar-width h-screen relative">
<!-- TopNavBar -->
<header class="h-16 px-container-padding flex justify-between items-center bg-[#080A0C]/80 backdrop-blur-md border-b border-[#272D33] shadow-sm z-10 w-full absolute top-0 left-0">
<div class="flex items-center gap-6">
<!-- Mobile Menu Trigger -->
<button class="md:hidden text-on-surface-variant hover:text-primary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<div class="font-headline-md text-headline-md text-on-surface hidden md:block">Nexa AI • Smart</div>
</div>
<nav class="hidden md:flex items-center gap-6">
<a class="text-primary font-bold border-b-2 border-primary pb-1" href="#">Models</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80" href="#">Settings</a>
</nav>
<div class="flex items-center gap-4">
<button class="text-on-surface-variant hover:text-primary transition-colors" title="Favorite">
<span class="material-symbols-outlined">star</span>
</button>
<button class="text-on-surface-variant hover:text-primary transition-colors" title="Share">
<span class="material-symbols-outlined">share</span>
</button>
<img alt="Alex Mercer" class="w-8 h-8 rounded-full border border-[#272D33] object-cover md:hidden" data-alt="A small, circular avatar portrait of a professional individual in a minimalist studio setting, high quality, soft studio lighting, sharp focus, neutral dark background to fit a dark UI theme." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBVvK6AzqAeXRGHx8V5ipP1xnK-IzhlThZW4IOMKWpVCPIBRj23pcN0-3X3z2_XBxdTSx6YWbQVoBqNjpjhNOm9EInkiwaOfM51w9Xzn_FPcso5Re8AQQyFwpqXLrPeu89C6LIIj6qQpM6A6f0eLkxV-xPbzcqawUAvm5D9fgB18YHFkbEbTUGa99rdIkah-CoJ77te0sXcKfHtacYWCibkp-3mzFpNupJ19qTG-IlLUNZ4oroPuyc4">
</div>
</header>
<!-- Chat Canvas -->
<main class="flex-1 overflow-y-auto pt-24 pb-32 px-4 md:px-container-padding flex justify-center w-full">
<div class="w-full max-w-[1200px] flex flex-col gap-8">
<!-- Date Divider -->
<div class="flex justify-center my-4">
<span class="px-3 py-1 bg-[#161B20] border border-[#272D33] rounded-full font-label-sm text-xs text-outline">TODAY</span>
</div>
<!-- User Message -->
<div class="flex justify-end w-full">
<div class="max-w-[80%] md:max-w-[70%]">
<div class="bg-[#161B20] text-on-surface font-body-md text-body-md rounded-2xl rounded-tr-sm p-4 border border-[#272D33] relative overflow-hidden">
<!-- Subtle amber accent on left vertical edge -->
<div class="absolute left-0 top-0 bottom-0 w-1 bg-primary-container/50"></div>
<p>Can you explain how quantum computing works in simple terms?</p>
</div>
</div>
</div>
<!-- AI Response -->
<div class="flex justify-start w-full group">
<!-- AI Avatar -->
<div class="w-8 h-8 rounded-xl bg-gradient-to-br from-[#161B20] to-[#111519] border border-[#272D33] flex items-center justify-center glow-amber-border mr-4 mt-1 flex-shrink-0 hidden md:flex">
<span class="font-display-lg text-[16px] text-primary tracking-tight leading-none">N</span>
</div>
<div class="max-w-[90%] md:max-w-[80%]">
<div class="bg-[#111519] text-on-surface font-body-md text-body-md rounded-2xl rounded-tl-sm p-5 border border-[#272D33]">
<p class="mb-5">Imagine you are trying to find the exit to a maze. A classical computer (like the one you're using right now) would trace every single path one by one until it finds the way out. It’s methodical, but if the maze is massive, it takes a very long time.</p>
<p class="mb-6">A <strong class="text-primary-container">quantum computer</strong>, on the other hand, floods the entire maze with water simultaneously. It explores all possible paths at exactly the same time, finding the exit almost instantly. It achieves this using a completely different set of rules based on quantum mechanics.</p>
<h3 class="font-headline-md text-[20px] text-primary-container mb-4 flex items-center gap-2">
<span class="material-symbols-outlined text-[20px]">science</span>
                                Key Principles
                            </h3>
<div class="space-y-4 mb-6">
<!-- Principle 1 -->
<div class="bg-[#161B20] p-4 rounded-xl border border-[#272D33] hover:border-primary/30 transition-colors">
<h4 class="font-bold text-on-surface mb-1 flex items-center gap-2">
<div class="w-2 h-2 rounded-full bg-primary-container"></div>
                                        Superposition
                                    </h4>
<p class="text-on-surface-variant text-sm">Classical bits are either a 0 or a 1 (like a coin on heads or tails). Quantum bits (qubits) can be a 0, a 1, or <em>both at the same time</em> (like a coin spinning in the air). This allows them to hold vastly more information.</p>
</div>
<!-- Principle 2 -->
<div class="bg-[#161B20] p-4 rounded-xl border border-[#272D33] hover:border-primary/30 transition-colors">
<h4 class="font-bold text-on-surface mb-1 flex items-center gap-2">
<div class="w-2 h-2 rounded-full bg-primary-container"></div>
                                        Entanglement
                                    </h4>
<p class="text-on-surface-variant text-sm">Qubits can be linked together in such a way that the state of one instantly determines the state of another, no matter how far apart they are. If one spinning coin stops on heads, the entangled coin instantly stops on tails.</p>
</div>
<!-- Principle 3 -->
<div class="bg-[#161B20] p-4 rounded-xl border border-[#272D33] hover:border-primary/30 transition-colors">
<h4 class="font-bold text-on-surface mb-1 flex items-center gap-2">
<div class="w-2 h-2 rounded-full bg-primary-container"></div>
                                        Interference
                                    </h4>
<p class="text-on-surface-variant text-sm">Quantum computers use the wave-like properties of qubits to cancel out wrong answers (destructive interference) and amplify the right ones (constructive interference), quickly filtering down to the correct solution.</p>
</div>
</div>
<p class="text-on-surface-variant">Because of these properties, quantum computers have the potential to solve certain problems—like simulating new molecules for medicine, optimizing complex logistics, or breaking advanced encryption—in seconds, whereas a classical supercomputer might take thousands of years.</p>
</div>
<!-- Message Actions -->
<div class="flex items-center gap-2 mt-2 ml-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
<button class="p-1.5 text-on-surface-variant hover:text-primary hover:bg-[#161B20] rounded-md transition-colors" title="Copy">
<span class="material-symbols-outlined text-[18px]">content_copy</span>
</button>
<button class="p-1.5 text-on-surface-variant hover:text-primary hover:bg-[#161B20] rounded-md transition-colors" title="Good response">
<span class="material-symbols-outlined text-[18px]">thumb_up</span>
</button>
<button class="p-1.5 text-on-surface-variant hover:text-error hover:bg-[#161B20] rounded-md transition-colors" title="Bad response">
<span class="material-symbols-outlined text-[18px]">thumb_down</span>
</button>
<div class="w-px h-4 bg-[#272D33] mx-1"></div>
<button class="p-1.5 text-on-surface-variant hover:text-primary hover:bg-[#161B20] rounded-md transition-colors flex items-center gap-1" title="Regenerate">
<span class="material-symbols-outlined text-[18px]">refresh</span>
<span class="font-label-sm text-xs">Regenerate</span>
</button>
</div>
</div>
</div>
</div>
</main>
<!-- Input Area (Fixed at bottom) -->
<div class="absolute bottom-0 left-0 w-full bg-gradient-to-t from-[#080A0C] via-[#080A0C] to-transparent pt-10 pb-6 px-4 md:px-container-padding flex justify-center z-10">
<div class="w-full max-w-[900px] relative">
<div class="bg-[#0D1013] border border-[#272D33] rounded-2xl p-2 flex flex-col focus-within:border-primary/50 focus-within:shadow-[0_0_15px_rgba(245,166,35,0.1)] transition-all duration-300">
<textarea class="w-full bg-transparent text-on-surface border-none focus:ring-0 resize-none p-3 font-body-md min-h-[60px] max-h-[200px]" placeholder="Ask anything..." rows="1"></textarea>
<div class="flex justify-between items-center px-2 pb-1">
<div class="flex items-center gap-1">
<button class="p-2 text-on-surface-variant hover:text-primary rounded-lg hover:bg-[#161B20] transition-colors">
<span class="material-symbols-outlined">attach_file</span>
</button>
<button class="p-2 text-on-surface-variant hover:text-primary rounded-lg hover:bg-[#161B20] transition-colors">
<span class="material-symbols-outlined">mic</span>
</button>
</div>
<button class="bg-primary-container text-[#080A0C] p-2 rounded-xl hover:bg-primary-fixed transition-colors flex items-center justify-center glow-amber-border">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">arrow_upward</span>
</button>
</div>
</div>
<div class="text-center mt-3 font-label-sm text-xs text-outline">
                    Nexa AI can make mistakes. Consider verifying important information.
                </div>
</div>
</div>
</div>
</body></html>

<!-- Active Chat - Nexa AI (Obsidian Amber) -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Settings - Nexa AI</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "inverse-on-surface": "#2f3133",
                    "tertiary-container": "#b2b7be",
                    "outline-variant": "#524534",
                    "on-tertiary-fixed": "#171c21",
                    "on-secondary-fixed": "#251a00",
                    "on-surface": "#e2e2e5",
                    "surface-tint": "#ffb955",
                    "on-primary": "#452b00",
                    "secondary-fixed-dim": "#edc157",
                    "surface-container": "#1e2022",
                    "surface-container-low": "#1a1c1e",
                    "secondary": "#edc157",
                    "background": "#111416",
                    "tertiary-fixed": "#dee3ea",
                    "on-error": "#690005",
                    "on-primary-fixed-variant": "#633f00",
                    "primary": "#ffc880",
                    "on-error-container": "#ffdad6",
                    "error": "#ffb4ab",
                    "primary-fixed": "#ffddb4",
                    "tertiary-fixed-dim": "#c2c7ce",
                    "tertiary": "#ced2d9",
                    "surface-container-high": "#282a2c",
                    "on-tertiary-container": "#43484e",
                    "primary-fixed-dim": "#ffb955",
                    "secondary-container": "#906d00",
                    "on-surface-variant": "#d7c3ae",
                    "surface-container-highest": "#333537",
                    "outline": "#9f8e7a",
                    "inverse-surface": "#e2e2e5",
                    "on-secondary-fixed-variant": "#5b4300",
                    "on-secondary-container": "#fff7ee",
                    "inverse-primary": "#835500",
                    "surface-variant": "#333537",
                    "primary-container": "#f5a623",
                    "surface": "#111416",
                    "error-container": "#93000a",
                    "surface-container-lowest": "#0c0e10",
                    "on-tertiary": "#2c3136",
                    "on-primary-fixed": "#291800",
                    "on-background": "#e2e2e5",
                    "on-primary-container": "#644000",
                    "surface-bright": "#37393c",
                    "on-secondary": "#3f2e00",
                    "surface-dim": "#111416",
                    "on-tertiary-fixed-variant": "#42474d",
                    "secondary-fixed": "#ffdf9b"
            },
            "borderRadius": {
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            },
            "spacing": {
                    "section-margin": "4rem",
                    "container-padding": "2rem",
                    "sidebar-width": "280px",
                    "element-gap": "1rem"
            },
            "fontFamily": {
                    "body-lg": ["Plus Jakarta Sans"],
                    "display-lg-mobile": ["Plus Jakarta Sans"],
                    "display-lg": ["Plus Jakarta Sans"],
                    "label-sm": ["Plus Jakarta Sans"],
                    "headline-md": ["Plus Jakarta Sans"],
                    "body-md": ["Plus Jakarta Sans"]
            },
            "fontSize": {
                    "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                    "display-lg-mobile": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "label-sm": ["13px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                    "headline-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
            }
          }
        }
      }
    </script>
<style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #080A0C; /* Base Layer mapping */
        }
        .card-gradient {
            background: linear-gradient(180deg, #161B20 0%, #111519 100%);
        }
        .card-border {
            border: 1px solid #272D33;
        }
        .toggle-checkbox:checked {
            right: 0;
            border-color: #f5a623;
        }
        .toggle-checkbox:checked + .toggle-label {
            background-color: #f5a623;
        }
    </style>
</head>
<body class="text-on-background min-h-screen flex overflow-x-hidden">
<!-- SideNavBar (Desktop Only) -->
<aside class="hidden md:flex flex-col h-full p-element-gap fixed left-0 top-0 w-sidebar-width bg-surface-container border-r border-outline-variant z-20 shadow-none">
<!-- Header -->
<div class="flex items-center gap-4 mb-8 pt-4 px-2">
<div class="w-12 h-12 rounded-full overflow-hidden border border-outline-variant flex-shrink-0">
<img alt="Alex Mercer" class="w-full h-full object-cover" data-alt="A cinematic, high-fashion portrait of a male professional named Alex Mercer, styled in minimalist dark clothing against a pure obsidian black background. The lighting is dramatic and moody, with a sharp amber rim light contouring his profile, reflecting the Nexa AI premium brand aesthetic. Professional, hyper-realistic, 8k resolution." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBD3LbBHcujLONAcesaDR3KfrjFeyw9Wi-EWjbq9eYYT1WJlVYJJ3StuqKBXzpA9u8w0CLT4h3-oQpsCqfZLVIRc_EOXENdj5Z-a0Lj2hQpvpJvM9jeMy0A-MnhJF1C9cf1aK1nT_VxeXSfNZchaga5jXichuQuIDdQLjUdypxqPt-k3jX_DyY-hbJBvLnypZLErziBnbbmt_ZYBZKIAXaG_jJ8QFe1F1F9PndkELzH9EsZYSWaPtRZ">
</div>
<div>
<h1 class="font-display-lg text-headline-md text-primary tracking-tight m-0">Nexa AI</h1>
<p class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-widest mt-1">Premium Concierge</p>
</div>
</div>
<!-- CTA -->
<button class="w-full bg-primary-container text-on-primary-container font-label-sm text-label-sm py-3 px-4 rounded-lg flex items-center justify-center gap-2 mb-8 hover:brightness-110 transition-all border-t border-[#ffe3aa]/30 active:scale-95 shadow-[inset_0_1px_0_rgba(255,255,255,0.2)]">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">add</span>
            New Chat
        </button>
<!-- Navigation Links -->
<nav class="flex-1 space-y-1">
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 font-body-md text-body-md" href="#">
<span class="material-symbols-outlined">history</span>
                Today
            </a>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 font-body-md text-body-md" href="#">
<span class="material-symbols-outlined">calendar_today</span>
                Yesterday
            </a>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 font-body-md text-body-md" href="#">
<span class="material-symbols-outlined">inventory_2</span>
                Archive
            </a>
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-primary font-bold border-r-2 border-primary bg-surface-container-high transition-colors duration-200 active:scale-95 font-body-md text-body-md" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">settings</span>
                Settings
            </a>
</nav>
<!-- Footer -->
<div class="mt-auto pt-4 border-t border-outline-variant/30">
<a class="flex items-center gap-3 px-4 py-3 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 font-body-md text-body-md" href="#">
<span class="material-symbols-outlined">person</span>
                Alex Mercer
            </a>
</div>
</aside>
<!-- Main Content Wrapper -->
<div class="flex-1 md:ml-sidebar-width flex flex-col min-h-screen">
<!-- TopNavBar -->
<header class="flex justify-between items-center h-16 px-container-padding bg-background/80 backdrop-blur-md border-b border-outline-variant shadow-sm sticky top-0 z-10">
<!-- Mobile Brand/Menu -->
<div class="flex items-center gap-4 md:hidden">
<span class="material-symbols-outlined text-on-surface cursor-pointer">menu</span>
<span class="font-headline-md text-headline-md text-on-surface">Nexa AI</span>
</div>
<!-- Desktop Product Name & Context Nav -->
<div class="hidden md:flex items-center gap-8">
<span class="font-headline-md text-headline-md text-on-surface font-extrabold tracking-tight">Nexa AI • Smart</span>
<nav class="flex gap-6 h-16">
<a class="flex items-center text-on-surface-variant font-medium hover:text-primary transition-all font-body-md text-body-md" href="#">Models</a>
<a class="flex items-center text-primary font-bold border-b-2 border-primary pb-1 font-body-md text-body-md pt-1" href="#">Settings</a>
</nav>
</div>
<!-- Trailing Actions -->
<div class="flex items-center gap-2">
<button class="p-2 text-on-surface-variant hover:text-primary transition-all rounded-full hover:bg-surface-container-high active:opacity-80 flex items-center justify-center">
<span class="material-symbols-outlined">star</span>
</button>
<button class="p-2 text-on-surface-variant hover:text-primary transition-all rounded-full hover:bg-surface-container-high active:opacity-80 flex items-center justify-center">
<span class="material-symbols-outlined">share</span>
</button>
<div class="w-8 h-8 rounded-full overflow-hidden ml-2 md:hidden border border-outline-variant">
<img alt="Alex Mercer" class="w-full h-full object-cover" data-alt="A cinematic, high-fashion portrait of a male professional named Alex Mercer, styled in minimalist dark clothing against a pure obsidian black background. The lighting is dramatic and moody, with a sharp amber rim light contouring his profile, reflecting the Nexa AI premium brand aesthetic. Professional, hyper-realistic, 8k resolution." src="https://lh3.googleusercontent.com/aida-public/AB6AXuC-L9JnxBmCZyB6o1Sz7J9z7pfHOL6MEiHZRWAGRxNmVx3wH1i89qpEozQ1kyWSQ3L-rs6NQDd3aVUqzN_g-thV5B7gp6ynmpfL2BLR8rTkGW57B5WdgaaD5CxBF-RUi2enTJfecALSuoWVsyC_TGLPiyM4IyNA_oBlOw7Wc-0YEzEqrVGNaOfrEHeNUnZsHafPrrQu6HdWYJJGuXGNhRNiOZ6rwVpV8fMhExCtAz3tSRrbt_d6D7xU">
</div>
</div>
</header>
<!-- Page Canvas -->
<main class="flex-1 p-container-padding pb-section-margin w-full max-w-5xl mx-auto">
<div class="mb-12">
<h2 class="font-display-lg text-display-lg text-on-surface mb-2 tracking-tight">Settings</h2>
<p class="font-body-md text-body-md text-on-surface-variant">Manage your preferences, account details, and AI behavior.</p>
</div>
<!-- Bento Layout Wrapper -->
<div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
<!-- Left Column (General, Appearance) -->
<div class="lg:col-span-7 space-y-8">
<!-- Section: General -->
<section class="card-gradient card-border rounded-[22px] p-1 shadow-lg shadow-black/20">
<div class="px-6 pt-6 pb-2">
<h3 class="font-label-sm text-label-sm text-primary uppercase tracking-widest mb-4">General Preferences</h3>
</div>
<div class="px-4 pb-4">
<!-- Row 1 -->
<div class="flex items-center justify-between py-4 border-b border-[#272D33]/50 last:border-0 group cursor-pointer hover:bg-white/[0.02] transition-colors px-2 rounded-lg">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full bg-[#111416] border border-[#272D33] flex items-center justify-center text-on-surface-variant group-hover:text-primary transition-colors shadow-inner shadow-white/5">
<span class="material-symbols-outlined text-[20px]">language</span>
</div>
<div>
<div class="font-body-md text-body-md text-on-surface font-medium">Language</div>
<div class="text-sm text-on-surface-variant mt-0.5">Interface and communication language</div>
</div>
</div>
<div class="flex items-center gap-2 text-on-surface-variant group-hover:text-primary transition-colors">
<span class="text-sm font-medium">English (US)</span>
<span class="material-symbols-outlined text-[20px]">chevron_right</span>
</div>
</div>
<!-- Row 2 -->
<div class="flex items-center justify-between py-4 border-b border-[#272D33]/50 last:border-0 group cursor-pointer hover:bg-white/[0.02] transition-colors px-2 rounded-lg">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full bg-[#111416] border border-[#272D33] flex items-center justify-center text-on-surface-variant group-hover:text-primary transition-colors shadow-inner shadow-white/5">
<span class="material-symbols-outlined text-[20px]">notifications_active</span>
</div>
<div>
<div class="font-body-md text-body-md text-on-surface font-medium">Notifications</div>
<div class="text-sm text-on-surface-variant mt-0.5">Manage email and push alerts</div>
</div>
</div>
<div class="flex items-center gap-2 text-on-surface-variant group-hover:text-primary transition-colors">
<span class="text-sm font-medium">All active</span>
<span class="material-symbols-outlined text-[20px]">chevron_right</span>
</div>
</div>
<!-- Row 3 -->
<div class="flex items-center justify-between py-4 border-b border-[#272D33]/50 last:border-0 px-2 rounded-lg">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full bg-[#111416] border border-[#272D33] flex items-center justify-center text-on-surface-variant shadow-inner shadow-white/5">
<span class="material-symbols-outlined text-[20px]">sync</span>
</div>
<div>
<div class="font-body-md text-body-md text-on-surface font-medium">Auto-Sync across devices</div>
<div class="text-sm text-on-surface-variant mt-0.5">Keep your session state synchronized</div>
</div>
</div>
<div class="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
<input checked="" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-on-primary-container border-4 border-primary-container appearance-none cursor-pointer transition-transform duration-200 ease-in-out z-10 translate-x-6 focus:ring-0 focus:outline-none" id="sync-toggle" name="toggle" type="checkbox">
<label class="toggle-label block overflow-hidden h-6 rounded-full bg-primary-container cursor-pointer transition-colors duration-200 ease-in-out" for="sync-toggle"></label>
</div>
</div>
</div>
</section>
<!-- Section: Appearance -->
<section class="card-gradient card-border rounded-[22px] p-1 shadow-lg shadow-black/20">
<div class="px-6 pt-6 pb-2">
<h3 class="font-label-sm text-label-sm text-primary uppercase tracking-widest mb-4">Appearance</h3>
</div>
<div class="px-4 pb-4">
<!-- Row 1 -->
<div class="flex items-center justify-between py-4 border-b border-[#272D33]/50 last:border-0 group cursor-pointer hover:bg-white/[0.02] transition-colors px-2 rounded-lg">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full bg-[#111416] border border-[#272D33] flex items-center justify-center text-on-surface-variant group-hover:text-primary transition-colors shadow-inner shadow-white/5">
<span class="material-symbols-outlined text-[20px]">dark_mode</span>
</div>
<div>
<div class="font-body-md text-body-md text-on-surface font-medium">Theme</div>
<div class="text-sm text-on-surface-variant mt-0.5">System default is Obsidian</div>
</div>
</div>
<div class="flex items-center gap-2 text-on-surface-variant group-hover:text-primary transition-colors">
<span class="text-sm font-medium">Dark Mode</span>
<span class="material-symbols-outlined text-[20px]">chevron_right</span>
</div>
</div>
<!-- Row 2 -->
<div class="flex items-center justify-between py-4 border-b border-[#272D33]/50 last:border-0 group cursor-pointer hover:bg-white/[0.02] transition-colors px-2 rounded-lg">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full bg-[#111416] border border-[#272D33] flex items-center justify-center text-on-surface-variant group-hover:text-primary transition-colors shadow-inner shadow-white/5">
<span class="material-symbols-outlined text-[20px]">palette</span>
</div>
<div>
<div class="font-body-md text-body-md text-on-surface font-medium">Accent Color</div>
<div class="text-sm text-on-surface-variant mt-0.5">Brand primary hue</div>
</div>
</div>
<div class="flex items-center gap-3 text-on-surface-variant">
<div class="w-4 h-4 rounded-full bg-[#F5A623] border border-white/20 shadow-[0_0_8px_rgba(245,166,35,0.4)]"></div>
<span class="text-sm font-medium group-hover:text-primary transition-colors">Amber</span>
<span class="material-symbols-outlined text-[20px] group-hover:text-primary transition-colors">chevron_right</span>
</div>
</div>
</div>
</section>
</div>
<!-- Right Column (AI Prefs, Account) -->
<div class="lg:col-span-5 space-y-8">
<!-- Section: AI Preferences -->
<section class="card-gradient card-border rounded-[22px] p-1 shadow-lg shadow-black/20">
<div class="px-6 pt-6 pb-2">
<h3 class="font-label-sm text-label-sm text-primary uppercase tracking-widest mb-4">AI Preferences</h3>
</div>
<div class="px-4 pb-4">
<!-- Row 1 -->
<div class="flex flex-col py-4 border-b border-[#272D33]/50 last:border-0 px-2 group cursor-pointer rounded-lg hover:bg-white/[0.02] transition-colors">
<div class="flex items-center justify-between w-full mb-2">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-on-surface-variant text-[20px] group-hover:text-primary transition-colors">smart_toy</span>
<div class="font-body-md text-body-md text-on-surface font-medium">Default Model</div>
</div>
<span class="material-symbols-outlined text-on-surface-variant text-[20px] group-hover:text-primary transition-colors">chevron_right</span>
</div>
<div class="pl-8 flex items-center justify-between">
<span class="text-sm text-primary font-semibold tracking-wide">Nexa AI • Smart</span>
<div class="px-2 py-0.5 rounded bg-primary-container/10 border border-primary-container/20">
<span class="text-[10px] text-primary uppercase tracking-wider font-bold">Active</span>
</div>
</div>
</div>
<!-- Row 2 -->
<div class="flex items-center justify-between py-4 border-b border-[#272D33]/50 last:border-0 px-2 rounded-lg">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-on-surface-variant text-[20px]">memory</span>
<div>
<div class="font-body-md text-body-md text-on-surface font-medium">Context Memory</div>
<div class="text-sm text-on-surface-variant mt-0.5">Remember previous interactions</div>
</div>
</div>
<div class="relative inline-block w-12 align-middle select-none transition duration-200 ease-in ml-4">
<input checked="" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-on-primary-container border-4 border-primary-container appearance-none cursor-pointer transition-transform duration-200 ease-in-out z-10 translate-x-6 focus:ring-0 focus:outline-none" id="memory-toggle" name="toggle2" type="checkbox">
<label class="toggle-label block overflow-hidden h-6 rounded-full bg-primary-container cursor-pointer transition-colors duration-200 ease-in-out" for="memory-toggle"></label>
</div>
</div>
<!-- Row 3 -->
<div class="flex flex-col py-4 border-b border-[#272D33]/50 last:border-0 px-2 group cursor-pointer hover:bg-white/[0.02] transition-colors rounded-lg">
<div class="flex items-center justify-between w-full mb-1">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-on-surface-variant text-[20px] group-hover:text-primary transition-colors">tune</span>
<div class="font-body-md text-body-md text-on-surface font-medium">Response Style</div>
</div>
<span class="material-symbols-outlined text-on-surface-variant text-[20px] group-hover:text-primary transition-colors">chevron_right</span>
</div>
<div class="pl-8 text-sm text-on-surface-variant">Balanced &amp; Concise</div>
</div>
</div>
</section>
<!-- Section: Account Summary -->
<section class="card-gradient card-border rounded-[22px] p-6 shadow-lg shadow-black/20 flex flex-col items-center text-center relative overflow-hidden">
<!-- Subtle Glow effect -->
<div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-1 bg-primary blur-md opacity-30"></div>
<div class="w-20 h-20 rounded-full overflow-hidden border-2 border-[#272D33] mb-4 relative z-10 shadow-[0_0_20px_rgba(245,166,35,0.1)]">
<img alt="Alex Mercer" class="w-full h-full object-cover" data-alt="A cinematic, high-fashion portrait of a male professional named Alex Mercer, styled in minimalist dark clothing against a pure obsidian black background. The lighting is dramatic and moody, with a sharp amber rim light contouring his profile, reflecting the Nexa AI premium brand aesthetic. Professional, hyper-realistic, 8k resolution." src="https://lh3.googleusercontent.com/aida-public/AB6AXuABeiPdxqnEZfAoWKYst-LC_XCJx9xF09plXTu6mw9TptAiX4LT_KMMamsjw6u0DpNV-wqpr-NMaRZv4OtpdlXEAP2yduymNrM-oRcYYQ7iMylkBBBh07LvEtEkoyZiNcl0khV5p9PAkwZf35aJhxV-JxPMIKqNvsHrt6mXbdlj6vjJFvyN0SICSDb1W7Z4C-mFP3lU1Y7pjsPAR6hVITAT8EA_qJYFsOqmKXITMTnXGAs4HsBT7yRK">
</div>
<h3 class="font-headline-md text-headline-md text-on-surface mb-1">Alex Mercer</h3>
<p class="font-body-md text-sm text-on-surface-variant mb-4">alex.mercer@nexa.ai</p>
<div class="flex items-center gap-2 px-3 py-1.5 rounded-full border border-primary/30 bg-primary/5 mb-6">
<span class="material-symbols-outlined text-[16px] text-primary" style="font-variation-settings: 'FILL' 1;">workspace_premium</span>
<span class="font-label-sm text-xs text-primary uppercase tracking-widest font-bold">Premium Concierge</span>
</div>
<button class="w-full py-2.5 rounded-lg border border-[#272D33] text-[#F5F3EE] font-medium text-sm hover:border-primary hover:text-primary transition-all shadow-sm hover:shadow-[0_0_12px_rgba(245,166,35,0.15)] flex justify-center items-center gap-2 group">
                             Manage Account
                             <span class="material-symbols-outlined text-[18px] opacity-70 group-hover:opacity-100 transition-opacity">open_in_new</span>
</button>
</section>
</div>
</div>
<!-- Danger Zone -->
<div class="mt-12 pt-8 border-t border-[#272D33] flex justify-end">
<button class="px-6 py-2.5 rounded-lg border border-error/30 text-error hover:bg-error/10 hover:border-error transition-all text-sm font-medium flex items-center gap-2">
<span class="material-symbols-outlined text-[18px]">logout</span>
                    Sign Out
                </button>
</div>
</main>
</div>
<!-- Script for custom toggle interaction (vanilla JS micro-interaction) -->
<script>
        document.querySelectorAll('.toggle-checkbox').forEach(toggle => {
            toggle.addEventListener('change', function() {
                if(this.checked) {
                    this.classList.add('translate-x-6', 'border-primary-container');
                    this.classList.remove('translate-x-0', 'border-[#333537]');
                    this.nextElementSibling.classList.add('bg-primary-container');
                    this.nextElementSibling.classList.remove('bg-[#1a1c1e]');
                } else {
                    this.classList.remove('translate-x-6', 'border-primary-container');
                    this.classList.add('translate-x-0', 'border-[#333537]');
                    this.nextElementSibling.classList.remove('bg-primary-container');
                    this.nextElementSibling.classList.add('bg-[#1a1c1e]');
                }
            });
        });
    </script>
</body></html>

<!-- Settings - Nexa AI (Obsidian Amber) -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Nexa AI - Error</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "inverse-on-surface": "#2f3133",
                        "tertiary-container": "#b2b7be",
                        "outline-variant": "#524534",
                        "on-tertiary-fixed": "#171c21",
                        "on-secondary-fixed": "#251a00",
                        "on-surface": "#e2e2e5",
                        "surface-tint": "#ffb955",
                        "on-primary": "#452b00",
                        "secondary-fixed-dim": "#edc157",
                        "surface-container": "#1e2022",
                        "surface-container-low": "#1a1c1e",
                        "secondary": "#edc157",
                        "background": "#111416",
                        "tertiary-fixed": "#dee3ea",
                        "on-error": "#690005",
                        "on-primary-fixed-variant": "#633f00",
                        "primary": "#ffc880",
                        "on-error-container": "#ffdad6",
                        "error": "#ffb4ab",
                        "primary-fixed": "#ffddb4",
                        "tertiary-fixed-dim": "#c2c7ce",
                        "tertiary": "#ced2d9",
                        "surface-container-high": "#282a2c",
                        "on-tertiary-container": "#43484e",
                        "primary-fixed-dim": "#ffb955",
                        "secondary-container": "#906d00",
                        "on-surface-variant": "#d7c3ae",
                        "surface-container-highest": "#333537",
                        "outline": "#9f8e7a",
                        "inverse-surface": "#e2e2e5",
                        "on-secondary-fixed-variant": "#5b4300",
                        "on-secondary-container": "#fff7ee",
                        "inverse-primary": "#835500",
                        "surface-variant": "#333537",
                        "primary-container": "#f5a623",
                        "surface": "#111416",
                        "error-container": "#93000a",
                        "surface-container-lowest": "#0c0e10",
                        "on-tertiary": "#2c3136",
                        "on-primary-fixed": "#291800",
                        "on-background": "#e2e2e5",
                        "on-primary-container": "#644000",
                        "surface-bright": "#37393c",
                        "on-secondary": "#3f2e00",
                        "surface-dim": "#111416",
                        "on-tertiary-fixed-variant": "#42474d",
                        "secondary-fixed": "#ffdf9b"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "section-margin": "4rem",
                        "container-padding": "2rem",
                        "sidebar-width": "280px",
                        "element-gap": "1rem"
                    },
                    "fontFamily": {
                        "body-lg": ["Plus Jakarta Sans"],
                        "display-lg-mobile": ["Plus Jakarta Sans"],
                        "display-lg": ["Plus Jakarta Sans"],
                        "label-sm": ["Plus Jakarta Sans"],
                        "headline-md": ["Plus Jakarta Sans"],
                        "body-md": ["Plus Jakarta Sans"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "display-lg-mobile": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "label-sm": ["13px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
                    }
                }
            }
        }
    </script>
<style>
        body {
            background-color: #080A0C; /* Base Layer */
            color: #e2e2e5;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        
        .glow-border {
            border: 1px solid #272D33;
            transition: all 0.3s ease;
        }
        
        .glow-border:hover {
            border-color: #F5A623;
            box-shadow: 0 0 8px rgba(245, 166, 35, 0.2);
        }
        
        .btn-primary {
            background-color: #F5A623;
            color: #080A0C;
            border-top: 1px solid rgba(255, 255, 255, 0.4);
        }
        
        .btn-secondary {
            background-color: transparent;
            color: #F5F3EE;
            border: 1px solid #272D33;
            transition: all 0.3s ease;
        }
        
        .btn-secondary:hover {
            border-color: #F5A623;
            box-shadow: 0 0 8px rgba(245, 166, 35, 0.2);
        }

        .pulse-icon {
            animation: subtlePulse 3s infinite alternate;
        }

        @keyframes subtlePulse {
            0% { opacity: 0.8; transform: scale(0.98); }
            100% { opacity: 1; transform: scale(1.02); }
        }
    </style>
</head>
<body class="flex min-h-screen">
<!-- TopNavBar (Mobile Only) -->
<nav class="md:hidden fixed top-0 w-full bg-background/80 dark:bg-background/80 backdrop-blur-md border-b border-outline-variant dark:border-outline-variant flex justify-between items-center h-16 px-container-padding z-40">
<div class="font-headline-md text-headline-md text-on-surface dark:text-on-surface">Nexa AI • Smart</div>
<div class="flex items-center gap-4">
<button class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80">
<span class="material-symbols-outlined" data-icon="star">star</span>
</button>
<button class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80">
<span class="material-symbols-outlined" data-icon="share">share</span>
</button>
<div class="w-8 h-8 rounded-full overflow-hidden glow-border">
<img alt="Alex Mercer" class="w-full h-full object-cover" data-alt="A small, professional headshot of Alex Mercer, an avatar. The image features a clean, high-end studio lighting setup with a subtle dark background, emphasizing clarity and focus in a modern, luxury tech aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuA4vaeEKkZ3QjiVYqcLGZ1RokpTT964J7bDxyl0RQWZYYvkpVgwiBRpu-MteZKmIcSmLPonUke5KLclhC_pia6PVjrSDN0AH8_YWoILo03o5WfQB4TjMTFqrBrLw-4dCvFzHCSRe4lUr2VibKtGX4aVERVjhq62wmCW-9zxLLaynLIoqwMsaJJAb2B6_NVCR0ntap_QBdMQMQao5rEnCrTCJMeEePP7y4JqO3CDD1Jn0QffaN3WZvPX">
</div>
</div>
</nav>
<!-- SideNavBar (Desktop) -->
<aside class="hidden md:flex flex-col fixed left-0 top-0 h-screen w-sidebar-width bg-surface-container dark:bg-surface-container border-r border-outline-variant dark:border-outline-variant shadow-none p-element-gap z-30 pt-8 pb-8">
<div class="mb-8 px-4">
<div class="font-display-lg text-display-lg text-primary dark:text-primary tracking-tight mb-1">Nexa AI</div>
<div class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-widest">Premium Concierge</div>
</div>
<button class="w-full mb-8 py-3 px-4 rounded-xl flex items-center justify-center gap-2 btn-primary font-label-sm text-label-sm uppercase tracking-wide">
<span class="material-symbols-outlined text-[18px]">add</span>
            New Chat
        </button>
<nav class="flex-1 flex flex-col gap-2">
<!-- Navigation items suppressed due to error state context priority -->
<div class="px-4 py-2 text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform rounded-lg flex items-center gap-3 cursor-pointer">
<span class="material-symbols-outlined">history</span>
<span class="font-body-md text-body-md">Today</span>
</div>
<div class="px-4 py-2 text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform rounded-lg flex items-center gap-3 cursor-pointer">
<span class="material-symbols-outlined">calendar_today</span>
<span class="font-body-md text-body-md">Yesterday</span>
</div>
<div class="px-4 py-2 text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform rounded-lg flex items-center gap-3 cursor-pointer">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-body-md text-body-md">Archive</span>
</div>
</nav>
<div class="mt-auto pt-4 border-t border-outline-variant/30">
<div class="px-4 py-3 text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 transition-transform rounded-lg flex items-center gap-3 cursor-pointer">
<span class="material-symbols-outlined">settings</span>
<span class="font-body-md text-body-md">Settings</span>
</div>
<div class="px-4 py-3 mt-2 flex items-center gap-3 rounded-lg hover:bg-surface-container-high cursor-pointer transition-colors">
<div class="w-8 h-8 rounded-full overflow-hidden glow-border">
<img alt="Alex Mercer" class="w-full h-full object-cover" data-alt="A small, professional headshot of Alex Mercer, an avatar. The image features a clean, high-end studio lighting setup with a subtle dark background, emphasizing clarity and focus in a modern, luxury tech aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDCyRtjUrYldY3bRDHUUuyxhRcJ63pL4xasMwruOuyM3uI30Ln6MfUxb6ijc-0EDHzC0_VEG8GDcAZqNSOlvJSc2ZaFTwgnQNlJD0JKlkqARtAysU-vKXbeFvQk_vkXFEvhYAndQXexbOhstItAL3Y260OnXM_b1CIFv7t4LsN3TOPOv8JAcGvnxsNX7SU4th90-yItKpDkWqcdHcHMafQTm0hHiQsPAwGgALYS3zDxC8_vVEWhwLee">
</div>
<span class="font-body-md text-body-md text-on-surface">Alex Mercer</span>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="flex-1 flex flex-col items-center justify-center min-h-screen pt-16 md:pt-0 md:ml-sidebar-width px-container-padding relative overflow-hidden">
<!-- Subtle background atmospheric effect -->
<div class="absolute inset-0 pointer-events-none opacity-20" style="background: radial-gradient(circle at 50% 40%, rgba(245, 166, 35, 0.05) 0%, transparent 60%);"></div>
<div class="max-w-[1200px] w-full flex flex-col items-center justify-center text-center relative z-10 p-8 rounded-[22px] glow-border" style="background: linear-gradient(180deg, #161B20 0%, #111519 100%);">
<div class="mb-8 pulse-icon">
<span class="material-symbols-outlined text-[80px] text-primary-container drop-shadow-[0_0_15px_rgba(245,166,35,0.3)]" style="font-variation-settings: 'wght' 300;">warning</span>
</div>
<h1 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-4">
                Something went wrong
            </h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-md mx-auto mb-10">
                Please try again in a moment. Our systems are working to resolve the issue.
            </p>
<button class="btn-secondary py-3 px-8 rounded-full font-label-sm text-label-sm uppercase tracking-widest flex items-center gap-2" onclick="location.reload()">
<span class="material-symbols-outlined text-[18px]">refresh</span>
                Retry
            </button>
</div>
</main>
</body></html>

<!-- Error - Nexa AI (Obsidian Amber) -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Nexa AI - Search Results</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              "colors": {
                      "inverse-on-surface": "#2f3133",
                      "tertiary-container": "#b2b7be",
                      "outline-variant": "#524534",
                      "on-tertiary-fixed": "#171c21",
                      "on-secondary-fixed": "#251a00",
                      "on-surface": "#e2e2e5",
                      "surface-tint": "#ffb955",
                      "on-primary": "#452b00",
                      "secondary-fixed-dim": "#edc157",
                      "surface-container": "#1e2022",
                      "surface-container-low": "#1a1c1e",
                      "secondary": "#edc157",
                      "background": "#111416",
                      "tertiary-fixed": "#dee3ea",
                      "on-error": "#690005",
                      "on-primary-fixed-variant": "#633f00",
                      "primary": "#ffc880",
                      "on-error-container": "#ffdad6",
                      "error": "#ffb4ab",
                      "primary-fixed": "#ffddb4",
                      "tertiary-fixed-dim": "#c2c7ce",
                      "tertiary": "#ced2d9",
                      "surface-container-high": "#282a2c",
                      "on-tertiary-container": "#43484e",
                      "primary-fixed-dim": "#ffb955",
                      "secondary-container": "#906d00",
                      "on-surface-variant": "#d7c3ae",
                      "surface-container-highest": "#333537",
                      "outline": "#9f8e7a",
                      "inverse-surface": "#e2e2e5",
                      "on-secondary-fixed-variant": "#5b4300",
                      "on-secondary-container": "#fff7ee",
                      "inverse-primary": "#835500",
                      "surface-variant": "#333537",
                      "primary-container": "#f5a623",
                      "surface": "#111416",
                      "error-container": "#93000a",
                      "surface-container-lowest": "#0c0e10",
                      "on-tertiary": "#2c3136",
                      "on-primary-fixed": "#291800",
                      "on-background": "#e2e2e5",
                      "on-primary-container": "#644000",
                      "surface-bright": "#37393c",
                      "on-secondary": "#3f2e00",
                      "surface-dim": "#111416",
                      "on-tertiary-fixed-variant": "#42474d",
                      "secondary-fixed": "#ffdf9b"
              },
              "borderRadius": {
                      "DEFAULT": "0.25rem",
                      "lg": "0.5rem",
                      "xl": "0.75rem",
                      "full": "9999px"
              },
              "spacing": {
                      "section-margin": "4rem",
                      "container-padding": "2rem",
                      "sidebar-width": "280px",
                      "element-gap": "1rem"
              },
              "fontFamily": {
                      "body-lg": [
                              "Plus Jakarta Sans"
                      ],
                      "display-lg-mobile": [
                              "Plus Jakarta Sans"
                      ],
                      "display-lg": [
                              "Plus Jakarta Sans"
                      ],
                      "label-sm": [
                              "Plus Jakarta Sans"
                      ],
                      "headline-md": [
                              "Plus Jakarta Sans"
                      ],
                      "body-md": [
                              "Plus Jakarta Sans"
                      ]
              },
              "fontSize": {
                      "body-lg": [
                              "18px",
                              {
                                      "lineHeight": "28px",
                                      "fontWeight": "400"
                              }
                      ],
                      "display-lg-mobile": [
                              "32px",
                              {
                                      "lineHeight": "40px",
                                      "letterSpacing": "-0.02em",
                                      "fontWeight": "700"
                              }
                      ],
                      "display-lg": [
                              "48px",
                              {
                                      "lineHeight": "56px",
                                      "letterSpacing": "-0.02em",
                                      "fontWeight": "700"
                              }
                      ],
                      "label-sm": [
                              "13px",
                              {
                                      "lineHeight": "16px",
                                      "letterSpacing": "0.05em",
                                      "fontWeight": "600"
                              }
                      ],
                      "headline-md": [
                              "24px",
                              {
                                      "lineHeight": "32px",
                                      "letterSpacing": "-0.01em",
                                      "fontWeight": "600"
                              }
                      ],
                      "body-md": [
                              "16px",
                              {
                                      "lineHeight": "24px",
                                      "fontWeight": "400"
                              }
                      ]
              }
            }
          }
        }
    </script>
<style>
        body {
            background-color: #080A0C;
            color: #e2e2e5;
        }
        
        .glow-border {
            border: 1px solid #272D33;
            transition: all 0.3s ease;
        }
        
        .glow-border:focus-within, .glow-border:hover {
            border-color: #F5A623;
            box-shadow: 0 0 8px 0 rgba(245, 166, 35, 0.2);
        }

        .bento-card {
            background: linear-gradient(180deg, #161B20 0%, #111519 100%);
            border: 1px solid #272D33;
            border-radius: 22px;
        }
        
        .highlight {
            color: #F5A623;
            font-weight: 600;
        }
    </style>
</head>
<body class="font-body-md text-body-md antialiased min-h-screen flex flex-col md:flex-row">
<!-- Mobile Nav Header -->
<div class="md:hidden flex justify-between items-center h-16 px-container-padding border-b border-outline-variant bg-surface-container w-full fixed top-0 z-50">
<div class="font-display-lg-mobile text-display-lg-mobile text-primary tracking-tight">Nexa AI</div>
<button class="text-on-surface p-2">
<span class="material-symbols-outlined">menu</span>
</button>
</div>
<!-- SideNavBar -->
<nav class="hidden md:flex flex-col h-full p-element-gap fixed left-0 top-0 h-screen w-sidebar-width bg-surface-container border-r border-outline-variant shadow-none z-40">
<div class="mb-8 mt-4 px-4">
<div class="font-display-lg text-display-lg text-primary tracking-tight">Nexa AI</div>
<div class="text-on-surface-variant font-label-sm text-label-sm mt-1">Premium Concierge</div>
</div>
<button class="mb-8 mx-4 bg-[#F5A623] text-[#080A0C] font-label-sm text-label-sm py-3 px-6 rounded-full flex items-center justify-center gap-2 border-t border-[#ffe6b3] hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined text-lg">add</span>
            New Chat
        </button>
<div class="flex-1 overflow-y-auto space-y-2 px-2">
<!-- Active state would be here if there was a direct match, but this is a search page -->
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95" href="#">
<span class="material-symbols-outlined">history</span>
<span class="font-body-md text-body-md">Today</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95" href="#">
<span class="material-symbols-outlined">calendar_today</span>
<span class="font-body-md text-body-md">Yesterday</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95" href="#">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-body-md text-body-md">Archive</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200 active:scale-95 mt-auto" href="#">
<span class="material-symbols-outlined">settings</span>
<span class="font-body-md text-body-md">Settings</span>
</a>
</div>
<div class="mt-auto pt-4 border-t border-outline-variant px-2">
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface hover:bg-surface-container-high transition-colors duration-200" href="#">
<img alt="Alex Mercer" class="w-8 h-8 rounded-full object-cover border border-outline-variant" data-alt="A small, professional headshot of an individual with a subtle warm glow, high-end corporate style, minimal background, sharp focus, sophisticated deep dark aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAsOIwFZjRZ1xofRTEBAbLoFhDeEdLx-aAL7PXyIzS2qloyJbWA81Av34uYOnPBoPI8gRMU04EkI7kxoFp0H0YO5XTRQbuGsFyJOe9buy_9KfXZOwx42Bm1SmPu-p0izmk9_Wr_04lyEg5XORgV_0eB9PpAoqEz2Q9ZB1lscGORsbE2k8Wvz29nmopbbLU2ssYoBeuM7HdznSjLG9YXKJm-6_7K-MHlUTezTNK76bXlg2MClyFIYV4q">
<span class="font-label-sm text-label-sm">Alex Mercer</span>
</a>
</div>
</nav>
<!-- Main Content Area -->
<main class="flex-1 flex flex-col min-h-screen pt-16 md:pt-0 md:ml-sidebar-width bg-background">
<!-- TopNavBar -->
<header class="hidden md:flex justify-between items-center h-16 px-container-padding border-b border-outline-variant bg-background/80 backdrop-blur-md shadow-sm sticky top-0 z-30 w-full">
<div class="flex items-center gap-4">
<span class="font-headline-md text-headline-md text-on-surface">Nexa AI • Smart</span>
</div>
<div class="flex items-center gap-6">
<nav class="flex gap-4">
<a class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80" href="#">Models</a>
<a class="text-on-surface-variant font-medium hover:text-primary transition-all active:opacity-80" href="#">Settings</a>
</nav>
<div class="flex items-center gap-3">
<button class="text-on-surface-variant hover:text-primary transition-colors p-2">
<span class="material-symbols-outlined">star</span>
</button>
<button class="text-on-surface-variant hover:text-primary transition-colors p-2">
<span class="material-symbols-outlined">share</span>
</button>
<img alt="Alex Mercer" class="w-8 h-8 rounded-full object-cover border border-outline-variant" data-alt="A small, professional headshot of an individual with a subtle warm glow, high-end corporate style, minimal background, sharp focus, sophisticated deep dark aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAPgx1w6wLlGd16dfO1Jm0erkg3XbDx4XqpUJd8ZSmFibLu9cU14QKl2jXKZe4gTNGrZk_C2__-VPQFRk1_lquRLXQDVKwbkzuNbadOsvc6xfDGU522TMD0K1xw8TajznOCQxIqxlogdzP6Dowj8DMceDWbfU56keq1EYOZskbm0A6LZzLnllkry_Idn95u1wHL6YHr-uilk4N_iaWvUUABAi6ZJPkrXNIDhQ0V0p90t-QCZjRNnlqC">
</div>
</div>
</header>
<!-- Search Canvas -->
<div class="flex-1 flex flex-col items-center w-full max-w-[1200px] mx-auto px-container-padding py-section-margin">
<!-- Search Input -->
<div class="w-full max-w-3xl mb-12">
<div class="relative w-full glow-border bg-[#0D1013] rounded-full flex items-center px-6 py-4">
<span class="material-symbols-outlined text-on-surface-variant mr-4 text-2xl">search</span>
<input class="w-full bg-transparent border-none outline-none text-on-surface font-body-lg text-body-lg placeholder-on-surface-variant focus:ring-0" placeholder="Search conversations..." type="text" value="Quantum">
<button class="ml-4 text-on-surface-variant hover:text-primary transition-colors">
<span class="material-symbols-outlined">close</span>
</button>
</div>
<div class="mt-4 flex gap-2 flex-wrap px-4">
<span class="px-3 py-1 rounded-full bg-primary/10 text-primary font-label-sm text-label-sm uppercase tracking-wider border border-primary/20">Physics</span>
<span class="px-3 py-1 rounded-full bg-primary/10 text-primary font-label-sm text-label-sm uppercase tracking-wider border border-primary/20">Computing</span>
<span class="px-3 py-1 rounded-full bg-primary/10 text-primary font-label-sm text-label-sm uppercase tracking-wider border border-primary/20">Recent</span>
</div>
</div>
<!-- Results List -->
<div class="w-full max-w-3xl space-y-6">
<h2 class="font-headline-md text-headline-md text-on-surface mb-6 flex items-center gap-2">
<span class="material-symbols-outlined text-primary">manage_search</span>
                    Search Results
                </h2>
<!-- Result Item 1 -->
<div class="bento-card p-6 hover:border-[#F5A623]/50 transition-colors cursor-pointer group">
<div class="flex justify-between items-start mb-3">
<h3 class="font-body-lg text-body-lg text-on-surface font-semibold group-hover:text-primary transition-colors">
                            Understanding <span class="highlight">Quantum</span> Computing
                        </h3>
<span class="text-on-surface-variant text-sm flex items-center gap-1">
<span class="material-symbols-outlined text-[16px]">schedule</span> 2 days ago
                        </span>
</div>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">
                        In our last session, we discussed how <span class="highlight">quantum</span> superposition allows qubits to represent multiple states simultaneously, exponentially increasing processing power for specific types of algorithms compared to classical bits.
                    </p>
<div class="mt-4 flex items-center gap-4 text-sm">
<div class="flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[16px]">forum</span> 14 messages
                        </div>
<div class="flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[16px]">folder_open</span> Research
                        </div>
</div>
</div>
<!-- Result Item 2 -->
<div class="bento-card p-6 hover:border-[#F5A623]/50 transition-colors cursor-pointer group">
<div class="flex justify-between items-start mb-3">
<h3 class="font-body-lg text-body-lg text-on-surface font-semibold group-hover:text-primary transition-colors">
<span class="highlight">Quantum</span> Algorithms Explained
                        </h3>
<span class="text-on-surface-variant text-sm flex items-center gap-1">
<span class="material-symbols-outlined text-[16px]">schedule</span> Last week
                        </span>
</div>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">
                        Shor's algorithm is a prime example of a <span class="highlight">quantum</span> algorithm that offers a significant speedup over classical counterparts. It efficiently factors large integers, which forms the basis of many modern cryptographic systems.
                    </p>
<div class="mt-4 flex items-center gap-4 text-sm">
<div class="flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[16px]">forum</span> 32 messages
                        </div>
<div class="flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[16px]">folder_open</span> Algorithms
                        </div>
</div>
</div>
<!-- Result Item 3 -->
<div class="bento-card p-6 hover:border-[#F5A623]/50 transition-colors cursor-pointer group opacity-80">
<div class="flex justify-between items-start mb-3">
<h3 class="font-body-lg text-body-lg text-on-surface font-semibold group-hover:text-primary transition-colors">
                            Introduction to <span class="highlight">Quantum</span> Mechanics
                        </h3>
<span class="text-on-surface-variant text-sm flex items-center gap-1">
<span class="material-symbols-outlined text-[16px]">schedule</span> Last month
                        </span>
</div>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">
                        The fundamental principles of <span class="highlight">quantum</span> mechanics lay the groundwork for understanding how subatomic particles behave. We covered wave-particle duality and the uncertainty principle.
                    </p>
<div class="mt-4 flex items-center gap-4 text-sm">
<div class="flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[16px]">forum</span> 8 messages
                        </div>
<div class="flex items-center gap-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[16px]">folder_open</span> Physics
                        </div>
</div>
</div>
</div>
<!-- Load More -->
<button class="mt-8 px-6 py-3 rounded-full border border-outline-variant text-on-surface-variant hover:text-primary hover:border-primary transition-colors font-label-sm text-label-sm tracking-wider uppercase">
                Load More Results
            </button>
</div>
</main>
</body></html>

<!-- Search - Nexa AI (Obsidian Amber) -->
<!DOCTYPE html><html class="dark" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Nexa AI - Chat</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "inverse-on-surface": "#2f3133",
                        "tertiary-container": "#b2b7be",
                        "outline-variant": "#524534",
                        "on-tertiary-fixed": "#171c21",
                        "on-secondary-fixed": "#251a00",
                        "on-surface": "#e2e2e5",
                        "surface-tint": "#ffb955",
                        "on-primary": "#452b00",
                        "secondary-fixed-dim": "#edc157",
                        "surface-container": "#1e2022",
                        "surface-container-low": "#1a1c1e",
                        "secondary": "#edc157",
                        "background": "#111416",
                        "tertiary-fixed": "#dee3ea",
                        "on-error": "#690005",
                        "on-primary-fixed-variant": "#633f00",
                        "primary": "#ffc880",
                        "on-error-container": "#ffdad6",
                        "error": "#ffb4ab",
                        "primary-fixed": "#ffddb4",
                        "tertiary-fixed-dim": "#c2c7ce",
                        "tertiary": "#ced2d9",
                        "surface-container-high": "#282a2c",
                        "on-tertiary-container": "#43484e",
                        "primary-fixed-dim": "#ffb955",
                        "secondary-container": "#906d00",
                        "on-surface-variant": "#d7c3ae",
                        "surface-container-highest": "#333537",
                        "outline": "#9f8e7a",
                        "inverse-surface": "#e2e2e5",
                        "on-secondary-fixed-variant": "#5b4300",
                        "on-secondary-container": "#fff7ee",
                        "inverse-primary": "#835500",
                        "surface-variant": "#333537",
                        "primary-container": "#f5a623",
                        "surface": "#111416",
                        "error-container": "#93000a",
                        "surface-container-lowest": "#0c0e10",
                        "on-tertiary": "#2c3136",
                        "on-primary-fixed": "#291800",
                        "on-background": "#e2e2e5",
                        "on-primary-container": "#644000",
                        "surface-bright": "#37393c",
                        "on-secondary": "#3f2e00",
                        "surface-dim": "#111416",
                        "on-tertiary-fixed-variant": "#42474d",
                        "secondary-fixed": "#ffdf9b"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "section-margin": "4rem",
                        "container-padding": "2rem",
                        "sidebar-width": "280px",
                        "element-gap": "1rem"
                    },
                    "fontFamily": {
                        "body-lg": ["Plus Jakarta Sans"],
                        "display-lg-mobile": ["Plus Jakarta Sans"],
                        "display-lg": ["Plus Jakarta Sans"],
                        "label-sm": ["Plus Jakarta Sans"],
                        "headline-md": ["Plus Jakarta Sans"],
                        "body-md": ["Plus Jakarta Sans"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", { "lineHeight": "28px", "fontWeight": "400" }],
                        "display-lg-mobile": ["32px", { "lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "display-lg": ["48px", { "lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700" }],
                        "label-sm": ["13px", { "lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600" }],
                        "headline-md": ["24px", { "lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600" }],
                        "body-md": ["16px", { "lineHeight": "24px", "fontWeight": "400" }]
                    }
                }
            }
        }
    </script>
<style>
        body {
            background-color: #080A0C; /* Base Layer */
            color: #e2e2e5; /* on-background */
        }
        
        .glow-border {
            border: 1px solid #272D33;
            transition: all 0.3s ease;
        }
        .glow-border:focus-within {
            border-color: #F5A623;
            box-shadow: 0 0 8px 0 rgba(245, 166, 35, 0.2);
        }

        .chat-bubble-ai {
            background-color: #111519;
            border: 1px solid #272D33;
        }

        .chat-bubble-user {
            background-color: #161B20;
            border-left: 2px solid #F5A623;
        }

        /* Hide scrollbar for clean look */
        ::-webkit-scrollbar {
            display: none;
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="font-body-md text-body-md h-screen flex flex-col overflow-hidden">
<!-- Top Navigation Bar -->
<header class="flex justify-between items-center h-16 px-4 bg-background/80 dark:bg-background/80 backdrop-blur-md border-b border-outline-variant dark:border-outline-variant shadow-sm z-50 sticky top-0 shrink-0">
<div class="flex items-center gap-3">
<button aria-label="Open Menu" class="p-2 text-on-surface hover:text-primary transition-colors active:scale-95">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">menu</span>
</button>
<div class="flex items-center gap-2">
<div class="w-8 h-8 rounded-full bg-primary-container flex items-center justify-center text-[#080A0C] font-bold shadow-[inset_0_1px_0_rgba(255,255,255,0.4)]">
                    N
                </div>
<span class="font-headline-md text-headline-md text-on-surface dark:text-on-surface tracking-tight">Nexa AI</span>
</div>
</div>
<div class="flex items-center gap-2">
<button aria-label="Models" class="p-2 text-on-surface-variant hover:text-primary transition-all active:opacity-80">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">tune</span>
</button>
<button aria-label="Settings" class="p-2 text-on-surface-variant hover:text-primary transition-all active:opacity-80">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">settings</span>
</button>
<img alt="Alex Mercer" class="w-8 h-8 rounded-full ml-2 object-cover border border-[#272D33]" data-alt="A close-up portrait of a professional individual representing Alex Mercer. The image should be highly detailed, featuring soft, dramatic lighting consistent with a premium, high-end tech environment. Deep shadows and subtle amber rim lighting highlight the features, maintaining a luxurious and authoritative yet approachable tone." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCTjAVrtKq8QvOKWYRFoUPPNkmygloPvVtJt0ijh2tWyC7YGIOX9dVnmk3GnxOx5n5YkI3duZc-8bXrEj3cz5XN6GyBX0Fk9Hx3JmJvQb6EAlQBnis7Ih6HooDtz6n_3gKqCZey3AKfXAYfNlJIN8fF7qU1MFLtT2m94x294JbolcuqNl6OLu45t3LRSXftRtvQnzxDDye33ghmpe7swJZwq4nIo1SaoQ5cSg6gUWnsNIAz5EqMWpMJ">
</div>
</header>
<!-- Main Chat Canvas -->
<main class="flex-1 overflow-y-auto p-4 flex flex-col gap-6 relative" id="chat-container">
<!-- Welcome State (Visible when empty, currently hidden for chat flow) -->
<!--
        <div class="flex-1 flex flex-col items-center justify-center text-center opacity-50">
             <div class="w-16 h-16 rounded-full bg-surface-container flex items-center justify-center mb-4 border border-outline-variant">
                  <span class="material-symbols-outlined text-3xl text-primary" style="font-variation-settings: 'FILL' 1;">auto_awesome</span>
             </div>
             <h2 class="font-headline-md text-headline-md text-on-surface mb-2">How can I assist you today?</h2>
             <p class="font-body-md text-body-md text-on-surface-variant">Nexa AI Premium Concierge</p>
        </div>
        -->
<!-- Chat History -->
<div class="flex flex-col gap-6 max-w-[1200px] mx-auto w-full pb-24">
<!-- AI Message -->
<div class="flex gap-3 max-w-[90%]">
<div class="w-8 h-8 rounded-full bg-primary-container shrink-0 flex items-center justify-center text-[#080A0C] font-bold shadow-[inset_0_1px_0_rgba(255,255,255,0.4)]">
                    N
                </div>
<div class="chat-bubble-ai rounded-2xl rounded-tl-sm p-4 text-on-surface">
<p class="mb-2">Good morning. I've analyzed the latest market trends for your portfolio as requested.</p>
<p>The tech sector is showing high volatility, but your primary assets remain stable. Would you like a detailed breakdown?</p>
</div>
</div>
<!-- User Message -->
<div class="flex gap-3 max-w-[90%] self-end flex-row-reverse">
<img alt="User" class="w-8 h-8 rounded-full shrink-0 object-cover border border-[#272D33]" data-alt="A close-up portrait of a professional individual representing the user. The image should be highly detailed, featuring soft, dramatic lighting consistent with a premium, high-end tech environment. Deep shadows and subtle amber rim lighting highlight the features, maintaining a luxurious and authoritative yet approachable tone." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAv70KBE59oMqIPwoJn9Nzw6wqb03k64cSVgsU3GaPFhkTJrOmj52AtxMGImifHtSlmboj0n5ifKtInoxxj2AIuwsPyPYsMU69faMV8nZ9rovwXZJHq_jYaSBPb0fuWy2PsJxM9qylPrl9Ytvl-4StTRVrRj9UA3hfhYKZOxLcHP3b0t2LN78f-1EaAicQVyhbJgM9pVQP-Rqpwkvlkv59_uXLI033uFX5Krv1qICHQu0HwUI01WCgp">
<div class="chat-bubble-user rounded-2xl rounded-tr-sm p-4 text-on-surface">
<p>Yes, please provide the breakdown. Focus specifically on the renewable energy sector changes over the last 48 hours.</p>
</div>
</div>
<!-- AI Message (Typing) -->
<div class="flex gap-3 max-w-[90%]">
<div class="w-8 h-8 rounded-full bg-primary-container shrink-0 flex items-center justify-center text-[#080A0C] font-bold shadow-[inset_0_1px_0_rgba(255,255,255,0.4)]">
                    N
                </div>
<div class="chat-bubble-ai rounded-2xl rounded-tl-sm p-4 text-on-surface flex items-center gap-1 h-12">
<div class="w-2 h-2 rounded-full bg-on-surface-variant animate-pulse"></div>
<div class="w-2 h-2 rounded-full bg-on-surface-variant animate-pulse delay-75"></div>
<div class="w-2 h-2 rounded-full bg-on-surface-variant animate-pulse delay-150"></div>
</div>
</div>
</div>
</main>
<!-- Composer Area -->
<div class="fixed bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-[#080A0C] via-[#080A0C] to-transparent pt-10 z-40">
<div class="max-w-[1200px] mx-auto">
<div class="relative flex items-end gap-2 bg-[#0D1013] rounded-[22px] p-2 glow-border">
<button aria-label="Attach File" class="p-2 shrink-0 text-on-surface-variant hover:text-primary transition-colors rounded-full hover:bg-surface-container">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">attach_file</span>
</button>
<textarea class="w-full bg-transparent border-none text-on-surface placeholder:text-on-surface-variant resize-none outline-none focus:ring-0 max-h-32 min-h-[40px] py-2 font-body-md text-body-md" oninput="this.style.height = ''; this.style.height = this.scrollHeight + 'px'" placeholder="Message Nexa..." rows="1"></textarea>
<div class="flex items-center gap-1 shrink-0 pb-1">
<button aria-label="Voice Input" class="p-2 text-on-surface-variant hover:text-primary transition-colors rounded-full hover:bg-surface-container hidden sm:block">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">mic</span>
</button>
<button aria-label="Send Message" class="p-2 bg-primary-container text-[#080A0C] rounded-full hover:bg-surface-tint transition-colors shadow-[inset_0_1px_0_rgba(255,255,255,0.4)] flex items-center justify-center w-10 h-10">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">arrow_upward</span>
</button>
</div>
</div>
<div class="text-center mt-2">
<span class="font-label-sm text-label-sm text-on-surface-variant/50">Nexa AI can make mistakes. Consider verifying important information.</span>
</div>
</div>
</div>
<!-- Hidden Sidebar Overlay (For mobile menu interactions if implemented) -->
<div class="fixed inset-0 bg-background/80 backdrop-blur-sm z-50 hidden" id="mobile-sidebar-overlay">
<nav class="fixed left-0 top-0 h-screen w-[280px] bg-surface-container border-r border-outline-variant flex flex-col p-4 shadow-none transform -translate-x-full transition-transform duration-300" id="mobile-sidebar">
<div class="flex items-center justify-between mb-8 px-2">
<span class="font-display-lg-mobile text-display-lg-mobile text-primary tracking-tight">Nexa AI</span>
<button class="p-2 text-on-surface-variant hover:text-primary transition-colors" id="close-sidebar">
<span class="material-symbols-outlined">close</span>
</button>
</div>
<button class="w-full mb-6 bg-primary-container text-[#080A0C] font-label-sm text-label-sm rounded-lg py-3 px-4 flex items-center justify-center gap-2 shadow-[inset_0_1px_0_rgba(255,255,255,0.4)] hover:bg-surface-tint transition-colors">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 0;">add</span>
                New Chat
            </button>
<div class="flex-1 overflow-y-auto flex flex-col gap-1">
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-primary font-bold border-r-2 border-primary bg-surface-container-high transition-colors duration-200" href="#">
<span class="material-symbols-outlined">history</span>
                    Today
                 </a>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200" href="#">
<span class="material-symbols-outlined">calendar_today</span>
                    Yesterday
                 </a>
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200" href="#">
<span class="material-symbols-outlined">inventory_2</span>
                    Archive
                 </a>
</div>
<div class="mt-auto pt-4 border-t border-outline-variant">
<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-on-surface-variant font-medium hover:bg-surface-container-high transition-colors duration-200" href="#">
<span class="material-symbols-outlined">settings</span>
                    Settings
                 </a>
</div>
</nav>
</div>
<script>
        // Auto-scroll chat to bottom
        const chatContainer = document.getElementById('chat-container');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    </script>
</body></html>