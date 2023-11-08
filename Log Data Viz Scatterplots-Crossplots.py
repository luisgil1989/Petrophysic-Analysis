# Creating Scatterplots (Crossplots) of Well Log Data
# The accompanying video for this notebook can be found on my YouTube channel at:
# Please check it out, like and subscribe.

# Introduction
# Scatterplots are a commonly used data visualisation tool to allow us to identify and determine if there is a
# relationship between two variables. We will also be able to tell if that relationship is a strong one or if there is
# no relationship.

# Within petrophysics scatterplots, or crossplots, are routinely used as part of the interpretation workflow.
# They allow us to determine key interpretation parameters such as:

# clay and shale end points for our clay or shale volume calculations

# outlier detection

# lithology identification

# hydrocarbon identification

# rock typing

# regression analysis
# and more


# More info on the library can be found at: https://chasm.kgs.ku.edu/ords/qualified.well_page.DisplayWell?f_kid=1042769301

#########################################################################################################################

# The first stage of any python project or notebook is generally to import the required libraries.
# In this case we are going to be using lasio to load our las file, pandas for storing our well log data,
# and matplotlib for visualising our data.


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

#########################################################################################################################

# print(df.head(10))
#
# #            SP   CALM   CALD   CALN      GR  ...    PE    CILD   ILD   DPLS  PIRM
# # DEPT                                        ...
# # 2830.0    NaN    NaN    NaN    NaN     NaN  ...   NaN     NaN   NaN    NaN   NaN
# # 2830.5  50.63   9.05   9.10   9.25   77.70  ...  4.66  145.33  6.88   0.32   NaN
# # 2831.0  49.94   9.05   9.11   9.25   95.61  ...  4.18  160.89  6.22   2.13  5.92
# # 2831.5  48.80   9.06   9.11   9.28  121.60  ...  3.97  180.03  5.55   5.43  4.94
# # 2832.0  47.42   9.12   9.11   9.26  154.57  ...  3.75  204.15  4.90   9.05  4.00
# # 2832.5  46.03   9.14   9.11   9.53  187.12  ...  3.53  228.68  4.37  13.21  3.39
# # 2833.0  44.61   9.22   9.19  10.07  213.77  ...  3.27  247.81  4.04  18.95  3.22
# # 2833.5  43.22   9.33   9.96   9.77  225.92  ...  2.92  259.86  3.85  24.92  3.41
# # 2834.0  42.05   9.58   9.92   9.52  194.43  ...  2.56  260.48  3.84  29.52  3.77
# # 2834.5  41.78  10.12  10.01   9.60  132.40  ...  2.35  250.84  3.99  29.80  4.17

############################################################################################################

# Creating a Crossplot / Scatterplot
# Now that we have our data loaded, we can begin creating our first scatterplot/crossplot of our logging data,
# in particular, we will use the density and neutron porosity measurements. These two measurements are often plotted
# like this and can tell us a number of different things about the intervals logged, including hydrocarbon presence,
# lithology, and bad data etc.

# # Set up the scatter plot
# plt.scatter(x='NPLS', y='RHOB', data=df)
#
# # Note:
# #  RHOB   .G/C3       Bulk Density
# #  NPLS   .%          Neutron Porosity (Limestone)
#
# plt.savefig('Scatter-Cross plots/Scatter test 1.png', dpi=300)
# plt.show()


############################################################################################################

# # Before we progress, we can set the default plot size for our scatterplots using plt.rcParams.
# #
# # We can see above that we now have a very simple and not very informative crossplot. Firstly,
# # the values and the way data is displayed is different to what we would expect.
#
# plt.rcParams['figure.figsize'] = (8, 8)
# # Set up the scatter plot
# plt.scatter(x='NPLS', y='RHOB', data=df)
#
# # Change the X and Y ranges
# plt.xlim(-5, 60)
#
# # For the y axis, we need to flip by passing in the scale values in reverse order
# plt.ylim(3.0, 1.5)
#
# plt.savefig('Scatter-Cross plots/Scatter test 2.png', dpi=300)
# plt.show()

