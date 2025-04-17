@echo off
echo ===========================================================
echo Rebuilding Athena in Docker container
echo ===========================================================
echo.

REM Optional coordinate system
set COORD=cartesian
if not "%~1"=="" set COORD=%~1

REM Optional problem generator
set PROB=blast
if not "%~2"=="" set PROB=%~2

echo Using coordination system: %COORD%
echo Using problem generator: %PROB%
echo.

docker run --rm -v "%cd%:/workspace" ^
  -w "/workspace" ^
  athena-custom ^
  /bin/bash -c "cd /athena && python3 configure.py --prob=%PROB% --coord=%COORD% --flux=hllc && make clean && make -j$(nproc)"

echo.
echo Athena has been rebuilt in Docker container.
echo Use run_athena_with_docker.bat to run simulations.
echo.

pause
