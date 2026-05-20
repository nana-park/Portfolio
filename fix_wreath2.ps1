$leftBranch = '<svg class="w-[40px] h-[70px] text-zinc-800" viewBox="0 0 50 100" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
    <path d="M 35 95 Q 15 60 40 10" stroke="currentColor" fill="none" stroke-width="2"/>
    <path d="M 33 88 Q 15 80 20 70 Q 30 75 33 88" />
    <path d="M 33 88 Q 45 90 50 80 Q 40 75 33 88" />
    <path d="M 28 73 Q 10 65 15 55 Q 25 60 28 73" />
    <path d="M 28 73 Q 40 75 45 65 Q 35 60 28 73" />
    <path d="M 25 58 Q 5 50 10 40 Q 20 45 25 58" />
    <path d="M 25 58 Q 37 60 42 50 Q 32 45 25 58" />
    <path d="M 26 43 Q 10 35 15 25 Q 25 30 26 43" />
    <path d="M 26 43 Q 38 45 43 35 Q 33 30 26 43" />
    <path d="M 31 28 Q 15 20 20 10 Q 30 15 31 28" />
    <path d="M 31 28 Q 43 30 48 20 Q 38 15 31 28" />
    <path d="M 38 13 Q 25 5 35 0 Q 45 5 38 13" />
</svg>'

$rightBranch = '<svg class="w-[40px] h-[70px] text-zinc-800" viewBox="0 0 50 100" fill="currentColor" xmlns="http://www.w3.org/2000/svg" style="transform: scaleX(-1);">
    <path d="M 35 95 Q 15 60 40 10" stroke="currentColor" fill="none" stroke-width="2"/>
    <path d="M 33 88 Q 15 80 20 70 Q 30 75 33 88" />
    <path d="M 33 88 Q 45 90 50 80 Q 40 75 33 88" />
    <path d="M 28 73 Q 10 65 15 55 Q 25 60 28 73" />
    <path d="M 28 73 Q 40 75 45 65 Q 35 60 28 73" />
    <path d="M 25 58 Q 5 50 10 40 Q 20 45 25 58" />
    <path d="M 25 58 Q 37 60 42 50 Q 32 45 25 58" />
    <path d="M 26 43 Q 10 35 15 25 Q 25 30 26 43" />
    <path d="M 26 43 Q 38 45 43 35 Q 33 30 26 43" />
    <path d="M 31 28 Q 15 20 20 10 Q 30 15 31 28" />
    <path d="M 31 28 Q 43 30 48 20 Q 38 15 31 28" />
    <path d="M 38 13 Q 25 5 35 0 Q 45 5 38 13" />
</svg>'

$skHtml = '
                <div class="relative group">
                    <div class="flex items-center gap-4">
                        ' + $leftBranch + '
                        <div class="text-center pb-2">
                            <p class="text-[10px] text-zinc-500 uppercase tracking-widest font-mono mb-1">Selected by</p>
                            <p class="text-[15px] font-bold text-zinc-900 leading-tight">SK AI<br>Accelerator</p>
                        </div>
                        ' + $rightBranch + '
                    </div>
                </div>'

$html = Get-Content -Path "index.html" -Raw -Encoding UTF8

$regexSK = '(?s)<!-- Award 2: SK AI -->.*?</div>\s*</div>\s*</div>\s*<!-- New Concept Diagram Block -->'
$html = $html -replace $regexSK, ("<!-- Award 2: SK AI -->
" + $skHtml + "
            </div>

            <!-- New Concept Diagram Block -->")

Set-Content -Path "index.html" -Value $html -Encoding UTF8
Write-Host "Done"
