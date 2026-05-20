$path1 = "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_news.png"
$path2 = "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_DIVE.png"

Add-Type -AssemblyName System.Drawing

function Resize-Image {
    param([string]$path, [string]$out, [int]$w)
    $img = [System.Drawing.Image]::FromFile($path)
    $h = [math]::Round($img.Height * ($w / $img.Width))
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.DrawImage($img, 0, 0, $w, $h)
    $g.Dispose()
    $img.Dispose()
    $bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
}

Resize-Image $path1 "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_news_web.png" 800
Resize-Image $path2 "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_DIVE_web.png" 800
