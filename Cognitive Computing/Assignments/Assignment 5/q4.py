# Q4. Generate x values using np.linspace() from -10 to 10 with 100 points. Use 
# each function from the list below and compute y values using NumPy: 
#  Y = x2 
#  Y = sin(x) 
#  Y = ex 
#  Y = log(|x| + 1) 
# Plot the chosen function using Matplotlib. Add title, labels, and grid for clarity. 

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y_values = {
    'Y = x^2': x**2,
    'Y = sin(x)': np.sin(x),
    'Y = e^x': np.exp(x),
    'Y = log(|x| + 1)': np.log(np.abs(x) + 1)
}

for label, y in y_values.items():
    plt.figure()
    plt.plot(x, y, label=label)
    plt.title(f'Plot of {label}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()