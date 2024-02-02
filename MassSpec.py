import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def plot_mass_spectrum(masses, abundances):
    plt.bar(masses, abundances, width=0.8, align='center', color='blue', alpha=0.7)
    
    plt.xlabel('m/z')
    plt.ylabel('Relative Abundance')
    plt.title('Mass Spectrum')

    # Set y-axis major and minor ticks
    ax = plt.gca()  # Get the current axis instance
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_minor_locator(MultipleLocator(5))

    plt.minorticks_on()
    plt.grid(axis='y', which='both')  # Display grids for both major and minor ticks
    plt.xticks(masses)
    
    plt.show()

# Isotope data
masses = [121, 123]
abundances = [100, 75]
plot_mass_spectrum(masses, abundances)
