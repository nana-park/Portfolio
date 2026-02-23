$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)
$lines = $content -split "`r`n"
$l = $lines[1448] # Line 1449
$lineBytes = [System.Text.Encoding]::UTF8.GetBytes($l.Trim())
Write-Host "Bytes: $($lineBytes -join ' ')"
