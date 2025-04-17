@echo off

echo Creating output directories...
mkdir vtk_output 2>nul

echo Running Athena with correct output settings...
docker run --rm ^
    -v "%~dp0:/workspace" ^
    -w "/workspace" ^
    athena-custom ^
    /athena/bin/athena -i time_density_cartesian.in -ovtk_output/time_density

echo Moving any stray VTK files to output directory...
for %%i in (*.vtk) do (
    echo Moving %%i to vtk_output directory
    move %%i vtk_output\ >nul
)

echo Done! Check the vtk_output directory for your files.
echo.

dir vtk_output\*.vtk

pause
