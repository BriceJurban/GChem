import numpy as np
import matplotlib.pyplot as plt

# Physical constant: electric constant (epsilon_0) [8.854187817 x 10^-12 C^2/N*m^2]
epsilon_0 = 8.854187817e-12

def electric_field(q, r0, x, y):
    """
    Compute the electric field vector E=(Ex,Ey) due to point charge q at r0.
    """
    r = np.sqrt((x-r0[0])**2 + (y-r0[1])**2)
    r_hat = np.array([(x-r0[0])/r, (y-r0[1])/r])
    E = q / (4 * np.pi * epsilon_0 * r**2) * r_hat
    return E

def main():
    # Set up grid of points
    nx, ny = 64, 64
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    # Create empty lists to store the total electric field at each point
    Ex, Ey = np.zeros(X.shape), np.zeros(Y.shape)

    # Charges and their positions
    charges = [(1e-9, (-1, 0)), (-1e-9, (1, 0))]   # Here, 1e-9 is a test charge value. It's not realistic, just for visualization.

    # Compute field vector at each point on the grid
    for charge in charges:
        ex, ey = electric_field(charge[0], charge[1], X, Y)
        Ex += ex
        Ey += ey

    # Create a stream plot of the electric field vectors
    fig, ax = plt.subplots(figsize=(8,8))
    ax.streamplot(X, Y, Ex, Ey, color=np.sqrt(Ex**2 + Ey**2), cmap=plt.cm.inferno, linewidth=1, density=2)
    
    # Plot the point charges
    for charge in charges:
        if charge[0] > 0:
            ax.plot(charge[1][0], charge[1][1], 'ro', markersize=8)
        else:
            ax.plot(charge[1][0], charge[1][1], 'bo', markersize=8)
    
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_title('Electric Field due to Point Charges')
    plt.show()

if __name__ == "__main__":
    main()
