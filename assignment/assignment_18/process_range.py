from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PartitionApp").getOrCreate()

# Generate 5 million records
df = spark.range(0, 5000000)

# Initial partitions
initial_parts = df.rdd.getNumPartitions()
print(f"\nInitial number of partitions: {initial_parts}")

# Increase to 12 using repartition
df_repartitioned = df.repartition(12)
repartition_parts = df_repartitioned.rdd.getNumPartitions()
print(f"Partitions after repartition(12): {repartition_parts}")

# Decrease to 3 using coalesce
df_coalesced = df_repartitioned.coalesce(3)
coalesce_parts = df_coalesced.rdd.getNumPartitions()
print(f"Partitions after coalesce(3): {coalesce_parts}\n")

spark.stop()
