from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext("local", "Employee Processing App")

# Read the CSV file into an RDD
raw_rdd = sc.textFile("employees.csv")

# Filter out the header row
header = raw_rdd.first()
data_rdd = raw_rdd.filter(lambda line: line != header)

# Parse each line into a list of (id, name, department, salary)
# Converting salary to integer so sorting and addition works properly
def parse_line(line):
    parts = line.split(",")
    return (parts[0], parts[1], parts[2], int(parts[3]))

employees_rdd = data_rdd.map(parse_line)

# Keep the data in memory for multiple operations
employees_rdd.cache()

# 1. Sort employees by salary in descending order and display
sorted_employees = employees_rdd.sortBy(lambda x: x[3], ascending=False).collect()
print("\n--- All Employees Sorted by Salary (Descending) ---")
for emp in sorted_employees:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}")
print("--------------------------------------------------\n")

# 2. Calculate the total salary paid in each department
# Map to (department, salary) and sum them up
dept_salaries = employees_rdd.map(lambda x: (x[2], x[3]))
total_salary_by_dept = dept_salaries.reduceByKey(lambda a, b: a + b).collect()
print("--- Total Salary by Department ---")
for dept, total in total_salary_by_dept:
    print(f"Department: {dept}, Total Salary: {total}")
print("----------------------------------\n")

# 3. Get the top 3 highest-paid employees and save to a file
top_three_employees = employees_rdd.sortBy(lambda x: x[3], ascending=False).take(3)

# Write the top 3 to a text file
with open("top_three_employees.txt", "w") as f:
    f.write("Top 3 Highest Paid Employees:\n")
    for emp in top_three_employees:
        f.write(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}\n")

print("Saved the top 3 highest-paid employees to 'top_three_employees.txt'.\n")

# Stop the Spark context
sc.stop()
