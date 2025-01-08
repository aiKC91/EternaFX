---
created: 2025-01-08T09:17:03-08:00
modified: 2025-01-08T09:17:06-08:00
---

# visualization_tools.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data):
    plt.hist(data, bins=50)
    plt.show()

def plot_scatterplot(x, y):
    sns.scatterplot(x=x, y=y)
    plt.show()

def plot_bar_chart(data):
    sns.barplot(x=data.index, y=data.values)
    plt.show()
