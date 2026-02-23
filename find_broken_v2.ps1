$path = "C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$content = [System.Text.Encoding]::UTF8.GetString($bytes)

# Search for any non-ASCII characters that might be broken
# Broken characters are often EF BF BD (U+FFFD)
# Let's also look for raw '??' strings which I might have introduced or were there.

$lines = $content -split "`r`n"
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    if ($line -match "\?" -or $line -match "" -or $line -match "\uFFFD") {
        # filter out common things like question marks in sentences if any
        if ($line -match "[\uFFFD]") {
            Write-Host "Line $($i+1): $($line.Trim())"
        }
    }
}
