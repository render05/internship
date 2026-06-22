# Assignment 16 - PySpark RDD Application

This is a PySpark application using RDDs to process a dataset of employees. 

It reads an employee CSV file, performs three operations:
1. Sorts all employees by salary in descending order and prints them.
2. Calculates and prints the total salary paid in each department.
3. Saves the top three highest-paid employees to a text file.

## Project Files
* employees.csv - Employee data
* process_employees.py - PySpark code using RDDs
* Dockerfile - Docker config to install Java, PySpark, and run the app
* top_three_employees.txt - Output file of top 3 employees

## How to Build and Run the Docker Container

1. Open your terminal in this folder.
2. Build the docker image:
```bash
docker build -t assignment-16 .
```

3. Run the container:
```bash
docker run --rm assignment-16
```
