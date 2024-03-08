from numpy import *
from pandas import *

varDf = read_csv("https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv")

print(varDf.loc[::20 , "Manufacturer":"Type"])