FROM python:3.10-slim

# Install OpenJDK JRE (required for Spark)
RUN apt-get update && \
    apt-get install -y default-jre && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark package
RUN pip install pyspark

WORKDIR /app

# Copy dataset and application script
COPY employees.csv .
COPY process_employees.py .

# Run the PySpark script
CMD ["python", "process_employees.py"]
