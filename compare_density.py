#!/usr/bin/env python3
"""
Comparison tool for Athena simulation outputs
Compares density profiles between time-density model and standard simulations
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def compare_density_profiles(file1, file2, output_file=None):
    """Compare density profiles from two different simulation outputs"""
    try:
        # Load data from both files
        time_density = np.loadtxt(file1)
        standard = np.loadtxt(file2)
        
        # Create plot
        plt.figure(figsize=(10, 6))
        
        # Plot density profiles
        plt.plot(time_density[:,0], time_density[:,4], label="Time Density", linewidth=2)
        plt.plot(standard[:,0], standard[:,4], label="Standard", linewidth=2, linestyle='--')
        
        # Add labels and formatting
        plt.xlabel("X")
        plt.ylabel("Density (ρ)")
        plt.legend()
        plt.title("Density Comparison: Time-Density Model vs Standard")
        plt.grid(alpha=0.3)
        
        # Save or display the plot
        if output_file:
            # Create output directory if it doesn't exist
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            plt.savefig(output_file, dpi=300)
            print(f"Comparison plot saved to: {output_file}")
        else:
            plt.show()
            
    except Exception as e:
        print(f"Error comparing files: {e}")
        return False
        
    return True

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python compare_density.py <time_density_file> <standard_file> [output_plot.png]")
        print("Example: python compare_density.py time_density.out1.00000 standard.out1.00000 comparison.png")
        
        # If no arguments provided, use default files for quick testing
        print("\nNo arguments provided. Using default files for demonstration:")
        file1 = "time_density.out1.00000"
        file2 = "standard.out1.00000"
        
        if os.path.exists(file1) and os.path.exists(file2):
            print(f"Found test files. Comparing {file1} and {file2}...")
            compare_density_profiles(file1, file2)
        else:
            print(f"Default files not found. Please specify input files.")
            sys.exit(1)
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        
        compare_density_profiles(file1, file2, output_file)
