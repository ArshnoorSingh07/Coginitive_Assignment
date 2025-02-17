import numpy as np
import matplotlib.pyplot as plt

# Use roll number as seed
roll_number = 123456  # Replace with your actual roll number
np.random.seed(roll_number)

# Generate dataset of 50 random values
data = np.random.randn(50)

# Create 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Line plot showing cumulative sum
axes[0, 0].plot(np.cumsum(data), color='b', linestyle='-', marker='o')
axes[0, 0].set_title("Cumulative Sum Plot")
axes[0, 0].set_xlabel("Index")
axes[0, 0].set_ylabel("Cumulative Sum")
axes[0, 0].grid(True)

# Scatter plot with random noise
axes[0, 1].scatter(range(50), data, color='r', alpha=0.6)
axes[0, 1].set_title("Scatter Plot with Noise")
axes[0, 1].set_xlabel("Index")
axes[0, 1].set_ylabel("Random Values")
axes[0, 1].grid(True)

plt.tight_layout()
plt.show()