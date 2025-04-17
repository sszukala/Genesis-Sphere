@echo off
SETLOCAL EnableDelayedExpansion

echo ===========================================================
echo Running Athena inside Docker container
echo ===========================================================
echo.

REM Check if input file was provided
if "%~1"=="" (
  echo ERROR: You must provide an input file
  echo Usage: %0 input_file.in [output_prefix]
  echo Example: %0 minimal_working.in test_output
  exit /b 1
)

REM Get input file
set INPUT_FILE=%~1

REM Use default output prefix if none provided
if "%~2"=="" (
  set OUTPUT_PREFIX=athena_output
) else (
  set OUTPUT_PREFIX=%~2
)

echo Input file: %INPUT_FILE%
echo Output prefix: %OUTPUT_PREFIX%
echo.

echo Starting Docker container...
echo.

REM Run Athena in Docker with the specified input file
docker run --rm -v "%CD%:/workspace" athena-custom /bin/bash -c "cd /workspace && /athena/bin/athena -i %INPUT_FILE% -o%OUTPUT_PREFIX%"

echo.
echo Docker container finished.
echo.

echo Checking if output files were created:
dir %OUTPUT_PREFIX%.*

echo.
echo Done!

ENDLOCAL
