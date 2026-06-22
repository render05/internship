from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

# 1. Sort products by sales descending and show
sorted_df = df.orderBy(col("sales").desc())
print("\n--- Sorted Products ---")
sorted_df.show()

# 2. Top 3 highest sales
print("--- Top 3 Products ---")
sorted_df.show(3)

# 3. Filter products with sales > 80,000 and save
filtered_df = df.filter(col("sales") > 80000)
filtered_df.write.mode("overwrite").csv("high_sales_output", header=True)

spark.stop()
