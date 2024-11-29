# -*- coding: utf-8 -*-
"""ConditionalHeatmapipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uedgQNT0jzpShVcGu2i7QwyIIno8VGe0
"""

# Conditional HeatMap

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the 'tips' dataset
data = sns.load_dataset("tips")

# Create a pivot table of average total bills grouped by day and time
pivot_table = data.pivot_table(index="day", columns="time", values="total_bill", aggfunc="mean")

# Plot a heatmap with annotations and a color gradient
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu")

# Display the heatmap
plt.show()