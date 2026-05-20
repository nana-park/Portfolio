Add-Type -AssemblyName System.Drawing
$i1 = [System.Drawing.Image]::FromFile("C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_DIVE.png")
Write-Host "DIVE: $($i1.Width)x$($i1.Height)"
$i1.Dispose()

$i2 = [System.Drawing.Image]::FromFile("C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_news.png")
Write-Host "News: $($i2.Width)x$($i2.Height)"
$i2.Dispose()

$i3 = [System.Drawing.Image]::FromFile("C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_hopzie.png")
Write-Host "Hopzie: $($i3.Width)x$($i3.Height)"
$i3.Dispose()

$i4 = [System.Drawing.Image]::FromFile("C:\Users\able2\.gemini\antigravity\scratch\portfolio\nahyun_imported\image_source\Projects_Products\thumnail_just do it.png")
Write-Host "Just do it: $($i4.Width)x$($i4.Height)"
$i4.Dispose()
