import matplotlib.pyplot as plt
import numpy as np

# Data
energy_levels = np.arange(1, 10)  # 1 through 9, where 9 represents "infinity"
energy_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "infinity"]
energy_aj = [-2.18, -0.545, -0.242, -0.136, -0.087, -0.061, -0.044, -0.034, 0]
energy_ev = [-13.6, -3.4, -1.51, -0.85, -0.54, -0.378, -0.278, -0.213, 0]

# Create the main figure and axis
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot the "lollipop" for aJ on the left y-axis
ax1.stem(energy_levels, energy_aj, basefmt=" ", linefmt='b-', markerfmt='bo', label='Energy in aJ')
ax1.set_xlabel('Energy level n')
ax1.set_ylabel('Energy in aJ', color='b')
ax1.set_xticks(energy_levels)
ax1.set_xticklabels(energy_labels)
ax1.tick_params('y', colors='b')

# Create a second y-axis for eV
ax2 = ax1.twinx()
ax2.stem(energy_levels, energy_ev, basefmt=" ", linefmt='r-', markerfmt='ro', label='Energy in eV')
ax2.set_ylabel('Energy in eV', color='r')
ax2.tick_params('y', colors='r')

# Set the title
plt.title('Energy levels of Hydrogen')

# Optionally, add legend to indicate the colors
#ax1.legend(loc='upper left')
#ax2.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
