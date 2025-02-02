# -*- coding: utf-8 -*-
"""ParallelCoordinates.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Parallel Coordinates

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Load the iris dataset
data = sns.load_dataset("iris")

# Create a parallel coordinates plot to visualize the data by species
parallel_coordinates(data, "species", color=("#556270", "#4ECDC4", "#C7F464"))

# Display the plot
plt.show()

