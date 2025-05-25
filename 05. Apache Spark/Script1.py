from pyspark import SparkContext

sc = SparkContext("local", "PrintSquaredRDD")

rdd = sc.parallelize([1, 2, 3, 4])

squaredRDD = rdd.map(lambda x: x * x)

result = squaredRDD.collect()

print("Squared RDD:", result)

sc.stop()