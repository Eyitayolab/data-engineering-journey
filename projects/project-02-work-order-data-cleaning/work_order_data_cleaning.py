import pandas as pd
from pathlib import Path


def load_data(csv_path):
    """Load CSV file into a pandas DataFrame."""
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows from {csv_path}")
    return df


def inspect_data(df):
    """Perform initial inspection of the DataFrame."""
    print("\n=== Initial Data Inspection ===")
    print(f"Number of rows: {len(df)}")
    print(f"\nFirst 5 rows:")
    print(df.head())
    print(f"\nShape: {df.shape}")
    print(f"\nColumn names: {df.columns.tolist()}")
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    print(f"\nDuplicate rows: {df.duplicated().sum()}")


def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    print("\n=== Removing Duplicates ===")
    initial_rows = len(df)
    df = df.drop_duplicates().copy()
    duplicates_removed = initial_rows - len(df)
    print(f"Removed {duplicates_removed} duplicate rows")
    print(f"Shape after removing duplicates: {df.shape}")
    print("\nMissing values after deduplication:")
    print(df.isnull().sum())
    return df


def clean_text_fields(df):
    """Clean and standardize text fields."""
    print("\n=== Cleaning Text Fields ===")
    
    # Get all text columns
    text_columns = df.select_dtypes(include=['object', 'str']).columns
    
    # Trim whitespace from all text columns
    for col in text_columns:
        df[col] = df[col].str.strip()
    print(f"✓ Trimmed whitespace from {len(text_columns)} text columns")
    
    # Standardize only categorical columns to lowercase
    categorical_columns = ['Status', 'Priority']
    for col in categorical_columns:
        if col in df.columns:
            df[col] = df[col].str.lower()
    print(f"✓ Standardized categorical columns: {', '.join(categorical_columns)}")
    
    # Standardize proper nouns to title case
    if 'Branch' in df.columns:
        df['Branch'] = df['Branch'].str.title()
    print("✓ Standardized Branch names to title case")
    
    # Replace inconsistent category values
    df["Status"] = df["Status"].replace({
        "complete": "completed"
    })

    if 'Priority' in df.columns:
        df["Priority"] = df["Priority"].replace({
            "med": "medium"
        })
    print("✓ Replaced inconsistent category values")
    
    return df


def convert_dates(df):
    """Convert date columns and report invalid values."""
    print("\n=== Converting Dates ===")

    for col in ["DateOpened", "CompletionDate"]:
        if col in df.columns:
            original_values = df[col].copy()

            df[col] = pd.to_datetime(
                df[col],
                format="mixed",
                errors="coerce"
            )

            invalid_mask = df[col].isna() & original_values.notna()

            if invalid_mask.any():
                print(f"\n⚠ Invalid {col} values found:")
                print(
                    pd.DataFrame({
                        "WorkOrderID": df.loc[invalid_mask, "WorkOrderID"],
                        "InvalidValue": original_values[invalid_mask]
                    })
                )

            print(f"✓ Converted {col} to datetime format")

    return df


def convert_numeric(df):
    """Convert HoursWorked to numeric format."""
    print("\n=== Converting Numeric Fields ===")
    
    if 'HoursWorked' in df.columns:
        df['HoursWorked'] = pd.to_numeric(df['HoursWorked'], errors='coerce')
        print("✓ Converted HoursWorked to numeric format")
        
        # Identify negative or invalid hours
        invalid_hours = df[df['HoursWorked'] < 0]
        if not invalid_hours.empty:
            print(f"\n⚠ Negative hours found ({len(invalid_hours)} rows):")
            print(invalid_hours[['WorkOrderID', 'HoursWorked', 'Status']])
            
            # Replace negative hours with missing values
            df.loc[df["HoursWorked"] < 0, "HoursWorked"] = pd.NA
            print("✓ Replaced negative hours with NA")
    
    return df


def validate_data(df):
    """Validate the cleaned dataset."""
    print("\n" + "="*50)
    print("=== Validation of the Cleaned Dataset ===")
    print("="*50)
    
    # Check required columns
    required_columns = ['WorkOrderID', 'DateOpened', 'Branch', 'Customer', 
                       'Technician', 'EquipmentType', 'Priority', 'Status', 
                       'HoursWorked', 'CompletionDate']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        print(f"❌ ERROR: Missing columns: {missing_columns}")
    else:
        print("✓ All required columns present")
    
    # Validate data types
    print("\nData Types:")
    print(df.dtypes)
    
    # Check for unexpected null patterns
    print("\nMissing Values Summary:")
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print(null_counts[null_counts > 0])
    else:
        print("✓ No missing values")
    
    # Validate business rules
    print("\nBusiness Rule Validation:")
    completed = df[df['Status'] == 'completed']
    print(f"✓ {len(completed)} completed work orders")
    
    positive_hours = df[df['HoursWorked'] > 0].shape[0]
    print(f"✓ {positive_hours} records with positive hours")
    
    remaining_duplicates = df.duplicated().sum()
    print(f"✓ {remaining_duplicates} duplicate rows remaining")
    
    negative_hours = (df["HoursWorked"] < 0).sum()
    print(f"✓ {negative_hours} negative HoursWorked values remaining")
    
    print("\nUnique Status values:")
    print(df["Status"].unique())
    
    print("\nUnique Priority values:")
    print(df["Priority"].unique())
    
    print("\nUnique Branch values:")
    print(df["Branch"].unique())
    
    # Final summary
    print("\n" + "="*50)
    print(f"Final Dataset: {df.shape[0]} rows × {df.shape[1]} columns")
    print("="*50)
    
    return df


def save_data(df, output_path):
    """Save cleaned DataFrame to CSV file."""
    print("\n=== Saving Cleaned Data ===")
    df.to_csv(output_path, index=False)
    print(f"✓ Cleaned dataset saved to: {output_path}")


def main():
    """Main pipeline for data cleaning."""
    print("\n" + "="*60)
    print("LiftFlow Work Order Data Cleaning Pipeline")
    print("="*60)
    
    # Setup paths
    repo_root = Path(__file__).resolve().parent
    input_path = repo_root / "data" / "liftflow_work_orders_messy.csv"
    output_path = repo_root / "data" / "liftflow_work_orders_clean.csv"
    
    # Execute pipeline
    df = load_data(input_path)
    inspect_data(df)
    df = remove_duplicates(df)
    df = clean_text_fields(df)
    df = convert_dates(df)
    df = convert_numeric(df)
    df = validate_data(df)
    save_data(df, output_path)
    
    print("\n✓ Data cleaning pipeline completed successfully!")


if __name__ == "__main__":
    main()
