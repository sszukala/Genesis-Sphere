#!/bin/bash
# Script to build GRChombo from source

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install required system packages
echo "Installing dependencies..."
sudo apt install -y build-essential g++ gfortran cmake git \
    libhdf5-serial-dev libfftw3-dev liblapack-dev libblas-dev \
    libopenmpi-dev openmpi-bin python3 python3-pip

# Install required Python packages from our requirements file
echo "Installing Python dependencies..."
pip3 install -r grchombo_requirements.txt

# Create workspace directory
echo "Creating GRChombo workspace..."
mkdir -p ~/grchombo
cd ~/grchombo

# Clone required repositories
echo "Cloning repositories..."
git clone https://github.com/GRChombo/Chombo.git
git clone https://github.com/GRChombo/GRChombo.git

# Set environment variables
echo "Setting up environment..."
export GRCHOMBO_SOURCE=~/grchombo/GRChombo
export CHOMBO_HOME=~/grchombo/Chombo

# Save environment variables to a file for later use
cat > ~/.grchombo_env << EOF
export GRCHOMBO_SOURCE=~/grchombo/GRChombo
export CHOMBO_HOME=~/grchombo/Chombo
EOF

echo "source ~/.grchombo_env" >> ~/.bashrc

# Configure and build Chombo
echo "Building Chombo library..."
cd ~/grchombo/Chombo

# Create Make.defs.local configuration
cat > Make.defs.local << EOF
DIM              = 3
DEBUG            = FALSE
OPT              = TRUE
PRECISION        = DOUBLE
CXX              = mpicxx -std=c++14
FC               = mpif90
MPI              = TRUE
USE_HDF          = TRUE
HDFINCFLAGS      = -I/usr/include/hdf5/serial
HDFLIBFLAGS      = -L/usr/lib/x86_64-linux-gnu/hdf5/serial -lhdf5 -lz
HDFMPIINCFLAGS   = -I/usr/include/hdf5/serial
HDFMPILIBFLAGS   = -L/usr/lib/x86_64-linux-gnu/hdf5/serial -lhdf5 -lz
EOF

# Build Chombo library
make lib

# Build a GRChombo example
echo "Building GRChombo example..."
cd ~/grchombo/GRChombo/Examples/ScalarField

# Copy the example parameter file
cp params.txt my_params.txt

# Build the example
make

echo "==============================================================="
echo "GRChombo build complete!"
echo "==============================================================="
echo "To run a test simulation, use:"
echo "cd ~/grchombo/GRChombo/Examples/ScalarField"
echo "mpirun -n 4 ./ScalarField3d my_params.txt"
echo 
echo "The environment is set up in your .bashrc file."
echo "To apply it to your current session, run:"
echo "source ~/.grchombo_env"
echo "==============================================================="
