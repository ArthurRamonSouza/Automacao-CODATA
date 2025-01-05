import tkinter as tk
import xlsx_handler as xh
import browser_manager as bm
from tkinter import filedialog
from datetime import datetime


class CodataRPA:

  def __init__(self, root):
    self.root = root
    self.root.title("Automação CODATA - LRO")
    self.sheet_name = "LRO"
    self.start_column = 'H'
    self.start_row = '10'

    # GUI Elements
    self.label_file_path = tk.Label(root, text="Arquivo:")
    self.label_file_path.grid(row=0, column=0, padx=10, pady=10)

    self.entry_file_path = tk.Entry(root, width=20, state='disabled')
    self.entry_file_path.grid(row=0, column=1, padx=10, pady=10)

    self.button_browse = tk.Button(root,
                                   text="Procurar",
                                   command=self.browse_file)
    self.button_browse.grid(row=0, column=2, padx=10, pady=10)

    self.label_sheet_name = tk.Label(root, text="Nome da Planilha:")
    self.label_sheet_name.grid(row=1, column=0, padx=10, pady=10)

    self.entry_sheet_name = tk.Entry(root, width=20)
    self.entry_sheet_name.insert(0, self.sheet_name)
    self.entry_sheet_name.grid(row=1, column=1, padx=10, pady=10)

    self.label_start_cell = tk.Label(root, text="Célula de Início:")
    self.label_start_cell.grid(row=1, column=2, padx=10, pady=10)

    self.entry_start_column = tk.Entry(root, width=5)
    self.entry_start_column.insert(0, self.start_column)
    self.entry_start_column.grid(row=1, column=3, padx=10, pady=10)

    self.entry_start_row = tk.Entry(root, width=5)
    self.entry_start_row.insert(0, self.start_row)
    self.entry_start_row.grid(row=1, column=4, padx=10, pady=10)

    self.label_username = tk.Label(root, text="Usuário:")
    self.label_username.grid(row=3, column=0, padx=10, pady=10)

    self.entry_username = tk.Entry(root, width=20)
    self.entry_username.grid(row=3, column=1, padx=10, pady=10)

    self.label_password = tk.Label(root, text="Senha:")
    self.label_password.grid(row=3, column=2, padx=15, pady=10)

    self.entry_password = tk.Entry(root, width=20, show="*")
    self.entry_password.grid(row=3, column=3, padx=10, pady=10)

    self.label_srh_username = tk.Label(root, text="Usuário SRH:")
    self.label_srh_username.grid(row=4, column=0, padx=10, pady=10)

    self.entry_srh_username = tk.Entry(root, width=20)
    self.entry_srh_username.grid(row=4, column=1, padx=10, pady=10)

    self.label_srh_password = tk.Label(root, text="Senha SRH:")
    self.label_srh_password.grid(row=4, column=2, padx=15, pady=10)

    self.entry_srh_password = tk.Entry(root, width=20, show="*")
    self.entry_srh_password.grid(row=4, column=3, padx=10, pady=10)

    self.button_open_file = tk.Button(root,
                                      text="Abrir Arquivo",
                                      command=self.rpa)
    self.button_open_file.grid(row=5, column=1, columnspan=2, pady=20)

  def browse_file(self):
    self.xlsx_path = filedialog.askopenfilename(filetypes=[("XLSX Files",
                                                            "*.xlsx")])
    if self.xlsx_path:
      self.entry_file_path.config(state='normal')
      self.entry_file_path.delete(0, tk.END)
      self.entry_file_path.insert(0, self.xlsx_path)
      self.entry_file_path.config(state='disabled')
    else:
      print("Error: No file selected.")

  def rpa(self):
    start = datetime.now().minute
    login = (self.entry_username.get(), self.entry_password.get())
    srh_login = (self.entry_srh_username.get(), self.entry_srh_password.get())
    login = ("sad2001", "ejsR#04061830")
    srh_login = ("sa2001", "codata")

    try:
      # Read the xlsx file, load the workbook and getting the sheet
      handler = xh.XlsxHandler()
      workbook = handler.open_workbook(self.xlsx_path)
      sheet = handler.get_sheet(workbook, self.sheet_name)

      # Call the selenium, in loop iterate through the data passing the matricula and edit all the columns needed
      browser = bm.BrowserManager()
      chrome_driver = browser.install_driver()
      browser.login_codata(chrome_driver, login)
      browser.login_srh(chrome_driver, srh_login)

      # Get the new values in CODATA website and write the data in the sheet
      row = int(self.start_row)
      while sheet[f"G{row}"].value is not None:
        new_values = []
        matricula = sheet[f"G{row}"].value

        if type(matricula) == str:
          matricula = matricula.replace(".", "").replace("-", "")
        elif type(float):
          matricula = str(matricula).split('.')[0]
          sheet[f"G{row}"].value = str(matricula)

        browser.search_matricula(chrome_driver, matricula)
        browser.get_data(chrome_driver, new_values)
        columns = ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R']
        handler.edit_sheet_row(sheet, row, columns, new_values)
        row += 1

      # Close the browser
      browser.close_driver(chrome_driver)
      # Rename, save and close the file
      handler.close_workbook(workbook, self.xlsx_path.replace(" ", "_"))
      end = datetime.now().minute
      print(f'Tempo de execucao em minutos {end -start}.')

    except FileNotFoundError:
      print(f"Error: File not found at path {self.xlsx_path}")
    except Exception as e:
      print(f"An error occurred on CodataRPA class: {e}")


if __name__ == "__main__":
  root = tk.Tk()
  app = CodataRPA(root)
  root.mainloop()
