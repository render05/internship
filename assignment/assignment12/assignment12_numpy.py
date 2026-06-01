#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assignment 12 - NumPy operations

Run:
  python assignment/assignment12/assignment12_numpy.py
"""

import numpy as np


def print_array_attributes(arr: np.ndarray, name: str = "arr") -> None:
    print(f"\nArray Attributes for {name}:")
    print("Shape:", arr.shape)
    print("Dimensions (ndim):", arr.ndim)
    print("Data type (dtype):", arr.dtype)
    print("Item size (itemsize):", arr.itemsize, "bytes")


def main():
    print("\n==================== Assignment 12: NumPy ====================")

    # 1) Create numpy array and convert 1D array to 2D
    arr1d = np.array([1, 2, 3, 4, 5, 6])
    print("\n1) Original 1D array:", arr1d)
    arr2d = arr1d.reshape(2, 3)
    print("Converted to 2D (2x3):\n", arr2d)

    # 2) Print Array Attributes (shape, dimensions, data type, itemsize)
    print_array_attributes(arr2d, "arr2d")

    # 3) Create a 3×3 NumPy array of all 9
    a_3x3 = np.full((3, 3), 9)
    print("\n3) 3x3 array filled with 9:\n", a_3x3)

    # 4) Create a 1D array of 10 evenly spaced values between 25 and 125
    evenly_spaced_10 = np.linspace(25, 125, 10)
    print("\n4) 10 evenly spaced values between 25 and 125:\n", evenly_spaced_10)

    # 5) Convert a Python list into a NumPy array
    py_list = [10, 20, 30, 40]
    np_from_list = np.array(py_list)
    print("\n5) Python list:", py_list)
    print("Converted to NumPy array:\n", np_from_list)

    # 6) Reverse a 1D NumPy array
    reversed_arr1d = evenly_spaced_10[::-1]
    print("\n6) Reverse of evenly spaced array:\n", reversed_arr1d)

    # 7) Create a 4×4×3 array and extract value at its second set, first row and last column
    # Interpret "second set" as index 1 along the first axis.
    a_4x4x3 = np.arange(4 * 4 * 3).reshape(4, 4, 3)
    value = a_4x4x3[1, 0, -1]  # second set (1), first row (0), last column (-1)
    print("\n7) a_4x4x3 shape:", a_4x4x3.shape)
    print("Extracted value at [1, 0, -1]:", value)

    # 8) Create a 4×4 and Extract Odd Rows and Even Columns
    a_4x4 = np.arange(16).reshape(4, 4)
    odd_rows = a_4x4[1::2, :]      # rows 1,3
    odd_rows_even_columns = odd_rows[:, 0::2]  # even columns (0,2)
    print("\n8) 4x4 array:\n", a_4x4)
    print("Odd rows and even columns (rows 1,3; cols 0,2):\n", odd_rows_even_columns)

    # 9) Slice the first two rows and first two columns of second set from a 4×4×3 array
    second_set_slice = a_4x4x3[1, :2, :2]
    print("\n9) From 4x4x3, slice second set index=1, first two rows/cols [:2,:2]:\n", second_set_slice)

    # 10) Replace all odd numbers in a NumPy array with -1 by iterating using for loop
    arr_replace = np.array([
        [23, 56, 78, 93],
        [71, 82, 13, 24],
    ])
    print("\n10) Original array for odd->-1 replacement:\n", arr_replace)

    arr_replaced = arr_replace.copy()
    for i in range(arr_replaced.shape[0]):
        for j in range(arr_replaced.shape[1]):
            if arr_replaced[i, j] % 2 != 0:
                arr_replaced[i, j] = -1

    print("Array after replacing odd numbers with -1:\n", arr_replaced)

    # 11) Get the indices of non-zero elements in an array
    non_zero_arr = np.array([1, 0, 2, 0, 3, 0, 4])
    indices_non_zero = np.nonzero(non_zero_arr)
    print("\n11) Array:", non_zero_arr)
    print("Indices of non-zero elements:", indices_non_zero)

    # 12) Perform arithmetic operations on two NumPy arrays element-wise
    arrA = np.array([1, 2, 3])
    arrB = np.array([4, 5, 6])
    print("\n12) arrA:", arrA)
    print("    arrB:", arrB)
    print("Element-wise Add:", arrA + arrB)
    print("Element-wise Multiply:", arrA * arrB)

    # 13) Compute dot product of two NumPy arrays
    arr1 = np.array([15, 20, 25])
    arr2 = np.array([10, 40, 37])
    dot = np.dot(arr1, arr2)
    print("\n13) Dot product")
    print("arr1:", arr1)
    print("arr2:", arr2)
    print("dot(arr1, arr2) =", dot)

    print("\n======================== Done ========================")


if __name__ == "__main__":
    main()

