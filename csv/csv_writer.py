import csv


def write_csv_file(csv_path):
  new_data = {
      'LRO - LEVANTAMENTO DOS RISCOS OCUPACIONAIS DAS AREAS ':
      'SECRETARIO DE ESTADO',
      'Unnamed: 1': '',
      'Unnamed: 2': 'ADMINISTRATIVA',
      'Unnamed: 3': 'ANTONIO RIBEIRO',
      'Unnamed: 4': 'SECRETARIO DE ESTADO',
      'Unnamed: 5': 'SECRETARIO DE ESTADO',
      'Unnamed: 6': '1915398',
      'Unnamed: 7': 'COMISSIONADO',
      'Unnamed: 8': 'M',
      'Unnamed: 9': '8 HORAS / DIA',
      'Unnamed: 10': 'NÃO',
      'Unnamed: 11': 'NÃO',
      'Unnamed: 12': 'NÃO',
      'Unnamed: 13': '13163663400',
      'Unnamed: 14': '540475',
      'Unnamed: 15': '',
      'Unnamed: 16': '19030240485',
      'Unnamed: 17': '2022023',
      'Unnamed: 18': ''
  }
  try:
    # Write the modified data back to the CSV file
    with open(csv_path, 'w', newline='') as file:
      fieldnames = list(new_data.keys())
      csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

      # Write the header
      csv_writer.writeheader()

      # Write the modified data
      csv_writer.writerow(new_data)
      print(f"File {csv_path} edited successfully!")

  except FileNotFoundError:
    print(f"Error: File not found at path {csv_path}")
  except Exception as e:
    print(f"An error occurred: {e}")
