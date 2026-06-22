FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y default-jre && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pyspark

WORKDIR /app

COPY process_range.py .

CMD ["python", "process_range.py"]
