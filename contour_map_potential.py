import numpy as np
import matplotlib.pyplot as plt


# Figure formatting
font_size = 12

# Problem parameters
specific_potential = 1.0  # V_0
pipe_radius = 1.0         # R


# Set boundaries of grid
x_plot_factor = 2.5      # multiplying factor to add space horizontally based on pipe_separation
y_plot_factor = 2.5      # mulitplying factor to add space vertically based on pipe_separation

x_min = -x_plot_factor * pipe_radius
x_max = -x_min
y_min = -y_plot_factor * pipe_radius
y_max = -y_min

# Plot 100 points of data in each direction
number_of_grid_points = 100

# Set up grid of (x,y) points
y, x = np.meshgrid(np.linspace(x_min, x_max, number_of_grid_points),
                   np.linspace(y_min, y_max, number_of_grid_points))

# Define V(x, y)

linear_charge_density_over_four_pi_vacuum_permittivity = 0.5 * specific_potential

logarithm_argument_numerator = pipe_radius  # place of zero potential
logarithm_argument_denominator = np.sqrt(np.power(x, 2) + np.power(y, 2))
electric_potential = 2.0 * linear_charge_density_over_four_pi_vacuum_permittivity * \
                     np.log(logarithm_argument_numerator / logarithm_argument_denominator)

# Set up plot
fig, ax = plt.subplots()

# Title window
# fig.canvas.set_window_title('')

# Set axis labels
ax.set_ylabel(r'$y$ [m]', size=font_size)
ax.set_xlabel(r'$x$ [m]', size=font_size)

# Set color scale
color_minimum = -specific_potential
color_maximum = specific_potential

# Create color map
colormap = ax.pcolormesh(x, y, electric_potential, cmap='viridis',
                         vmin=color_minimum, vmax=color_maximum)

# Set up axes to match x & y grids
ax.axis([x.min(), x.max(), y.min(), y.max()])

# Create color bar
fig.colorbar(colormap, ax=ax)

# Title plot
plt.title("Electric Potential " + r'$V$' + " Around\n"
          "An Infinitely Long Pipe of Radius " +
          r'$R = $' + str(pipe_radius) + " m\n" 
          r'Held at $V_0 = +$' +
          str(specific_potential) + " V")

# Label color bar
fig.text(0.84, 0.92, r'$V(x, y)$ [V] ', ha='center', va='center', size=font_size)

# Write potential
fig.text(0.5, 0.2, r'$V(x, y) = \frac{V_0}{2} \ln\frac{R}{\sqrt{x^2+y^2}}$',
         ha='center', va='center', size=font_size)

# Show the plots
plt.show()
