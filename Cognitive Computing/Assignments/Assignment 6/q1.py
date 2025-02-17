import numpy as np
import matplotlib.pyplot as plt

# User input for M
M = float(input("Enter the value for M: "))

# Generate x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Compute y values
y1 = M * x**2
y2 = M * np.sin(x)

# Plot both functions
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label=r'$y = M \cdot x^2$', linestyle='-', color='b')
plt.plot(x, y2, label=r'$y = M \cdot sin(x)$', linestyle='--', color='r')

# Add title, legend, and grid
plt.title("Mathematical Functions Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()
