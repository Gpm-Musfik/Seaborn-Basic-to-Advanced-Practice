# -*- coding: utf-8 -*-
"""PointPlot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pPHJxHB4EVtIGGMNSSw-Pcs5eZ8LftPX
"""

# Point Plot

import seaborn as sns  # Import seaborn for data visualization
import matplotlib.pyplot as plt  # Import matplotlib for plotting

data = sns.load_dataset("tips")  # Load the 'tips' dataset

sns.pointplot(x="day", y="total_bill", data=data)  # Create a point plot with 'day' and 'total_bill'

plt.show()  # Display the plot

