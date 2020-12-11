
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np

# Create figure object with title and make the height/width ratio = 1:3

figure_title = 'Figure 1.18 in Griffiths, Introduction to Electrodynamics, 4th Ed.'
fig = plt.figure(figsize=plt.figaspect(0.333), num=figure_title)
# Create in 1-row, 3-column table of subplots the first subplot
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
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

# v of x,y,z = r**2 r-hat
r = np.sqrt(x**2+y**2+z**2)
u = x*r
v = y*r
w = z*r


# Create vectors at grid points x, y, z of components u, v, w normalized
ax1.quiver(x, y, z, u, v, w, normalize=True)
plt.title(r'$\vec{v}=r^2\hat{r}\vec{\nabla}*\vec{v}=4r$')

# Make a second subplot on the same grid with arrows (vector = (u = 0, v = 0, w = 1))
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
u = x/r**3
v = y/r**3
w = z/r**3
ax2.quiver(x, y, z, u, v, w, normalize=True)

plt.title(r'$\vec{v}=1/r^2\hat{r}\vec{\nabla}*\vec{v}=0$')
plt.show()

