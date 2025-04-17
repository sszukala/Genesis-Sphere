#!/bin/bash
# Script to rebuild Athena with cartesian coordinates

echo "Rebuilding Athena with cartesian coordinates..."

cd /athena

python3 configure.py \
    --prob=blast \
    --coord=cartesian \
    --flux=hllc

make clean

make -j$(nproc)

echo "Rebuild complete! You can now use cartesian coordinates in your input files."
