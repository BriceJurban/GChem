import matplotlib.pyplot as plt
from mendeleev import element

def plot_ionization_energies():
    # Extract symbols and ionization energies for elements 1 to 108
    symbols = [element(i).symbol for i in range(1, 108)]
    
    ionization_energies = []
    for i in range(1, 108):
        ie_list = element(i)._ionization_energies
        if ie_list:
            energy_str = str(ie_list[0]).split()[-1] # Split and get the last part
            ionization_energies.append(float(energy_str))
        else:
            ionization_energies.append(None)

    # Plotting
    plt.figure(figsize=(20, 8))
    plt.plot(symbols, ionization_energies, marker='o', linestyle='-')
    plt.title("First Ionization Energies of Elements")
    plt.xlabel("Element")
    plt.ylabel("First Ionization Energy (eV)")
    plt.xticks(rotation=45)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    plt.savefig("ionization_energies.png")
    plt.show()

if __name__ == "__main__":
    plot_ionization_energies()
