# Assignment 18

This is a PySpark application that generates a DataFrame of 5 million records and manipulates partitions.

It does the following:
1. Generates 5 million numbers using spark.range().
2. Prints the initial partition count.
3. Increases the partition count to 12 using repartition().
4. Reduces the partition count to 3 using coalesce().

## Files
* process_range.py - Python spark script
* Dockerfile - Docker container configuration

## How to build and run

1. Build image:
```bash
docker build -t assignment-18 .
```

2. Run container:
```bash
docker run --rm assignment-18
```
