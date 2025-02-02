# -*- coding: utf-8 -*-
"""MultiPalette.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Multi Palette

import seaborn as sns  # Import seaborn for plotting
import matplotlib.pyplot as plt  # Import matplotlib for displaying plots

data = sns.load_dataset("tips")  # Load the 'tips' dataset

# Create a boxplot with day as x-axis, total_bill as y-axis, and time as hue
sns.boxplot(x="day", y="total_bill", hue="time", data=data, palette="Set2")

plt.show()  # Display the plot

