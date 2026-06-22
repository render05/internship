import sys
from datetime import datetime

def main():
    # Print a welcome message
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
