# Assignment 17

This is a PySpark DataFrame application that analyzes a dataset of sales.

It reads the sales CSV file into a DataFrame, performs the following:
1. Sorts all products by sales in descending order and prints them.
2. Displays the top 3 highest-sales products.
3. Filters products with sales greater than 80,000 and saves the output to a CSV folder.

## Files
* sales.csv - sales dataset
* process_sales.py - python spark code using DataFrames
* Dockerfile - docker configuration
* high_sales_output/ - output folder with the filtered CSV

## How to build and run

1. Build image:
```bash
docker build -t assignment-17 .
```

2. Run container:
```bash
docker run --rm assignment-17
```
