# Data-Management

run <span style="color:blue">docker pull hortonworks/sandbox-hdp:2.6.5</span>

docker pull hortonworks/sandbox-hdp:2.6.5

docker run -d --name hdp-sandbox -p 1080:1080 -p 4040:4040 -p 8080:8080 -p 8888:8888 -p 9995:9995 -p 16010:16010 -p 50070:50070 -p 8088:8088 hortonworks/sandbox-hdp:2.6.5

1080 - Ambari UI
4040 - Spark UI
8080 - Hive
8888 - Jupyter Notebook
9995 - Zeppelin
16010 - HBase
50070 - HDFS
8088 - YARN (Yet Another Resource Negotiator)
