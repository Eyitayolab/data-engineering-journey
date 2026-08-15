# Liftflow Work Orders Analysis

This project provides a small pandas-based analysis of Liftflow work-order data. It loads a CSV dataset, previews the records, and reports the number of rows and columns.

## Project Files

- `Liftflow Project 1.py` - Python analysis script.
- `liftflow_work_orders.csv` - Source work-order dataset.
- `liftflow_work_orders.numbers` - Companion Apple Numbers spreadsheet.
- `AGENTS.md` - Instructions for AI coding agents working on this project.

## Dataset

The dataset contains 100 work orders and 10 columns:

- Work order ID
- Date opened
- Branch
- Customer
- Technician
- Equipment type
- Priority
- Status
- Hours worked
- Completion date

## Requirements

- Python 3
- pandas

The project includes a virtual environment in `.venv/`. Use it when running the script:

```bash
.venv/bin/python "Liftflow Project 1.py"
```

If the environment has not been set up yet, install pandas with:

```bash
python3 -m pip install pandas
```

## Current Output

The script prints the first five rows of the dataset, followed by the total row and column counts.

Expected summary:

```text
Number of rows in the dataframe: 100
Number of columns in the dataframe: 10
```

## Data Safety

Treat `liftflow_work_orders.csv` as the source dataset. Save transformed or analyzed results to a separate output file rather than overwriting the source data.

## Code overview

- `Liftflow Project 1.py` exposes two small helpers:
	- `load_data(path: str) -> pd.DataFrame` — loads the CSV and is easy to test.
	- `summarize_df(df: pd.DataFrame) -> Tuple[int, int]` — returns (rows, cols).
- The `main()` function prints a preview, the shape, dtypes, missing-value counts, and the tail.
- These functions have docstrings and type hints — prefer calling them in tests or other modules instead of copying library internals into this file.

## Contributors

- Oluwaseun Ojo — author, dataset creator