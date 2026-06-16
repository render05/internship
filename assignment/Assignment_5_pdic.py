# 1) Repeat a tuple three times using the * operator
t = (1, 2, 3)
result = t * 3
print("1. Repeated Tuple:", result)

# 2) Join three separate tuples into one new tuple using the + operator
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)
new_tuple = t1 + t2 + t3
print("2. Combined Tuple:", new_tuple)

# 3) Check whether a specific element exists inside a tuple using the in keyword
t = (10, 20, 30, 40, 50)
element = 30
if element in t:
    print("3.", element, "exists in the tuple")
else:
    print("3.", element, "does not exist in the tuple")

# 4) Calculate total, highest value, and lowest value from a tuple
# without using sum(), max(), and min()
t = (12, 45, 7, 89, 23)

total = 0
highest = t[0]
lowest = t[0]

for num in t:
    total += num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("4. Total =", total)
print("   Highest =", highest)
print("   Lowest =", lowest)

# 5) Filter a tuple and keep only values greater than 10
n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for i in n:
    if i > 10:
        filtered += (i,)

print("5. Filtered Tuple:", filtered)

# 6) Determine how many elements are in a set without using len()
s = {"cat", "dog", "bird", "fish"}

count = 0
for item in s:
    count += 1

print("6. Number of elements =", count)

# 7) Combine two sets into one containing all unique elements
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

combined = s1.union(s2)

print("7. Combined Set:", combined)

# 8) Find all elements that are common to both sets
common = s1.intersection(s2)

print("8. Common Elements:", common)

# 9) Find all elements that are in either set but not in both
result = s1.symmetric_difference(s2)

print("9. Elements in either set but not both:", result)