import sys
import pandas as pd

file='./testData.csv'

colNames=[]
dataTypes=[]
queryList =[]

with open(file,'r') as f:
    topLine = f.readline()
    for name  in list(topLine.split(',')):
        colNames.append(name)


df = pd.read_csv(file)
for col,dtype in df.dtypes.items():
    dataTypes.append(dtype)

def evalData(i):
    dobb = dataTypes[i]
    mat dobb:
        case:

def queryBuilder():
    dbName="test1"
    prompt=""
    for i=0 i<len(colNames) i++:
        prompt+= colNames[i]
        prompt+= evalData(i)
    


CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    JoinDate DATE DEFAULT CURRENT_DATE
);
