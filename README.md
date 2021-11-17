# Data-Engineer

### This program takes tabular Data from .txt file and saves it into .csv and creates SQL tables on bases of Country
### Data format
|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
|D|Alex|123457|20101012|20121013|MVD|Paul|SA|USA|06031987|A|
|D|John|123458|20101012|20121013|MVD|Paul|TN|IND|06031987|A|
|D|Mathew|123459|20101012|20121013|MVD|Paul|WAS|PHIL|06031987|A|
|D|Matt|12345|20101012|20121013|MVD|Paul|BOS|NYC|06031987|A|
|D|Jacob|1256|20101012|20121013|MVD|Paul|VIC|AU|06031987|A|

### To run
```python
python main.py
```
### Creates Staging table named customer with schema


| Field               | Type         | Null | Key | Default | Extra |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| Customer_Name       | varchar(255) | NO   |     | NULL    |       |
| Customer_ID         | varchar(18)  | NO   |     | NULL    |       |
| Customer_Open_Date  | date         | NO   |     | NULL    |       |
| Last_Consulted_DATE | date         | YES  |     | NULL    |       |
| Vaccination_Type    | char(5)      | YES  |     | NULL    |       |
| Doctor_Consulted    | char(255)    | YES  |     | NULL    |       |
| State               | char(5)      | YES  |     | NULL    |       |
| Country             | char(5)      | YES  |     | NULL    |       |
| Date_of_Birth       | date         | YES  |     | NULL    |       |
| Active_Customer     | char(1)      | YES  |     | NULL    |       |

### Data Example

| Customer_Name | Customer_ID | Customer_Open_Date | Last_Consulted_DATE | Vaccination_Type | Doctor_Consulted | State | Country | Date_of_Birth | Active_Customer |

| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| Alex          | 123457      | 2010-10-12         | 2012-10-13          | MVD              | Paul             | SA    | USA     | 1987-06-03    | A               |
| John          | 123458      | 2010-10-12         | 2012-10-13          | MVD              | Paul             | TN    | IND     | 1987-06-03    | A               |
| Mathew        | 123459      | 2010-10-12         | 2012-10-13          | MVD              | Paul             | WAS   | PHIL    | 1987-06-03    | A               |
| Mathew        | 123459      | 2010-10-12         | 2012-10-13          | MVD              |                  | WAS   | PHIL    | 1987-06-03    | A               |
| Matt          | 12345       | 2010-10-12         | 2012-10-13          | MVD              | Paul             | BOS   | NYC     | 1987-06-03    | A               |
| Jacob         | 1256        | 2010-10-12         | 2012-10-13          | MVD              | Paul             | VIC   | AU      | 1987-06-03    | A               |
| Jacob         | 1256        | 2010-10-12         | 2012-10-13          | MVD              | Paul             | VIC   | AU      | 1987-06-03    | A               |
| Jacob         | 1256        | 2010-10-12         | 2012-10-13          | MVD              | Paul             | VIC   | AU      | 1987-06-03    | A               |
| John1         | 123458      | 2010-10-12         | 2012-10-13          | MVD              | Paul             | TN    | IND     | 1987-06-03    | A               |
| John2         | 123458      | 2010-10-12         | 2012-10-13          | MVD              | Paul             | TN    | IND     | 1987-06-03    | A               |
