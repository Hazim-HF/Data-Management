from pyhive import hive
import pandas as pd
import os
os.getcwd()

conn = hive.Connection(
    host="localhost",
    port=10000,
    username="maria_dev",
)

cursor = conn.cursor()


cursor.execute("SHOW TABLES")
for result in cursor.fetchall():
    print(result)

cursor.execute("""
CREATE TABLE project.adult (
    Age INT,
    Workclass STRING, 
    Final_Weight INT, 
    Education STRING, 
    Edu_Num INT,
    Marital_Status STRING, 
    Occupation STRING, 
    Relationship STRING, 
    Race STRING,
    Sex STRING,
    Capital_Gain INT,
    Capital_Loss INT, 
    Hours_Per_Week INT,
    Native_Country STRING,
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/maria_dev/
""")

query = """
SELECT * FROM project.adult
"""

df = pd.read_sql(query, conn)
print(df.head())

# python code

adult = pd.read_csv('project/adult.csv', header=None)
adult.columns = ['age', 'workclass', 'final_weight', 'education', 'education_num', 'marital_status',
                 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                 'hours_per_week', 'native_country', 'income']
adult['age'].value_counts()

cursor.execute("""
CREATE TABLE IF NOT EXISTS project.my_table (
               number INT,
               name STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
               """)

cursor.execute("""
               LOAD DATA INPATH '/home/maria_dev/test.csv' INTO TABLE project.my_table
               """)

name = pd.read_csv('project/data/imdb/name.basics.tsv/name.basics.tsv', sep='\t')
name.head()

# check missing value
name.isna().sum().sum() # 9 missing values.

# check duplicated value
name.duplicated().sum() # no duplicated values