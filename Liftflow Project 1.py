"""Liftflow work-orders quick analysis.

This small script loads the `liftflow_work_orders.csv` dataset, prints
the first five rows, and reports the dataframe dimensions.

Exported helpers are small and typed to make the code easier to test
and to provide useful hover/type information in IDEs.
"""

from typing import Tuple

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
	"""Load a CSV file into a pandas DataFrame.

	Args:
		path: Path to the CSV file.

	Returns:
		A pandas DataFrame containing the loaded data.
	"""
	return pd.read_csv(path)


def summarize_df(df: pd.DataFrame) -> Tuple[int, int]:
	"""Return (rows, columns) for `df`."""
	return int(df.shape[0]), int(df.shape[1])


def main() -> None:
	df = load_data("liftflow_work_orders.csv")
	print(df.head())
	rows, cols = summarize_df(df)
	print(f"Number of rows in the dataframe: {rows}")
	print(f"Number of columns in the dataframe: {cols}")

	# Additional lightweight diagnostics useful during exploration
	print("Data types of each column:")
	print(df.dtypes)

	print("Missing values in each column:")
	print(df.isnull().sum())

	print("Last five rows of the dataframe:")
	print(df.tail())


if __name__ == "__main__":
	main()