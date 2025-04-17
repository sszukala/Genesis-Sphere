# Running Athena in Docker

## Option 1: Using PowerShell

```powershell
# Run using the PowerShell script
.\run_athena_docker.ps1
```

## Option 2: Using Command Prompt

```cmd
# Run using the batch file
run_athena_docker.bat
```

## Option 3: Direct Docker Command

### In PowerShell:
```powershell
$currentPath = (Get-Location).Path
docker run -it --rm -v "${currentPath}:/workspace" athena-custom
```

### In Command Prompt:
```cmd
docker run -it --rm -v "%cd%:/workspace" athena-custom
```

## Running Athena Inside the Container

Once inside the Docker container (you'll see a prompt like `root@container:/workspace#`), run:

```bash
# Run Athena with your input file
/athena/bin/athena -i time_density_spherical_fixed.in -otime_density_fixed
```

To exit the container when done:
```bash
exit
```
