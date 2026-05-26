import pandas as pd


def main():
    # -------------------- 1) Pandas Series --------------------
    print("\n==================== 1) PANDAS SERIES ====================")

    # Create a Pandas Series from Dictionary
    s_from_dict = pd.Series({"math": 95, "science": 88, "english": 91})
    print("\nSeries from dict:\n", s_from_dict)

    # Create a Pandas Series from Lists
    s_from_list = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
    print("\nSeries from list:\n", s_from_list)

    # Access the elements of a Series in Pandas
    print("\nAccess elements:")
    print("s_from_dict['math'] =", s_from_dict["math"])  # label
    print("s_from_list['b'] =", s_from_list["b"])  # label
    print("s_from_list.iloc[2] =", s_from_list.iloc[2])  # position

    # -------------------- 2) DataFrames --------------------
    print("\n==================== 2) DATAFRAMES ====================")

    # Make a Pandas DataFrame with a two-dimensional Python list
    data_2d = [["Alice", 23], ["Bob", 25], ["Charlie", 21]]
    df_from_2d = pd.DataFrame(data_2d, columns=["Name", "Age"])
    print("\nDataFrame from 2D list:\n", df_from_2d)

    # Create DataFrame from Python dict
    df_from_dict = pd.DataFrame({"Name": ["Alice", "Bob"], "Score": [85, 90]})
    print("\nDataFrame from dict:\n", df_from_dict)

    # Create Pandas dataframe using list of lists
    df_from_list_of_lists = pd.DataFrame(
        [["Math", 90], ["Science", 80], ["English", 88]],
        columns=["Subject", "Marks"],
    )
    print("\nDataFrame from list of lists:\n", df_from_list_of_lists)

    # Create a Pandas dataframe using list of tuples
    df_from_list_of_tuples = pd.DataFrame(
        [("Student1", 100), ("Student2", 95), ("Student3", 97)],
        columns=["Student", "Total"],
    )
    print("\nDataFrame from list of tuples:\n", df_from_list_of_tuples)

    # Create a Pandas DataFrame from List of Dicts
    list_of_dicts = [
        {"id": 1, "city": "Delhi", "temp": 35},
        {"id": 2, "city": "Mumbai", "temp": 30},
        {"id": 3, "city": "Chennai", "temp": 32},
    ]
    df_from_list_of_dicts = pd.DataFrame(list_of_dicts)
    print("\nDataFrame from list of dicts:\n", df_from_list_of_dicts)

    # -------------------- 3) Data iteration & selection --------------------
    print("\n==================== 3) DATA ITERATION & SELECTION ====================")

    df = pd.DataFrame(
        [
            [1, "Delhi", 35, 72000],
            [2, "Mumbai", 30, 65000],
            [3, "Chennai", 32, 68000],
            [4, "Bengaluru", 28, 61000],
            [5, "Kolkata", 33, 70000],
        ],
        columns=["id", "city", "temp", "population"],
    )
    df.index = ["r1", "r2", "r3", "r4", "r5"]
    print("\nBase DataFrame df:\n", df)

    # Different ways to iterate over rows in Pandas dataframe
    print("\n--- Iteration methods ---")

    print("\n1) iterrows():")
    for idx, row in df.iterrows():
        if idx in ["r1", "r3"]:
            print(f"{idx}: city={row['city']}, temp={row['temp']}")

    print("\n2) itertuples():")
    for row in df.itertuples(index=True):
        if row.Index in ["r2", "r4"]:
            print(f"{row.Index}: id={row.id}, temp={row.temp}")

    print("\n3) for loop using index + loc (label-based):")
    for i in df.index[:2]:
        print(f"{i}: {df.loc[i, ['city', 'temp']].to_dict()}")

    # Selecting rows in pandas DataFrame based on conditions
    print("\n--- Conditional selection ---")
    selected = df[df["temp"] >= 32]
    print("Cities with temp >= 32:\n", selected)

    # Select any row from a dataframe using iloc[]
    print("\nRow selection using iloc[] (iloc[2]):")
    print(df.iloc[2])

    # Limited rows selection with given column
    print("\nLimited rows selection (first 3 rows, only 'city' column):")
    limited = df.loc[df.index[:3], ["city"]]
    print(limited)

    # Drop rows from the dataframe based on certain condition applied on a column
    print("\n--- Drop rows based on condition ---")
    dropped = df.drop(df[df["temp"] < 32].index)  # keep only temp >= 32
    print("Rows dropped where temp < 32 (result):\n", dropped)

    # Insert row at given position in Pandas Dataframe
    print("\n--- Insert row at given position ---")
    df_insert_test = df.copy()
    new_row = pd.DataFrame(
        [[6, "Jaipur", 36, 60000]],
        columns=["id", "city", "temp", "population"],
        index=["r_new"],
    )

    insert_pos = 2  # insert after first 2 rows (by iloc position)
    top = df_insert_test.iloc[:insert_pos]
    bottom = df_insert_test.iloc[insert_pos:]
    df_inserted = pd.concat([top, new_row, bottom])
    print("After inserting at position", insert_pos, ":\n", df_inserted)

    # Create a list from rows in Pandas dataframe
    print("\n--- Create list from rows ---")
    list_of_rows_as_lists = [list(x) for x in df.itertuples(index=False, name=None)]
    print("List of rows (each row as list):\n", list_of_rows_as_lists)

    list_of_records = df.to_dict(orient="records")
    print("\nList of records (each row as dict):\n", list_of_records)


if __name__ == "__main__":
    main()

