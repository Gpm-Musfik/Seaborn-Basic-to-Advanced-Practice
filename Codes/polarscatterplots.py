# -*- coding: utf-8 -*-
"""PolarScatterPlots.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Polar Scatter Plots

import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import numpy as np  # Importing numpy for random number generation

r = np.random.rand(100)  # Generate 100 random values for radius
theta = 2 * np.pi * r  # Convert random values to angles

plt.figure(figsize=(6, 6))  # Set figure size
plt.subplot(projection="polar")  # Set polar plot projection
plt.scatter(theta, r, alpha=0.75)  # Plot the scatter plot on polar coordinates
plt.show()  # Display the plot

