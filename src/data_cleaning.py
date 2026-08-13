import os
import pandas as pd


RAW_DATA_PATH = "data/raw/online_retail.xlsx"
PROCESSED_DATA_PATH = "data/processed/cleaned_sales_data.csv"


def load_data():
    """Load the raw Online Retail dataset."""

    df = pd.read_excel(RAW_DATA_PATH)

    print("Dataset loaded successfully.")
    print(f"Raw dataset shape: {df.shape}")

    return df


def clean_data(df):
    """Clean and prepare the Online Retail dataset for analysis."""

    df = df.copy()

    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Remove exact duplicate rows
    df = df.drop_duplicates()

    # 3. Convert invoice date to datetime
    df["invoicedate"] = pd.to_datetime(
        df["invoicedate"],
        errors="coerce"
    )

    # 4. Remove rows with invalid dates
    df = df.dropna(subset=["invoicedate"])

    # 5. Remove cancelled invoices
    df = df[
        ~df["invoiceno"]
        .astype(str)
        .str.startswith("C")
    ]

    # 6. Keep completed positive-quantity sales
    df = df[df["quantity"] > 0]

    # 7. Remove zero or negative prices
    df = df[df["unitprice"] > 0]

    # 8. Remove products without descriptions
    df = df.dropna(subset=["description"])

    # 9. Create total sales value
    df["sales"] = df["quantity"] * df["unitprice"]

    # 10. Create useful time variables
    df["year"] = df["invoicedate"].dt.year
    df["month"] = df["invoicedate"].dt.month
    df["month_name"] = df["invoicedate"].dt.month_name()
    df["day_of_week"] = df["invoicedate"].dt.day_name()

    # 11. Clean CustomerID while preserving missing customers
    df["customerid"] = df["customerid"].astype("Int64")

    return df


def validate_data(df):
    """Run basic validation checks on the cleaned dataset."""

    print("\n--- Cleaned Dataset Validation ---")

    print(f"Cleaned dataset shape: {df.shape}")

    print(
        "Duplicate rows:",
        df.duplicated().sum()
    )

    print(
        "Cancelled invoices:",
        df["invoiceno"]
        .astype(str)
        .str.startswith("C")
        .sum()
    )

    print(
        "Non-positive quantities:",
        (df["quantity"] <= 0).sum()
    )

    print(
        "Non-positive prices:",
        (df["unitprice"] <= 0).sum()
    )

    print(
        "Missing descriptions:",
        df["description"].isna().sum()
    )

    print(
        "Missing Customer IDs:",
        df["customerid"].isna().sum()
    )

    print(
        "Missing invoice dates:",
        df["invoicedate"].isna().sum()
    )


def save_data(df):
    """Save the cleaned dataset."""

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print(
        f"\nCleaned dataset saved to "
        f"{PROCESSED_DATA_PATH}"
    )


def main():
    """Run the complete data-cleaning pipeline."""

    df = load_data()

    cleaned_df = clean_data(df)

    validate_data(cleaned_df)

    save_data(cleaned_df)


if __name__ == "__main__":
    main()