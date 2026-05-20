$leaves = ''
$numLeaves = 15

for ($i = 0; $i -lt $numLeaves; $i++) {
    $t = $i / ($numLeaves - 1)
    
    # Arc from bottom-center to top-left
    $angle = -[Math]::PI/2 + ([Math]::PI * 0.45) * $t
    $r = 75
    $cx = 95
    $cy = 100
    
    $x = $cx + $r * [Math]::Cos($angle)
    $y = $cy + $r * [Math]::Sin($angle)
    
    $tangent = $angle + [Math]::PI/2
    
    # Inner leaf (towards center)
    $innerRot = ($tangent - 0.45) * 180 / [Math]::PI
    $leaves += '<path d="M0,0 C-8,-10 -16,-5 -20,5 C-12,10 -4,5 0,0" transform="translate(' + [Math]::Round($x,2) + ',' + [Math]::Round($y,2) + ') scale(0.65) rotate(' + [Math]::Round($innerRot,2) + ')" fill="currentColor"/>'
    
    # Outer leaf (away from center)
    $outerRot = ($tangent + 0.45) * 180 / [Math]::PI
    $leaves += '<path d="M0,0 C8,-10 16,-5 20,5 C12,10 4,5 0,0" transform="translate(' + [Math]::Round($x,2) + ',' + [Math]::Round($y,2) + ') scale(0.7) rotate(' + [Math]::Round($outerRot,2) + ')" fill="currentColor"/>'
}

$svg = '<svg class="w-[200px] h-[150px] text-zinc-900 mb-2" viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Left Branch -->
    <g transform="translate(5, -15)">
        ' + $leaves + '
        <path d="M95,100 A75,75 0 0,0 20,25" fill="none" stroke="currentColor" stroke-width="1.5"/>
    </g>
    <!-- Right Branch -->
    <g transform="translate(195, -15) scale(-1, 1)">
        ' + $leaves + '
        <path d="M95,100 A75,75 0 0,0 20,25" fill="none" stroke="currentColor" stroke-width="1.5"/>
    </g>
</svg>'

$html = Get-Content -Path "index.html" -Raw -Encoding UTF8

$regex = '(?s)<svg class="w-\[230px\] h-\[65px\] text-zinc-800 mb-2" viewBox="0 0 200 75" fill="none".*?</svg>'
$html = $html -replace $regex, $svg

Set-Content -Path "index.html" -Value $html -Encoding UTF8
Write-Host "Done"
