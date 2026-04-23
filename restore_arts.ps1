$content = Get-Content index.html -Raw -Encoding UTF8

$pattern = '(?s)<div class="w-full relative group">\s*<img src="nahyun_imported/image_source/About_Life/Culinary/KakaoTalk_20260423_000013760_02.jpg".*?<!-- Travel Gallery -->'

$replacement = @"
                            <div class="w-full relative group">
                                <img src="nahyun_imported/image_source/About_Life/Culinary/KakaoTalk_20260423_000013760_02.jpg" alt="Culinary Gallery" class="w-full aspect-[4/3] object-cover object-center rounded-[3px] transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                            </div>
                            <div class="w-full relative group">
                                <img src="nahyun_imported/image_source/About_Life/Culinary/KakaoTalk_20260422_235853863_13.jpg" alt="Culinary Gallery" class="w-full aspect-square object-cover object-center rounded-[3px] transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                            </div>
                            <div class="w-full relative group">
                                <img src="nahyun_imported/image_source/About_Life/Culinary/1.jpg" alt="Culinary Gallery" class="w-full aspect-[4/5] object-cover object-[center_25%] rounded-[3px] transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                            </div>
                        </div>
                    </div>
                        
                        <!-- Sports Gallery -->
                        <div id="gallery-col-sports" class="right-gallery grid-cols-2 md:grid-cols-3 gap-3 w-full hidden">
                            <div class="flex flex-col gap-3">
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default">
                                    <img src="nahyun_imported/image_source/About_Life/Sports/KakaoTalk_20260423_011157587_01.jpg" alt="Climbing" class="w-full aspect-square object-cover object-[center_60%] transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Climbing</h4>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col gap-3">
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default">
                                    <img src="nahyun_imported/image_source/About_Life/Sports/KakaoTalk_20260423_011157587.jpg" alt="Jiu-jitsu" class="w-full aspect-[4/3] object-cover object-top transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Jiu-jitsu</h4>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col gap-3"></div>
                        </div>

                        <!-- Arts Gallery -->
                        <div id="gallery-col-arts" class="right-gallery grid-cols-2 md:grid-cols-3 gap-3 w-full hidden">
                            <div class="flex flex-col gap-3">
                                <div class="w-full relative group overflow-hidden rounded-[3px] cursor-default">
                                    <img src="nahyun_imported/image_source/About_Life/Arts/KakaoTalk_20260423_010048901_01.jpg" alt="Michel Henry" class="w-full aspect-[3/4] object-cover object-center transform group-hover:scale-[1.03] transition-transform duration-500 ease-out">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#150d0a]/80 via-[#150d0a]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    <div class="absolute bottom-0 left-0 w-full px-4 pb-3 flex flex-col justify-end translate-y-3 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-300">
                                        <h4 class="text-white font-sans text-[11px] font-medium tracking-wider">Michel Henry</h4>
                                    </div>
                                </div>
                            </div>
                            <div class="flex flex-col gap-3"></div>
                            <div class="flex flex-col gap-3"></div>
                        </div>
                        
                        <!-- Travel Gallery -->
"@

$content = $content -replace $pattern, $replacement
Set-Content index.html -Value $content -Encoding UTF8
