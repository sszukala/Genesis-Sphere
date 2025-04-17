#!/bin/bash
cd /athena
python3 configure.py --prob=blast --coord=cartesian --flux=hllc
make clean
make -j$(nproc)
echo "Athena rebuilt with Cartesian coordinates"
