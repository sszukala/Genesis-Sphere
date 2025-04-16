@echo off
echo Running all visualization scripts...

echo Installing dependencies from requirements.txt
pip install -r requirements.txt

echo.
echo Running cube_sphere_emergent_space.py
python cube_sphere_emergent_space.py

echo.
echo Running big_bang_crunch.py
python big_bang_crunch.py

echo.
echo Running cube_to_tesseract.py
python cube_to_tesseract.py

echo.
echo Running genesis_timespace.py
python genesis_timespace.py

echo.
echo All visualizations have been generated in the timespace_sim directory
echo.
dir .\timespace_sim\*.gif

pause
