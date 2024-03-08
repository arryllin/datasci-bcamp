from numpy import *
from pandas import *

varDf = read_csv("https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv")

varMinMean = round(varDf["Min.Price"].mean(), 1)
varMaxMean = round(varDf["Max.Price"].mean(), 1)

varValues = {"Min.Price": varMinMean, "Max.Price": varMaxMean}
varDf = varDf.fillna(value=varValues)

print(varDf)