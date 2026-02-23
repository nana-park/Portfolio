import os

file_path = r"C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\projects\hopzie.html"

# The new content for the 2-column layout
new_html = """                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <!-- Visual Column (The Problem: Messy YouTube Description) -->
                    <div
                        class="glass-card p-0 bg-[#050505] relative overflow-hidden group border border-white/5 flex items-center justify-center min-h-[500px]">
                        <!-- Centering & Scaling Wrapper -->
                        <div class="scale-[0.65] sm:scale-[0.8] origin-center">
                            <!-- Mockup Container (Fixed Phone Size) -->
                            <div
                                class="relative w-[300px] h-[600px] bg-[#0f0f0f] rounded-[2.5rem] shadow-2xl border-[6px] border-[#2a2a2a] overflow-hidden flex flex-col shrink-0">

                                <!-- 1. YouTube Header -->
                                <div
                                    class="flex justify-between items-center px-4 py-3 border-b border-white/5 bg-[#0f0f0f] z-20 h-12 shrink-0">
                                    <div class="flex items-center gap-1">
                                        <!-- Real SVG Logo Icon -->
                                        <div class="w-7 h-5 flex items-center justify-center">
                                            <svg viewBox="0 0 68 48" class="w-full h-full text-red-600 fill-current">
                                                <path
                                                    d="M66.52,7.74c-0.78-2.93-2.49-5.41-5.42-6.19C55.79,.13,34,0,34,0S12.21,.13,6.9,1.55 C3.97,2.33,2.27,4.81,1.48,7.74C0.06,13.05,0,24,0,24s0.06,10.95,1.48,16.26c0.78,2.93,2.49,5.41,5.42,6.19 C12.21,47.87,34,48,34,48s21.79-0.13,27.1-1.55c2.93-0.78,4.64-3.26,5.42-6.19C67.94,34.95,68,24,68,24S67.94,13.05,66.52,7.74z">
                                                </path>
                                                <path d="M 45,24 27,14 27,34" fill="white"></path>
                                            </svg>
                                        </div>
                                        <span class="text-white font-bold text-sm tracking-tighter leading-none"
                                            style="font-family: 'Roboto Condensed', sans-serif;">YouTube</span>
                                    </div>
                                    <div class="flex items-center gap-4 text-white">
                                        <i class="fas fa-cast text-xs"></i>
                                        <i class="fas fa-bell text-xs"></i>
                                        <i class="fas fa-search text-xs"></i>
                                        <div
                                            class="w-6 h-6 rounded-full bg-purple-600 text-[10px] flex items-center justify-center font-bold">
                                            M</div>
                                    </div>
                                </div>

                                <!-- 2. Video Player Placeholder -->
                                <div
                                    class="w-full aspect-video bg-[#1a1a1a] relative group/video cursor-pointer shrink-0">
                                    <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80"
                                        class="w-full h-full object-cover opacity-60 group-hover/video:opacity-40 transition-opacity">
                                    <div class="absolute inset-0 flex items-center justify-center">
                                        <i
                                            class="fas fa-play text-white text-3xl opacity-80 drop-shadow-lg group-hover/video:scale-110 transition-transform"></i>
                                    </div>
                                    <!-- Progress Bar -->
                                    <div class="absolute bottom-0 left-0 w-full h-1 bg-white/20">
                                        <div class="w-1/3 h-full bg-red-600"></div>
                                    </div>
                                    <div
                                        class="absolute bottom-2 right-2 bg-black/80 px-1.5 py-0.5 rounded text-[10px] text-white font-medium">
                                        12:45</div>
                                </div>

                                <!-- 3. Video Info -->
                                <div class="px-4 py-3 shrink-0">
                                    <h1 class="text-white text-sm font-bold leading-snug mb-1.5 line-clamp-2">
                                        Minimalist Desk Setup 2024 | Productivity Tools & Gear Review 💻
                                    </h1>
                                    <div class="text-[11px] text-gray-400 mb-4 flex items-center gap-1">
                                        <span>125K views</span>
                                        <span>•</span>
                                        <span>2 days ago</span>
                                    </div>

                                    <!-- Channel Bar -->
                                    <div class="flex items-center justify-between mb-4">
                                        <div class="flex items-center gap-3">
                                            <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                                                class="w-9 h-9 rounded-full object-cover">
                                            <div class="flex flex-col justify-center">
                                                <div class="text-white text-xs font-bold leading-tight">Creator
                                                    Techie</div>
                                                <div class="text-[10px] text-gray-400 leading-tight mt-0.5">
                                                    48.2K
                                                </div>
                                            </div>
                                        </div>
                                        <button
                                            class="bg-white text-black text-[11px] font-bold px-3.5 py-1.5 rounded-full hover:bg-gray-200 transition-colors">Subscribe</button>
                                    </div>

                                    <!-- Action Buttons (Dimmed) -->
                                    <div class="flex gap-2 overflow-x-auto no-scrollbar mb-4 opacity-60">
                                        <div
                                            class="flex items-center gap-1.5 bg-[#1a1a1a] px-3 py-1.5 rounded-full text-white text-[11px] border border-white/5 whitespace-nowrap">
                                            <i class="far fa-thumbs-up"></i> 4.5K
                                        </div>
                                        <div
                                            class="flex items-center gap-1.5 bg-[#1a1a1a] px-3 py-1.5 rounded-full text-white text-[11px] border border-white/5 whitespace-nowrap">
                                            <i class="far fa-comment-alt"></i> Share
                                        </div>
                                    </div>
                                </div>

                                <!-- 4. Description Box (THE PAIN POINT) -->
                                <div
                                    class="flex-1 bg-[#1a1a1a] mx-4 rounded-xl p-3 relative overflow-hidden flex flex-col border border-[#333] min-h-0 mb-4">
                                    <div class="flex justify-between items-center mb-2 shrink-0">
                                        <div class="text-white text-xs font-bold">Description</div>
                                        <i class="fas fa-times text-gray-400 text-xs cursor-pointer"></i>
                                    </div>

                                    <!-- Pain Point Content: Messy Links -->
                                    <div class="messy-scroll overflow-y-auto flex-1 pr-1 space-y-3 relative">
                                        <p class="text-gray-300 text-[11px] leading-relaxed">
                                            Here are all the links to the products I mentioned in the video!
                                            Check
                                            them out below 👇
                                        </p>

                                        <!-- THE CLUTTER -->
                                        <div class="bg-black/30 rounded-lg p-3 border border-red-500/30 relative">
                                            <!-- Pain Point Badge -->
                                            <div
                                                class="absolute -top-2 -right-2 bg-red-500 text-white text-[9px] font-bold px-2 py-0.5 rounded-full shadow-lg z-10 animate-subtle-pulse border border-[#1a1a1a]">
                                                Manual & Messy
                                            </div>

                                            <div class="space-y-3">
                                                <!-- Item 1 -->
                                                <div>
                                                    <div class="text-[11px] text-gray-300 font-semibold mb-0.5">
                                                        1.
                                                        Mechanical Keyboard (Keychron Q1)</div>
                                                    <div
                                                        class="text-[10px] text-blue-400 truncate cursor-pointer hover:underline opacity-80">
                                                        https://coupang.com/vp/products/12345?itemId=...</div>
                                                </div>
                                                <!-- Item 2 -->
                                                <div>
                                                    <div class="text-[11px] text-gray-300 font-semibold mb-0.5">
                                                        2.
                                                        Logitech MX Master 3S Mouse</div>
                                                    <div
                                                        class="text-[10px] text-blue-400 truncate cursor-pointer hover:underline opacity-80">
                                                        https://amazon.com/dp/B09HM94VDS/ref=...</div>
                                                </div>
                                                <!-- Item 3 -->
                                                <div>
                                                    <div class="text-[11px] text-gray-300 font-semibold mb-0.5">
                                                        3.
                                                        BenQ ScreenBar Halo</div>
                                                    <div
                                                        class="text-[10px] text-blue-400 truncate cursor-pointer hover:underline opacity-80">
                                                        https://smartstore.naver.com/benq/products/...</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Fade out effect at bottom to imply more scrolling -->
                                    <div
                                        class="absolute bottom-0 left-0 w-full h-8 bg-gradient-to-t from-[#1a1a1a] to-transparent pointer-events-none">
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>

                    <!-- Text Column (Right) -->
                    <div class="flex flex-col gap-6">
                        <!-- Consumer Card -->
                        <div
                            class="glass-panel p-8 bg-gradient-to-br from-white/5 to-transparent relative overflow-hidden flex-1 border border-white/5">
                            <div class="relative z-10">
                                <div class="flex items-center gap-4 mb-6">
                                    <div
                                        class="w-10 h-10 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-400">
                                        <i class="fas fa-user-tag"></i>
                                    </div>
                                    <h3 class="text-xl font-bold text-white">For Consumers</h3>
                                </div>
                                <h4 class="text-sm font-semibold text-zinc-500 mb-6 uppercase tracking-wide">
                                    Disconnected
                                    Journey</h4>

                                <ul class="space-y-4 text-sm text-zinc-400 leading-relaxed">
                                    <li class="flex items-start gap-3">
                                        <span class="text-red-400 mt-1 text-xs shrink-0"><i
                                                class="fas fa-times"></i></span>
                                        <span><strong>The Loop:</strong> Endless switching between YouTube comments and
                                            product pages.</span>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="text-red-400 mt-1 text-xs shrink-0"><i
                                                class="fas fa-times"></i></span>
                                        <span><strong>Blind Clicks:</strong> In our product, prices aren't immediately
                                            visible, but stock status is checkable. However, users can view products from
                                            other videos by the same creator all at once.</span>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <!-- Creator Card -->
                        <div
                            class="glass-panel p-8 bg-gradient-to-br from-white/5 to-transparent relative overflow-hidden flex-1 border border-white/5">
                            <div class="relative z-10">
                                <div class="flex items-center gap-4 mb-6">
                                    <div
                                        class="w-10 h-10 rounded-full bg-amber-500/10 flex items-center justify-center text-amber-500">
                                        <i class="fas fa-video"></i>
                                    </div>
                                    <h3 class="text-xl font-bold text-white">For Creators</h3>
                                </div>
                                <h4 class="text-sm font-semibold text-zinc-500 mb-6 uppercase tracking-wide">
                                    Administrative
                                    Burden</h4>

                                <ul class="space-y-4 text-sm text-zinc-400 leading-relaxed">
                                    <li class="flex items-start gap-3">
                                        <span class="text-red-400 mt-1 text-xs shrink-0"><i
                                                class="fas fa-times"></i></span>
                                        <span><strong>Manual Curation:</strong> Organising purchase links in comments is
                                            a massive time-sink.</span>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="text-red-400 mt-1 text-xs shrink-0"><i
                                                class="fas fa-times"></i></span>
                                        <span><strong>Dead Ends:</strong> Links break when items sell out, requiring
                                            constant updates.</span>
                                    </li>
                                    <li class="flex items-start gap-3">
                                        <span class="text-red-400 mt-1 text-xs shrink-0"><i
                                                class="fas fa-times"></i></span>
                                        <span><strong>Fee Chaos:</strong> Hard to compare commission rates across
                                            different open markets.</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
"""


print("Script starting...", flush=True)
try:
    with open(file_path, "r", encoding="utf-8") as f:
        print("Reading file...", flush=True)
        lines = f.readlines()
        print(f"Read {len(lines)} lines.", flush=True)

    # Replace lines 416 to 914 (inclusive, 1-based)
    # 416 -> index 415
    # 914 -> index 913
    # Slice to keep: :415 and 914:
    # Note: 914: starts at index 914, which is line 915. Correct.

    updated_lines = lines[:415] + [new_html + "\n"] + lines[914:]

    print(f"Writing {len(updated_lines)} lines...", flush=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print("File updated successfully.", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
    import traceback
    traceback.print_exc()

