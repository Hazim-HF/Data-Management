# Data-Management

1. Pull docker image <br>
  docker pull hortonworks/sandbox-hdp:2.6.5

2. Run HDP Sandbox container <br>
  docker run -d --name hdp-sandbox <br>
  --hostname sandbox-hdp.hortonworks.com <br>
  --privileged <br>
  -p 8080:8080 -p 2222:22 <br>
  -p 80:80 -p 2181:2181 -p 8042:8042 -p 7077:7077 -p 8888:8888 <br>
  -p 50070:50070 -p 9000:9000 -p 10000:10000 <br>
  -p 9995:9995 -p 8020:8020 <br>
  hortonworks/sandbox-hdp:2.6.5

3. View log <br>
   docker logs -f hdp-sandbox <br>
   output : Ambari Server 'STARTED'

4. Use SSH into the Container <br>
   ssh root@localhost -p 2222

5. If port in use, change port using <br>
  e.g., -p 15070:50070 `http://localhost:15070`

6. Remove a container <br>
  docker rm hdp-sandbox

7. Remane container <br>
  docker run --name sandbox-hdp2

8. To start a sandbox later <br>
   docker start hdp-sandbox

1080 - Ambari UI <br>
4040 - Spark UI <br>
8080 - Hive <br>
8888 - Jupyter Notebook <br>
9995 - Zeppelin <br>
16010 - HBase <br>
50070 - HDFS <br>
8088 - YARN (Yet Another Resource Negotiator) <br>

https://github.com/kontext-tech/winutils/blob/master/hadoop-3.4.0-win10-x64/bin/winutils.exe
