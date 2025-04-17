@echo off
SETLOCAL EnableDelayedExpansion

echo ===========================================================
echo Rebuilding Athena in git folder
echo ===========================================================
echo.

REM Set the path to the Athena folder
set ATHENA_PATH=.\athena

REM Check if Athena folder exists
if not exist "%ATHENA_PATH%" (
  echo ERROR: Athena folder not found at %ATHENA_PATH%
  echo Make sure you have cloned the Athena repository
  exit /b 1
)

cd %ATHENA_PATH%

REM Configuring Athena with default options
echo Configuring Athena...
python configure.py --prob=blast --coord=cartesian --flux=hllc

REM Compiling Athena
echo.
echo Compiling Athena...
make clean
make

echo.
echo Athena has been rebuilt. You can now run it with different boundary conditions.
echo.

REM Return to the original directory
cd ..

ENDLOCAL
