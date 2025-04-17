@echo off
echo ===================================================
echo Installing GRChombo in Windows Subsystem for Linux
echo ===================================================
echo.

echo This script will:
echo 1. Check if WSL is installed
echo 2. Launch Ubuntu (or install it if needed)
echo 3. Run the GRChombo build script in WSL
echo.

REM Check if WSL is enabled
wsl --status > nul 2>&1
if %errorlevel% neq 0 (
    echo WSL is not enabled. Enabling it now...
    echo This may require administrator privileges.
    echo.
    echo After enabling WSL, you'll need to restart your computer.
    
    REM Try to enable WSL
    powershell -Command "Start-Process powershell -ArgumentList 'Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux' -Verb RunAs"
    
    echo.
    echo After your system restarts, please run this script again.
    echo.
    pause
    exit /b
)

REM Check if Ubuntu is installed
wsl -d Ubuntu -- echo "Ubuntu is installed" > nul 2>&1
if %errorlevel% neq 0 (
    echo Ubuntu is not installed. Installing it now...
    echo This may take several minutes.
    echo.
    
    REM Install Ubuntu
    powershell -Command "Start-Process powershell -ArgumentList 'wsl --install -d Ubuntu' -Verb RunAs"
    
    echo.
    echo Please wait for Ubuntu to be installed and set up your username and password.
    echo After setup is complete, run this script again.
    echo.
    pause
    exit /b
)

echo Ubuntu is installed. Copying build script and requirements...
REM Copy the build script and requirements to the WSL home directory
copy /Y "build_grchombo.sh" "%USERPROFILE%\AppData\Local\Temp\build_grchombo.sh"
copy /Y "grchombo_requirements.txt" "%USERPROFILE%\AppData\Local\Temp\grchombo_requirements.txt"

echo Setting execute permissions and running the build script...
wsl -d Ubuntu -- bash -c "cp /mnt/c/Users/*/AppData/Local/Temp/build_grchombo.sh ~/build_grchombo.sh && cp /mnt/c/Users/*/AppData/Local/Temp/grchombo_requirements.txt ~/grchombo_requirements.txt && chmod +x ~/build_grchombo.sh && ~/build_grchombo.sh"

echo.
echo GRChombo installation in WSL has completed.
echo To access your GRChombo installation, open Ubuntu and run:
echo cd ~/grchombo
echo.
pause
