# Assignment 4
# Python functions + basic file practice


def max_of_three(a, b, c):
    """Return the maximum of three numbers."""
    return max(a, b, c)


def distinct_elements(lst):
    """Return a new list with distinct elements from the first list (preserve order)."""
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def multiply_all(lst):
    """Multiply all numbers in a list. For an empty list, return 1."""
    product = 1
    for x in lst:
        product *= x
    return product


def factorial(n):
    """Calculate factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("factorial() is defined only for non-negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def in_range(number, low, high):
    """Check whether a number falls within a given inclusive range [low, high]."""
    return low <= number <= high


def even_numbers(lst):
    """Return a list containing only even numbers from the given list."""
    return [x for x in lst if x % 2 == 0]


def is_prime(n):
    """Return True if n is prime, otherwise False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def count_case_letters(s):
    """Count uppercase and lowercase letters in a string.

    Returns:
        (upper_count, lower_count)
    """
    upper_count = 0
    lower_count = 0

    for ch in s:
        if "A" <= ch <= "Z":
            upper_count += 1
        elif "a" <= ch <= "z":
            lower_count += 1

    return upper_count, lower_count


def write_practice_file():
    """Practise writing/appending data in a file."""
    path = "assignment4_data.txt"

    # Write mode (creates/overwrites)
    with open(path, "w", encoding="utf-8") as f:
        f.write("Assignment 4 - File Practice\n")
        f.write("Initial content written using 'w' mode.\n")

    # Append mode
    with open(path, "a", encoding="utf-8") as f:
        f.write("Appended content using 'a' mode.\n")

    return path


if __name__ == "__main__":
    # Quick self-test / demonstration (safe to remove if not needed)
    print("Max of (3, 7, 2):", max_of_three(3, 7, 2))
    print("Distinct from [1,2,2,3,1]:", distinct_elements([1, 2, 2, 3, 1]))
    print("Multiply all [2,3,4]:", multiply_all([2, 3, 4]))
    print("Factorial of 5:", factorial(5))
    print("Reverse 'hello':", reverse_string("hello"))
    print("Is 5 in range [1,10]?:", in_range(5, 1, 10))
    print("Even numbers from [1,2,3,4,5]:", even_numbers([1, 2, 3, 4, 5]))
    print("Is 29 prime?:", is_prime(29))
    u, l = count_case_letters("AbCdeF")
    print("Uppercase:", u, "Lowercase:", l)

    created_path = write_practice_file()
    print("Created/updated file:", created_path)

