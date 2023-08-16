import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Sample data
x = np.array([0.5, 1.2, 1.8, 3.9, 5.7, 8.3])
y = np.array([0.1112, 0.21688, 0.40032, 0.86736, 1.39768, 1.84592])

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
regress_values = x * slope + intercept

# Plotting
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, regress_values, color='black', label='Linear Regression')

# Setting plot titles and labels
plt.title('[Y] of [Analyte] as a Function of [X]')
plt.xlabel('X-Axis Title [Units]')
plt.ylabel('Y-Axis Title [Units]')

# Annotating the linear regression equation and R^2 on the plot
plt.text(min(x), max(y) - (max(y) - min(y)) * 0.1, 
         f'y = {slope:.4f}x + {intercept:.4f}', color='black')
plt.text(min(x), max(y) - (max(y) - min(y)) * 0.15, 
         f'R^2 = {r_value**2:.4f}', color='black')

# Setting the window based on the domain and range of the data
plt.xlim(min(x) - 0.1*(max(x)-min(x)), max(x) + 0.1*(max(x)-min(x)))
plt.ylim(min(y) - 0.1*(max(y)-min(y)), max(y) + 0.1*(max(y)-min(y)))

# Displaying the plot
#plt.legend()
plt.grid(True)
plt.show()