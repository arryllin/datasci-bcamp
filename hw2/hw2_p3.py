from numpy import *
from pandas import *

varDf = DataFrame(random.randint(10, 40, 60).reshape(-1, 4))

for varRow in range(15):
    if varDf.iloc[varRow].sum() > 100:
        print(varDf.iloc[varRow])