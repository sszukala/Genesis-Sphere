# Run Athena in Docker with proper commands
$currentPath = (Get-Location).Path
Write-Host "Starting Athena Docker container using directory: $currentPath"
docker run -it --rm -v "${currentPath}:/workspace" athena-custom /bin/bash -c "
echo '=== Running Athena with fixed settings ==='
/athena/bin/athena -i time_density_spherical_fixed2.in -otime_density_fixed

echo '=== Available Integrators and Options ==='
# List valid integrators
cd /athena
grep -r 'integrator ==' src/task_list/time_integrator.cpp | grep -o 'integrator == \"[^\"]*\"' | sort | uniq

echo '=== Valid Boundary Types ==='
# Try to detect valid boundary types
grep -r 'GetBoundaryFlag' src/mesh/meshboundary.cpp --include='*.cpp' -A 20 | grep -o '\"[a-z_]*\"' | sort | uniq
"
