import matplotlib.pyplot as plt

# Data
energy_levels = [1, 2, 3, 4, 5, 6, 7, 8, "infinity"]
energy_aj = [-2.18, -0.545, -0.242, -0.136, -0.087, -0.061, -0.044, -0.034, 0]
energy_ev = [-13.6, -3.4, -1.51, -0.85, -0.54, -0.378, -0.278, -0.213, 0]

# Create the main figure and axis
fig, ax1 = plt.subplots()

# Plot the data in aJ on the left y-axis
ax1.plot(energy_levels, energy_aj, 'b-', label='Energy in aJ')
ax1.set_xlabel('Energy level n')
ax1.set_ylabel('Energy in aJ', color='b')
ax1.tick_params('y', colors='b')

# Create a second y-axis to plot the data in eV
ax2 = ax1.twinx()
ax2.plot(energy_levels, energy_ev, 'r-', label='Energy in eV')
ax2.set_ylabel('Energy in eV', color='r')
ax2.tick_params('y', colors='r')

# Set the title and show the plot
plt.title('Energy levels of Hydrogen')
plt.show()
