#!/usr/bin/env python3
"""
VTK File Reader utility for the Genesis-Sphere project
Provides functions to read various VTK file formats and extract simulation data
"""

import numpy as np
import vtk
from vtk.util import numpy_support
import os.path
import sys

def read_vtk_legacy(filename):
    """Read a legacy VTK file and extract data"""
    try:
        # Determine the appropriate reader
        first_line = open(filename, 'r').readline()
        if 'UNSTRUCTURED' in first_line:
            reader = vtk.vtkUnstructuredGridReader()
        elif 'POLYDATA' in first_line:
            reader = vtk.vtkPolyDataReader()
        else:
            reader = vtk.vtkStructuredPointsReader()
            
        reader.SetFileName(filename)
        reader.Update()
        
        # Return the reader output
        return reader.GetOutput()
    except Exception as e:
        print(f"Error reading legacy VTK file {filename}: {e}")
        return None

def read_vtk_xml(filename):
    """Read an XML VTK file and extract data"""
    try:
        # Determine appropriate reader based on extension
        _, ext = os.path.splitext(filename)
        
        if ext.lower() == '.vtp':
            reader = vtk.vtkXMLPolyDataReader()
        elif ext.lower() == '.vtu':
            reader = vtk.vtkXMLUnstructuredGridReader()
        elif ext.lower() == '.vti':
            reader = vtk.vtkXMLImageDataReader()
        elif ext.lower() == '.vtr':
            reader = vtk.vtkXMLRectilinearGridReader()
        elif ext.lower() == '.vts':
            reader = vtk.vtkXMLStructuredGridReader()
        else:
            raise ValueError(f"Unsupported XML VTK extension: {ext}")
            
        reader.SetFileName(filename)
        reader.Update()
        
        # Return the reader output
        return reader.GetOutput()
    except Exception as e:
        print(f"Error reading XML VTK file {filename}: {e}")
        return None

def extract_data_from_vtk(vtk_data):
    """Extract numpy data from VTK data object"""
    data = {}
    
    # Get time from field data if available
    time = 0.0
    try:
        field_data = vtk_data.GetFieldData()
        if field_data.GetArray("TIME"):
            time = field_data.GetArray("TIME").GetValue(0)
    except:
        pass
    
    # Get points if available
    try:
        points_vtk = vtk_data.GetPoints().GetData()
        points_np = numpy_support.vtk_to_numpy(points_vtk)
        
        # Add coordinate data
        data['x'] = points_np[:, 0]
        if points_np.shape[1] > 1:
            data['y'] = points_np[:, 1]
        if points_np.shape[1] > 2:
            data['z'] = points_np[:, 2]
    except:
        # No points data available
        pass
        
    # Extract point data
    point_data = vtk_data.GetPointData()
    num_point_arrays = point_data.GetNumberOfArrays()
    
    for i in range(num_point_arrays):
        array_name = point_data.GetArrayName(i)
        array_vtk = point_data.GetArray(i)
        array_np = numpy_support.vtk_to_numpy(array_vtk)
        
        # Process based on number of components
        num_components = array_vtk.GetNumberOfComponents()
        if num_components > 1:
            # Handle vector data
            if array_name.lower() in ["velocity", "vel"]:
                data['vel1'] = array_np[:, 0]
                data['vel2'] = array_np[:, 1] if num_components > 1 else np.zeros_like(array_np[:, 0])
                data['vel3'] = array_np[:, 2] if num_components > 2 else np.zeros_like(array_np[:, 0])
            elif array_name.lower() in ["b", "bcc", "magnetic"]:
                data['B1'] = array_np[:, 0]
                data['B2'] = array_np[:, 1] if num_components > 1 else np.zeros_like(array_np[:, 0])
                data['B3'] = array_np[:, 2] if num_components > 2 else np.zeros_like(array_np[:, 0])
            else:
                # Generic vector field
                for j in range(num_components):
                    data[f"{array_name}{j+1}"] = array_np[:, j]
        else:
            # Handle scalar data
            if array_name.lower() in ["rho", "density"]:
                data['rho'] = array_np
            elif array_name.lower() in ["press", "pressure", "p"]:
                data['press'] = array_np
            else:
                data[array_name] = array_np
    
    # Extract cell data
    cell_data = vtk_data.GetCellData()
    num_cell_arrays = cell_data.GetNumberOfArrays()
    
    for i in range(num_cell_arrays):
        array_name = cell_data.GetArrayName(i)
        array_vtk = cell_data.GetArray(i)
        array_np = numpy_support.vtk_to_numpy(array_vtk)
        
        # Add cell_ prefix to distinguish from point data
        data[f"cell_{array_name}"] = array_np
    
    return time, data

