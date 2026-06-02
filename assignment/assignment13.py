import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def replace_nan_and_swap_2d():
    # Given 2D array
    arr2d = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]], dtype=float)

    # 1) Replace NaN with 0
    arr2d_no_nan = np.nan_to_num(arr2d, nan=0.0)

    # 1) Interchange 3 rows and 3 columns
    # For this input we only have 2 rows and 4 columns.
    # So we swap the available rows (0 <-> 1) and swap columns 0 <-> 3.
    # (Swapping these keeps it meaningful for the given shape.)
    arr2d_swapped = arr2d_no_nan.copy()
    arr2d_swapped[[0, 1], :] = arr2d_swapped[[1, 0], :]
    arr2d_swapped[:, [0, 3]] = arr2d_swapped[:, [3, 0]]

    return arr2d, arr2d_no_nan, arr2d_swapped


def move_axes_3d():
    # 2) Move axes of a 3D array
    a3 = np.arange(24).reshape(2, 3, 4)  # shape (2,3,4)

    # Example: move axis 0 -> -1 (end)
    moved1 = np.moveaxis(a3, 0, -1)

    # Example: move axis tuple (0,1) -> (-1,0)
    moved2 = np.moveaxis(a3, (0, 1), (-1, 0))

    return a3, moved1, moved2


def replace_nan_with_column_average():
    # 3) Replace NaN values with average of columns
    arr3 = np.array(
        [
            [1.0, np.nan, 3.0, 4.0],
            [5.0, 6.0, np.nan, 8.0],
            [9.0, 10.0, 11.0, np.nan],
        ]
    )

    col_means = np.nanmean(arr3, axis=0)  # mean per column (ignores NaN)

    arr3_filled = arr3.copy()
    nan_positions = np.isnan(arr3_filled)
    # Replace each NaN with the mean of its column
    col_indices = np.where(nan_positions)[1]
    arr3_filled[nan_positions] = np.take(col_means, col_indices)

    return arr3, col_means, arr3_filled


def replace_negative_with_zero():
    # 4) Replace negative value with zero in numpy array
    arr4 = np.array([[1, -2, 3], [-4, 5, -6]])
    arr4_replaced = arr4.copy()
    arr4_replaced[arr4_replaced < 0] = 0
    return arr4, arr4_replaced


def mode_1d(x: np.ndarray):
    counts = Counter(x.tolist())
    max_count = max(counts.values())
    modes = sorted([val for val, c in counts.items() if c == max_count])
    return modes


def mean_median_mode_2d(arr2d: np.ndarray):
    flat = arr2d.flatten()
    mean_val = float(np.mean(flat))
    median_val = float(np.median(flat))
    modes = mode_1d(flat)
    return mean_val, median_val, modes


def solve_linear_system():
    # 6) Solve system using linalg() and inverse method
    # x - 2y + 3z = 9
    # -x + 3y - z = -6
    # 2x - 5y + 5z = 17
    A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]], dtype=float)
    b = np.array([9, -6, 17], dtype=float)

    sol_linalg = np.linalg.solve(A, b)

    A_inv = np.linalg.inv(A)
    sol_inverse = A_inv @ b

    return A, b, sol_linalg, sol_inverse


def plot_semester_comparison():
    # 7) Plot to compare at least 2 semester results
    semesters = np.array([1, 2, 3, 4])
    semA = np.array([62, 68, 71, 75])
    semB = np.array([58, 64, 69, 73])

    plt.figure(figsize=(8, 5))
    plt.plot(semesters, semA, marker='o', label='Semester Result A')
    plt.plot(semesters, semB, marker='s', label='Semester Result B')
    plt.title('Comparison of Semester Results')
    plt.xlabel('Semester')
    plt.ylabel('Marks')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()


def assignment_13():
    print("\n==================== Assignment 13 (Student Version) ====================")

    # 1
    arr2d, arr2d_no_nan, arr2d_swapped = replace_nan_and_swap_2d()
    print("\n1) Replace NaN with 0 and swap rows/columns")
    print("Original 2D array:\n", arr2d)
    print("After NaN -> 0:\n", arr2d_no_nan)
    print("After swapping:\n", arr2d_swapped)

    # 2
    a3, moved1, moved2 = move_axes_3d()
    print("\n2) Move axes in 3D array")
    print("Original shape:", a3.shape)
    print("After moveaxis(a3,0,-1) shape:", moved1.shape)
    print("After moveaxis(a3,(0,1),(-1,0)) shape:", moved2.shape)

    # 3
    arr3, col_means, arr3_filled = replace_nan_with_column_average()
    print("\n3) Replace NaN with column average")
    print("Input array with NaN:\n", arr3)
    print("Column means:\n", col_means)
    print("Filled array:\n", arr3_filled)

    # 4
    arr4, arr4_replaced = replace_negative_with_zero()
    print("\n4) Replace negative values with zero")
    print("Original:\n", arr4)
    print("After replace:\n", arr4_replaced)

    # 5
    A2 = np.array([[1, 2], [3, 4]])
    B2 = np.array([[5, 5], [6, 7]])
    meanA, medianA, modesA = mean_median_mode_2d(A2)
    meanB, medianB, modesB = mean_median_mode_2d(B2)

    print("\n5) Mean, Median, Mode for two 2D arrays")
    print("Array A:\n", A2)
    print("Mean:", meanA, "Median:", medianA, "Mode(s):", modesA)
    print("Array B:\n", B2)
    print("Mean:", meanB, "Median:", medianB, "Mode(s):", modesB)

    # 6
    A_lin, b_lin, sol_linalg, sol_inverse = solve_linear_system()
    print("\n6) Solve linear system using linalg and inverse")
    print("A matrix:\n", A_lin)
    print("b vector:", b_lin)
    print("Solution (np.linalg.solve): [x, y, z] =", sol_linalg)
    print("Solution (inverse method): [x, y, z] =", sol_inverse)

    # 7
    print("\n7) Plot semester comparison (Matplotlib window will open)")
    plot_semester_comparison()
    plt.show()

    print("\n==================== Completed ====================")


if __name__ == '__main__':
    assignment_13()

