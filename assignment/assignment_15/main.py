import sys
from datetime import datetime

print("Python version running inside container:")
print(sys.version)

print("\nCurrent date and time:")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
