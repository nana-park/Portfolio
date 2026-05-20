$leftBranch = '<svg class="w-[50px] h-[90px] text-zinc-900" viewBox="0 0 60 120" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
    <!-- Main stem -->
    <path d="M 45,115 Q 15,80 35,10" stroke="currentColor" stroke-width="2" fill="none" />
    
    <!-- Leaves generated perfectly -->
    <!-- Leaf 1 (bottom) -->
    <path d="M 41,105 C 10,100 15,70 34,92 Z" />
    <path d="M 41,105 C 60,110 65,80 34,92 Z" />
    
    <!-- Leaf 2 -->
    <path d="M 33,91 C 5,85 10,55 29,78 Z" />
    <path d="M 33,91 C 55,95 60,65 29,78 Z" />
    
    <!-- Leaf 3 -->
    <path d="M 28,75 C 0,65 10,35 25,60 Z" />
    <path d="M 28,75 C 50,80 55,50 25,60 Z" />
    
    <!-- Leaf 4 -->
    <path d="M 24,57 C -5,45 5,15 23,43 Z" />
    <path d="M 24,57 C 45,60 50,30 23,43 Z" />
    
    <!-- Leaf 5 -->
    <path d="M 23,40 C -5,25 10,-5 26,25 Z" />
    <path d="M 23,40 C 45,40 45,10 26,25 Z" />
    
    <!-- Top Leaf -->
    <path d="M 34,10 C 20,-5 50,-5 35,12 Z" />
</svg>'

$rightBranch = '<svg class="w-[50px] h-[90px] text-zinc-900" viewBox="0 0 60 120" fill="currentColor" xmlns="http://www.w3.org/2000/svg" style="transform: scaleX(-1);">
    <path d="M 45,115 Q 15,80 35,10" stroke="currentColor" stroke-width="2" fill="none" />
    <path d="M 41,105 C 10,100 15,70 34,92 Z" />
    <path d="M 41,105 C 60,110 65,80 34,92 Z" />
    <path d="M 33,91 C 5,85 10,55 29,78 Z" />
    <path d="M 33,91 C 55,95 60,65 29,78 Z" />
    <path d="M 28,75 C 0,65 10,35 25,60 Z" />
    <path d="M 28,75 C 50,80 55,50 25,60 Z" />
    <path d="M 24,57 C -5,45 5,15 23,43 Z" />
    <path d="M 24,57 C 45,60 50,30 23,43 Z" />
    <path d="M 23,40 C -5,25 10,-5 26,25 Z" />
    <path d="M 23,40 C 45,40 45,10 26,25 Z" />
    <path d="M 34,10 C 20,-5 50,-5 35,12 Z" />
</svg>'

$googleHtml = '
                <div class="relative group w-full md:w-[280px]">
                    <div class="flex items-center justify-center gap-3">
                        ' + $leftBranch + '
                        <div class="text-center pb-2 flex-1">
                            <p class="text-[10px] text-zinc-500 uppercase tracking-widest font-mono mb-1">Funded by</p>
                            <p class="text-[14px] font-bold text-zinc-900 leading-[1.3]">Google for Media<br>Startups</p>
                        </div>
                        ' + $rightBranch + '
                    </div>
                </div>'

$skHtml = '
                <div class="relative group w-full md:w-[280px]">
                    <div class="flex items-center justify-center gap-3">
                        ' + $leftBranch + '
                        <div class="text-center pb-2 flex-1">
                            <p class="text-[10px] text-zinc-500 uppercase tracking-widest font-mono mb-1">Selected by</p>
                            <p class="text-[14px] font-bold text-zinc-900 leading-[1.3]">SK AI<br>Accelerator</p>
                        </div>
                        ' + $rightBranch + '
                    </div>
                </div>'

$html = Get-Content -Path "index.html" -Raw -Encoding UTF8

$regexGoogle = '(?s)<div class="relative group">\s*<div class="flex items-center gap-4">.*?Google for Media<br>Startups</p>\s*</div>.*?</div>\s*</div>'
$html = $html -replace $regexGoogle, $googleHtml

$regexSK = '(?s)<div class="relative group">\s*<div class="flex items-center gap-4">.*?SK AI<br>Accelerator</p>\s*</div>.*?</div>\s*</div>'
$html = $html -replace $regexSK, $skHtml

Set-Content -Path "index.html" -Value $html -Encoding UTF8
Write-Host "Done"
