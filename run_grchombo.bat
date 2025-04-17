@echo off
echo ===================================================
echo Running GRChombo Docker container
echo ===================================================
echo.

echo Creating workspace for simulation outputs...
mkdir grchombo_output 2>nul

echo.
echo Starting GRChombo Docker container...
echo You'll be placed inside the container with your current directory mounted.
echo.
echo Inside the container, you can run:
echo   1. Run the ScalarField example:
echo      cd /grchombo/GRChombo/Examples/ScalarField
echo      mpirun -np 2 ./ScalarField3d params.txt
echo.
echo   2. Copy output files to your host:
echo      cp *.3d.* /workspace/grchombo_output/
echo.
echo Press any key to start the container...
pause > nul

docker run -it --rm -v "%cd%:/workspace" grchombo-local

echo.
echo Container session ended.
echo.
echo Check the grchombo_output directory for your simulation results.
pause
