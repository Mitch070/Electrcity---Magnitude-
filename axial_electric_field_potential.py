import matplotlib.pyplot as plt
import numpy as np

# Configure figure
figure_title = 'Axial Electric Field and Potential above Uniformly Charged Disk'
number_of_plots = 2
fig = plt.figure(figsize=plt.figaspect(1./number_of_plots), num=figure_title)
subplot1 = fig.add_subplot(1, 2, 1)                      # Create electric field plot
subplot2 = fig.add_subplot(1, 2, 2)                      # Create electric potential plot

# Plot parameters
number_of_grid_points = 1000                        # Set number of points to plot
maximum_field = 2.0
maximum_potential = maximum_field

# Simulation parameters
charge_over_four_pi_vacuum_permittivity = 1.0       # Set charge units
radius = 1.0                                        # Set disk radius
maximum_height = 5 * radius                         # Set sampling maximum to z = 5 * R

# String describing simulation parameters
charge_density_string = r'$\rho(\vec{r}) = \frac{q}{4 \pi R^2} \theta(R-r) \delta(z)$'
charge_string = r'$q = 4\pi\varepsilon_0$'
radius_string = r'$R =$' + '{} m'.format(radius)
text_string = charge_density_string + '\n' + charge_string + '\n' + radius_string

# Set up separate grids for above and below the disk
above_axial_distances = np.linspace(1/number_of_grid_points, maximum_height, num=number_of_grid_points-1)
below_axial_distances = np.linspace(-1/number_of_grid_points, -maximum_height, num=number_of_grid_points-1)

# Calculate E_z(z)
axial_electric_field_above = (2. / radius**2) * charge_over_four_pi_vacuum_permittivity * above_axial_distances * \
                             (1./np.abs(above_axial_distances) - np.power(radius**2 + above_axial_distances**2, -1/2))
axial_electric_field_below = (2. / radius**2) * charge_over_four_pi_vacuum_permittivity * below_axial_distances * \
                             (1./np.abs(below_axial_distances) - np.power(radius**2 + below_axial_distances**2, -1/2))

# Calculate V(z)
axial_electric_potential_above = (2. / radius**2) * charge_over_four_pi_vacuum_permittivity * \
                                 (np.sqrt(radius**2 + above_axial_distances**2) - np.abs(above_axial_distances))
axial_electric_potential_below = (2. / radius**2) * charge_over_four_pi_vacuum_permittivity * \
                                 (np.sqrt(radius**2 + below_axial_distances**2) - np.abs(below_axial_distances))

# Plot E_z(z)
subplot1.plot(above_axial_distances, axial_electric_field_above, color='blue')
subplot1.plot(below_axial_distances, axial_electric_field_below, color='blue')
subplot1.set_title("Electric Field")
subplot1.set_xlabel(r'$z$ (m)')
subplot1.set_ylabel(r'$E_z(z)$ (N/C)')
subplot1.set_xlim(-maximum_height, maximum_height)
subplot1.set_ylim(-maximum_field, maximum_field)
subplot1.axhline(color='black')
subplot1.axvline(color='black', linestyle='--')
subplot1.text(1/maximum_height, -0.5*maximum_field, text_string)

# Plot V(z)
subplot2.plot(above_axial_distances, axial_electric_potential_above, color='orange')
subplot2.plot(below_axial_distances, axial_electric_potential_below, color='orange')
subplot2.set_title("Electric Potential")
subplot2.set_xlabel(r'$z$ (m)')
subplot2.set_ylabel(r'$V(z)$ (J/C)')
subplot2.set_xlim(-maximum_height, maximum_height)
subplot2.set_ylim(-maximum_potential, maximum_potential)
subplot2.axhline(color='black')
subplot2.axvline(color='black', linestyle='--')
subplot2.text(1/maximum_height, -0.5*maximum_potential, text_string)

# Display plot with tight layout
plt.tight_layout()
plt.show()
