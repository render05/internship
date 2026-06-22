# Assignment 15: Dockerized Python Version & Time Checker

A simple, Dockerized Python application that displays the current Python version running inside the container along with the current system date and time.

---

## Table of Contents
- [Assignment Overview](#assignment-overview)
- [Project Structure](#project-structure)
- [How to Build and Run](#how-to-build-and-run)
  - [Prerequisites](#prerequisites)
  - [1. Build the Docker Image](#1-build-the-docker-image)
  - [2. Run the Docker Container](#2-run-the-docker-container)
- [File Explanations](#file-explanations)
  - [main.py](#mainpy)
  - [Dockerfile](#dockerfile)
- [Sample Output](#sample-output)

---

## Assignment Overview
The goal of this assignment is to:
1. Create a Python script (`main.py`) that prints the current Python version and current date/time.
2. Package the application in a Docker container using a `python:3.12-slim` base image.
3. Configure the container to automatically execute the script on startup.
4. Document the process with instructions and a sample output screenshot.

---

## Project Structure
```text
assignment_15/
├── Dockerfile          # Contains Docker instructions to package the app
├── main.py             # Python script that prints version and date/time
├── requirements.txt    # List of dependencies (none needed, included for completeness)
├── screenshot.png      # Screenshot of the running application
└── README.md           # This documentation file
```

---

## How to Build and Run

### Prerequisites
Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your system.

### 1. Build the Docker Image
Open your terminal (PowerShell, Command Prompt, or terminal of your choice), navigate to the `assignment_15` folder, and run the following command to build the Docker image:

```bash
docker build -t assignment-15 .
```

*Note: The `-t assignment-15` tag names our image `assignment-15`, and the `.` at the end tells Docker to look for the `Dockerfile` in the current directory.*

### 2. Run the Docker Container
Once the image is built successfully, run the container using the command below:

```bash
docker run --rm assignment-15
```

*Note: The `--rm` flag automatically cleans up and removes the container after it exits, keeping your system tidy.*

---

## File Explanations

### `main.py`
This is a simple Python script using standard built-in libraries (`sys` and `datetime`) so no external pip installations are necessary.
```python
import sys
from datetime import datetime

def main():
    print("=========================================")
    print("      Docker Python Version Checker      ")
    print("=========================================")
    
    # Get and print the current Python version
    python_version = sys.version
    print(f"Current Python Version: {python_version}")
    
    # Get and print the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time:  {current_time}")
    print("=========================================")

if __name__ == "__main__":
    main()
```

### `Dockerfile`
The Dockerfile configures the container step-by-step:
```dockerfile
# Use the official python:3.12-slim image as the base image
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the Python script into the container's working directory
COPY main.py .

# Run the Python script when the container starts
CMD ["python", "main.py"]
```

---

## Sample Output

When the container runs, it will output something similar to the following in your terminal:

```text
=========================================
      Docker Python Version Checker      
=========================================
Current Python Version: 3.12.3 (main, Apr  9 2024, 08:25:12) [GCC 12.2.0]
Current Date and Time:  2026-06-22 21:05:30
=========================================
```

### Execution Screenshot
Below is a screenshot of the container execution:

![Sample Output Screenshot](screenshot.png)
