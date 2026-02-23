# Fix style.css
$cssPath = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\style.css"
$css = [System.IO.File]::ReadAllText($cssPath, [System.Text.Encoding]::UTF8)
# Replace broken arrow characters (U+FFFD) or literal arrows with CSS escape
$css = [regex]::Replace($css, "content:\s*'[^']*[^']*'", "content: '\2192'")
$css = [regex]::Replace($css, "content:\s*'→'", "content: '\2192'")
$css = [regex]::Replace($css, "content:\s*' →'", "content: ' \2192'")
[System.IO.File]::WriteAllText($cssPath, $css, (New-Object System.Text.UTF8Encoding($false)))

# Fix style_banner.css
$bannerPath = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\style_banner.css"
if (Test-Path $bannerPath) {
    $banner = [System.IO.File]::ReadAllText($bannerPath, [System.Text.Encoding]::UTF8)
    $banner = [regex]::Replace($banner, "content:\s*'[^']*[^']*'", "content: '\2192'")
    $banner = [regex]::Replace($banner, "content:\s*'→'", "content: '\2192'")
    [System.IO.File]::WriteAllText($bannerPath, $banner, (New-Object System.Text.UTF8Encoding($false)))
}

Write-Host "Fixed CSS arrows using escapes."
