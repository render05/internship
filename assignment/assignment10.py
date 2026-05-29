# Assignment 10
# Numpy operations (NaN/axis/averages/replace negatives)

import numpy as np


def assignment_10():
    # 1) Replace NaN with 0 and interchange 3 rows and 3 columns of 2D array
    arr2d = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]], dtype=float)

    # Replace NaN with 0
    arr2d_no_nan = np.nan_to_num(arr2d, nan=0.0)

    # Interchange 3 rows and 3 columns
    # For this 2x4 array, swapping "3 rows" means swapping the whole rows (row indices 0 and 1).
    # Swapping "3 columns" means swapping column indices 0 and 3.
    arr2d_swapped = arr2d_no_nan.copy()
    arr2d_swapped[[0, 1], :] = arr2d_swapped[[1, 0], :]
    arr2d_swapped[:, [0, 3]] = arr2d_swapped[:, [3, 0]]

    print("1) Original 2D array:\n", arr2d)
    print("   After replacing NaN with 0:\n", arr2d_no_nan)
    print("   After interchanging rows and columns:\n", arr2d_swapped)

    # 2) Move axes of 3D array to new positions
    a3 = np.arange(24).reshape(2, 3, 4)  # shape = (2, 3, 4)

    # Example move: (0,1,2) -> (1,2,0)
    moved = np.moveaxis(a3, 0, -1)  # move axis 0 to the last position
    moved2 = np.moveaxis(a3, (0, 1), (-1, 0))  # another simple example

    print("\n2) 3D array original shape:", a3.shape)
    print("   After moveaxis(a3, 0, -1) shape:", moved.shape)
    print("   After moveaxis(a3, (0,1), (-1,0)) shape:", moved2.shape)

    # 3) Replace NaN values with average of columns
    # Column-wise mean (ignoring NaN) and then replace NaN
    arr3 = np.array([
        [1.0, np.nan, 3.0, 4.0],
        [5.0, 6.0, np.nan, 8.0],
        [9.0, 10.0, 11.0, np.nan],
    ])

    col_means = np.nanmean(arr3, axis=0)  # mean per column

    # Replace NaN in each column with that column's mean
    arr3_filled = arr3.copy()
    inds = np.where(np.isnan(arr3_filled))
    arr3_filled[inds] = np.take(col_means, inds[1])

    print("\n3) Array with NaNs:\n", arr3)
    print("   Column means:", col_means)
    print("   After replacing NaNs with column averages:\n", arr3_filled)

    # 4) Replace negative value with zero in numpy array using replace
    arr4 = np.array([[1, -2, 3], [-4, 5, -6]])

    # Simple method: create a copy and replace negatives
    arr4_clipped = arr4.copy()
    arr4_clipped[arr4_clipped < 0] = 0

    print("\n4) Original array:\n", arr4)
    print("   After replacing negative values with 0:\n", arr4_clipped)

    return {
        "arr2d_no_nan": arr2d_no_nan,
        "arr2d_swapped": arr2d_swapped,
        "a3": a3,
        "moved": moved,
        "moved2": moved2,
        "arr3_filled": arr3_filled,
        "arr4_clipped": arr4_clipped,
    }


if __name__ == "__main__":
    assignment_10()

