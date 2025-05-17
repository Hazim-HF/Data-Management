from pyhive import hive
import pandas as pd

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