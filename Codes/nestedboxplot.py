# -*- coding: utf-8 -*-
"""NestedBoxPlot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Nested Box Plot

import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for displaying plots

# Load the 'tips' dataset
data = sns.load_dataset("tips")

# Create a boxplot to compare 'total_bill' by 'day', split by 'sex'
sns.boxplot(x="day", y="total_bill", hue="sex", data=data, dodge=True)

# Display the plot
plt.show()

