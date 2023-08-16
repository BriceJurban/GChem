import numpy as np
import matplotlib.pyplot as plt

def lennard_jones(r, epsilon, sigma):
    """
    Compute the Lennard-Jones potential between two particles.
    """
    term1 = (sigma / r) ** 12
    term2 = (sigma / r) ** 6
    return 4 * epsilon * (term1 - term2)

def main():
    # Parameters for hydrogen-hydrogen interaction based on literature
    epsilon = 5.14e-21  # J
    sigma = 2.82e-10    # m

    # Generate distances (r values)
    r = np.linspace(1e-10, 6e-10, 400)
    V = lennard_jones(r, epsilon, sigma)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(r, V, label='Lennard-Jones Potential')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(sigma, color='red', linestyle='--', label='σ')
    plt.title('Lennard-Jones Potential for H-H Bonding')
    plt.xlabel('Distance (r)')
    plt.ylabel('Potential Energy (V)')
    plt.ylim([-2*epsilon, epsilon])
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()