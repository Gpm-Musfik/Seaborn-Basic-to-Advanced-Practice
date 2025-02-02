# -*- coding: utf-8 -*-
"""ScatterRegression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Scatter Regression

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in "tips" dataset
data = sns.load_dataset("tips")

# Create a scatter plot with a regression line
sns.lmplot(x="total_bill", y="tip", data=data)

# Display the plot
plt.show()

