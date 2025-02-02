# -*- coding: utf-8 -*-
"""AnnotatedHeatmapBorder.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uedgQNT0jzpShVcGu2i7QwyIIno8VGe0
"""

# Annotated Heatmap Border

# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data (10 rows, 12 columns)
data = np.random.rand(10, 12)

# Create heatmap with annotations and grid lines
sns.heatmap(data, annot=True, linewidths=0.5, linecolor="gray")

# Display the plot
plt.show()