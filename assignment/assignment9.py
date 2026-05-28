import re
from datetime import datetime

import pandas as pd


# ============================================================
# Regex helpers (practical validations)
# ============================================================

# Notes:
# - Email regex kept pragmatic (covers most common real emails).
# - Mobile regex supports optional +country code and 10-digit local numbers.
EMAIL_REGEX = re.compile(
    r"^(?P<local>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+)\.(?P<tld>[A-Za-z]{2,})$"
)

# Accepts:
# - 10 digits: 9876543210
# - optional +91: +919876543210
# - optional separators: spaces/dashes
MOBILE_REGEX = re.compile(r"^(?:\+?\s*\d{1,3}[\s-]?)?(?:\d[\s-]?){10}$")

NAME_REGEX = re.compile(r"^[A-Za-z]+(?:\s+[A-Za-z]+)*$")

# Allow common address chars: letters, digits, spaces, commas, dots, hyphens, hashes, slashes
ADDRESS_REGEX = re.compile(r"^[A-Za-z0-9\s\,\.\-\#\/]+$")


def is_valid_email(s: str) -> bool:
    if s is None:
        return False
    s = str(s).strip()
    if not s:
        return False
    return EMAIL_REGEX.match(s) is not None


def clean_mobile(s: str) -> str:
    """Normalize mobile to digits-only."""
    if s is None:
        return ""
    s = str(s)
    return re.sub(r"\D+", "", s)


def is_valid_mobile(s: str) -> bool:
    if s is None:
        return False
    raw = str(s).strip()
    if not raw:
        return False
    if MOBILE_REGEX.match(raw) is None:
        return False

    digits = clean_mobile(raw)

    # Accept either 10 digits (local) or country+local digits.
    # (Kept intentionally broad for assignment purposes.)
    return len(digits) in {10, 11, 12, 13, 14, 15}


def clean_name(s: str) -> str:
    if s is None:
        return ""
    return " ".join(str(s).strip().split()).title()


def clean_address(s: str) -> str:
    if s is None:
        return ""
    s = str(s).strip()
    return re.sub(r"\s+", " ", s)


# ============================================================
# Main assignment
# ============================================================


def main() -> None:
    print("\n==================== Assignment 9 ====================")
    print("Regex validation + pandas datetime exploration + CSV cleaning/analysis\n")

    # --------------------
    # 1) Load CSV
    # --------------------
    csv_path = "data.csv"
    df = pd.read_csv(csv_path)

    print("--- Raw data ---")
    print(df)

    # --------------------
    # 2) Data cleaning using regex-based validators
    # --------------------
    df["name_clean"] = df["name"].apply(clean_name)
    df["address_clean"] = df["address"].apply(clean_address)
    df["mobile_clean"] = df["mobile"].apply(clean_mobile)

    df["name_valid"] = df["name_clean"].apply(lambda x: bool(NAME_REGEX.match(x)))
    df["address_valid"] = df["address_clean"].apply(lambda x: bool(ADDRESS_REGEX.match(x)))
    df["mobile_valid"] = df["mobile"].apply(is_valid_mobile)
    df["email_valid"] = df["email"].apply(is_valid_email)

    # Essential row validity: at least name, mobile, email valid
    df["row_valid"] = df["name_valid"] & df["mobile_valid"] & df["email_valid"]

    print("\n--- Validation flags ---")
    print(
        df[
            [
                "name",
                "name_clean",
                "name_valid",
                "mobile",
                "mobile_clean",
                "mobile_valid",
                "email",
                "email_valid",
            ]
        ]
    )

    # Summary of validation counts
    print("\n--- Validation summary ---")
    summary = {
        "rows_total": len(df),
        "rows_valid": int(df["row_valid"].sum()),
        "rows_invalid": int((~df["row_valid"]).sum()),
        "valid_emails": int(df["email_valid"].sum()),
        "valid_mobiles": int(df["mobile_valid"].sum()),
    }
    for k, v in summary.items():
        print(f"{k}: {v}")

    # Keep only valid rows for further analysis
    df_valid = df[df["row_valid"]].copy()

    # Derive some simple features
    df["address_length"] = df["address_clean"].fillna("").apply(len)
    df["name_length"] = df["name_clean"].fillna("").apply(len)
    df["mobile_length"] = df["mobile_clean"].fillna("").apply(len)

    print("\n--- Cleaned dataframe (selected columns) ---")
    print(
        df[
            [
                "name_clean",
                "address_clean",
                "mobile_clean",
                "email",
                "name_valid",
                "address_valid",
                "mobile_valid",
                "email_valid",
                "row_valid",
                "address_length",
            ]
        ]
    )

    # Analysis outputs (meaningful groupings even with small data)
    print("\n--- Analysis: address length bins (df) ---")
    bins = [0, 10, 20, 999999]
    labels = ["short", "medium", "long"]
    df["address_len_bin"] = pd.cut(
        df["address_length"], bins=bins, labels=labels, include_lowest=True
    )

    addr_bin_counts = df["address_len_bin"].value_counts(dropna=False).sort_index()
    print(addr_bin_counts)

    # Ensure derived column exists in df_valid
    if "name_length" not in df_valid.columns:
        df_valid["name_length"] = df_valid["name_clean"].fillna("").apply(len)

    print("\n--- Analysis: top name lengths among valid rows ---")
    print(df_valid[["name_clean", "name_length"]].sort_values("name_length", ascending=False))

    # --------------------
    # 3) pandas datetime exploration
    # --------------------
    print("\n==================== 2) pandas datetime exploration ====================")

    # Derived toy dates: create signup_date from row order.
    # (In real datasets this would come from a date column.)
    start_date = datetime(2024, 1, 1)
    df["signup_date"] = pd.to_datetime(
        [start_date + pd.Timedelta(days=i) for i in range(len(df))]
    )

    print("\n1) signup_date parsed")
    print(df[["name_clean", "signup_date"]])

    # Datetime components
    df["year"] = df["signup_date"].dt.year
    df["month"] = df["signup_date"].dt.month
    df["day"] = df["signup_date"].dt.day
    df["dayofweek"] = df["signup_date"].dt.day_name()

    print("\nDerived datetime components (year/month/day/dayofweek):")
    print(df[["name_clean", "year", "month", "day", "dayofweek"]])

    # Sorting by datetime
    print("\n2) Sort by signup_date:")
    print(df.sort_values("signup_date")[["name_clean", "signup_date"]])

    # Resampling on a time index
    time_series = df.set_index("signup_date").assign(new_users=1).sort_index()[["new_users"]]
    daily = time_series.resample("D").sum()
    print("\n3) Resampled daily new_users:")
    print(daily)

    # Rolling mean on the daily series
    daily["rolling_2d_mean"] = daily["new_users"].rolling(window=2, min_periods=1).mean()
    print("\n4) Rolling mean (window=2) on daily:")
    print(daily)

    # Shift example
    daily["prev_day_new_users"] = daily["new_users"].shift(1)
    print("\n5) Shift example (prev_day_new_users):")
    print(daily)

    # Robust parsing with errors='coerce'
    print("\n6) Example: pd.to_datetime with errors='coerce'")
    weird_dates = pd.Series(["2024-01-01", "not-a-date", "2024-01-03"])
    parsed = pd.to_datetime(weird_dates, errors="coerce")
    print(pd.DataFrame({"raw": weird_dates, "parsed": parsed}))

    print("\n==================== Done ====================")


if __name__ == "__main__":
    main()

