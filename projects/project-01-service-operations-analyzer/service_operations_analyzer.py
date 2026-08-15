"""Liftflow work-orders quick analysis.

This small script loads the `liftflow_work_orders.csv` dataset, prints
the first five rows, and reports the dataframe dimensions.

Exported helpers are small and typed to make the code easier to test
and to provide useful hover/type information in IDEs.
"""

from typing import Tuple

import pandas as pd


# ----------------
# Data helpers
# ----------------
def load_data(path: str) -> pd.DataFrame:
	"""Load a CSV file into a pandas DataFrame.

	Args:
		path: Path to the CSV file.

	Returns:
		A pandas DataFrame containing the loaded data.
	"""
	# keep this function minimal so it is easy to test and reuse
	return pd.read_csv(path)


def summarize_df(df: pd.DataFrame) -> Tuple[int, int]:
	"""Return (rows, columns) for `df`."""
	return int(df.shape[0]), int(df.shape[1])


# ----------------
# Main explorer
# ----------------
def main() -> None:
	# Load the dataset from the project root
	df = load_data("liftflow_work_orders.csv")

	# Quick preview: first five rows
	print(df.head())

	# Summarize shape and print(rows, columns)
	rows, cols = summarize_df(df)
	print(f"Number of rows in the dataframe: {rows}")
	print(f"Number of columns in the dataframe: {cols}")

	# Additional lightweight diagnostics useful during exploration
	# - column dtypes
	print("Data types of each column:")
	print(df.dtypes)

	# - missing value counts per column
	print("Missing values in each column:")
	print(df.isnull().sum())

	# - last five rows to check tail behavior
	print("Last five rows of the dataframe:")
	print(df.tail())


if __name__ == "__main__":
	main()