# Assignment 16

This is a PySpark application using RDDs to process the employee dataset.

## Files
* employees.csv - dataset
* process_employees.py - python spark code
* Dockerfile - docker configuration
* top_three_employees.txt - output file

## How to build and run

1. Build image:
```bash
docker build -t assignment-16 .
```

2. Run container:
```bash
docker run --rm assignment-16
```
