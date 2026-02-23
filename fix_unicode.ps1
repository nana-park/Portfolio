$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)

# The broken pattern on lang-btn line: ? + FFFD + FFFD (was a 4-byte emoji like 🌐)
# Replace with just the globe emoji directly
$q = [char]63        # ?
$repl = [char]0xFFFD # replacement char

$brokenEmoji = "$q$repl$repl"

# Replace with globe emoji 🌐
$globe = [System.Char]::ConvertFromUtf32(0x1F310)  # 🌐

$content = $content.Replace("<span>$brokenEmoji</span> English", "<span>$globe</span> English")

$outBytes = [System.Text.Encoding]::UTF8.GetBytes($content)
[System.IO.File]::WriteAllBytes($path, $outBytes)

Write-Host "Done! Replaced broken emoji with globe emoji."

# Verify
$lines = $content -split "`r`n"
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "lang-btn") {
        Write-Host "Line $($i+1): $($lines[$i].Trim())"
    }
}
