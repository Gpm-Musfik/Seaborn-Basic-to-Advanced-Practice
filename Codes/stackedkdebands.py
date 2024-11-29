# -*- coding: utf-8 -*-
"""StackedKDEBands.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# stacked KDE bands
import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting

data = sns.load_dataset("tips")  # Load the 'tips' dataset

# Create a stacked KDE plot to visualize the distribution of total_bill by sex
sns.kdeplot(data=data, x="total_bill", hue="sex", multiple="fill")

plt.show()  # Display the plot

