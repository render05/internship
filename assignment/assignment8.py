import pandas as pd


def main():
    print("\n==================== Assignment 8 (Pandas) ====================")

    # ============================================================
    # 1) Convert a series of date-strings to a timeseries
    # ============================================================
    print("\n1) Convert date-strings to a timeseries")

    date_strings = [
        "2024-01-01",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05",
    ]
    values = [10, 12, 9, 14, 13]

    s = pd.Series(values, index=pd.to_datetime(date_strings))
    s.name = "value"

    print("Date index (parsed):")
    print(s.index)
    print("Timeseries (Series):")
    print(s)

    # Also as a DataFrame
    ts_df = s.to_frame()
    print("Timeseries (DataFrame):")
    print(ts_df)

    # ============================================================
    # 2) Inner merge / Left join / Right join / Index join
    # ============================================================
    print("\n2) Merges and joins (df1, df2 using common column 'ID')")

    df1 = pd.DataFrame(
        {
            "ID": [1, 2, 3, 4],
            "name": ["Alice", "Bob", "Charlie", "Diana"],
            "score1": [85, 90, 78, 88],
        }
    )

    df2 = pd.DataFrame(
        {
            "ID": [3, 4, 5],
            "city": ["Delhi", "Mumbai", "Chennai"],
            "score2": [80, 92, 75],
        }
    )

    print("df1:")
    print(df1)
    print("\ndf2:")
    print(df2)

    # Inner merge
    inner_merged = pd.merge(df1, df2, on="ID", how="inner")
    print("\n(a) Inner merge on 'ID' (pd.merge, how='inner'):")
    print(inner_merged)

    # Left join
    left_joined = pd.merge(df1, df2, on="ID", how="left")
    print("\n(b) Left join on 'ID' (pd.merge, how='left'):")
    print(left_joined)
    print(
        "\nHow missing values are handled (Left join):\n"
        "- All rows from df1 are kept.\n"
        "- If an ID from df1 does not exist in df2, the columns coming from df2\n"
        "  (e.g., 'city', 'score2') become NaN."
    )

    # Right join
    right_joined = pd.merge(df1, df2, on="ID", how="right")
    print("\n(c) Right join on 'ID' (pd.merge, how='right'):")
    print(right_joined)

    # Index-Based Join
    # Set ID as index for df1 and df2 and use df.join
    df1_indexed = df1.set_index("ID")
    df2_indexed = df2.set_index("ID")

    # Default join keeps left index; use how='left' / 'right' as needed
    index_left = df1_indexed.join(df2_indexed, how="left")
    print("\n(d) Index-based join using df.join() on the index (df1_indexed.join(df2_indexed, how='left')):")
    print(index_left)

    index_inner = df1_indexed.join(df2_indexed, how="inner")
    print("\n(e) Index-based join using df.join() with how='inner':")
    print(index_inner)

    # Compare: inner merge result vs index_inner
    print("\nComparison: pd.merge inner vs df.join inner (should match on matching IDs):")
    print("pd.merge inner:")
    print(inner_merged.sort_values("ID").reset_index(drop=True))
    print("df.join inner:")
    print(index_inner.sort_index().reset_index())

    # ============================================================
    # 2) Merging with Multiple Keys
    # ============================================================
    print("\n2) Merging with multiple keys")

    df_left_keys = pd.DataFrame(
        {
            "ID": [1, 2, 2, 3],
            "Date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-01"],
            "value_left": [100, 200, 210, 300],
        }
    )

    df_right_keys = pd.DataFrame(
        {
            "ID": [2, 2, 3, 4],
            "Date": ["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-01"],
            "value_right": [999, 888, 777, 666],
        }
    )

    df_left_keys["Date"] = pd.to_datetime(df_left_keys["Date"]).dt.date
    df_right_keys["Date"] = pd.to_datetime(df_right_keys["Date"]).dt.date

    multi_key_merged = pd.merge(
        df_left_keys,
        df_right_keys,
        on=["ID", "Date"],
        how="inner",
    )

    print("df_left_keys:")
    print(df_left_keys)
    print("\ndf_right_keys:")
    print(df_right_keys)
    print("\nInner merge on multiple keys ['ID','Date']:")
    print(multi_key_merged)

    # ============================================================
    # 3) concat vertically then merge with a third dataframe
    #    also: understand join() vs merge()
    # ============================================================
    print("\n3) concat + merge, and join() vs merge()")

    dfA = pd.DataFrame(
        {
            "ID": [1, 2],
            "term": ["Math", "Physics"],
            "mark": [80, 75],
        }
    )

    dfB = pd.DataFrame(
        {
            "ID": [3, 4],
            "term": ["Chem", "Bio"],
            "mark": [88, 92],
        }
    )

    # Vertical concatenation
    concat_df = pd.concat([dfA, dfB], axis=0, ignore_index=True)
    print("dfA:")
    print(dfA)
    print("\ndfB:")
    print(dfB)
    print("\nVertically concatenated (pd.concat) result:")
    print(concat_df)

    dfC = pd.DataFrame(
        {
            "ID": [1, 2, 4],
            "department": ["Science", "Science", "Science"],
        }
    )
    print("\ndfC:")
    print(dfC)

    # Merge concatenated with dfC on common key 'ID'
    merged_with_c = pd.merge(concat_df, dfC, on="ID", how="inner")
    print("\nMerge concatenated df with dfC on 'ID' (inner):")
    print(merged_with_c)

    # Explanation: join() vs merge()
    print(
        "\nPrimary differences between df.join() and pd.merge():\n"
        "1) pd.merge()\n"
        "   - Merges DataFrames based on columns (or specified keys).\n"
        "   - Can merge using multiple keys easily: on=['ID','Date']\n"
        "   - Supports different join types via how='inner'/'left'/'right'/'outer'.\n\n"
        "2) df.join()\n"
        "   - Primarily joins on the index of the DataFrames.\n"
        "   - Useful when you already have meaningful indices (like ID or datetime).\n"
        "   - Can also join on a column, but typical/most common usage is index-based alignment."
    )


if __name__ == "__main__":
    main()

