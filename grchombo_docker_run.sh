#!/bin/bash
# Script to run GRChombo via Docker

# Pull the GRChombo Docker image
echo "Pulling GRChombo Docker image..."
docker pull sszukala/grchombo:latest

# Create output directory if it doesn't exist
echo "Creating output directory..."
mkdir -p grchombo_output

# Run the container with current directory mounted
echo "Starting GRChombo Docker container..."
docker run -it --rm \
    -v "$(pwd):/workspace" \
    -w "/workspace" \
    sszukala/grchombo:latest

echo "GRChombo Docker session ended."
