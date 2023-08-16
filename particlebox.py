import numpy as np
import matplotlib.pyplot as plt

def wave_function(n, x, L):
    """Compute the wave function for a given quantum number n and box length L."""
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def plot_wave_functions(L, max_n):
    """Plot wave functions for quantum numbers up to max_n."""
    x = np.linspace(0, L, 1000)  # Define the x-values
    
    plt.figure(figsize=(10, 6))
    
    for n in range(1, max_n + 1):
        psi = wave_function(n, x, L)
        plt.plot(x, psi, label=f'n = {n}')
    
    plt.title('Wave functions for an electron in a 1-D box')
    plt.xlabel('Position (x)')
    plt.ylabel('Wave function (Ψ)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parameters
L = 1.0  # Box length
max_n = 4  # Maximum quantum number to plot

plot_wave_functions(L, max_n)