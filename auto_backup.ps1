# AI PM Portfolio Auto-Backup Script
# This script commits and pushes all changes to GitHub every 1 hour (3600 seconds).

$interval = 3600 # 1 hour in seconds
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

Write-Host ">>> Starting Auto-Backup for Portfolio..." -ForegroundColor Cyan
Write-Host ">>> Backup interval: 1 hour" -ForegroundColor Green

while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host ">>> [$timestamp] Checking for changes..." -ForegroundColor Yellow
    
    # Detect files over 100MB
    $largeFiles = Get-ChildItem -Path . -Recurse -File | Where-Object { $_.Length -gt 100MB }
    
    # Check if there are changes to commit
    $status = git status --porcelain
    if ($status) {
        if ($largeFiles) {
            Write-Host ">>> [WARNING] Large files detected (>100MB):" -ForegroundColor Red
            foreach ($file in $largeFiles) {
                Write-Host "    - $($file.FullName) ($([Math]::Round($file.Length/1MB, 2)) MB)" -ForegroundColor Yellow
            }
            Write-Host ">>> These files will be skipped for now. Please ask the AI to help with 'Git LFS' if you need to back them up." -ForegroundColor Cyan
        }

        Write-Host ">>> Changes detected. Backing up..." -ForegroundColor Green
        git add .
        # Exclude known large files to avoid push failure
        foreach ($file in $largeFiles) {
            $relativeId = Resolve-Path -Path $file.FullName -Relative
            git reset $relativeId
        }
        
        git commit -m "Auto-backup: $timestamp"
        $pushResult = git push origin main 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host ">>> Backup successfully pushed to GitHub!" -ForegroundColor Cyan
        }
        else {
            Write-Host ">>> [ERROR] Push failed. See details above." -ForegroundColor Red
        }
    }
    else {
        Write-Host ">>> No changes to backup." -ForegroundColor Gray
    }
    
    Write-Host ">>> Next backup in 1 hour. Keep this window open." -ForegroundColor Gray
    Start-Sleep -Seconds $interval
}
