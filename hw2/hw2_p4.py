from numpy import *
from pandas import *

varDf = DataFrame(random.randint(1, 100, size=(4,4)))
varDfRows = varDf
varDfCols = varDf.transpose()

varRowSum = array.([(lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfRows,1), (lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfRows,2), (lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfRows,3), (lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfRows,4)])
varColSum = array.([(lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfCols,1), (lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfCols,2), (lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfCols,3), (lambda varDf, varLine: varDf.iloc[varLine].sum())(varDfCols,4)])