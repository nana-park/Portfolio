$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)

$lines = $content -split "`r`n"
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    # match any character > 127
    if ($line -match "[^\x00-\x7F]") {
        # filter out the ones we know are good (stars, globe)
        # 🌐 is \uD83C\uDF10
        # ★ is \u2605
        # &copy; is actually a character 0xA9 in some encodings but usually in HTML it's &copy;
        # Let's just output them all and see.
        Write-Host "Line $($i+1): $($line.Trim())"
    }
}
