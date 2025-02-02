# -*- coding: utf-8 -*-
"""ScatterMarginalHist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Scatter Marginal Hist

import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Load the 'tips' dataset
data = sns.load_dataset("tips")

# Create a jointplot with 'total_bill' on x-axis and 'tip' on y-axis
# Include marginal histograms with 20 bins and filled bars
sns.jointplot(x="total_bill", y="tip", data=data, marginal_kws=dict(bins=20, fill=True))

# Display the plot
plt.show()

