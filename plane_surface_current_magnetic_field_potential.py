# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Create figure
figure_title = 'Magnetic Field and Potential Above and Below a Plane Surface Current'
number_of_plots = 2
fig = plt.figure(figsize=plt.figaspect(1./number_of_plots), num=figure_title)
plt.suptitle(figure_title)

# Plot parameters
maximum_x = 2
number_of_grid_points_in_one_direction = 5

# Simulation parameters
current_magnetic_permeability_product = 1.0

# String describing simulation parameters
current_density_string = r'$\vec{J}(\vec{r}) = K \delta(z) \hat{x}$'
current_string = r'$K = 1/\mu_0$'
current_text_string = current_density_string + '\n' + current_string

# Strings describing field and potential
field_string = r'$\vec{B}(\vec{r}) = \mathrm{sgn}(z) \frac{\mu_0 K}{2} \hat{y}$'
potential_string = r'$\vec{A}(\vec{r}) = -\frac{\mu_0 K}{2} |z| \hat{x}$'

# Create in 1-row, 3-column table of subplots the first subplot
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Set up the grid
#   In the x-direction
x_minimum = -maximum_x
x_maximum = maximum_x
n_x_points = number_of_grid_points_in_one_direction-1
x_points = np.linspace(x_minimum, x_maximum, n_x_points)
#   In the y-direction
y_minimum = x_minimum
y_maximum = x_maximum
n_y_points = n_x_points
y_points = np.linspace(y_minimum, y_maximum, n_y_points)
#   In the z-direction
z_minimum = x_minimum
z_maximum = x_maximum
n_z_points = number_of_grid_points_in_one_direction-1
z_points = np.linspace(z_minimum, z_maximum, n_z_points)
#   Put all of the grid vectors into matrices
x, y, z = np.meshgrid(x_points, y_points, z_points)

# Make the direction data for the arrows for magnetic field (B = (u = 0, v = sgn(z) u0 K / 2, w = 0))
u = 0.
v = np.sign(z) * current_magnetic_permeability_product / 2
w = 0.

# Create vectors at grid points x, y, z of components u, v, w normalized
ax1.quiver(x, y, z, u, v, w, normalize=False)

# Label graph
plt.title(r'Magnetic Field $\vec{B} [T]$')
ax1.set_xlabel(r'$x$ (m)')
ax1.set_ylabel(r'$y$ (m)')
ax1.set_zlabel(r'$z$ (m)')
ax1.text(x_minimum, y_minimum, 2.5*z_minimum, field_string)

# Create in 1-row, 3-column table of subplots the second subplot
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Make the direction data for the arrows for magnetic potential (A = (u = -u0 K |z| / 2, v = 0, w = 0))
u = -1. * current_magnetic_permeability_product * np.abs(z) / 2
v = 0.
w = 0.

# Create vector field
ax2.quiver(x, y, z, u, v, w, normalize=False, color='orange')

# Label graph
plt.title(r'Magnetic Potential $\vec{A}$ [T m]')
ax2.set_xlabel(r'$x$ (m)')
ax2.set_ylabel(r'$y$ (m)')
ax2.set_zlabel(r'$z$ (m)')
ax2.text(x_minimum, y_minimum, 2.5*z_minimum, potential_string)


# Place current text string down and to the left of the right figure
ax2.text(2.25*x_minimum, 2.25*y_minimum, 2.25*z_minimum, current_text_string)

plt.show()

