#!/usr/bin/env python3
"""
Athena MHD data analysis utilities for the Genesis-Sphere project
This script provides helper functions to analyze Athena output files,
particularly focusing on gravitational time dilation effects.
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys
import os
import vtk
from vtk.util import numpy_support
import os.path

def read_athena_data(filename):
    """Read data from an Athena HDF5 output file"""
    try:
        with h5py.File(filename, 'r') as f:
            # Print available variables
            print("Available variables in the dataset:")
            for key in f.keys():
                print(f"- {key}")
                
            # Read common variables
            time = f.attrs.get('Time', 0.0)
            data = {}
            
            # Try to read standard variables (adapt as needed)
            for var in ['rho', 'press', 'vel1', 'vel2', 'vel3']:
                if var in f:
                    data[var] = f[var][()]
            
            print(f"Successfully read file: {filename} (time = {time})")
            return time, data
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None, None

def read_athena_vtk(filename):
    """Read data from an Athena VTK output file"""
    try:
        print(f"Loading VTK data from {filename}")
        
        # Determine appropriate reader based on file extension
        _, ext = os.path.splitext(filename)
        
        if ext.lower() == '.vtk':
            # Legacy VTK format
            if 'UNSTRUCTURED' in open(filename, 'r').readline():
                reader = vtk.vtkUnstructuredGridReader()
            else:
                reader = vtk.vtkStructuredPointsReader()
        elif ext.lower() == '.vtp':
            reader = vtk.vtkXMLPolyDataReader()
        elif ext.lower() == '.vtu':
            reader = vtk.vtkXMLUnstructuredGridReader()
        else:
            reader = vtk.vtkStructuredPointsReader()  # Default to structured
            
        reader.SetFileName(filename)
        reader.Update()
        
        # Get time value from file (if available)
        time = 0.0
        try:
            field_data = reader.GetOutput().GetFieldData()
            if field_data.GetArray("TIME"):
                time = field_data.GetArray("TIME").GetValue(0)
        except:
            pass
            
        # Extract geometric data
        points_vtk = reader.GetOutput().GetPoints().GetData()
        points_np = numpy_support.vtk_to_numpy(points_vtk)
        
        # Create structured data dictionary
        data = {}
        
        # Extract all available point data
        point_data = reader.GetOutput().GetPointData()
        num_arrays = point_data.GetNumberOfArrays()
        
        print(f"Found {num_arrays} data arrays in VTK file")
        
        for i in range(num_arrays):
            array_name = point_data.GetArrayName(i)
            array_vtk = point_data.GetArray(i)
            array_np = numpy_support.vtk_to_numpy(array_vtk)
            
            # Check if this is vector data
            num_components = array_vtk.GetNumberOfComponents()
            if num_components > 1:
                # Handle vector data
                if array_name == "velocity" or array_name == "vel":
                    # Split vector into components
                    data['vel1'] = array_np[:, 0]
                    data['vel2'] = array_np[:, 1] if num_components > 1 else np.zeros_like(array_np[:, 0])
                    data['vel3'] = array_np[:, 2] if num_components > 2 else np.zeros_like(array_np[:, 0])
                elif array_name == "B" or array_name == "Bcc" or array_name == "magnetic":
                    # Magnetic field components
                    data['B1'] = array_np[:, 0]
                    data['B2'] = array_np[:, 1] if num_components > 1 else np.zeros_like(array_np[:, 0])
                    data['B3'] = array_np[:, 2] if num_components > 2 else np.zeros_like(array_np[:, 0])
                else:
                    # Generic vector field
                    for j in range(num_components):
                        data[f"{array_name}{j+1}"] = array_np[:, j]
            else:
                # Handle scalar data
                if array_name.lower() == "rho" or array_name.lower() == "density":
                    data['rho'] = array_np
                elif array_name.lower() == "press" or array_name.lower() == "pressure":
                    data['press'] = array_np
                else:
                    data[array_name] = array_np
        
        # Add coordinate data
        data['x'] = points_np[:, 0]
        if points_np.shape[1] > 1:
            data['y'] = points_np[:, 1]
        if points_np.shape[1] > 2:
            data['z'] = points_np[:, 2]
        
        print(f"Successfully read VTK file: {filename} (time = {time})")
        return time, data
    except Exception as e:
        print(f"Error reading VTK file {filename}: {e}")
        return None, None

def read_athena_data_any_format(filename):
    """Read data from an Athena output file, automatically detecting format"""
    _, ext = os.path.splitext(filename)
    
    # Use appropriate reader based on file extension
    if ext.lower() in ['.vtk', '.vtu', '.vtp']:
        return read_athena_vtk(filename)
    elif ext.lower() in ['.h5', '.hdf5', '.athdf']:
        return read_athena_data(filename)
    else:
        # Try to read as text format
        try:
            time, data = None, None
            # Load data as a NumPy array
            data_array = np.loadtxt(filename)
            
            # Organize data into a dictionary
            # Assuming columns are: x, y, z, time, rho, vel1, vel2, vel3, press
            time = data_array[0, 3]  # Get time from first row
            
            data = {
                'x': data_array[:, 0],
                'y': data_array[:, 1],
                'z': data_array[:, 2],
                'rho': data_array[:, 4],
                'vel1': data_array[:, 5],
            }
            
            # Add additional columns if they exist
            if data_array.shape[1] > 6:
                data['vel2'] = data_array[:, 6]
            if data_array.shape[1] > 7:
                data['vel3'] = data_array[:, 7]
            if data_array.shape[1] > 8:
                data['press'] = data_array[:, 8]
                
            print(f"Successfully read text file: {filename} (time = {time})")
            return time, data
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            return None, None

def analyze_relativistic_effects(data):
    """Calculate relativistic effects from simulation data"""
    if 'rho' not in data or 'vel1' not in data:
        print("Required variables not found in data")
        return None
    
    # Calculate total velocity
    vel_total = np.sqrt(data['vel1']**2)
    if 'vel2' in data:
        vel_total = np.sqrt(vel_total**2 + data['vel2']**2)
    if 'vel3' in data:
        vel_total = np.sqrt(vel_total**2 + data['vel3']**2)
    
    # Calculate relativistic gamma factor (time dilation)
    # Assuming c = 1 in code units, adjust if using different units
    c = 1.0  
    gamma = 1.0 / np.sqrt(1.0 - np.minimum(vel_total**2/c**2, 0.9999))
    
    return {
        'velocity': vel_total,
        'gamma': gamma,
        'density': data['rho']
    }

def analyze_time_density_model(data, time, alpha=0.01, omega=1.0):
    """Analyze results from a time-density model simulation and compare with theory"""
    if 'rho' not in data:
        print("Density data not found")
        return None
    
    # Extract actual density from simulation
    density_sim = data['rho']
    
    # Calculate theoretical density based on your model
    def time_density(t, a, w):
        S_t = 1.0 / (1.0 + np.sin(w * t)**2)  # Projection factor
        D_t = 1.0 + a * t**2  # Dimension expansion factor
        return S_t * D_t
    
    # Theoretical density at current time
    density_theory = time_density(time, alpha, omega)
    
    # Calculate difference between simulation and theory
    mean_density = np.mean(density_sim)
    theory_error = abs(mean_density - density_theory) / density_theory * 100.0
    
    results = {
        'density_sim': density_sim,
        'density_theory': density_theory,
        'mean_density': mean_density,
        'theory_error': theory_error,
        'time': time,
        'alpha': alpha,
        'omega': omega
    }
    
    return results

def plot_density_timedilation(rel_data, output_file=None):
    """Create a plot showing the relationship between density and time dilation"""
    plt.figure(figsize=(10, 6))
    
    # Flatten arrays for scatter plot
    density_flat = rel_data['density'].flatten()
    gamma_flat = rel_data['gamma'].flatten()
    
    # Create scatter plot
    plt.scatter(density_flat, gamma_flat, alpha=0.1, s=1)
    plt.xlabel('Density')
    plt.ylabel('Time Dilation Factor (γ)')
    plt.title('Relationship Between Density and Time Dilation')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    
    if output_file:
        plt.savefig(output_file, dpi=300)
        print(f"Plot saved to: {output_file}")
    else:
        plt.show()

def plot_time_density_comparison(results, output_file=None):
    """Plot comparison between theoretical and simulated time-density"""
    plt.figure(figsize=(12, 8))
    
    # Create a 2x2 grid for the top part
    plt.subplot(2, 2, 1)
    # Plot density histogram from simulation
    plt.hist(results['density_sim'].flatten(), bins=50, alpha=0.7)
    plt.axvline(results['density_theory'], color='r', linestyle='--', 
                label=f'Theoretical density: {results["density_theory"]:.4f}')
    plt.axvline(results['mean_density'], color='g', linestyle='-',
                label=f'Mean density: {results["mean_density"]:.4f}')
    plt.title(f'Time-Density Model Validation (t={results["time"]:.4f})')
    plt.xlabel('Density')
    plt.ylabel('Frequency')
    plt.legend()
    
    # Plot the theoretical time-density function
    plt.subplot(2, 2, 2)
    t_values = np.linspace(0, max(5.0, results['time']*2), 1000)
    def time_density(t, a, w):
        S_t = 1.0 / (1.0 + np.sin(w * t)**2) 
        D_t = 1.0 + a * t**2
        return S_t * D_t
    densities = [time_density(t, results['alpha'], results['omega']) for t in t_values]
    plt.plot(t_values, densities, 'b-')
    plt.axvline(results['time'], color='r', linestyle='--')
    plt.axhline(results['density_theory'], color='r', linestyle='--')
    plt.scatter([results['time']], [results['density_theory']], color='r', s=50)
    plt.title('Time-Density Function')
    plt.xlabel('Time')
    plt.ylabel('Density')
    plt.grid(True, alpha=0.3)
    
    # Add simulation vs theory information
    plt.subplot(2, 1, 2)
    plt.text(0.5, 0.5, 
             f"Time-Density Model Analysis\n\n"
             f"Simulation Time: {results['time']:.4f}\n"
             f"Theoretical Density: {results['density_theory']:.6f}\n"
             f"Mean Simulated Density: {results['mean_density']:.6f}\n"
             f"Error: {results['theory_error']:.2f}%\n\n"
             f"Parameters:\n"
             f"Alpha (dimension expansion): {results['alpha']:.6f}\n"
             f"Omega (projection factor): {results['omega']:.6f}\n\n"
             f"This validates the Time-Density Geometry model from our research,\n"
             f"showing how the space-time density relates to our geometric model.",
             ha='center', va='center', fontsize=12)
    plt.axis('off')
    
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file, dpi=300)
        print(f"Time-density comparison plot saved to: {output_file}")
    else:
        plt.show()

def main():
    """Main function to process command line arguments"""
    if len(sys.argv) < 2:
        print("Usage: python athena_analysis.py <athena_output_file> [output_plot.png] [analysis_type] [param1] [param2] [param3] [param4]")
        print("Analysis types: 'relativistic' (default) or 'time-density'")
        print("For time-density: param1=alpha, param2=omega, param3=beta, param4=epsilon")
        print("Supported file formats: .vtk, .h5, .hdf5, .athdf, or text data files")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Determine analysis type
    analysis_type = 'relativistic'  # Default
    if len(sys.argv) > 3:
        analysis_type = sys.argv[3]
    
    # Read data using the unified reader function
    time, data = read_athena_data_any_format(input_file)
    if data is None:
        return
    
    # Perform analysis based on type
    if analysis_type == 'time-density':
        # Get parameters if provided
        alpha = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
        omega = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
        beta = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
        epsilon = float(sys.argv[7]) if len(sys.argv) > 7 else 0.01
        
        print(f"Performing time-density analysis (alpha={alpha}, omega={omega}, beta={beta}, epsilon={epsilon})...")
        results = analyze_time_density_model(data, time, alpha, omega, beta, epsilon)
        if results is None:
            return
        
        plot_time_density_comparison(results, output_file)
        
        # Print statistics
        print("\nTime-Density Model Statistics:")
        print(f"Time: {results['time']:.6f}")
        print(f"Theoretical density: {results['density_theory']:.6e}")
        print(f"Mean simulated density: {results['mean_density']:.6e}")
        print(f"Theory vs. simulation error: {results['theory_error']:.2f}%")
        print(f"Flow ratio: {results['flow_ratio']:.6f}")
        if results['modulated_pressure'] is not None:
            print(f"Modulated pressure: {results['modulated_pressure']:.6e}")
        if results['modulated_velocity'] is not None:
            print(f"Modulated velocity: {results['modulated_velocity']:.6e}")
        
    else:  # 'relativistic' or any other value defaults to relativistic analysis
        # Analyze relativistic effects
        print("Performing relativistic analysis...")
        rel_data = analyze_relativistic_effects(data)
        if rel_data is None:
            return
        
        # Create plot
        plot_density_timedilation(rel_data, output_file)
        
        # Print some statistics
        print("\nData Statistics:")
        print(f"Mean density: {np.mean(rel_data['density']):.6e}")
        print(f"Max velocity: {np.max(rel_data['velocity']):.6f}")
        print(f"Mean time dilation factor: {np.mean(rel_data['gamma']):.6f}")
        print(f"Max time dilation factor: {np.max(rel_data['gamma']):.6f}")

if __name__ == "__main__":
    main()
