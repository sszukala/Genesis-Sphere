Write-Host "Starting Athena Docker container..." -ForegroundColor Green
$currentPath = (Get-Location).Path
docker run -it --rm -v "${currentPath}:/workspace" athena-custom
