@echo off
echo ===========================================================
echo Checking available boundary types in Docker Athena
echo ===========================================================
echo.

echo This script will run a command to find valid boundary types in the Athena source code.
echo.

docker run --rm -v "%cd%:/workspace" ^
  -w "/workspace" ^
  athena-custom ^
  /bin/bash -c "grep -r 'return BoundaryFlag::' /athena/src/bvals/utils/boundary_flag.cpp | sort | uniq"

echo.
echo ===========================================================
echo Valid boundary condition types:
echo  - outflow: Flow passes through the boundary
echo  - reflect/reflecting: Flow bounces off the boundary
echo  - periodic: Domain wraps around to the other side
echo  - user: Custom user-defined boundary conditions
echo  - polar/polar_wedge: For spherical coordinates
echo ===========================================================
echo.
echo To run a simulation with valid boundaries, use:
echo run_athena_with_docker.bat minimal_working_alt.in my_output

pause
