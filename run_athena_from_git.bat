@echo off
SETLOCAL EnableDelayedExpansion

echo ===========================================================
echo Running Athena from local git folder
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

REM Set the path to the Athena executable in the git folder
set ATHENA_PATH=.\athena\bin\athena

REM Check if Athena executable exists
if not exist "%ATHENA_PATH%" (
  echo ERROR: Athena executable not found at %ATHENA_PATH%
  echo Make sure you have compiled Athena in the git folder
  exit /b 1
)

echo Running Athena from git folder...
echo.

REM Run Athena with the specified input file
%ATHENA_PATH% -i %INPUT_FILE% -o%OUTPUT_PREFIX%

echo.
echo Athena execution finished.
echo.

echo Checking if output files were created:
dir %OUTPUT_PREFIX%.*

echo.
echo Done!

ENDLOCAL
