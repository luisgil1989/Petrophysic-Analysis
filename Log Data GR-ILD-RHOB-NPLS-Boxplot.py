import pandas as pd
import matplotlib.pyplot as plt
import lasio

# Import necessary libraries

# Load the LAS file using LASIO
las = lasio.read("Data/1044222726.las")

# Convert the LAS file to a pandas DataFrame
df = las.df()
df.reset_index(inplace=True)
df.dropna(inplace=True)
df.rename(columns={'DEPT':'DEPTH'}, inplace=True)

# Define a dictionary for customizing the outliers
red_circle = dict(markerfacecolor='red', marker='o', markeredgecolor='white')

# Set up a figure and subplots for GR, RHOB, ILD, and NPLS
fig, axes = plt.subplots(1, 4, figsize=(16, 6))

# Plot GR in the first subplot (ax1)
df['GR'].plot(kind='box', ax=axes[0], showmeans=True, notch=True, flierprops=red_circle)
axes[0].set_xlabel('GR (Gamma Ray)')
axes[0].set_ylabel('Values')
axes[0].set_title('Boxplot of Gamma Ray (GR)')

# Plot RHOB in the second subplot (ax2)
df['RHOB'].plot(kind='box', ax=axes[1], showmeans=True, notch=True, flierprops=red_circle)
axes[1].set_xlabel('RHOB (Density)')

axes[1].set_ylabel('Values')
axes[1].set_title('Boxplot of Density (RHOB)')

# Plot ILD in the third subplot (ax3)
df['ILD'].plot(kind='box', ax=axes[2], showmeans=True, notch=True, flierprops=red_circle)
axes[2].set_xlabel('ILD (Deep Induction Resistivity)')
axes[2].set_ylabel('Values')
axes[2].set_title('Boxplot of Deep Induction Resistivity (ILD)')

# Plot NPLS in the fourth subplot (ax4)
df['NPLS'].plot(kind='box', ax=axes[3], showmeans=True, notch=True, flierprops=red_circle)
axes[3].set_xlabel('NPLS')
axes[3].set_ylabel('Values')
axes[3].set_title('Boxplot of NPLS')

plt.tight_layout()  # Adjust the layout for better visualization

plt.savefig('Boxplot/GR-ILD-RHOB-NPLS-Boxplot.png', dpi=300)
plt.show()
