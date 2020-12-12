import matplotlib.pyplot as plt
import numpy as np

# Configure figure
figure_title = 'radial Electric Field and Potential inside Uniformly Charged Disk'
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
charge_density_string = r'$\rho(\vec{r}) = \frac{3q}{4\pi R^3} \theta(R-r) $'
charge_string = r'$q = 4\pi\varepsilon_0$'
radius_string = r'$R =$' + '{} m'.format(radius)
text_string = charge_density_string + '\n' + charge_string + '\n' + radius_string

# Set up separate grids for inside and outside the disk
inside_radial_distances = np.linspace(1/number_of_grid_points,radius, num=number_of_grid_points-1)
outside_radial_distances = np.linspace(radius, maximum_height, num=number_of_grid_points-1)

# Calculate E_r(r)
radial_electric_field_inside = charge_over_four_pi_vacuum_permittivity * inside_radial_distances/(radius**3)

radial_electric_field_outside = charge_over_four_pi_vacuum_permittivity * outside_radial_distances**-2

# Calculate V(r)
radial_electric_potential_inside = - charge_over_four_pi_vacuum_permittivity * radius/inside_radial_distances**3
radial_electric_potential_outside = - charge_over_four_pi_vacuum_permittivity * 1/radius**2

# Plot E_r(r)
subplot1.plot(inside_radial_distances, radial_electric_field_inside, color='blue')
subplot1.plot(outside_radial_distances, radial_electric_field_outside, color='blue')
subplot1.set_title("Electric Field")
subplot1.set_xlabel(r'$r$ (m)')
subplot1.set_ylabel(r'$E_r(r)$ (N/C)')
subplot1.set_xlim(0, maximum_height)
subplot1.set_ylim(-maximum_field, maximum_field)
subplot1.axhline(color='black')
subplot1.axvline(x=radius, color='black', linestyle='--')
subplot1.text(1/maximum_height, -0.5*maximum_field, text_string)

# Plot V(r)
subplot2.plot(inside_radial_distances, radial_electric_potential_inside, color='orange')
subplot2.plot(radial_electric_potential_outside, color='orange')
subplot2.set_title("Electric Potential")
subplot2.set_xlabel(r'$r$ (m)')
subplot2.set_ylabel(r'$V(r)$ (J/C)')
subplot2.set_xlim(0, maximum_height)
subplot2.set_ylim(-maximum_potential, maximum_potential)
subplot2.axhline(color='black')
subplot2.axvline(x=radius, color='black', linestyle='--')
subplot2.text(1/maximum_height, -0.5*maximum_potential, text_string)

# Display plot with tight layout
plt.tight_layout()
plt.show()
