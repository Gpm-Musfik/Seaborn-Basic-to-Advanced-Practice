# -*- coding: utf-8 -*-
"""ScatterHueStyle.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Scatter Hue Style

import seaborn as sns; import matplotlib.pyplot as plt  # Import necessary libraries

data = sns.load_dataset("tips")  # Load the "tips" dataset

# Create a scatter plot with 'total_bill' on x-axis, 'tip' on y-axis, and differentiate by 'day' and 'time'
sns.scatterplot(x="total_bill", y="tip", hue="day", style="time", data=data)

plt.show()  # Display the plot

