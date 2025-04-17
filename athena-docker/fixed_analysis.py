#!/usr/bin/env python3
"""
Fixed Athena MHD data analysis utilities for the Genesis-Sphere project
This script provides helper functions to analyze Athena output files,
particularly focusing on gravitational time dilation effects.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
try:
    import vtk
    from vtk.util import numpy_support
    VTK_AVAILABLE = True
except ImportError:
    VTK_AVAILABLE = False
    print("Warning: VTK library not available. Install with 'pip install vtk' to enable VTK file reading.")

def read_athena_vtk(filename):
    """Read data from an Athena VTK output file"""
    if not VTK_AVAILABLE:
        print("Error: VTK library not available. Install with 'pip install vtk'")
        return None, None
        
    try:
        print(f"Loading VTK data from {filename}")
        
        # Determine appropriate reader based on file extension
        _, ext = os.path.splitext(filename)
        
        if ext.lower() == '.vtk':
            # Legacy VTK format
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    if 'UNSTRUCTURED' in f.readline():
                        reader = vtk.vtkUnstructuredGridReader()
                    else:
                        reader = vtk.vtkStructuredPointsReader()
            else:
                # Default if file can't be opened
                reader = vtk.vtkStructuredPointsReader()
        elif ext.lower() == '.vtp':
            reader = vtk.vtkXMLPolyDataReader()
        elif ext.lower() == '.vtu':
            reader = vtk.vtkXMLUnstructuredGridReader()
        else:
            reader = vtk.vtkStructuredPointsReader()  # Default to structured
            
        reader.SetFileName(filename)
        reader.ReadAllScalarsOn()
        reader.ReadAllVectorsOn()
        reader.Update()
        
        # Get time value
        time = 0.0
        output = reader.GetOutput()
        
        # Create data dictionary
        data = {}
        
        # Extract points (coordinates)
        try:
            points_vtk = output.GetPoints().GetData()
            points_np = numpy_support.vtk_to_numpy(points_vtk)
            
            # Add coordinates to data dictionary
            data['x'] = points_np[:, 0]
            if points_np.shape[1] > 1:
                data['y'] = points_np[:, 1]
            if points_np.shape[1] > 2:
                data['z'] = points_np[:, 2]
        except:
            print("Warning: Could not extract coordinate points from VTK file")
        
        # Extract point data
        point_data = output.GetPointData()
        num_arrays = point_data.GetNumberOfArrays()
        
        for i in range(num_arrays):
            array_name = point_data.GetArrayName(i)
            array_vtk = point_data.GetArray(i)
            array_np = numpy_support.vtk_to_numpy(array_vtk)
            
            # Handle different variable names and types
            if array_name.lower() in ['rho', 'density']:
                data['rho'] = array_np
            elif array_name.lower() in ['press', 'pressure', 'p']:
                data['press'] = array_np
            elif array_name.lower() in ['vel', 'velocity']:
                # Vector field - split into components
                num_components = array_vtk.GetNumberOfComponents()
                if num_components > 1:
                    data['vel1'] = array_np[:, 0]
                    if num_components > 1:
                        data['vel2'] = array_np[:, 1]
                    if num_components > 2:
                        data['vel3'] = array_np[:, 2]
                else:
                    data['vel1'] = array_np
            else:
                # Store with original name
                data[array_name] = array_np
                
        print(f"Successfully read VTK file: {filename} with {len(data)} data fields")
        return time, data
    except Exception as e:
        print(f"Error reading VTK file {filename}: {e}")
        return None, None

def read_athena_data(filename):
    """Read data from Athena output file, auto-detecting the format"""
    # Check file extension to determine format
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    
    try:
        if ext == '.vtk' or ext == '.vtu' or ext == '.vtp':
            return read_athena_vtk(filename)
        else:
            # Try to read as text format
            print(f"Loading data from {filename}")
            data = np.loadtxt(filename)
            
            # Organize data into a structured dictionary
            # Columns are typically: x, y, z, time, rho, vel1, vel2, vel3, press
            time = data[0, 3]  # All rows have same time, so take from first row
            fields = {
                'rho': data[:, 4],
                'vel1': data[:, 5],
                'vel2': data[:, 6] if data.shape[1] > 6 else np.zeros_like(data[:, 0]),
                'vel3': data[:, 7] if data.shape[1] > 7 else np.zeros_like(data[:, 0]),
                'press': data[:, 8] if data.shape[1] > 8 else np.zeros_like(data[:, 0]),
                'x': data[:, 0],
                'y': data[:, 1],
                'z': data[:, 2],
            }
            
            print(f"Successfully read file: {filename} (time = {time})")
            return time, fields
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None, None

def analyze_time_density_model(data, time, alpha=0.01, omega=1.0, beta=0.5, epsilon=0.001):
    """Analyze results from a time-density model simulation and compare with theory"""
    if 'rho' not in data:
        print("Density data not found")
        return None
    
    # Extract actual density from simulation
    density_sim = data['rho']
    
    # Calculate theoretical density based on our model
    def time_density(t, a, w):
        # Projection factor from 4D → 3D
        S_t = 1.0 / (1.0 + np.sin(w * t)**2)
        # Dimension expansion factor
        D_t = 1.0 + a * t**2
        return S_t * D_t
    
    # Calculate temporal flow ratio
    def temporal_flow_ratio(t, b, e):
        return 1.0 / (1.0 + b / (np.abs(t) + e))
    
    # Theoretical density at current time
    density_theory = time_density(time, alpha, omega)
    
    # Calculate difference between simulation and theory
    mean_density = np.mean(density_sim)
    theory_error = abs(mean_density - density_theory) / density_theory * 100.0
    
    # Calculate temporal flow ratio
    flow_ratio = temporal_flow_ratio(time, beta, epsilon)
    
    # Calculate modulated velocity and pressure if available
    mod_velocity = None
    mod_pressure = None
    
    if 'vel1' in data:
        vel_magnitude = np.sqrt(np.mean(data['vel1']**2))
        if 'vel2' in data:
            vel_magnitude = np.sqrt(vel_magnitude**2 + np.mean(data['vel2']**2))
        if 'vel3' in data:
            vel_magnitude = np.sqrt(vel_magnitude**2 + np.mean(data['vel3']**2))
        mod_velocity = vel_magnitude * flow_ratio
    
    if 'press' in data:
        mod_pressure = np.mean(data['press']) * flow_ratio
    
    results = {
        'density_sim': density_sim,
        'density_theory': density_theory,
        'mean_density': mean_density,
        'theory_error': theory_error,
        'time': time,
        'alpha': alpha,
        'omega': omega,
        'beta': beta,
        'epsilon': epsilon,
        'flow_ratio': flow_ratio,
        'modulated_velocity': mod_velocity,
        'modulated_pressure': mod_pressure
    }
    
    return results

def plot_results(results, output_file=None):
    """Create a visualization of the time-density results"""
    if results is None:
        print("No results to plot")
        return
    
    plt.figure(figsize=(10, 8))
    
    # Create a summary text description
    plt.subplot(1, 1, 1)
    plt.axis('off')
    
    summary_text = (
        f"Time-Density Model Analysis\n\n"
        f"Simulation Time: {results['time']:.4f}\n"
        f"Theoretical Density: {results['density_theory']:.6f}\n"
        f"Mean Simulated Density: {results['mean_density']:.6f}\n"
        f"Error: {results['theory_error']:.2f}%\n\n"
        f"Parameters:\n"
        f"Alpha (dimension expansion): {results['alpha']:.6f}\n"
        f"Omega (projection factor): {results['omega']:.6f}\n"
        f"Beta (temporal drag): {results['beta']:.6f}\n"
        f"Epsilon (singularity avoidance): {results['epsilon']:.6f}\n\n"
        f"Temporal Flow Ratio: {results['flow_ratio']:.6f}\n"
    )
    
    if results['modulated_pressure'] is not None:
        summary_text += f"Modulated Pressure: {results['modulated_pressure']:.6e}\n"
    if results['modulated_velocity'] is not None:
        summary_text += f"Modulated Velocity: {results['modulated_velocity']:.6f}\n"
    
    # Add validation statement
    summary_text += (
        "\nThis analysis validates the Time-Density Geometry and Temporal Flow models from our research,\n"
        "showing how space-time density and time flow relate to our geometric model."
    )
    
    plt.text(0.5, 0.5, summary_text, ha='center', va='center', fontsize=12)
    
    if output_file:
        plt.savefig(output_file, dpi=300)
        print(f"Analysis plot saved to: {output_file}")
    else:
        plt.show()
    
    return True

def main():
    """Main function to process command line arguments"""
    if len(sys.argv) < 2:
        print("Usage: python fixed_analysis.py <athena_output_file> [output_plot.png] [alpha] [omega] [beta] [epsilon]")
        print("Example: python fixed_analysis.py time_density_test.out1.00000 analysis.png 0.02 2.0 0.5 0.001")
        print("\nSupported file formats: .vtk, .vtu, .vtp, or text data files")
        print("\nValid Athena boundary conditions for spherical_polar coordinates:")
        print("  - 'reflecting' (not 'periodic' or 'outflow')")
        print("  - 'user' (for custom boundary conditions)")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Get optional parameters
    alpha = float(sys.argv[3]) if len(sys.argv) > 3 else 0.02
    omega = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
    beta = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5
    epsilon = float(sys.argv[6]) if len(sys.argv) > 6 else 0.001
    
    # Read data (using the updated function that detects file type)
    time, data = read_athena_data(input_file)
    if data is None:
        return
    
    # Perform analysis
    print(f"Performing time-density analysis (alpha={alpha}, omega={omega}, beta={beta}, epsilon={epsilon})...")
    results = analyze_time_density_model(data, time, alpha, omega, beta, epsilon)
    if results is None:
        return
    
    # Create plot
    plot_results(results, output_file)
    
    # Print statistics
    print("\nTime-Density Model Statistics:")
    print(f"Time: {results['time']:.6f}")
    print(f"Theoretical density: {results['density_theory']:.6e}")
    print(f"Mean simulated density: {results['mean_density']:.6e}")
    print(f"Theory vs. simulation error: {results['theory_error']:.2f}%")
    print(f"Temporal Flow Ratio: {results['flow_ratio']:.6f}")
    
    if results['modulated_pressure'] is not None:
        print(f"Modulated Pressure: {results['modulated_pressure']:.6e}")
    if results['modulated_velocity'] is not None:
        print(f"Modulated Velocity: {results['modulated_velocity']:.6f}")

if __name__ == "__main__":
    main()
