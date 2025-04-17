@echo off
SETLOCAL EnableDelayedExpansion

echo ===========================================================
echo Rebuilding Athena inside Docker container
echo ===========================================================
echo.

echo Supported coordinate systems: cartesian, cylindrical, spherical_polar
echo Supported problems: blast, mhd_blast, time_density, etc.
echo.

set /p COORD="Enter coordinate system [cartesian]: "
if "!COORD!"=="" set COORD=cartesian

set /p PROB="Enter problem type [blast]: "
if "!PROB!"=="" set PROB=blast

set /p FLUX="Enter flux type [hllc]: "
if "!FLUX!"=="" set FLUX=hllc

echo.
echo Will rebuild Athena with:
echo   - Coordinate system: !COORD!
echo   - Problem: !PROB!
echo   - Flux: !FLUX!
echo.
set /p CONFIRM="Proceed? [Y/n]: "
if /i "!CONFIRM!"=="n" exit /b

echo.
echo Starting Docker container to rebuild Athena...
echo This may take a few minutes...
echo.

REM Run rebuild commands in Docker
docker run --rm -v "%CD%:/workspace" athena-custom /bin/bash -c "cd /athena && python3 configure.py --coord=!COORD! --prob=!PROB! --flux=!FLUX! && make clean && make -j"

echo.
echo Athena has been rebuilt with the specified options.
echo You can now run simulations with the new configuration.
echo.

ENDLOCAL
