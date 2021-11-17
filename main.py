import pandas as pd
from Helper import create_table,get_data,get_col,get_table,insert_table
import os
f= open('Data.txt','r')

header=""
bod=[]

for i in f:
    dat=i[1:].strip().split('|')
    if dat[0]=='H':
        header=dat[1:]
    else:
        bod.append(dat[1:])
f.close()
df=pd.DataFrame(data=bod,index=None,columns=header)
if not os.path.isfile('data.csv'):
  df.to_csv('data.csv',index=False)
else:
  df.to_csv('data.csv',index=False,header=False,mode='a')


df['Open_Date']=pd.to_datetime(df['Open_Date'])
df['Last_Consulted_Date']=pd.to_datetime(df['Last_Consulted_Date'])
df['DOB']=[i[len(i)-4:]+i[0:len(i)-4] for i in df['DOB'].tolist()]
df['DOB']= pd.to_datetime(df['DOB'],dayfirst=True)

tab=get_table()

if tab is None:
  create_table("customer")
elif "customer" not in tab:
  create_table("customer")
else:
  print("already created")

lis=get_col()
col= "`,`".join([str(i) for i in lis])

for i,row in df.iterrows():
  insert_table(col,row,"customer")

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