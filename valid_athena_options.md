# Valid Athena Options for Your Docker Build

Based on the error messages, here are the valid options for your current Athena build:

## Time Integrators

Your build supports the following time integrators:
- `rk1` - First-order Runge-Kutta (Forward Euler)
- `rk2` - Second-order Runge-Kutta
- `rk3` - Third-order Runge-Kutta
- `rk4` - Fourth-order Runge-Kutta (if compiled with this option)

The `vl2` integrator appears to be unavailable in your specific build.

## Boundary Conditions

Your build supports the following boundary types:
- `reflecting` - Reflection boundary
- `polar_wedge` - Special boundary for poles in spherical coordinates
- `user` - User-defined boundary (requires custom implementation)

Common boundary types that are NOT supported in your build:
- `outflow` - Not available
- `periodic` - Not available
- `inflow` - Not available

## Command Examples

To run with a valid configuration:

```bash
# Run with a fixed simulation file
/athena/bin/athena -i time_density_spherical_fixed2.in -otime_density_fixed
```

## Troubleshooting

If you encounter errors:

1. Check that your integrator is one of: rk1, rk2, rk3, rk4
2. Make sure boundary conditions use valid types
3. Verify that your mesh dimensions and problem parameters match expectations

You can rebuild Athena with custom options:

```bash
cd /athena
python3 configure.py --prob=blast --coord=spherical_polar --flux=hllc --integrator=vl2
make clean
make -j$(nproc)
```
