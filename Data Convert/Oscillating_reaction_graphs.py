# Packages / libraries - Math
import os # provides functions for interacting with the operating system
import numpy as np # perform a wide variety of mathematical operations on arrays
import pandas as pd # analyzing, cleaning, exploring, and manipulating data
from matplotlib import pyplot as plt # graph
import matplotlib.pyplot as plt
import seaborn as sns # graph
%matplotlib inline
import seaborn.objects as so

# Loading data
df = pd.read_csv('D:\\Documentos\\Python\\new_data\\RF6001.csv')

#Size of graph
sns.set(rc={'figure.figsize':(12,10)})
# Style of grph
sns.set_style("whitegrid")
# write grph
ax = sns.lineplot(x = 'Time /s', y = 'Absorbance (460 nm)', color ='black', data = df)
# Scale
ax.set_xlim(xmin = 0, xmax = 7553.0)
ax.set_ylim(ymin = 0)
plt.savefig('RF6001.png')

