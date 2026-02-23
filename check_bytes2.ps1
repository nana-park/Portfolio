$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)
$lines = $content -split "`r`n"
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "lang-btn|English|Korean") {
        Write-Host "Line $($i+1): $($lines[$i].Trim())"
        $lineBytes = [System.Text.Encoding]::UTF8.GetBytes($lines[$i].Trim())
        Write-Host "Bytes: $($lineBytes -join ' ')"
    }
}
