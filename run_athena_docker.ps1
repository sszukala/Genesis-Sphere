# Run Athena in Docker with proper PowerShell volume mounting
$currentPath = (Get-Location).Path
Write-Host "Starting Athena Docker container using directory: $currentPath"
docker run -it --rm -v "${currentPath}:/workspace" athena-custom
