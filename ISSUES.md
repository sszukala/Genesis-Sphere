# Error and Issue Tracking

This document tracks all known issues in the Genesis-Sphere project that need to be addressed.

## Athena Simulation Issues

### 1. Invalid Boundary Conditions
**Problem**: Athena rejects certain boundary condition types that are specified in input files.  
**Files Affected**:
- `time_density_spherical.in`
- `time_density_spherical_fixed.in`
- Other `.in` files with invalid boundary conditions

**Error Message**: `FATAL ERROR` related to boundary conditions  
**Solution**: Use only valid boundary conditions supported by your Athena build:
- `reflecting` - Working in most builds
- `outflow` - Appears to work in some configurations
- `polar_wedge` - For spherical coordinates
- `periodic` - Works in most cases

### 2. Missing Output Files
**Problem**: Athena simulations complete but don't produce output files  
**Files Affected**: All simulation output files  
**Symptoms**: No `.out*` or `.vtk` files are generated despite successful execution  
**Solution**: 
- Check that output directories exist and are writable
- Verify the `-o` parameter has no space (e.g., `-ooutput_name` not `-o output_name`)
- Add explicit `out_dir` parameter in the `<output1>` block

### 3. Simulation Configuration Issues
**Problem**: Some simulations fail to initialize or complete  
**Files Affected**:
- `time_density_cartesian.in`
- `time_density_spherical.in`

**Error Symptoms**: Docker exits without proper error message  
**Solution**: 
- Include required parameters for the chosen problem generator
- For `blast` problems, ensure `radius`, `center_x1`, etc. are defined
- For custom problems, add all required parameters

## Docker Issues

### 4. Docker Path Mounting Problems
**Problem**: Windows path mounting in Docker sometimes fails  
**Files Affected**: Docker execution scripts  
**Error Symptoms**: "Cannot mount volume" or "No such file or directory"  
**Solutions**:
- Use absolute paths: `-v "C:\full\path\to\directory:/workspace"`
- Replace backslashes with forward slashes
- Try using Docker Desktop settings to share drives

### 5. Docker Permissions
**Problem**: Files created inside Docker containers have incorrect permissions  
**Files Affected**: Output files from Docker runs  
**Symptoms**: Cannot modify or delete files after Docker creates them  
**Solution**: 
- Add appropriate user mapping to Docker run command
- Fix permissions after creation: `chmod -R 777 output_directory`

## Input File Issues

### 6. Missing Required Parameters
**Problem**: Input files missing required parameters for the chosen problem  
**Files Affected**:
- `time_density_spherical.in`
- Other `.in` files

**Error Symptoms**: "Required parameter not found" or silent failures  
**Solution**: Ensure all required parameters are present for each problem type:
- For `blast`: Add `radius`, `center_x1`, `center_x2`, and pressure parameters
- For `time_density`: Add matching parameters to meet expectations

### 7. Incorrect Time Integration
**Problem**: Some input files specify invalid time integrators  
**Files Affected**: Multiple `.in` files  
**Error Symptoms**: "Invalid integrator" or "Unknown integrator"  
**Solution**: Use only valid integrators in the `<time>` block:
- `rk2` - 2nd-order Runge-Kutta (recommended)
- Instead of `vl2` use `rk2`

## Analysis Script Issues

### 8. VTK Library Dependencies
**Problem**: Analysis scripts fail due to missing VTK library  
**Files Affected**:
- `athena_analysis.py`
- `fixed_analysis.py`

**Error Symptoms**: ImportError for VTK module  
**Solution**:
- Install VTK: `pip install vtk`
- Add error handling for missing VTK
- Use conditional imports

### 9. Data Format Compatibility
**Problem**: Analysis scripts sometimes fail to read data files  
**Files Affected**: 
- Analysis scripts
- Output data files

**Error Symptoms**: "Error reading file" or KeyError for missing data  
**Solution**:
- Add better format detection and error handling
- Support multiple file formats (VTK, HDF5, text)
- Standardize on a single output format

## Other Issues

### 10. Inconsistent Directory Structure
**Problem**: Scripts assume different directory structures  
**Files Affected**: Multiple scripts and batch files  
**Symptoms**: File not found errors, incorrect paths  
**Solution**:
- Standardize directory structure
- Use relative paths consistently
- Add configuration options for output directories

### 11. Python Environment Management
**Problem**: Dependencies aren't consistently managed across scripts  
**Files Affected**: All Python scripts  
**Symptoms**: Missing module errors, version conflicts  
**Solution**:
- Create and document a consistent environment setup
- Use virtual environments
- Maintain a single comprehensive requirements.txt

### 12. Documentation Gaps
**Problem**: Documentation doesn't cover all error scenarios  
**Files Affected**: README.md and other docs  
**Symptoms**: Users struggle to resolve errors  
**Solution**:
- Add troubleshooting section to README
- Document common errors and solutions
- Create example scripts with validated configurations

## Priority Issues to Fix First

1. **Invalid Boundary Conditions** - This is preventing simulations from running
2. **Missing Required Parameters** - Causes silent failures in simulations
3. **Docker Path Mounting** - Prevents Docker workflows from functioning
4. **Missing Output Files** - Makes analysis impossible even when simulations run
5. **VTK Library Dependencies** - Prevents analysis scripts from functioning

## Next Steps

1. Create a minimal working input file with validated parameters and boundary conditions
2. Test Docker workflows with absolute paths to ensure consistent mounting
3. Add better error handling to analysis scripts
4. Document valid parameter combinations for each problem type
5. Create a troubleshooting guide with common error messages and solutions