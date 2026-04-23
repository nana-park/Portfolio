$content = Get-Content -Raw -Encoding UTF8 index.html

$newTravelBlock = @"
                        <!-- Travel Gallery -->
                        <div id="gallery-col-travel" class="right-gallery grid-cols-2 md:grid-cols-3 gap-3 w-full hidden">
                            <div class="flex flex-col gap-3">
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Korea">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Korea/Jeju-1.jpg" alt="Travel Jeju" class="w-full aspect-square object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Jeju, Korea</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Asia">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Asia/Hongkong-1.jpg" alt="Travel Hongkong" class="w-full aspect-[4/5] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Hong Kong</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Europe">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Europe/Georgia-1.jpg" alt="Travel Georgia" class="w-full aspect-square object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Georgia</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Asia">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Asia/Thai-1.jpg" alt="Travel Thai" class="w-full aspect-[4/5] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Thailand</h4>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col gap-3">
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Korea">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Korea/울릉도.jpg" alt="Travel Ulleungdo" class="w-full aspect-[4/5] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Ulleungdo, Korea</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Asia">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Asia/Indonesia-1.jpg" alt="Travel Indonesia" class="w-full aspect-[3/4] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Indonesia</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Europe">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Europe/Georgia-2.jpg" alt="Travel Georgia" class="w-full aspect-square object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Georgia</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="South America">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/South America/Peru-1.jpg" alt="Travel Peru" class="w-full aspect-[4/5] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Peru</h4>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col gap-3">
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Korea">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Korea/전라도-고성-1.jpg" alt="Travel Goseong" class="w-full aspect-[3/4] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Goseong, Korea</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="Asia">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/Asia/Maleisia-1.jpg" alt="Travel Malaysia" class="w-full aspect-square object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Malaysia</h4>
                                    </div>
                                </div>
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default" data-dest="South America">
                                    <img src="nahyun_imported/image_source/About_Life/Travel/South America/Chile-1.jpg" alt="Travel Chile" class="w-full aspect-[4/3] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Chile</h4>
                                    </div>
                                </div>
                            </div>
                        </div>
"@

$pattern = '(?s)<!-- Travel Gallery -->.*?(?=<!-- Volunteering Gallery -->)'
$content = $content -replace $pattern, $newTravelBlock

# Also revert JS changes if any
$jsOld = "if (!gal.classList.contains('columns-2')) gal.classList.add('grid');
                        else gal.classList.add('block');"
$jsNew = "gal.classList.add('grid');"
$content = $content.Replace($jsOld, $jsNew)

# Now, implement the REAL JS FIX to solve the "Left column empty" bug when filtering inside rigid columns:
# When filtering travel images, we need to completely rearrange them!
# We can collect all images in the gallery, filter them, and then re-apportion them evenly among the 3 columns!

$jsFilterLogicPattern = '(?s)document.querySelectorAll\(''.travel-dest-btn''\).forEach\(b => b.addEventListener\(''click'', \(e\) => {.*?}\)\);'

$jsFilterReplacement = @"
            document.querySelectorAll('.travel-dest-btn').forEach(b => b.addEventListener('click', (e) => {
                e.preventDefault();
                const dest = e.currentTarget.getAttribute('data-filter');
                
                // Active state
                document.querySelectorAll('.travel-dest-btn').forEach(btn => {
                    btn.classList.remove('text-[#d97706]', 'font-bold');
                    btn.classList.add('text-zinc-400', 'font-medium');
                    const dot = btn.querySelector('.indicator-dot');
                    if(dot) dot.remove();
                });
                const clicked = e.currentTarget;
                clicked.classList.add('text-[#d97706]', 'font-bold');
                clicked.classList.remove('text-zinc-400', 'font-medium');
                clicked.insertAdjacentHTML('afterbegin', '<span class="w-[5px] h-[5px] rounded-full bg-[#d97706] mr-2 indicator-dot"></span>');

                // DOM Rearrangement Fix for 3 rigid columns
                const travelGallery = document.getElementById('gallery-col-travel');
                if(!travelGallery) return;
                
                const columns = Array.from(travelGallery.querySelectorAll('.flex.flex-col'));
                const allItems = Array.from(travelGallery.querySelectorAll('.group'));
                
                // Get all matching items
                const visibleItems = allItems.filter(item => dest === 'All Destinations' || item.getAttribute('data-dest') === dest);
                const hiddenItems = allItems.filter(item => dest !== 'All Destinations' && item.getAttribute('data-dest') !== dest);
                
                // Hide non-matching items
                hiddenItems.forEach(item => item.style.display = 'none');
                
                // Show matching items and redistribute into columns sequentially
                visibleItems.forEach((item, index) => {
                    item.style.display = 'block';
                    const targetColIndex = index % columns.length; // 0, 1, 2, 0, 1, 2...
                    columns[targetColIndex].appendChild(item);
                });
            }));
"@

$content = $content -replace $jsFilterLogicPattern, $jsFilterReplacement

Set-Content -Path index.html -Value $content -Encoding UTF8
