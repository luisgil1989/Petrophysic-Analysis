# Creating Simple Log Plots of Well Log Data


# Please check it out, like and subscribe.

# Introduction

# Well log plots are a common visualization tool within geoscience and petrophysics.
# They allow easy visualization of data (for example, Gamma Ray, Neutron Porosity, Bulk Density, etc)
# that has been acquired along the length (depth) of a wellbore. On these plots we display our logging measurements on
# the x axis and measure depth or true vertical depth on the y-axis.


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

# print(df.head())

#            SP  CALM  CALD  CALN      GR  ...    PE    CILD   ILD  DPLS  PIRM
# DEPT                                     ...
# 2830.0    NaN   NaN   NaN   NaN     NaN  ...   NaN     NaN   NaN   NaN   NaN
# 2830.5  50.63  9.05  9.10  9.25   77.70  ...  4.66  145.33  6.88  0.32   NaN
# 2831.0  49.94  9.05  9.11  9.25   95.61  ...  4.18  160.89  6.22  2.13  5.92
# 2831.5  48.80  9.06  9.11  9.28  121.60  ...  3.97  180.03  5.55  5.43  4.94
# 2832.0  47.42  9.12  9.11  9.26  154.57  ...  3.75  204.15  4.90  9.05  4.00

# We can see from the returned results that we have several columns of data, each column represents measurements
# that have been taken whilst the logging tools have been moved along the well.


# The columns represent the following:

# ~Curve Information Block
# #MNEM   .UNIT         API CODE      Curve Description
# #-------.-------    -------------   -----------------------
#  DEPT   .F          00 001 00 00:   Measured Depth
#  SP     .MV         07 010 01 00:   Self Potential
#  CALM   .IN         07 280 12 00:   Microlog Caliper
#  CALD   .IN         45 280 13 00:   Litho Density Caliper
#  CALN   .IN         45 280 24 00:   Compensated Neutron Caliper
#  GR     .GAPI       07 310 01 00:   Gamma Ray
#  MINV   .OHMM       07 270 04 00:   Microinverse Focused
#  MNOR   .OHMM       07 270 04 00:   Micronormal Focused
#  LWTLB  .LB         00 000 00 00:   Line Weight
#  DRHO   .G/C3       45 356 01 00:   Density Correction
#  SFL    .OHMM       07 220 04 00:   Shallow Focussed Resistivity
#  RHOB   .G/C3       45 350 02 00:   Bulk Density
#  NPLS   .%          42 330 01 00:   Neutron Porosity (Limestone)
#  PE     .BARN/E     45 358 00 00:   Photoelectric Cross Section
#  CILD   .MMHO       07 110 45 00:   Deep Induction Cond. Envir. Cor
#  ILD    .OHMM       07 120 45 00:   Deep Induction Resistivity
#  DPLS   .%          45 890 10 00:   Density Porosity (2.71 g/cc)
#  PIRM   .OHMM       07 120 44 00:   Envir. corr., Phased ILM



# # To make it easier to work with our dataframe, we can convert the dataframe index, which is set to depth,
# # to a column within the dataframe. We can achieve this by reseting the index like so.
# #
# # Note that inplace=True allows us to make the changes to the original dataframe object.
# #
df.reset_index(inplace=True)

# print(df.head())
#
# #      DEPT     SP  CALM  CALD  CALN  ...    PE    CILD   ILD  DPLS  PIRM
# # 0  2830.0    NaN   NaN   NaN   NaN  ...   NaN     NaN   NaN   NaN   NaN
# # 1  2830.5  50.63  9.05  9.10  9.25  ...  4.66  145.33  6.88  0.32   NaN
# # 2  2831.0  49.94  9.05  9.11  9.25  ...  4.18  160.89  6.22  2.13  5.92
# # 3  2831.5  48.80  9.06  9.11  9.28  ...  3.97  180.03  5.55  5.43  4.94
# # 4  2832.0  47.42  9.12  9.11  9.26  ...  3.75  204.15  4.90  9.05  4.00

###########################################################################################

# We need to do a slight rename on the DEPT column and change it to DEPTH

df.rename(columns={'DEPT':'DEPTH'}, inplace=True)

# print(df.head())
#
# #     DEPTH     SP  CALM  CALD  CALN  ...    PE    CILD   ILD  DPLS  PIRM
# # 0  2830.0    NaN   NaN   NaN   NaN  ...   NaN     NaN   NaN   NaN   NaN
# # 1  2830.5  50.63  9.05  9.10  9.25  ...  4.66  145.33  6.88  0.32   NaN
# # 2  2831.0  49.94  9.05  9.11  9.25  ...  4.18  160.89  6.22  2.13  5.92
# # 3  2831.5  48.80  9.06  9.11  9.28  ...  3.97  180.03  5.55  5.43  4.94
# # 4  2832.0  47.42  9.12  9.11  9.26  ...  3.75  204.15  4.90  9.05  4.00

############################################################################################

# # # Creating a Simple Line Plot
# # # We can easily create a simple plot by calling upon df.plot() and passing in two of our columns
# #
# df.plot('GR', 'DEPTH')
# plt.savefig('Log Plot/QuickPlot.png', dpi=300)
# plt.show()

##############################################################################################

