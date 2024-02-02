import matplotlib.pyplot as plt
import numpy as np

# Data
energy_levels = ["1", "2", "3", "4", "5", "6", "7", "8", "infinity"]
energy_aj = [-2.18, -0.545, -0.242, -0.136, -0.087, -0.061, -0.044, -0.034, 0]
energy_ev = [-13.6, -3.4, -1.51, -0.85, -0.54, -0.378, -0.278, -0.213, 0]

# Create the main figure and axis
fig, ax1 = plt.subplots(figsize=(8, 6))

# Width of the bars
width = 0.4

# Set positions for bars
ind = np.arange(len(energy_levels))

# Plot the bars for aJ on the left y-axis
bars1 = ax1.bar(ind, energy_aj, width, color='b', label='Energy in aJ')
ax1.set_xlabel('Energy level n')
ax1.set_ylabel('Energy in aJ', color='b')
ax1.tick_params('y', colors='b')

# Create a second y-axis for eV
ax2 = ax1.twinx()
bars2 = ax2.bar(ind + width, energy_ev, width, color='r', label='Energy in eV')
ax2.set_ylabel('Energy in eV', color='r')
ax2.tick_params('y', colors='r')

# Labeling the x-axis with energy levels
ax1.set_xticks(ind + width / 2)
ax1.set_xticklabels(energy_levels)

# Set the title
plt.title('Energy levels of Hydrogen')

# Optionally, add legend to indicate the colors
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
