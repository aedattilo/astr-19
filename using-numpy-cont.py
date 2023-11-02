import numpy as np

x = 1.0
y = 2.0

# exponents and logarithms
print(f"np.exp({x}) = {np.exp(x)}")
print(f"np.log({x}) = {np.log(x)}")
print(f"np.log10({x}) = {np.log10(x)}")
print(f"np.log2({x}) = {np.log2(x)}")

# min/max/misc functions
x = -1.0
print(f"np.fabs({x}) = {np.fabs(x)}")
print(f"np.fmin({x}, {y}) = {np.fmin(x, y)}")
print(f"np.fmax({x}, {y}) = {np.fmax(x, y)}")

# populate arrays
n = 100
z = np.arange(n, dtype=float)
z *= 2.0*np.pi / float(n-1)
sin_z = np.sin(z)

# interpolation
print(f"Our interpolated value of sin(0.75) = {np.interp(0.75, z, sin_z)}.")
print(f"Actual value of sin(0.75) = {np.sin(0.75)}.")