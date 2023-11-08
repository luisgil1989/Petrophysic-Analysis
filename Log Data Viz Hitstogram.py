# Introduction
#
# Histograms are a great way to explore the distribution of data. They are a commonly used tool within petrophysics
# for understanding the spread and distribution of data, and for picking key interpretation parameters such as shale
# or clay volume minimum and maximum values.

# -------------

# Loading and Checking Data
# The first step is to import the required libraries: pandas, matplotlib and LASIO.
# lasio is a library that has been developed to handle and work with LAS files.

# More info on the library can be found at: https://chasm.kgs.ku.edu/ords/qualified.well_page.DisplayWell?f_kid=1042769301


import pandas as pd
import matplotlib.pyplot as plt
import lasio

#To load our file in, we can use the .read() method from LASIO like so:

las = lasio.read("Data/1044222726.las")

# We then convert the las file to a pandas dataframe object.

df = las.df()

# Using the .describe() method we can explore the summary statistics of the data.

# print(df.describe())
#
#                SP        CALM        CALD  ...         ILD        DPLS        PIRM
# count  739.000000  739.000000  739.000000  ...  739.000000  739.000000  737.000000
# mean     9.593004    8.890189    9.045629  ...   13.691137   13.855115   15.346635
# std     38.450648    0.400948    0.423789  ...   22.988253   10.160586   25.100663
# min    -55.500000    8.370000    8.590000  ...    0.610000   -6.390000    0.670000
# 25%    -34.355000    8.680000    8.900000  ...    2.795000    6.500000    3.120000
# 50%     31.850000    8.840000    8.940000  ...    5.210000   10.930000    5.340000
# 75%     43.810000    8.900000    9.060000  ...    8.660000   21.015000    9.670000
# max     66.680000   11.480000   12.730000  ...  109.140000   58.750000  117.270000
#
# [8 rows x 17 columns]

# --------------------------------------------

# Creating Histograms Using pandas
# We can create a quick histogram using pandas without relying on importing other libraries.

# df['GR'].plot(kind='hist')
# plt.xlabel('Gamma Ray - API', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.show()

# The plot was saved as HistoTest1 at the folder names "Histograms"

# This generates a very minimal plot. We can see that the values range from around 25 to 150, with
#     a very small piece of data between 200 to 300 API. Each bin is around 25 API wide, which is quite a large range.
#
# We can control this by specifying a set number for the bins argument, in this example we will set it to 30.

# plt.hist(df['GR'], bins=30)
# plt.xlabel('Gamma Ray - API', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.show()

# The plot was saved as HistoTest2 at the folder names "Histograms"

# Let's tidy the plot up a little by adding edge colours to the bins.

# plt.hist(df['GR'], bins=30, edgecolor='black')
# plt.xlabel('Gamma Ray - API', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.show()


# The plot was saved as HistoTest3 at the folder names "Histograms"



# To tidy the plot up further, we can assign both an x and y label, and also set the x-axis limits.

# plt.hist(df['GR'], bins=30, color='red', alpha=0.5, edgecolor='black')
# plt.xlabel('Gamma Ray - API', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.xlim(0,175)
#
# plt.savefig('Histograms/HistoTest4.png', dpi=300)
#
# plt.show()


# When calculating clay and shale volumes we often use the percentiles as our interpretation parameters.
#
# These can be calculated using built in pandas functions: mean() and quantile().

# mean = df['GR'].mean()
# p5 = df['GR'].quantile(0.05)
# p95 = df['GR'].quantile(0.95)
#
# print(f'Mean: \t {mean}')
# print(f'P05: \t {p5}')
# print(f'P95: \t {p95}')
#
# Mean: 	 56.78223274695534
# P05: 	 18.288999999999998
# P95: 	 134.69400000000002

# To get an idea of where these points fall in relation to our data, we can add them onto the plot using axvline
# and passing in the calculated variables, a colour and a label.

# mean = df['GR'].mean()
# p5 = df['GR'].quantile(0.05)
# p95 = df['GR'].quantile(0.95)
#
#
# df['GR'].plot(kind='hist', bins=30, color='red', alpha=0.5, edgecolor='black')
# plt.xlabel('Gamma Ray', fontsize=14)
# plt.ylabel('Frequency', fontsize=14)
# plt.xlim(0,175)
#
# plt.axvline(mean, color='blue', label='mean')
# plt.axvline(p5, color='green', label='5th Percentile')
# plt.axvline(p95, color='purple', label='95th Percentile')
#
# plt.legend()
# plt.savefig('Histograms/GR Histogram.png', dpi=300)
# plt.show()

# In addition to the bars, we can also add in a kernel density estimation,
# which provides us with a line illustrating the distribution of the data.

mean = df['GR'].mean()
p5 = df['GR'].quantile(0.05)
p95 = df['GR'].quantile(0.95)


df['GR'].plot(kind='hist', bins=30, color='red', alpha=0.5, density=True, edgecolor='black')
df['GR'].plot(kind='kde', color='black')
plt.xlabel('Gamma Ray', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.xlim(0,175)

plt.axvline(mean, color='blue', label='mean')
plt.axvline(p5, color='green', label='5th Percentile')
plt.axvline(p95, color='purple', label='95th Percentile')

plt.legend()
plt.savefig('Histograms/GR Histogram-KernelDensity.png', dpi=300)
plt.show()


