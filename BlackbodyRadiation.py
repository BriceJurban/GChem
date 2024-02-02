import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck constant (J*s)
c = 3.0e8     # Speed of light (m/s)
kB = 1.38e-23 # Boltzmann constant (J/K)

# Planck's law
def planck(wavelength, T):
    numerator = 8 * np.pi * h * c
    denominator = (wavelength**5) * (np.exp(h * c / (wavelength * kB * T)) - 1)
    return numerator / denominator

# Rayleigh-Jeans Law
def rayleigh_jeans(wavelength, T):
    return (8 * np.pi * kB * T) / (wavelength**4)

# Wavelength range: 100 nm to 3000 nm 
wavelengths = np.linspace(100e-9, 3000e-9, 1000) # Convert nm to m
frequencies = c / wavelengths * 1e-12 # Convert Hz to THz

# Calculate intensities
I_5000K = planck(wavelengths, 5000)
I_7000K = planck(wavelengths, 7000)
I_classical = rayleigh_jeans(wavelengths, 5000)  # for classical, we can use either temperature as it fails at high frequencies

# Mask for classical theory
RJ_mask = wavelengths > 800e-9

# Plot
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(wavelengths*1e9, I_5000K, 'r', label='5000 K')  # Convert m to nm for plotting
ax1.plot(wavelengths*1e9, I_7000K, 'b', label='7000 K')
ax1.plot(wavelengths[RJ_mask]*1e9, I_classical[RJ_mask], 'k--', label='Classical Theory (Rayleigh-Jeans)')

# X-axis labels
ax1.set_xlabel('Wavelength (nm)', color='b')
ax1.tick_params('x', colors='b')

# Second x-axis for frequency
#ax2 = ax1.twiny()
#ax2.plot(frequencies, np.zeros_like(frequencies), alpha=0) # Create a twin axis without plotting anything
#ax2.set_xlabel('Frequency (10^12 Hz)', color='r')
#ax2.tick_params('x', colors='r')
#ax2.set_xlim(ax1.get_xlim()[1] * c * 1e-3, ax1.get_xlim()[0] * c * 1e-3)  # Note the reversed order to set_xlim


# Y-axis label
ax1.set_ylabel('Intensity')

# Title and legend
plt.title('Blackbody Radiation')
ax1.legend()

plt.tight_layout()
plt.show()
