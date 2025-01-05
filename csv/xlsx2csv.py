import pandas as pd


def convert_xlsx_to_csv(self):
  self.csv_path = None
  # Read Excel file
  df = pd.read_excel(self.xlsx_path, self.sheet_name)

  # Set the CSV path if not provided
  if self.csv_path is None:
    self.csv_path = self.xlsx_path.replace('.xlsx', f'_{self.sheet_name}.csv')

  # Convert and save to CSV
  df.to_csv(self.csv_path, index=False)
