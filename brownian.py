import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def brownian_motion(N, dt, delta):
    """
    Simulate a 2D Brownian motion.
    N: Number of steps
    dt: Time step
    delta: Intensity of the random force
    """
    x = np.empty(N)
    y = np.empty(N)
    
    # Initial position is at the center
    x[0], y[0] = 0, 0
    
    # Generate random displacements for each step
    dx = np.sqrt(dt) * np.random.randn(N-1)
    dy = np.sqrt(dt) * np.random.randn(N-1)
    
    # Cumulative sum to generate the path
    x[1:] = np.cumsum(dx)
    y[1:] = np.cumsum(dy)
    
    return x, y

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

# Parameters
N = 1000
dt = 0.1
delta = 2.0

x, y = brownian_motion(N, dt, delta)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_title("2D Brownian Motion")
line, = ax.plot([], [], 'r-')

ani = animation.FuncAnimation(fig, update, N, fargs=[x, y, line], interval=10, blit=False)

plt.show()
