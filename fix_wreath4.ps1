$leftBranch = '<div class="w-[50px] h-[80px] bg-no-repeat bg-left mix-blend-multiply opacity-90" style="background-image: url(''images/award.png''); background-size: 200% auto;"></div>'
$rightBranch = '<div class="w-[50px] h-[80px] bg-no-repeat bg-right mix-blend-multiply opacity-90" style="background-image: url(''images/award.png''); background-size: 200% auto;"></div>'

$googleHtml = '
                <div class="relative group w-full md:w-[280px]">
                    <div class="flex items-center justify-center gap-3">
                        ' + $leftBranch + '
                        <div class="text-center pb-1 flex-1">
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
                        <div class="text-center pb-1 flex-1">
                            <p class="text-[10px] text-zinc-500 uppercase tracking-widest font-mono mb-1">Selected by</p>
                            <p class="text-[14px] font-bold text-zinc-900 leading-[1.3]">SK AI<br>Accelerator</p>
                        </div>
                        ' + $rightBranch + '
                    </div>
                </div>'

$html = Get-Content -Path "index.html" -Raw -Encoding UTF8

$regexGoogle = '(?s)<div class="relative group w-full md:w-\[280px\]">\s*<div class="flex items-center justify-center gap-3">.*?Google for Media<br>Startups</p>\s*</div>.*?</div>\s*</div>'
$html = $html -replace $regexGoogle, $googleHtml

$regexSK = '(?s)<div class="relative group w-full md:w-\[280px\]">\s*<div class="flex items-center justify-center gap-3">.*?SK AI<br>Accelerator</p>\s*</div>.*?</div>\s*</div>'
$html = $html -replace $regexSK, $skHtml

Set-Content -Path "index.html" -Value $html -Encoding UTF8
Write-Host "Done"
