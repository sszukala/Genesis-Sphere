@echo off

echo === Finding and organizing VTK files ===
echo.

echo Creating output directories...
mkdir vtk_output 2>nul

echo Searching for VTK files in current directory...
dir /b *.vtk

echo.
echo Moving VTK files to vtk_output directory...
for %%i in (*.vtk) do (
    echo Moving %%i to vtk_output directory
    move %%i vtk_output\ >nul 2>nul
)

echo.
echo Checking if the VTK files were moved successfully:
dir vtk_output\*.vtk 2>nul

echo.
echo === NOTES ===
echo If the files were not moved, it may be because:
echo 1. They are being accessed by another program
echo 2. You don't have permission to move them
echo 3. They've already been moved to the vtk_output directory

pause
