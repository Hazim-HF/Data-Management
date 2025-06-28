from pyhive import hive

# establish a connection to Hive
conn = hive.Connection(
    host='localhost',
    port=10000,
    username='maria_dev'
)

cursor = conn.cursor()

def hive_query(query):
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)

cursor.execute("""
               CREATE DATABASE IF NOT EXISTS project2
               """)

for year in range(1987, 2009):
    location = f"/user/maria_dev/project2/{year}"
    table_name = f"project2.airline_{year}"
# Create external table pointing to the CSV
    cursor.execute(f"""
    CREATE EXTERNAL TABLE IF NOT EXISTS {table_name} (
        Year INT,
        Month INT,
        DayofMonth INT,
        DayOfWeek INT,
        DepTime INT,
        CRSDepTime INT,
        ArrTime INT,
        CRSArrTime INT,
        UniqueCarrier STRING,
        FlightNum INT,
        TailNum STRING,
        ActualElapsedTime INT,
        CRSElapsedTime INT,
        AirTime INT,
        ArrDelay INT,
        DepDelay INT,
        Origin STRING,
        Dest STRING,
        Distance INT,
        TaxiIn INT,
        TaxiOut INT,
        Cancelled INT,
        CancellationCode STRING,
        Diverted INT,
        CarrierDelay INT,
        WeatherDelay INT,
        NASDelay INT,
        SecurityDelay INT,
        LateAircraftDelay INT
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    LOCATION '{location}'
    TBLPROPERTIES ("skip.header.line.count"="1")
    """)


cursor.execute("SHOW TABLES IN project2")
tables = cursor.fetchall()

for (table, ) in tables:
    cursor.execute(f"DROP TABLE IF EXISTS project2.{table}")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS project2.airports (
                iata STRING,
                airport STRING,
                city STRING,
                state STRING,
                country STRING,
                lat FLOAT,
                long FLOAT
               )
                ROW FORMAT DELIMITED
                FIELDS TERMINATED BY ','
                STORED AS TEXTFILE
                LOCATION '/user/maria_dev/project2/airports'
                TBLPROPERTIES ("skip.header.line.count"="1")
                """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS project2.carriers (
                Code STRING,
                Description STRING
               )
                ROW FORMAT DELIMITED
                FIELDS TERMINATED BY ','
                STORED AS TEXTFILE
                LOCATION '/user/maria_dev/project2/carriers'
                TBLPROPERTIES ("skip.header.line.count"="1")
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS project2.plane_data (
                tailnum STRING,
                type STRING,
                manufacturer STRING,
                issue_date STRING,
                model STRING,
                status STRING,
                serial_number STRING,
                engine_type STRING,
                year INT
               )
                ROW FORMAT DELIMITED
                FIELDS TERMINATED BY ','
                STORED AS TEXTFILE
                LOCATION '/user/maria_dev/project2/plane_data'
                TBLPROPERTIES ("skip.header.line.count"="1")
""")

cursor.execute("DROP TABLE project2.plane_data")

hive_query("SELECT tailnum FROM project2.plane_data")

# delay patterns
# what times of day have the lowest average delays.

query = """
SHOW TABLES IN"""
