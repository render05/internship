from pyspark import SparkContext

sc = SparkContext("local", "EmployeeApp")

raw_rdd = sc.textFile("employees.csv")
header = raw_rdd.first()
data_rdd = raw_rdd.filter(lambda line: line != header)

def parse_line(line):
    parts = line.split(",")
    return (parts[0], parts[1], parts[2], int(parts[3]))

employees_rdd = data_rdd.map(parse_line)
employees_rdd.cache()

# Sort and display
sorted_employees = employees_rdd.sortBy(lambda x: x[3], ascending=False).collect()
print("\n--- Sorted by Salary ---")
for emp in sorted_employees:
    print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}")
print("------------------------\n")

# Department totals
dept_salaries = employees_rdd.map(lambda x: (x[2], x[3]))
total_salary_by_dept = dept_salaries.reduceByKey(lambda a, b: a + b).collect()
print("--- Salary by Department ---")
for dept, total in total_salary_by_dept:
    print(f"{dept}: {total}")
print("----------------------------\n")

# Save top 3
top_three = employees_rdd.sortBy(lambda x: x[3], ascending=False).take(3)
with open("top_three_employees.txt", "w") as f:
    f.write("Top 3 Highest Paid Employees:\n")
    for emp in top_three:
        f.write(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}\n")

sc.stop()
