$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)

# Find all lines containing the replacement character U+FFFD
$lines = $content -split "`r`n"
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i].Contains([char]0xFFFD)) {
        Write-Host "Line $($i+1): $($lines[$i].Trim())"
    }
}
