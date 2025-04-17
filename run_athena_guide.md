# Guide to Running Athena in Docker

## Option 1: Using PowerShell

```powershell
# Run the PowerShell script
.\run_athena_docker.ps1
```

## Option 2: Using Command Prompt

```cmd
run_athena_docker.bat
```

## Option 3: Direct Docker Command

```powershell
# For PowerShell
$currentPath = (Get-Location).Path
docker run -it --rm -v "${currentPath}:/workspace" athena-custom
```

```cmd
# For Command Prompt
docker run -it --rm -v "%cd%:/workspace" athena-custom
```

## Once Inside Docker Container

After successfully entering the Docker container, you'll see a prompt like `root@container:/workspace#`. Then run:

```bash
# Run Athena with your input file
/athena/bin/athena -i time_density_spherical_fixed.in -otime_density_fixed

# If you encounter errors, check input file syntax:
cat time_density_spherical_fixed.in

# To exit the container when done
exit
```

Remember: The `/athena/bin/athena` command only works INSIDE the Docker container, not in your host PowerShell.
