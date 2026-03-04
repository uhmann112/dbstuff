import sys
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="testDB",
    user="postgres",
    password="",
    host="/run/postgresql/",
    port="5432"
)
cur = conn.cursor()


file='./testData.csv'

colNames=[]
dataTypes=[]
queryList =[]
prompt ="CREATE TABLE "
with open(file,'r') as f:
    topLine = f.readline()
    for name  in list(topLine.split(',')):
        colNames.append(name)


df = pd.read_csv(file)
for col,dtype in df.dtypes.items():
    dataTypes.append(dtype)


def evalData(i):
    dobb = dataTypes[i]
    match dobb:
        case "str":
            return "VARCHAR(100)"
        case "int64":
            return "INT"
        case "float64":
            return "FLOAT"
        case "bool":
            return "BOOLEAN"
        case "datetime64[ns]":
            return "DATETIME"


def queryBuilder():
    global prompt
    tbName="testTable"
    prompt+=tbName
    prompt+=" (\n"

    for i in range(len(colNames)):
        prompt+= colNames[i]
        prompt+=" "
        prompt+= evalData(i)
        if i < len(colNames) - 1:
            prompt += ","
        prompt+="\n"

    prompt+=");"
    print(prompt)


queryBuilder()

cur.execute(prompt)
conn.commit()
