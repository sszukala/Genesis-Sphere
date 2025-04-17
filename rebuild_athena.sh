#!/bin/bash

echo "Rebuilding Athena with proper configuration for common boundary conditions..."
cd /athena

# Configure Athena with explicit boundary condition support
python3 configure.py \
    --prob=blast \
    --coord=cartesian \
    --flux=hllc \
    --eos=adiabatic

make clean
make -j$(nproc)

echo "Rebuild complete! Let's test the boundary conditions now."
