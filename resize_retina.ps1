$path1 = "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_news.png"
$path2 = "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_DIVE.png"

Add-Type -AssemblyName System.Drawing

function Resize-Image {
    param([string]$path, [string]$out, [int]$w)
    $img = [System.Drawing.Image]::FromFile($path)
    $h = [math]::Round($img.Height * ($w / $img.Width))
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    
    # Highest quality settings to preserve crisp UI text
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    
    $g.DrawImage($img, 0, 0, $w, $h)
    $g.Dispose()
    $img.Dispose()
    $bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
}

# 1200px is the optimal 2x Retina resolution for a ~600px container
Resize-Image $path1 "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_news_web.png" 1200
Resize-Image $path2 "C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_DIVE_web.png" 1200
