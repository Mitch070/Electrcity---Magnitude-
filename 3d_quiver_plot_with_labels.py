# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=plt.figaspect(0.5))

# Create in 1-row, 3-column table of subplots the first subplot
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Set up the grid
#   In the x-direction
x_minimum = -10
x_maximum = 10
n_x_points = 9
x_points = np.linspace(x_minimum, x_maximum, n_x_points)
#   In the y-direction
y_minimum = x_minimum
y_maximum = x_maximum
n_y_points = n_x_points
y_points = np.linspace(y_minimum, y_maximum, n_y_points)
#   In the z-direction
z_minimum = x_minimum
z_maximum = x_maximum
n_z_points = 5
z_points = np.linspace(z_minimum, z_maximum, n_z_points)
#   Put all of the grid vectors into matrices
x, y, z = np.meshgrid(x_points, y_points, z_points)

# Make the direction data for the arrows (vector = (u = x, v = y, w = z))
u = x
v = y
w = z

# Create vectors at grid points x, y, z of components u, v, w normalized
ax1.quiver(x, y, z, u, v, w, normalize=True)
plt.title(r'Vector Field $\vec{v} = r \hat{r}$ with Divergence $\vec{\nabla}\cdot\vec{v} = 3$')

# Create in 1-row, 3-column table of subplots the second subplot
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# v = r-hat / r = r-vector / r^2
r_squared = np.power(x, 2) + np.power(y, 2) + np.power(z, 2)
u = np.divide(x, r_squared, where=r_squared != 0)
v = np.divide(y, r_squared, where=r_squared != 0)
w = np.divide(z, r_squared, where=r_squared != 0)

ax2.quiver(x, y, z, u, v, w, normalize=True)
plt.title(r'Vector Field $\vec{v} = \frac{1}{r} \hat{r}$ with Divergence $\vec{\nabla}\cdot\vec{v} = \frac{1}{r^2}$')

plt.show()

