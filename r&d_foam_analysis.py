# -*- coding: utf-8 -*-
"""R&D Foam Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17wT2FzPKKV3DAcIP8pwZzqywx4mKGp3E

Seaborn Graph for All Foam Formulas
"""

# Commented out IPython magic to ensure Python compatibility.
#Import Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.style as style
import collections
from scipy.stats import linregress
# %matplotlib inline

# Read .csv
Labfoam = pd.read_csv('/content/R&D DATABASE - Master Labtech Data(HTT) (2).csv').dropna(axis=0,how='all')

# Edit
Labfoam['Compressive Strength @25% [kPa]'] = Labfoam['Compressive Strength @25% [kPa]'].str.replace(',','')
Labfoam['Compressive Strength @25% [kPa]'] = Labfoam['Compressive Strength @25% [kPa]'].astype(float)
Labfoam['Comp/Density']= (Labfoam['Compressive Strength @25% [kPa]']/Labfoam['Density [kg/m^3]'])

# All Labtech Foam
Lfoam = Labfoam[['Formula Name','Density [kg/m^3]','Compressive Strength @25% [kPa]','Brittleness @ 20%RH','Comp/Density','Month_Year']]

# Show all unique Formula Numbers
capture = r"([0-9][0-9][0-9])"
Lfoam['Formula Number'] = Lfoam['Formula Name'].str.extract(capture)
print(Lfoam['Formula Number'].unique())

# Filter Foams by Friability
gLfoam = Lfoam[Lfoam['Brittleness @ 20%RH']<=3]

#All Nanjiang Foam
# Insert .csv here
Nanfoam = pd.read_csv('/content/R&D DATABASE - Master Nanjing Data(HTT) (2).csv')

# Isolate important columns
Nfoam = Nanfoam[['Formula Name','Density [kg/m^3]','Compressive Strength @25% [kPa]','Brittleness @ 20%RH','Month_Year']]

# Filter Foams by Friability
gNfoam = Nfoam[Nfoam['Brittleness @ 20%RH']<=3]

#All Combined "Good" R&D Foam
allgfoam = pd.concat([gLfoam,gNfoam],axis=0)

# Create Time Period column
allgfoam['Time_Period'] = allgfoam['Month_Year']
for x in allgfoam['Month_Year']:
    if x == "Jul_22" or x == 'Aug_22' or x == 'Sept_22' or x =='Oct_22' or x =='Nov_22' or x =='Dec_22':
      allgfoam.loc[allgfoam['Month_Year'] == x, 'Time_Period'] = 'Jul - Dec 2022'
    elif x == 'Jan_23' or x =='Feb_23' or x =='Mar_23' or x =='Apr_23' or x =='May_23':
      allgfoam.loc[allgfoam['Month_Year'] == x, 'Time_Period'] = 'Jan - May 2023'
    elif x == 'Jun_23':
      allgfoam.loc[allgfoam['Month_Year'] == x, 'Time_Period'] = 'June 2023'
    else:
      allgfoam.loc[allgfoam['Month_Year'] == x, 'Time_Period'] = 'nan'

# Create Compressive Strength vs. Density Graph
from matplotlib import style
# using the style for the plot
plt.style.use('seaborn-darkgrid')

# Seaborn lmplot
graph = sns.lmplot(data = allgfoam, x='Density [kg/m^3]',y='Compressive Strength @25% [kPa]',hue='Brittleness @ 20%RH',fit_reg=False,
           palette='RdYlGn_r')
plt.ylim(0, 100)
plt.xlim(0, 200)
plt.title('All Foam Formulas by Brittleness @ 20%RH')

'''
# Make Target Box
plt.plot([50, 50], [30, 20], 'o:', color='blue')
plt.plot([100, 100], [30, 20], 'o:', color='blue')
plt.plot([50, 100], [20, 20], 'o:', color='blue')
plt.plot([50, 100], [30, 30], 'o:', color='blue')
'''