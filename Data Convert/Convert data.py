# Packages / libraries - Math
import os #provides functions for interacting with the operating system
import numpy as np # processamento de grandes, multi-dimensionais arranjos e matrizes, juntamente com uma grande coleção de funções matemáticas de alto nível para operar sobre estas matrizes
import pandas as pd # oferece estruturas e operações para manipular tabelas numéricas e séries temporais
#from pathlib import Path
#import xlwings as xw
#import glob

# Loanding data
raw_data = pd.read_csv('D:\\Documentos\\Python\\old_data\\RF6001.txt')

# Delete 41 rows and define a new store a new variable df
df = raw_data.iloc[41:]

# write new file
df.to_csv('D:\\Documentos\\Python\\old_data\\RF6001.csv')

#loading new data, creating dataframe and mantain the index
new_data = pd.read_csv('D:\\Documentos\\Python\\old_data\\RF6001.csv', delim_whitespace = True)
#new_data = pd.read_csv('D:\\Documentos\\Python\\RF6001.csv', delimiter=',')

# Adding new column headings
new_data.columns = ['Time /s','Absorbance (460 nm)']

# Write new file
new_data.to_csv('D:\\Documentos\\Python\\new_data\\RF6001.csv')
new_data


