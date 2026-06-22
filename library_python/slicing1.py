# import pandas as pd 
# # data ={
# #     "marks":[12,32,43]


# df = pd.DataFrame([['a','b'],['c','d']],columns = ['col1','col2'])
# print(df)
# import pandas as pd 
# # data ={
# #     "marks":[12,32,43]


# df = pd.DataFrame(
#     [['a','b',5,6],['c','d',4,3],['s','f',5,4]
#      ],
#        columns = ['col1','col2','col3','col4']
# )
# df.index =['r1','r2','r3']# label to loc ,int to iloc
# print(df)
# res =df.loc['r1':'r2','col1':'col3']
# print(res)

#Acessing
# import pandas as pd 

# df = pd.DataFrame(
#     [['a','b',5,6],['c','d',4,3],['s','f',5,4]
#      ],
#        columns = ['col1','col2','col3','col4']
# )
# df.index =['r1','r2','r3']# label to loc ,int to iloc
# print(df)
# df.iloc[1,2:4]=[5,6]
# print(df)
# import pandas as pd 

# df = pd.DataFrame(
#     [['a','b',5,6],['c','d',4,3],['s','f',5,4]
#      ],
#        columns = ['col1','col2','col3','col4']
# )
# df.index =['r1','r2','r3']# label to loc ,int to iloc
# print(df)
# res =df.drop(['r1','r2'])
# print(res)
# import pandas as pd 

# df = pd.DataFrame(
#     [['a','b',5,6],['c','d',4,3],['s','f',5,0]
#      ],
#        columns = ['col1','col2','col3','col4']
# )
# df.index =['r1','r2','r3']# label to loc ,int to iloc

# res =df[df['col4']!=0]
# print(res)
import pandas as pd


def main():
    # -------------------- 1) Pandas Series --------------------
    print("\n==================== 1) PANDAS SERIES ====================")

    # Create a Pandas Series from Dictionary
    d = {"math": 95, "science": 88, "english": 91}
    s_dict = pd.Series(d)
    print("\nSeries from dict:\n", s_dict)

    # Create a Pandas Series from Lists
    lst = [10, 20, 30, 40]
    s_list = pd.Series(lst, index=["a", "b", "c", "d"])
    print("\nSeries from list:\n", s_list)

    # Access the elements of a Series in Pandas
    print("\nAccess elements:")
    print("s_dict['math'] =", s_dict["math"])  # label-based
    print("s_list['b'] =", s_list["b"])  # label-based
    print("s_list.iloc[2] =", s_list.iloc[2])  # position-based

    # -------------------- 2) DataFrames --------------------
    print("\n==================== 2) DATAFRAMES ====================")

    # Make a Pandas DataFrame with a two-dimensional Python list
    data_2d = [["Alice", 23], ["Bob", 25], ["Charlie", 21]]
    df_from_2d = pd.DataFrame(data_2d, columns=["Name", "Age"])
    print("\nDataFrame from 2D list:\n", df_from_2d)

    # Create DataFrame from Python dict
    data_dict = {"Name": ["Alice", "Bob"], "Score": [85, 90]}
    df_from_dict = pd.DataFrame(data_dict)
    print("\nDataFrame from dict:\n", df_from_dict)

    # Create Pandas dataframe using list of lists
    data_ll = [["Math", 90], ["Science", 80], ["English", 88]]
    df_ll = pd.DataFrame(data_ll, columns=["Subject", "Marks"])
    print("\nDataFrame from list of lists:\n", df_ll)

    # Create a Pandas dataframe using list of tuples
    data_tuples = [("Student1", 100), ("Student2", 95), ("Student3", 97)]
    df_tuples = pd.DataFrame(data_tuples, columns=["Student", "Total"])
    print("\nDataFrame from list of tuples:\n", df_tuples)

    # Create a Pandas DataFrame from List of Dicts
    lod = [
        {"id": 1, "city": "Delhi", "temp": 35},
        {"id": 2, "city": "Mumbai", "temp": 30},
        {"id": 3, "city": "Chennai", "temp": 32},
    ]
    df_lod = pd.DataFrame(lod)
    print("\nDataFrame from list of dicts:\n", df_lod)

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

    print("\n3) for loop over index + loc (label-based):")
    for i in df.index[:2]:
        print(f"{i}: {df.loc[i, ['city', 'temp']].to_dict()}")

    # Selecting rows in pandas DataFrame based on conditions
    print("\n--- Conditional selection ---")
    hot_cities = df[df["temp"] >= 32]
    print("Cities with temp >= 32:\n", hot_cities)

    # Select any row from a dataframe using iloc[]
    print("\nRow selection using iloc[]:")
    print("df.iloc[2] =\n", df.iloc[2])

    # Limited rows selection with given column
    print("\nLimited rows selection (first 3 rows with only given column 'city'):")
    limited = df.loc[df.index[:3], ["city"]]
    print(limited)

    print("\nAnother limited selection (rows 1..3 with columns ['city','temp']):")
    limited2 = df.iloc[1:4][["city", "temp"]]
    print(limited2)

    # Drop rows from the dataframe based on certain condition applied on a column
    print("\n--- Drop rows based on condition ---")
    dropped = df.drop(df[df["temp"] < 32].index)  # keep only temp >= 32
    print("Dropped rows where temp < 32 (result):\n", dropped)

    # Insert row at given position in Pandas Dataframe
    print("\n--- Insert row at position ---")
    df2 = df.copy()
    new_row = pd.DataFrame(
        [[6, "Jaipur", 36, 60000]],
        columns=["id", "city", "temp", "population"],
        index=["r_new"],
    )

    insert_pos = 2  # after first 2 rows (iloc position)
    upper = df2.iloc[:insert_pos]
    lower = df2.iloc[insert_pos:]
    df_inserted = pd.concat([upper, new_row, lower])
    print("After inserting new row at position", insert_pos, ":\n", df_inserted)

    # Create a list from rows in Pandas dataframe
    print("\n--- Create list from rows ---")
    # list of rows as lists
    list_of_rows = [list(x) for x in df.itertuples(index=False, name=None)]
    print("List of rows (each row as list):\n", list_of_rows)

    # list of dicts (records)
    list_of_records = df.to_dict(orient="records")
    print("\nList of records (each row as dict):\n", list_of_records)


if __name__ == "__main__":
    main()