# # Quick Subplot
# #
# # If we want to view all of the columns within the dataframe, we can generate a subplot grid.
# #
# # This is done by taking the same line as before (df.plot()),
# # and instead of passing in curve names, we pass in subplots=True. We can also specify a figure size (figsize(),
# # which controls how large the plot will appear.
#
# df.plot(subplots=True, figsize=(15, 15))
# plt.savefig('Log Plot/QuickSubPlot.png', dpi=300)
# plt.show()
#
#
# # And we now see a grid of plots, one for each of the columns within the dataframe. This is a useful way to check where
# # we have data and where we may have gaps.
#
# # We do not have much control over this plot, but we will now see how we can start building up a log plot with multiple
# # columns and have full control over the scale, colour and visual appearance of the plot.

############################################################################################################################

# Working with Subplots in Matplotlib



# # Create subplots for GR, ILD  against Depth
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
#
# # Plot GR on the first subplot
# ax1.plot(df['GR'], df['DEPTH'], color='black')
# ax1.set_xlabel('GR [API]')
# ax1.set_ylabel('Depth [Ft]')
# ax1.invert_yaxis()  # Invert y-axis to show depth increasing downwards
# ax1.grid(True)
#
# # Plot ILD on the second subplot
# ax2.plot(df['ILD'], df['DEPTH'], color='green')
# ax2.set_xlabel('ILD (Deep Induction Resistivity) [Ohmm]')
# ax2.semilog()
# ax2.invert_yaxis()  # Invert y-axis to show depth increasing downwards
# ax2.grid(True)
#
# plt.tight_layout()  # Adjust subplots to prevent overlap
# plt.savefig('Log Plot/GR-ILD-Subplots.png', dpi=300)
# plt.show()


# # Create subplots for GR, ILD and RHOB against Depth
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
#
# # Plot GR on the first subplot
# ax1.plot(df['GR'], df['DEPTH'], color='black')
# ax1.set_xlabel('GR [API]')
# ax1.set_ylabel('Depth [Ft]')
# ax1.invert_yaxis()  # Invert y-axis to show depth increasing downwards
# ax1.grid(True)
#
# # Plot ILD on the second subplot
# ax2.plot(df['ILD'], df['DEPTH'], color='yellow')
# ax2.set_xlabel('ILD (Deep Induction Resistivity) [Ohmm]')
# ax2.semilogx()
# ax2.invert_yaxis()  # Invert y-axis to show depth increasing downwards
# ax2.grid(True)
#
# # Plot RHOB on the third subplot
# ax3.plot(df['RHOB'], df['DEPTH'], color='gray')
# ax3.set_xlabel('RHOB (Bulk Density) [G/C3]')
# ax3.invert_yaxis()  # Invert y-axis to show depth increasing downwards
# ax3.grid(True)
#
#
# plt.tight_layout()  # Adjust subplots to prevent overlap
# plt.savefig('Log Plot/GR-ILD-RHOBSubplots.png', dpi=300)
# plt.show()



#####################################################



# Create subplots for GR, ILD, RHOB, and NPLS against Depth
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Plot GR on the first subplot
ax1.plot(df['GR'], df['DEPTH'], color='black')
ax1.set_xlabel('GR (Gamma Ray)')
ax1.set_ylabel('Depth')
ax1.invert_yaxis()  # Invert y-axis to show depth increasing downwards
ax1.xaxis.set_ticks_position('top')  # Put x-axis on top
ax1.grid(True)

# Plot ILD on the second subplot
ax2.plot(df['ILD'], df['DEPTH'], color='yellow')
ax2.set_xlabel('ILD (Deep Induction Resistivity)')
ax2.set_yticklabels([])  # Remove y-axis labels
ax2.invert_yaxis()  # Invert y-axis to show depth increasing downwards
ax2.xaxis.set_ticks_position('top')  # Put x-axis on top
ax2.grid(True)

# Plot RHOB on the third subplot
ax3.plot(df['RHOB'], df['DEPTH'], color='gray', label='RHOB')
ax3.set_xlabel('RHOB')
ax3.invert_yaxis()  # Invert y-axis to show depth increasing downwards
ax3.xaxis.set_ticks_position('top')  # Put x-axis on top
ax3.yaxis.set_ticks_position('right')  # Put y-axis on the right
ax3.set_yticklabels([])  # Remove y-axis labels
ax3.grid(True)

# Create a twin x-axis and plot NPLS on the second x-axis
ax3_twinx = ax3.twiny()
ax3_twinx.plot(df['NPLS'], df['DEPTH'], color='red', label='NPLS')
ax3_twinx.set_xlabel('NPLS')
ax3_twinx.invert_yaxis()  # Invert y-axis to show depth increasing downwards
ax3_twinx.invert_xaxis()  # Invert x-axis for 'NPLS'
ax3_twinx.set_xlim(0, 40)  # Set NPLS limit between 0 and 40
ax3_twinx.xaxis.set_ticks_position('top')  # Put x-axis on top
ax3_twinx.grid(True)

# Get the handles and labels from both plots
handles1, labels1 = ax3.get_legend_handles_labels()
handles2, labels2 = ax3_twinx.get_legend_handles_labels()

# Concatenate the handles and labels
handles = handles1 + handles2
labels = labels1 + labels2

# Create a single legend for both RHOB and NPLS
ax3.legend(handles, labels, loc='upper left')


plt.tight_layout()  # Adjust subplots to prevent overlap

plt.savefig('Log Plot/GR-ILD-RHOB-NPLSSubplot.png', dpi=300)
plt.show()
