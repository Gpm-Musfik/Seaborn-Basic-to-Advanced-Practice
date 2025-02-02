# -*- coding: utf-8 -*-
"""AnnotatedPairPlots.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uedgQNT0jzpShVcGu2i7QwyIIno8VGe0
"""

# Annotated Pair Plots

import seaborn as sns  # For data visualization
import matplotlib.pyplot as plt  # For plot display

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a pair plot with species as the hue and custom markers
sns.pairplot(data, hue="species", markers=["o", "s", "D"])

# Add a title to the plot
plt.suptitle("Pair Plot with Annotations", y=1.02)

# Display the plot
plt.show()