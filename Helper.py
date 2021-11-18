import mysql.connector
import pandas as pd
# connect to databse mysql change the database if you want to use differentone
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Wu@tang1434",
  database="mysql"
)
mycursor = mydb.cursor()

# Function to create new tbale with the name paassed

def create_table(nam):
  sql='''CREATE TABLE  {0} (Customer_Name varchar(255) NOT NULL,Customer_ID varchar(18) NOT NULL,Customer_Open_Date DATE NOT NULL,Last_Consulted_DATE DATE,Vaccination_Type char(5),Doctor_Consulted char(255),State char(5),Country char(5),Date_of_Birth DATE,Active_Customer char(1))'''
  mycursor.execute(sql.format((nam)))
  print("Table"+nam+"created")

# Function to Insert data into table
def insert_table(col,row,tab):
  sql = "INSERT INTO `" +tab+ "` (`" +col+ "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
  if isinstance(row,pd.Series):
    mycursor.execute(sql, tuple(row))
  else:
    mycursor.execute(sql,row)
  mydb.commit()

# Retrive the names of table form database 
def get_table():
  mycursor.execute("show tables")
  tab=[i[0] for i in mycursor]
  return tab

# Retrive the column name from the table customer
def get_col():
  mycursor.execute("select column_name from information_schema.columns where table_name='customer' ORDER BY ORDINAL_POSITION")
  lis=[i[0] for i in mycursor]
  res = []
  [res.append(x) for x in lis if x not in res]
  return res
# Retrive the data from customer table
def get_data():
  sql="SELECT *,country FROM customer"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  return myresult
