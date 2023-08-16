import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the isotopes for U-238 decay series
# Format: (number of protons, number of neutrons)
isotopes = [
    (92, 146),  # U-238
    (90, 144),  # Th-234
    (91, 143),  # Pa-234
    (92, 142),  # U-234
    (90, 140),  # Th-230
    (88, 138),  # Ra-226
    (86, 136),  # Rn-222
    (84, 134),  # Po-218
    (82, 132),  # Pb-214
    (83, 131),  # Bi-214
    (84, 130),  # Po-214
    (82, 128),  # Pb-210
    (83, 127),  # Bi-210
    (84, 126),  # Po-210
    (82, 124)   # Pb-206
]

# Extract data for plotting
protons = [iso[0] for iso in isotopes]
neutrons = [iso[1] for iso in isotopes]

# Plotting
fig, ax = plt.subplots()
ax.scatter(protons, neutrons, s=100, color='blue', label='Isotopes')

# Highlighting the U-238 decay series (just for demonstration)
decay_series = [(92, 146), (90, 144)]  # Add more points if needed for highlighting
for p, n in decay_series:
    ax.add_patch(patches.Circle((p, n), radius=0.5, color='red'))

ax.set_xlabel('Number of Protons')
ax.set_ylabel('Number of Neutrons')
ax.set_title('Segre Chart')
ax.grid(True)
ax.legend()
plt.show()
