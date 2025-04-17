@echo off

echo Starting Athena Docker container...

docker run -it --rm -v "%cd%:/workspace" athena-custom
