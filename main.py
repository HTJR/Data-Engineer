import pandas as pd
from Helper import create_table,get_data,get_col,get_table,insert_table
import os
f= open('Data.txt','r')

header=""
bod=[]
# Read data from file and store header and data seperaty

for i in f:
    dat=i[1:].strip().split('|')
    if dat[0]=='H':
        header=dat[1:]
    else:
        bod.append(dat[1:])
f.close()

#create dataframe
#if program is run multiple time the rest of the data is appended in data.csv file

df=pd.DataFrame(data=bod,index=None,columns=header)
if not os.path.isfile('data.csv'):
  df.to_csv('data.csv',index=False)
else:
  df.to_csv('data.csv',index=False,header=False,mode='a')

#convert the date column to date format

df['Open_Date']=pd.to_datetime(df['Open_Date'])
df['Last_Consulted_Date']=pd.to_datetime(df['Last_Consulted_Date'])
df['DOB']=[i[len(i)-4:]+i[0:len(i)-4] for i in df['DOB'].tolist()]
df['DOB']= pd.to_datetime(df['DOB'],dayfirst=True)

#get  all the table in database
tab=get_table()
#create table customer if not exist in database
if tab is None:
  create_table("customer")
elif "customer" not in tab:
  create_table("customer")
else:
  print("already created")

#get column names from table customer
lis=get_col()
col= "`,`".join([str(i) for i in lis])
#insert data from dataframe to table customer
for i,row in df.iterrows():
  insert_table(col,row,"customer")

# Get data from customer table
# it stores the data of each customer into its respective tables 
# if the table doesnt exist it is created
myresult = get_data()
for x in myresult:
  country=x[-1]
  info=x[0:-1]
  tab=get_table()
  cn="table_"+country.lower()
  if cn not in tab:
    create_table("Table_"+country)
    insert_table(col,info,cn)
  else:
    insert_table(col,info,cn)
