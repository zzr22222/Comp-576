import matplotlib as plt


import numpy as np


# Create a figure and axis
fig, ax = plt.subplots()

# Generate data for the plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the sine wave
ax.plot(x, y, label='Sine wave')

# Adding labels and title
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Sine Wave Plot')

# legend
ax.legend()

