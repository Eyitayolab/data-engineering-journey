# Liftflow Dataset Project

## Project shape

- The working analysis script is `Liftflow Project 1.py`.
- The source dataset is `liftflow_work_orders.csv`; treat it as read-only input.
- `liftflow_work_orders.numbers` is a companion spreadsheet and is not the Python runtime input.
- Run the script with `.venv/bin/python "Liftflow Project 1.py"` from the project directory.

## Autosave and data safety

- When a task creates or changes a dataframe or analysis result, persist the result explicitly before reporting completion.
- Write derived data to a clearly named output CSV, such as `liftflow_work_orders_autosave.csv`; never overwrite `liftflow_work_orders.csv` unless the user explicitly requests that.
- Keep output paths relative to the project directory and preserve the source column names unless the task requires a documented transformation.
- After writing an output, verify that the file exists and can be read back successfully.
- Keep exploratory prints and generated outputs separate from the source dataset.

## Change and validation conventions

- Make focused changes in the existing script and preserve its simple pandas-based structure.
- Use the project virtual environment for execution and validate the changed workflow by running the script.