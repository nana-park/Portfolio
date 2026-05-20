$content = Get-Content -Raw -Encoding UTF8 "projects/hopzie.html"
$content = $content -replace 'bg-\[#050505\]', 'bg-white'
$content = $content -replace 'bg-\[#0a0a0a\]', 'bg-zinc-50'
$content = $content -replace 'bg-\[#080808\]', 'bg-zinc-50'
$content = $content -replace 'bg-\[#111111\]', 'bg-zinc-50'
$content = $content -replace 'bg-\[#1a1a1a\]', 'bg-zinc-100'
$content = $content -replace 'bg-\[#222\]', 'bg-zinc-100'
$content = $content -replace 'text-zinc-200', 'text-zinc-900'
$content = $content -replace 'text-zinc-300', 'text-zinc-700'
$content = $content -replace 'text-zinc-400', 'text-zinc-500'
[IO.File]::WriteAllText((Resolve-Path "projects/hopzie.html").Path, $content, [System.Text.Encoding]::UTF8)
Write-Output "Cleaned up remaining dark mode hex codes."
