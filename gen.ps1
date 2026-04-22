$dir = "C:\Users\able2\.gemini\antigravity\scratch\Portfolio\nahyun_imported\image_source\About_Life\Culinary"
$allFiles = Get-ChildItem -Path $dir -Filter "*.jpg" | Select-Object -ExpandProperty Name

$req = @(
    "KakaoTalk_20260422_235853863_06.jpg",
    "KakaoTalk_20260422_235853863_07.jpg",
    "KakaoTalk_20260422_235853863_08.jpg",
    "KakaoTalk_20260423_004121914.jpg",
    "KakaoTalk_20260422_235853863_10.jpg",
    "KakaoTalk_20260422_235853863_09.jpg"
)

$pool = $allFiles | Where-Object { $req -notcontains $_ }
$pool = $pool | Get-Random -Count $pool.Count

$col1 = @("KakaoTalk_20260422_235853863_06.jpg", "KakaoTalk_20260423_004121914.jpg")
$col2 = @("KakaoTalk_20260422_235853863_07.jpg", "KakaoTalk_20260422_235853863_10.jpg")
$col3 = @("KakaoTalk_20260422_235853863_08.jpg", "KakaoTalk_20260422_235853863_09.jpg")

$idx = 0
foreach ($f in $pool) {
    if ($idx % 3 -eq 0) { $col1 += $f }
    elseif ($idx % 3 -eq 1) { $col2 += $f }
    else { $col3 += $f }
    $idx++
}

$script:aspects = @('aspect-square', 'aspect-[3/4]', 'aspect-[4/5]', 'aspect-[4/3]')

$html = "<div class=`"grid grid-cols-2 md:grid-cols-3 gap-3 w-full flex-grow`" id=`"life-gallery`">`n"

function GetColHtml($arr) {
    $out = "    <div class=`"flex flex-col gap-3`">`n"
    foreach ($f in $arr) {
        $aspect = $script:aspects | Get-Random
        $out += "        <div class=`"w-full relative group`">`n"
        $out += "            <img src=`"nahyun_imported/image_source/About_Life/Culinary/$f`" alt=`"Culinary Gallery`" class=`"w-full $aspect object-cover object-center rounded-[3px] hover:opacity-90 cursor-pointer transition-opacity`">`n"
        $out += "        </div>`n"
    }
    $out += "    </div>`n"
    return $out
}

$html += GetColHtml $col1
$html += GetColHtml $col2
$html += GetColHtml $col3
$html += "</div>"

Set-Content -Path "temp_html.txt" -Value $html
