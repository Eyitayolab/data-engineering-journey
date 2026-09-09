# Work Order Data Cleaning Project

## Skills Demonstrated

- Python
- Pandas
- Data Cleaning
- Data Validation
- CSV Processing
- Datetime Handling
- Modular Programming
- Git

## Project Structure

```text
project-02-work-order-data-cleaning/
│
├── data/
│   ├── liftflow_work_orders_messy.csv
│   └── liftflow_work_orders_clean.csv
├── README.md
├── requirements.txt
└── work_order_data_cleaning.py
```

## Technologies Used

- Python 3
- Pandas
- pathlib

# Work Order Data Cleaning Project

## Business Problem

The LiftFlow work order dataset contained messy, inconsistent data that needed to be cleaned and standardized before it could be used for analysis and reporting. Raw data had formatting issues, duplicates, and missing values that could lead to inaccurate insights.

## Issues Found

### Data Quality Issues Identified
- **3 duplicate rows** — Exact row duplicates present in the dataset
- **3 malformed dates** — Inconsistent date formats:
  - WO-1021: `07/15/2026` (MM/DD/YYYY instead of YYYY-MM-DD)
  - WO-1047: `2026/07/22` (slashes instead of dashes)
  - WO-1092: `not-a-date` (invalid text value)
- **Text inconsistencies** — Extra whitespace, mixed capitalization across text fields
- **1 negative value** — HoursWorked = -2.0 (WO-1084)
- **Missing values** — 
  - CompletionDate: 42 nulls (expected for open work orders)
  - Customer, Technician, EquipmentType: 1 null each
  - HoursWorked: 2 nulls

## Cleaning Decisions

| Issue | Decision | Rationale |
|-------|----------|-----------|
| Duplicates | Removed (3 rows) | Prevent metric inflation and analysis errors |
| Malformed dates | Standardized in the cleaned output file | Corrected during cleaning without changing the messy source dataset |
| Invalid date (WO-1092) | Left as empty/NaT | No real date value available; null indicates missing data |
| Text whitespace | Trimmed | Ensures consistency and prevents duplicate-looking entries |
| Capitalization | Standardized to lowercase | Uniform formatting for analysis and grouping |
| Missing CompletionDate | Preserved | Valid for open work orders (Status = "open"/"in progress") |
| Negative hours | Flagged but retained | Allows data quality review before deletion decision |

## Tools Used

- **Python 3.14** — Programming language
- **Pandas** — Data manipulation and cleaning
- **Pathlib** — File path handling

## Final Result

### Dataset Statistics
- **Rows**: 100 (from 103 original)
- **Columns**: 10
- **Duplicates removed**: 3
- **Completed work orders**: 56
- **Records with positive hours**: 97

### Data Types (After Cleaning)
- WorkOrderID: string
- DateOpened: datetime64[us]
- Branch, Customer, Technician, EquipmentType, Priority, Status: string
- HoursWorked: float64
- CompletionDate: string

### Validation Passed
✓ All required columns present  
✓ Data types validated  
✓ Business rules checked  
✓ Missing value patterns reviewed  

### Output Files
- **liftflow_work_orders_clean.csv** — Cleaned dataset ready for analysis (100 rows)
- **liftflow_work_orders_messy.csv** — Original messy dataset preserved as input and left unchanged

## Running the Script

```bash
python work_order_data_cleaning.py
```

The script will:
1. Load and inspect the raw data
2. Remove duplicates
3. Clean and standardize text fields
4. Convert and validate dates
5. Validate data quality
6. Save cleaned dataset to `data/liftflow_work_orders_clean.csv`