# #########################################################################################################
#
# # Adding Labels to the Axes:
# # The scatterplot above is not much use to anyone else, there are no labels or units on the axes. So we need to tell the
# # reader of the plot what is plotted against what.
#
# # We can add these in using plt.xlabel and plt.ylabel.
#
# # Set up the scatter plot
# plt.scatter(x='NPLS', y='RHOB', data=df)
#
# # Change the X and Y ranges
# plt.xlim(-5, 60)
#
# # For the y axis, we need to flip by passing in the scale values in reverse order
# plt.ylim(3.0, 1.5)
#
# # Add in labels for the axes
# plt.ylabel('(RHOB) .G/C3 Bulk Density', fontsize=14)
# plt.xlabel('(NPLS ) .% Neutron Porosity (Limestone)', fontsize=14)
# plt.savefig('Scatter-Cross plots/Scatter test 3.png', dpi=300)
#
# plt.show()

# #####################################################################################################################
#
# # We can add a third variable onto our scatterplot through the use of colour. For this plot, we will add in
# # the c argument and pass it the Gamma Ray (GR) column from the dataframe.
# #
# # To control the range of colours shown we need to pass in values to vmin and vmax.
# # In this example, we will set these to 0 and 100.
#
# # Set up the scatter plot
# plt.scatter(x='NPLS', y='RHOB', data=df,  c='GR', vmin=0, vmax=100)
#
# # Change the X and Y ranges
# plt.xlim(-5, 60)
#
# # For the y axis, we need to flip by passing in the scale values in reverse order
# plt.ylim(3.0, 1.5)
#
# # Add in labels for the axes
# plt.ylabel('(RHOB) .G/C3 Bulk Density', fontsize=14)
# plt.xlabel('(NPLS ) .% Neutron Porosity (Limestone)', fontsize=14)
# plt.savefig('Scatter-Cross plots/Scatter test 4.png', dpi=300)
#
# plt.show()



# ###############################################################
#
# # Changing Colormap and Adding Colorbar
#
# # To understand what the colours on the plot mean, we can add a colorbar.
# # There are a few ways to add colorbars to our plot. As we are just using
# # plt.scatter which is a single figure, we can call upon plt.colorbar()
# # and the also pass in the label we want to display alongside it.
#
# # To change the colour map we are using, we can set it to one of the ones at the webpage below using the cmap argument in
# # plt.scatter(). For this example, we will use rainbow. This will allow low Gamma Ray values to appear in purple/blue and
# # high values to appear in red.
#
# # Set up the scatter plot
# plt.scatter(x='NPLS', y='RHOB', data=df,  c='GR', vmin=0, vmax=100, cmap='rainbow')
#
# # Change the X and Y ranges
# plt.xlim(-5, 60)
#
# # For the y axis, we need to flip by passing in the scale values in reverse order
# plt.ylim(3.0, 1.5)
#
# # Add in labels for the axes
# plt.ylabel('(RHOB) .G/C3 Bulk Density', fontsize=14)
# plt.xlabel('(NPLS ) .% Neutron Porosity (Limestone)', fontsize=14)
#
# # Make the colorbar show
# plt.colorbar(label='Gamma Ray - API')
#
#
# plt.savefig('Scatter-Cross plots/Scatter test 4.png', dpi=300)
#
# plt.show()

#################################################################################################

# Adding Gridlines & Plot Styling

# Style sheets allow us to control the look and feel of the plots. You can find a full list of examples on the matplotlib website
# at: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
#
# To set a style sheet we can use plt.style.use('bmh'). 'bmh' is a particular style that can be found in the reference link above.


#Set the style sheet to bmh
plt.style.use('bmh')

# Set up the scatter plot
plt.scatter(x='NPLS', y='RHOB', data=df,  c='GR', vmin=0, vmax=100, cmap='rainbow')

# Change the X and Y ranges
plt.xlim(-5, 60)

# For the y axis, we need to flip by passing in the scale values in reverse order
plt.ylim(3.0, 1.5)

# Add in labels for the axes
plt.ylabel('(RHOB) .G/C3 Bulk Density', fontsize=14)
plt.xlabel('(NPLS ) .% Neutron Porosity (Limestone)', fontsize=14)

# Make the colorbar show
plt.colorbar(label='Gamma Ray - API')


plt.savefig('Scatter-Cross plots/Scatter-Cross-RHOB-NPLS-GR.png', dpi=300)

plt.show()