def read_athena_vtk(filename):
    """Read data from an Athena VTK output file"""
    try:
        print(f"Loading VTK data from {filename}")
        
        # Determine if it's legacy or XML VTK
        _, ext = os.path.splitext(filename)
        
        if ext.lower() == '.vtk':
            vtk_data = read_vtk_legacy(filename)
        else:
            vtk_data = read_vtk_xml(filename)
            
        if vtk_data is None:
            return None, None
            
        # Extract data from VTK object
        time, data = extract_data_from_vtk(vtk_data)
        
        print(f"Successfully read VTK file: {filename} (time = {time})")
        print(f"Available fields: {', '.join(data.keys())}")
        
        return time, data
    except Exception as e:
        print(f"Error reading VTK file {filename}: {e}")
        return None, None

def list_vtk_contents(filename):
    """List all available data arrays in a VTK file without loading the full data"""
    try:
        print(f"Examining contents of VTK file: {filename}")
        
        # Determine if it's legacy or XML VTK
        _, ext = os.path.splitext(filename)
        
        if ext.lower() == '.vtk':
            vtk_data = read_vtk_legacy(filename)
        else:
            vtk_data = read_vtk_xml(filename)
            
        if vtk_data is None:
            return
            
        # List point data
        point_data = vtk_data.GetPointData()
        num_point_arrays = point_data.GetNumberOfArrays()
        
        print(f"\nPoint Data ({num_point_arrays} arrays):")
        for i in range(num_point_arrays):
            array_name = point_data.GetArrayName(i)
            array = point_data.GetArray(i)
            num_components = array.GetNumberOfComponents()
            data_type = array.GetDataType()
            type_name = vtk.vtkImageScalarTypeNameMacro(data_type)
            print(f"  - {array_name}: {num_components} component(s), type: {type_name}")
        
        # List cell data
        cell_data = vtk_data.GetCellData()
        num_cell_arrays = cell_data.GetNumberOfArrays()
        
        print(f"\nCell Data ({num_cell_arrays} arrays):")
        for i in range(num_cell_arrays):
            array_name = cell_data.GetArrayName(i)
            array = cell_data.GetArray(i)
            num_components = array.GetNumberOfComponents()
            data_type = array.GetDataType()
            type_name = vtk.vtkImageScalarTypeNameMacro(data_type)
            print(f"  - {array_name}: {num_components} component(s), type: {type_name}")
        
        # Get information about dimensions/points
        try:
            points = vtk_data.GetPoints()
            num_points = points.GetNumberOfPoints()
            print(f"\nGeometry: {num_points} points")
        except:
            print("\nNo point data available")
            
    except Exception as e:
        print(f"Error examining VTK file {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vtk_reader.py <vtk_file> [list]")
        print("  - Provide a VTK file to read its contents")
        print("  - Add 'list' parameter to only list arrays without loading data")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    if len(sys.argv) > 2 and sys.argv[2].lower() == 'list':
        list_vtk_contents(filename)
    else:
        time, data = read_athena_vtk(filename)
        
        if data:
            print("\nSummary of data read from file:")
            for key, value in data.items():
                if isinstance(value, np.ndarray):
                    print(f"  - {key}: shape {value.shape}, range [{value.min():.6g}, {value.max():.6g}]")
                else:
                    print(f"  - {key}: {value}")
