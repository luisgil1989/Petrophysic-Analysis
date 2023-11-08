# Loading and Exploring Log LAS Files With Python


# Introduction
# Log ASCII Standard (LAS) files are a common Oil & Gas industry format for storing and transferring well log data.
#

#
# This code illustrates how to load data in from a LAS file and carry out a basic QC of the data before plotting it on
# a log plot.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#
# Loading and Checking Data
# The first step is to import the required libraries: pandas, matplotlib and LASIO.
# lasio is a library that has been developed to handle and work with LAS files.

# More info on the library can be found at: https://chasm.kgs.ku.edu/ords/qualified.well_page.DisplayWell?f_kid=1042769301


import pandas as pd
import matplotlib.pyplot as plt
import lasio

#To load our file in, we can use the .read() method from LASIO like so:

las = lasio.read("Data/1044222726.las")


# print(las.sections.keys())

# dict_keys(['Version', 'Well', 'Curves', 'Parameter', 'Other'])

######################################################################

# print(las.sections['Version'])
#--------------------------------#
# Mnemonic  Unit  Value  Description
# --------  ----  -----  -----------
# VERS            2.0    CWLS log ASCII Standard -VERSION 2.0
# WRAP            NO     Single line per depth step

#########################################################################

#Now that our file has been loaded, we can start investigating it's contents.

# To find information out about where the file originated from, such as the well name, location and what the depth range
# of the file covers, we can create a simple for loop to go over each header item.
# Using Python's f-string we can join the items together.

# for item in las.sections['Well']:
#     print(f"{item.descr} ({item.mnemonic}): \t\t {item.value}")
#----------------------------------------------------------------------
#  (STRT): 		 2830.0
#  (STOP): 		 3200.0
#  (STEP): 		 0.5
#  (NULL): 		 -999.25
# COMPANY (COMP): 		 ORCA OPERATING COMPANY LLC.
# WELL (WELL): 		 CANTON SWD #1
# FIELD (FLD): 		 BITIKOFER
# LOCATION (LOC): 		 API: #15-113-21342
# PROVINCE (PROV): 		 KANSAS
# SERVICE COMPANY (SRVC): 		 Tucker Wireline Services
# LOG DATE (DATE): 		 SEP 15 2010
# UNIQUE WELL ID (UWI):
# LICENCE (LIC):

# We can see above that we have the key information about the well, such as the name and location.





###############################################################################
# We can also call upon the sections in a different way. In this case we can use las.well to call upon the well section.
#
# If we just want to extract the Well Name, we can simply call it by using the following:

# print(las.well.WELL.value)
#-----------------------------
# CANTON SWD #1




################################################################################

# To quickly see what curve mnemonics are present within the las file we can loop through las.curves and print the mnemonic.

# for curve in las.curves:
#     print(curve.mnemonic)
# ------------------------------------------------
# DEPT
# SP
# CALM
# CALD
# CALN
# GR
# MINV
# MNOR
# LWTLB
# DRHO
# SFL
# RHOB
# NPLS
# PE
# CILD
# ILD
# DPLS
# PIRM






#######################################################################################

# To see what curves are present within the las file, we can repeat the process with the
# Curve Item object and call upon the unit and descr functions to get info on the units
# and the curve's description. The enumerate function allows us to keep a count of the '
# 'number of curves that are present within the file. As enumerate returns a 0 on the first
# 'loop, we need to 1 to it if we want to include the depth curve.


