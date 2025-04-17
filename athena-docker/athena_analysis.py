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
    if 'rho' not in data:/ (abs(t) + epsilon))
        print("Density data not found")
        return Nonensity_model(data, time, alpha=0.01, omega=1.0, beta=1.0, epsilon=0.01):
    """Analyze results from a time-density model simulation and compare with theory"""
    # Extract actual density from simulation
    density_sim = data['rho']ot found")
        return None
    # Calculate theoretical density based on your model
    def time_density(t, a, w):rom simulation
        S_t = 1.0 / (1.0 + np.sin(w * t)**2)  # Projection factor
        D_t = 1.0 + a * t**2  # Dimension expansion factor
        return S_t * D_tcal density based on your model
    def time_density(t, a, w):
    # Theoretical density at current time*2)  # Projection factor
    density_theory = time_density(time, alpha, omega)actor
        return S_t * D_t
    # Calculate difference between simulation and theory
    mean_density = np.mean(density_sim)me
    theory_error = abs(mean_density - density_theory) / density_theory * 100.0
    
    results = { temporal flow ratio
        'density_sim': density_sim,o(time, beta, epsilon)
        'density_theory': density_theory,
        'mean_density': mean_density, velocity
        'theory_error': theory_error,
        'time': time,y = None
        'alpha': alpha,
        'omega': omegasure = np.mean(data['press']) * flow_ratio
    }f 'vel1' in data:
        vel_magnitude = np.sqrt(np.mean(data['vel1']**2))
    return resultsin data:
            vel_magnitude = np.sqrt(vel_magnitude**2 + np.mean(data['vel2']**2))
def plot_density_timedilation(rel_data, output_file=None):
    """Create a plot showing the relationship between density and time dilation"""
    plt.figure(figsize=(10, 6))l_magnitude * flow_ratio
    
    # Flatten arrays for scatter plotmulation and theory
    density_flat = rel_data['density'].flatten()
    gamma_flat = rel_data['gamma'].flatten()y_theory) / density_theory * 100.0
    
    # Create scatter plot
    plt.scatter(density_flat, gamma_flat, alpha=0.1, s=1)
        'density_theory': density_theory,
    plt.xlabel('Density')ean_density,
    plt.ylabel('Time Dilation Factor (γ)')
    plt.title('Relationship Between Density and Time Dilation')
    plt.xscale('log')a,
    plt.yscale('log')a,
    plt.grid(True, alpha=0.3)
        'epsilon': epsilon,
    if output_file:': flow_ratio,
        plt.savefig(output_file, dpi=300)ressure,
        print(f"Plot saved to: {output_file}")ty
    else:
        plt.show()
    return results
