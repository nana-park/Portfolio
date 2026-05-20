$content = Get-Content -Raw -Encoding UTF8 "projects/hopzie.html"
$replacements = @{
    "text-white" = "text-zinc-900";
    "text-zinc-300" = "text-zinc-700";
    "text-zinc-400" = "text-zinc-500";
    "border-white/5" = "border-zinc-200";
    "border-white/10" = "border-zinc-200";
    "border-white/20" = "border-zinc-300";
    "bg-white/5" = "bg-zinc-50";
    "bg-white/10" = "bg-zinc-100";
    "bg-white/20" = "bg-zinc-200";
    "hover:bg-white/5" = "hover:bg-zinc-100";
    "hover:border-white/10" = "hover:border-zinc-300";
    "text-amber-500" = "text-[#d97706]";
    "bg-[#0f0f0f]" = "bg-white";
    "bg-[#1a1a1a]" = "bg-zinc-50";
    "border-[#2a2a2a]" = "border-zinc-200";
    "border-[#333]" = "border-zinc-200";
    "text-gray-300" = "text-zinc-600";
    "bg-black/30" = "bg-zinc-100";
    "bg-black/80" = "bg-white/90 shadow-sm text-zinc-900";
    "from-[#1a1a1a]" = "from-zinc-50";
    "bg-[#121212]" = "bg-white";
    "bg-[#1e1e1e]" = "bg-zinc-50";
    "border-[#333333]" = "border-zinc-200";
    "bg-[#2d2d2d]" = "bg-zinc-100";
    "bg-[#222]" = "bg-zinc-50";
    "text-gray-400" = "text-zinc-500"
}

# In PowerShell, a hashtable does not guarantee order.
# To prevent overlapping replacements (if any), we'll sort them by length descending, though here they don't overlap much.

foreach ($key in $replacements.Keys) {
    $content = $content.Replace($key, $replacements[$key])
}

[IO.File]::WriteAllText((Resolve-Path "projects/hopzie.html").Path, $content, [System.Text.Encoding]::UTF8)
Write-Output "Done"