# for count, curve in enumerate(las.curves):
#     print(f"Curve: {curve.mnemonic}, \t Units: {curve.unit}, \t Description: {curve.descr}")
# print(f"There are a total of: {count+1} curves present within this file")
# ----------------------------------------------------------------------------------
# Curve: DEPT, 	 Units: F, 	 Description: Measured Depth
# Curve: SP, 	 Units: MV, 	 Description: Self Potential
# Curve: CALM, 	 Units: IN, 	 Description: Microlog Caliper
# Curve: CALD, 	 Units: IN, 	 Description: Litho Density Caliper
# Curve: CALN, 	 Units: IN, 	 Description: Compensated Neutron Caliper
# Curve: GR, 	 Units: GAPI, 	 Description: Gamma Ray
# Curve: MINV, 	 Units: OHMM, 	 Description: Microinverse Focused
# Curve: MNOR, 	 Units: OHMM, 	 Description: Micronormal Focused
# Curve: LWTLB, 	 Units: LB, 	 Description: Line Weight
# Curve: DRHO, 	 Units: G/C3, 	 Description: Density Correction
# Curve: SFL, 	 Units: OHMM, 	 Description: Shallow Focussed Resistivity
# Curve: RHOB, 	 Units: G/C3, 	 Description: Bulk Density
# Curve: NPLS, 	 Units: %, 	 Description: Neutron Porosity (Limestone)
# Curve: PE, 	 Units: BARN/E, 	 Description: Photoelectric Cross Section
# Curve: CILD, 	 Units: MMHO, 	 Description: Deep Induction Cond. Envir. Cor
# Curve: ILD, 	 Units: OHMM, 	 Description: Deep Induction Resistivity
# Curve: DPLS, 	 Units: %, 	 Description: Density Porosity (2.71 g/cc)
# Curve: PIRM, 	 Units: OHMM, 	 Description: Envir. corr., Phased ILM
# There are a total of: 18 curves present within this file

# Important note:
#
# if we want to remove a curve from the las. file, we use the following code:
#     las.delete_curve('name of the curve')
# once the curved is remove, we use the following code to export the .las file:
# las.write('Exports/nameofthefile.las')



#
# ----------------------------------------------------------------------------------------------

# Converting LAS File to a Pandas Dataframe
#
# Data loaded in using LASIO can be converted to a pandas dataframe using the .df() function. This allows us to
# easily plot data and pass it into one of the many machine learning algorithms.

# we run the following code:
well = las.df()
# print(well.head())


# this is the result:
#            SP  CALM  CALD  CALN      GR  ...    PE    CILD   ILD  DPLS  PIRM
# DEPT                                     ...
# 2830.0    NaN   NaN   NaN   NaN     NaN  ...   NaN     NaN   NaN   NaN   NaN
# 2830.5  50.63  9.05  9.10  9.25   77.70  ...  4.66  145.33  6.88  0.32   NaN
# 2831.0  49.94  9.05  9.11  9.25   95.61  ...  4.18  160.89  6.22  2.13  5.92
# 2831.5  48.80  9.06  9.11  9.28  121.60  ...  3.97  180.03  5.55  5.43  4.94
# 2832.0  47.42  9.12  9.11  9.26  154.57  ...  3.75  204.15  4.90  9.05  4.00



# ---------------------

# To find out more information about data, we can call upon the .info() and .describe() functions.
#
# The .info() function provides information about the data types and how many non-null values are present within each curve.
# The .describe() function, provides statistical information about each curve and can be a useful QC for each curve.

# print(well.describe())
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


# print(well.info())
#
# <class 'pandas.core.frame.DataFrame'>
# Index: 741 entries, 2830.0 to 3200.0
# Data columns (total 17 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   SP      739 non-null    float64
#  1   CALM    739 non-null    float64
#  2   CALD    739 non-null    float64
#  3   CALN    739 non-null    float64
#  4   GR      739 non-null    float64
#  5   MINV    739 non-null    float64
#  6   MNOR    739 non-null    float64
#  7   LWTLB   739 non-null    float64
#  8   DRHO    739 non-null    float64
#  9   SFL     739 non-null    float64
#  10  RHOB    739 non-null    float64
#  11  NPLS    739 non-null    float64
#  12  PE      739 non-null    float64
#  13  CILD    739 non-null    float64
#  14  ILD     739 non-null    float64
#  15  DPLS    739 non-null    float64
#  16  PIRM    737 non-null    float64
# dtypes: float64(17)
# memory usage: 104.2 KB
# None

# Quick Plot
# Using the ploting function within pandas, we can plot all curves on a single plot.

# well.plot()
# plt.show(
#
#     note: the plot was saved as "Plot Test.png"

# We can plot individual curves by supplying a y variable argument like so:

# well.plot(y='GR')



# Convert LAS data to a pandas DataFrame
las_df = well

# Export the DataFrame to a CSV file
las_df.to_csv('Data/1044222726.csv')

# Export the DataFrame to an Excel file
las_df.to_excel('Data/1044222726.xlsx')