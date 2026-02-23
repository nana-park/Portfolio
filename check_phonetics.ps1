$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)
$lines = $content -split "`r`n"

$l185 = $lines[184] # Line 185
$l217 = $lines[216] # Line 217

Write-Host "Line 185: $($l185.Trim())"
Write-Host "Line 185 Bytes: $(([System.Text.Encoding]::UTF8.GetBytes($l185.Trim())) -join ' ')"

Write-Host "Line 217: $($l217.Trim())"
Write-Host "Line 217 Bytes: $(([System.Text.Encoding]::UTF8.GetBytes($l217.Trim())) -join ' ')"
