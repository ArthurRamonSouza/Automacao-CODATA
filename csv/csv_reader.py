import csv


def read_csv_file(csv_path, start_line):
  try:
    with open(csv_path, 'r') as file:
      # Read the entire CSV file into a list of dictionaries
      with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

      # Accessing the data row by row
      for index, row in enumerate(data):
        if index >= start_line:
          print(row)  # You can process or manipulate the data here as needed
        else:
          index += 1
    return data

  except FileNotFoundError:
    print(f"Error: File not found at path {csv_path}")
  except Exception as e:
    print(f"An error occurred: {e}")
