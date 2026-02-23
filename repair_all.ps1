$utf8 = New-Object System.Text.UTF8Encoding($false)

# 1. FIX HTML (index.html)
$htmlPath = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$html = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)

# Replacement mappings for HTML
# 🌐 -> &#127760;
# ★ -> &#9733;
# Phonetics
# b͈aŋ -> b&#840;a&#331;
# hjʌn -> hj&#652;n

$html = [regex]::Replace($html, "<span>[^\w\s]{1,5}</span> English", "<span>&#127760;</span> English")
$html = $html.Replace('★★★★★', "&#9733;&#9733;&#9733;&#9733;&#9733;")
# Match variations of the broken phonetics in HTML
$html = [regex]::Replace($html, '<div class="id-phonetic-symbol">[^<]+</div>', '<div class="id-phonetic-symbol">b&#840;a&#331;</div>')
$html = [regex]::Replace($html, '<div class="id-faded-symbol">[^<]+</div>', '<div class="id-faded-symbol">hj&#652;n</div>')

[System.IO.File]::WriteAllText($htmlPath, $html, $utf8)

# 2. FIX CSS (style.css)
$stylePath = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\style.css"
$style = [System.IO.File]::ReadAllText($stylePath, [System.Text.Encoding]::UTF8)
# Replace ANY non-ascii content value with arrow escape
# We know they are on ::after elements
$style = $style.Replace(".story-arrow::after {`r`n    content: '';", ".story-arrow::after {`r`n    content: '\2192';")
$style = $style.Replace(".project-link::after {`r`n    content: '';", ".project-link::after {`r`n    content: '\2192';")
$style = $style.Replace(".btn-stories::after {`r`n    content: ' ';", ".btn-stories::after {`r`n    content: ' \2192';")

# Backup broad regex replacement for any remaining broken arrows in style.css
$style = [regex]::Replace($style, "content:\s*'[^'\w\s\-\:;]+'", "content: '\2192'")

[System.IO.File]::WriteAllText($stylePath, $style, $utf8)

# 3. FIX Banner CSS (style_banner.css)
$bannerPath = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\style_banner.css"
if (Test-Path $bannerPath) {
    $banner = [System.IO.File]::ReadAllText($bannerPath, [System.Text.Encoding]::UTF8)
    $banner = $banner.Replace(".banner-arrow::after {`r`n    content: '';", ".banner-arrow::after {`r`n    content: '\2192';")
    [System.IO.File]::WriteAllText($bannerPath, $banner, $utf8)
}

Write-Host "All files repaired with HTML entities and CSS escapes."
