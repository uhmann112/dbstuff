import sys
import pandas as pd

file='./testData.csv'

colNames=[]
dataTypes=[]


with open(file,'r') as f:
    topLine = f.readline()
    for name  in list(topLine.split(',')):
        colNames.append(name)


df = pd.read_csv(file)
for col,dtype in df.dtypes.items():
    dataTypes.append(dtype)
    print(dtype)
