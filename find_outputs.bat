@echo off

echo === Searching for Athena output files... ===
echo.

echo Looking in current directory:
dir /b *.out*
echo.

echo Looking in subdirectories (this may take a moment):
dir /b /s *.out*
echo.

echo Looking for VTK files:
dir /b /s *.vtk
echo.

echo Looking for HDF5 files:
dir /b /s *.h5 *.hdf5
echo.

echo === ANALYSIS INSTRUCTIONS ===
echo If you found output files, try analyzing them with:
echo python athena-docker\fixed_analysis.py [output_file] analysis_result.png 0.02 2.0 0.5 0.001
echo.

echo Parameters: alpha=0.02, omega=2.0, beta=0.5, epsilon=0.001
echo.

echo Output files are often named in the format: [problem_id].out1.00000
echo If no files are found, check if:
echo 1. The simulation actually created output files
echo 2. They were saved to a different directory
echo 3. You have specified an output directory in your input file

pause
