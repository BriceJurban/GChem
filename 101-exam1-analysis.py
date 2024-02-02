import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, kurtosis, skew
from matplotlib.ticker import MultipleLocator

# Raw test scores
raw_scores = [
60, 58, 57, 54, 53, 53, 53, 53, 52, 51, 51, 51, 51, 51, 51, 50, 50, 49, 48, 48, 47, 47, 47, 47, 47, 46, 46, 46, 46, 45, 45, 45, 45, 45, 45, 45, 44, 44, 44, 44, 44, 43, 43, 43, 42, 42, 42, 42, 42, 41, 41, 41, 41, 40, 40, 40, 39, 38, 38, 37, 37, 37, 37, 37, 36, 36, 36, 36, 35, 34, 34, 34, 33, 33, 33, 33, 33, 33, 33, 32, 32, 32, 32, 31, 31, 31, 31, 31, 31, 31, 31, 30, 30, 29, 29, 28, 27, 27, 26, 26, 26, 25, 25, 25, 24, 22, 22, 21, 21, 20, 16, 12
]

# Round scores to nearest integer
rounded_scores = np.round(raw_scores)

# Compute statistics
mean_score = np.mean(rounded_scores)
std_dev = np.std(rounded_scores)

# Histogram
plt.hist(raw_scores, bins=5, density=False, alpha=0.6, color='b', edgecolor='black', label='Data')


# Plot normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = norm.pdf(x, mean_score, std_dev)
plt.plot(x, pdf, 'k', linewidth=2, label=f'Fit\nMean={mean_score:.2f}\nStd Dev={std_dev:.2f}')
plt.gca().xaxis.set_major_locator(MultipleLocator(10))
plt.legend()
plt.title('Chem 101-001 Midterm 1 Matching/Multiple Choice Score Distribution')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.show()

# Compute skewness and kurtosis
skewness = skew(rounded_scores)
kurt = kurtosis(rounded_scores)

print(f"Mean: {mean_score}")
print(f"Standard Deviation: {std_dev}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurt}")

if abs(skewness) < 0.5 and abs(kurt) < 0.5:
    print("The distribution is approximately normal.")
else:
    print("The distribution deviates from normality.")
