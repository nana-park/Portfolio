$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)

# Find the card-stars line and show its exact bytes
$lines = $content -split "`r`n"
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "card-stars") {
        $lineBytes = [System.Text.Encoding]::UTF8.GetBytes($lines[$i])
        Write-Host "Line $($i+1) bytes: $($lineBytes -join ' ')"
        break
    }
}
