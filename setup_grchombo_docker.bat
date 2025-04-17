@echo off
echo ===================================================
echo Setting up GRChombo Docker environment for Windows
echo ===================================================
echo.

echo First, we'll build a local GRChombo Docker image...
cd grchombo
call build_grchombo_docker.bat

echo.
echo Creating workspace for simulation outputs...
mkdir grchombo_output 2>nul

echo.
echo Starting GRChombo Docker container...
echo You'll be placed inside the container with your current directory mounted.
echo.
echo To run a test simulation once inside the container:
echo    cd /grchombo/GRChombo/Examples/ScalarFieldCosmo
echo    make
echo    mpirun -np 2 ./ScalarFieldCosmo3d params.txt
echo.
echo Or use the helper script:
echo    run-scalar-cosmo
echo.
echo Press any key to start the container...
pause > nul

docker run -it --rm -v "%cd%:/workspace" grchombo-local
