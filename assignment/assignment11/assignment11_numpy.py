import numpy as np
from collections import Counter


def combine_1d_and_2d(arr1, arr2d):
    """Combine a 1D array with a 2D array (element-wise by broadcasting)."""
    # arr1 shape (n,) and arr2d shape (m,n) => result (m,n)
    return arr2d + arr1


def flatten_2d(arr2d):
    return arr2d.flatten()


def reverse_array(arr):
    return arr[::-1]


def max_min_rows_cols(arr2d):
    rows, cols = arr2d.shape
    max_val = arr2d.max()
    min_val = arr2d.min()
    return rows, cols, max_val, min_val


def select_elements(arr2d):
    """Select elements from a given array.

    - each element (return all)
    - specific element (row 0 col 1)
    - a few specific elements using indexing
    """
    each_element = arr2d.copy()
    specific_0_1 = arr2d[0, 1]
    specific_rows_cols = arr2d[[0, 1], [0, 1]]  # (0,0) and (1,1)
    return each_element, specific_0_1, specific_rows_cols


def sum_2d_using_for_loop(arr2d):
    total = 0
    for i in range(arr2d.shape[0]):
        for j in range(arr2d.shape[1]):
            total += arr2d[i, j]
    return total


def elementwise_ops(a, b):
    return {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b,
    }


def iterate_3d_for_and_nditer(a3):
    # for-loop iteration
    elems_for = []
    for i in range(a3.shape[0]):
        for j in range(a3.shape[1]):
            for k in range(a3.shape[2]):
                elems_for.append(a3[i, j, k])

    # nditer iteration
    elems_nditer = [x for x in np.nditer(a3)]

    return elems_for, elems_nditer


def mode_1d(x):
    """Compute mode of 1D array x.

    If multiple values tie for highest frequency, return all modes (sorted).
    """
    counts = Counter(map(lambda v: v.item() if hasattr(v, "item") else v, x))
    max_count = max(counts.values())
    modes = sorted([val for val, c in counts.items() if c == max_count])
    return modes


def mean_median_mode_2d(arr2d):
    flat = arr2d.flatten()
    mean_val = np.mean(flat)
    median_val = np.median(flat)
    modes = mode_1d(flat)
    return mean_val, median_val, modes


def main():
    # ------------------------------
    # 1) Combining 1D and 2D arrays
    # ------------------------------
    print("\n================ Assignment 11: NumPy Basics ================")

    arr1 = np.array([3, 4])            # shape (2,)
    arr2d = np.array([[1, 0], [2, 5]])  # shape (2,2)

    combined = combine_1d_and_2d(arr1, arr2d)
    print("\n1) Combine 1D + 2D (broadcast add)")
    print("arr1:\n", arr1)
    print("arr2d:\n", arr2d)
    print("combined (arr2d + arr1):\n", combined)

    # ------------------------------
    # 2) Flatten a 2D numpy array into 1D
    # ------------------------------
    print("\n2) Flatten 2D -> 1D")
    flat = flatten_2d(arr2d)
    print("Original 2D:\n", arr2d)
    print("Flattened 1D:\n", flat)

    # ------------------------------
    # 3) Reverse a numpy array
    # ------------------------------
    print("\n3) Reverse a numpy array")
    reversed_flat = reverse_array(flat)
    print("Original 1D:\n", flat)
    print("Reversed 1D:\n", reversed_flat)

    # ------------------------------
    # 4) Practice operations
    # ------------------------------
    print("\n4) Max/Min/Rows-cols + selection + sums + elementwise operations")

    rows, cols, max_val, min_val = max_min_rows_cols(arr2d)
    print("Array:\n", arr2d)
    print("Rows:", rows, "Cols:", cols)
    print("Max value:", max_val)
    print("Min value:", min_val)

    each_element, specific_0_1, specific_rows_cols = select_elements(arr2d)
    print("\nSelection: each element (copy) ->\n", each_element)
    print("Specific element arr2d[0,1]:", specific_0_1)
    print("Specific elements arr2d[[0,1],[0,1]] (diagonal):", specific_rows_cols)

    arr_for_sum = np.array([[1, 2, 3], [4, 5, 6]])
    sum_for = sum_2d_using_for_loop(arr_for_sum)
    print("\nSum of 2D using for loop")
    print("arr_for_sum:\n", arr_for_sum)
    print("Sum:", sum_for)

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    ops = elementwise_ops(a, b)
    print("\nElementwise add/sub/mul/div")
    print("a:\n", a)
    print("b:\n", b)
    for k, v in ops.items():
        print(f"{k}:\n{v}")

    # ------------------------------
    # 5) Iterate 3D array using for loop and nditer
    # ------------------------------
    print("\n5) Iterate 3D array using for-loop and nditer")
    a3 = np.arange(1, 9).reshape(2, 2, 2)  # shape (2,2,2)
    print("3D array a3:\n", a3)

    elems_for, elems_nditer = iterate_3d_for_and_nditer(a3)
    print("\nElements (for-loop order):", elems_for)
    print("Elements (nditer order):  ", elems_nditer)

    # ------------------------------
    # 6) Mean / Median / Mode for two NumPy 2D arrays
    #    (as requested: calculate mean median mode for two 2D arrays)
    # ------------------------------
    print("\n6) Mean / Median / Mode for two NumPy 2D arrays")

    # Example 2D arrays
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 5], [6, 7]])

    meanA, medianA, modesA = mean_median_mode_2d(A)
    meanB, medianB, modesB = mean_median_mode_2d(B)

    print("Array A:\n", A)
    print("A mean:", meanA)
    print("A median:", medianA)
    print("A mode(s):", modesA)

    print("\nArray B:\n", B)
    print("B mean:", meanB)
    print("B median:", medianB)
    print("B mode(s):", modesB)

    # also show the combination example requested in the task statement (arr1 + arr2)
    # using NumPy arrays (1D)
    print("\nExtra (from sample program): average of two 1D NumPy arrays")
    arr1_s = np.array([3, 4])
    arr2_s = np.array([1, 0])
    avg = (arr1_s + arr2_s) / 2
    print("arr1_s:\n", arr1_s)
    print("arr2_s:\n", arr2_s)
    print("Average of NumPy arrays:\n", avg)

    print("\n====================== Done ======================")


if __name__ == "__main__":
    main()