def plot_time_density_comparison(results, output_file=None):
    """Plot comparison between theoretical and simulated time-density"""
    plt.figure(figsize=(12, 8)))e relationship between density and time dilation"""
    plt.figure(figsize=(10, 6))
    # Create a 2x2 grid for the top part
    plt.subplot(2, 2, 1) scatter plot
    # Plot density histogram from simulationen()
    plt.hist(results['density_sim'].flatten(), bins=50, alpha=0.7)
    plt.axvline(results['density_theory'], color='r', linestyle='--', 
                label=f'Theoretical density: {results["density_theory"]:.4f}')
    plt.axvline(results['mean_density'], color='g', linestyle='-',
                label=f'Mean density: {results["mean_density"]:.4f}')
    plt.title(f'Time-Density Model Validation (t={results["time"]:.4f})')
    plt.xlabel('Density')tion Factor (γ)')
    plt.ylabel('Frequency') Between Density and Time Dilation')
    plt.legend()log')
    plt.yscale('log')
    # Plot the theoretical time-density function
    plt.subplot(2, 2, 2)
    t_values = np.linspace(0, max(5.0, results['time']*2), 1000)
        plt.savefig(output_file, dpi=300)
    def time_density(t, a, w): {output_file}")
        S_t = 1.0 / (1.0 + np.sin(w * t)**2) 
        D_t = 1.0 + a * t**2
        return S_t * D_t
    plot_time_density_comparison(results, output_file=None):
    densities = [time_density(t, results['alpha'], results['omega']) for t in t_values]
    plt.plot(t_values, densities, 'b-')
    plt.axvline(results['time'], color='r', linestyle='--')
    plt.axhline(results['density_theory'], color='r', linestyle='--')
    plt.scatter([results['time']], [results['density_theory']], color='r', s=50)
    plt.title('Time-Density Function')lation
    plt.xlabel('Time')density_sim'].flatten(), bins=50, alpha=0.7)
    plt.ylabel('Density')density_theory'], color='r', linestyle='--', 
    plt.grid(True, alpha=0.3)etical density: {results["density_theory"]:.4f}')
    plt.axvline(results['mean_density'], color='g', linestyle='-',
    # Add simulation vs theory informationan_density"]:.4f}')
    plt.subplot(2, 1, 2)sity Model Validation (t={results["time"]:.4f})')
    plt.text(0.5, 0.5, ce(0.01, max(5.0, results['time']*2), 1000)')
             f"Time-Density Model Analysis\n\n"ts['beta'], results['epsilon']) for t in t_range]
             f"Simulation Time: {results['time']:.4f}\n"
             f"Theoretical Density: {results['density_theory']:.6f}\n"
             f"Mean Simulated Density: {results['mean_density']:.6f}\n"
             f"Error: {results['theory_error']:.2f}%\n\n"], color='r', s=50)
             f"Parameters:\n"Ratio Function') max(5.0, results['time']*2), 1000)
             f"Alpha (dimension expansion): {results['alpha']:.6f}\n"
             f"Omega (projection factor): {results['omega']:.6f}\n\n"
             f"This validates the Time-Density Geometry model from our research,\n"
             f"showing how the space-time density relates to our geometric model.",
             ha='center', va='center', fontsize=12)
    plt.axis('off')2, 4)
    x_labels = []densities = [time_density(t, results['alpha'], results['omega']) for t in t_values]
    plt.tight_layout()ities, 'b-')
    plt.axvline(results['time'], color='r', linestyle='--')
    if output_file:ulated_pressure'] is not None:ults['density_theory'], color='r', linestyle='--')
        plt.savefig(output_file, dpi=300)nsity_theory']], color='r', s=50)
        print(f"Time-density comparison plot saved to: {output_file}")
    else:('Time')
        plt.show()dulated_velocity'] is not None:nsity')
        x_labels.append('Velocity')    plt.grid(True, alpha=0.3)
def main():alues.append(results['modulated_velocity'])
    """Main function to process command line arguments"""
    if len(sys.argv) < 2:
        print("Usage: python athena_analysis.py <athena_output_file.h5> [output_plot.png] [analysis_type] [param1] [param2] [param3] [param4]")
        print("Analysis types: 'relativistic' (default) or 'time-density'")
        print("For time-density: param1=alpha, param2=omega, param3=beta, param4=epsilon")
        returnid(True, alpha=0.3)"Theoretical Density: {results['density_theory']:.6f}\n"
    else:         f"Mean Simulated Density: {results['mean_density']:.6f}\n"
    input_file = sys.argv[1]No pressure or velocity data available", ts['theory_error']:.2f}%\n\n"
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
        plt.axis('off')         f"Alpha (dimension expansion): {results['alpha']:.6f}\n"
    # Determine analysis typeega']:.6f}\n\n"
    analysis_type = 'relativistic'  # Defaulteometry model from our research,\n"
    if len(sys.argv) > 3: the space-time density relates to our geometric model.",
        analysis_type = sys.argv[3]el Analysis with Temporal Flow\n\n"r', fontsize=12)
                f"Simulation Time: {results['time']:.4f}\n"plt.axis('off')
    # Read data f"Theoretical Density: {results['density_theory']:.6f}\n"
    time, data = read_athena_data(input_file)sults['mean_density']:.6f}\n"
    if data is None:nsity Error: {results['theory_error']:.2f}%\n\n"
        return  f"Parameters:\n"file:
                f"Alpha (dimension expansion): {results['alpha']:.6f}\n"    plt.savefig(output_file, dpi=300)
    # Perform analysis based on typefactor): {results['omega']:.6f}\n"son plot saved to: {output_file}")
    if analysis_type == 'time-density': {results['beta']:.6f}\n"
        # Get parameters if providedty avoidance): {results['epsilon']:.6f}\n\n"
        alpha = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01}\n")
        omega = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
        beta = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0esults['modulated_pressure'] is not None:ain function to process command line arguments"""
        epsilon = float(sys.argv[7]) if len(sys.argv) > 7 else 0.01
        
        print(f"Performing time-density analysis (alpha={alpha}, omega={omega}, beta={beta}, epsilon={epsilon})...")elocity'] is not None:es: 'relativistic' (default) or 'time-density'")
        results = analyze_time_density_model(data, time, alpha, omega, beta, epsilon)+= f"Modulated Velocity: {results['modulated_velocity']:.6f}\n" time-density: param1=alpha, param2=omega")
        if results is None:rn
            returnemporal Flow models from our research,\n" \
                 f"showing how the space-time density and time flow relate to our geometric model."t_file = sys.argv[1]
        plot_time_density_comparison(results, output_file) 2 else None
        ='center', fontsize=11)
        # Print statistics
        print("\nTime-Density Model Statistics:")
        print(f"Time: {results['time']:.6f}")
        print(f"Theoretical density: {results['density_theory']:.6e}")
        print(f"Mean simulated density: {results['mean_density']:.6e}")utput_file:
        print(f"Theory vs. simulation error: {results['theory_error']:.2f}%")
        print(f"Temporal Flow Ratio: {results['flow_ratio']:.6f}")n plot saved to: {output_file}")t_file)
        
        if results['modulated_pressure'] is not None:
            print(f"Modulated Pressure: {results['modulated_pressure']:.6e}")
        sed on type
        if results['modulated_velocity'] is not None:ain function to process command line arguments"""nalysis_type == 'time-density':
            print(f"Modulated Velocity: {results['modulated_velocity']:.6e}")< 2:ers if provided
        output_file.h5> [output_plot.png] [analysis_type] [param1] [param2]")else 0.01
    else:  # 'relativistic' or any other value defaults to relativistic analysisprint("Analysis types: 'relativistic' (default) or 'time-density'")omega = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
        # Analyze relativistic effects: param1=alpha, param2=omega")]) if len(sys.argv) > 6 else 1.0
        print("Performing relativistic analysis...")7 else 0.01
        rel_data = analyze_relativistic_effects(data)
        if rel_data is None:silon})...")
            return
        
        # Create plot    # Determine analysis type            return
        plot_density_timedilation(rel_data, output_file)ivistic'  # Default
        (sys.argv) > 3:ot_time_density_comparison(results, output_file)
        # Print some statistics        analysis_type = sys.argv[3]        









    main()if __name__ == "__main__":        print(f"Max time dilation factor: {np.max(rel_data['gamma']):.6f}")        print(f"Mean time dilation factor: {np.mean(rel_data['gamma']):.6f}")        print(f"Max velocity: {np.max(rel_data['velocity']):.6f}")        print(f"Mean density: {np.mean(rel_data['density']):.6e}")        print("\nData Statistics:")













































    main()if __name__ == "__main__":        print(f"Max time dilation factor: {np.max(rel_data['gamma']):.6f}")        print(f"Mean time dilation factor: {np.mean(rel_data['gamma']):.6f}")        print(f"Max velocity: {np.max(rel_data['velocity']):.6f}")        print(f"Mean density: {np.mean(rel_data['density']):.6e}")        print("\nData Statistics:")        # Print some statistics                plot_density_timedilation(rel_data, output_file)        # Create plot                    return        if rel_data is None:        rel_data = analyze_relativistic_effects(data)        print("Performing relativistic analysis...")        # Analyze relativistic effects    else:  # 'relativistic' or any other value defaults to relativistic analysis                print(f"Theory vs. simulation error: {results['theory_error']:.2f}%")        print(f"Mean simulated density: {results['mean_density']:.6e}")        print(f"Theoretical density: {results['density_theory']:.6e}")        print(f"Time: {results['time']:.6f}")        print("\nTime-Density Model Statistics:")        # Print statistics                plot_time_density_comparison(results, output_file)                    return        if results is None:        results = analyze_time_density_model(data, time, alpha, omega)        print(f"Performing time-density analysis (alpha={alpha}, omega={omega})...")                omega = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0        alpha = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01        # Get parameters if provided    if analysis_type == 'time-density':    # Perform analysis based on type            return    if data is None:    time, data = read_athena_data(input_file)    # Read data            # Print statistics
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
