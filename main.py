import os

from src.utils.file_utils import get_page_number
from src.utils.sheet_operations import create_sheet
from src.utils.rpa import rpa_rename

filepath = 'C:\\RPA-ArtigoTeste\\' #considerar ler a partir do arquivo yml
files = os.listdir(filepath)

wb, sheet = create_sheet(filepath)

#Loop to filter .pdf files, apply the rpa_rename function and update the sheet
for file in files:
    if file.endswith('.pdf') and file[0].isdigit():
        number = get_page_number(file)

        rpa_rename(filepath, file, number)

        sheet.append([file, 'documento alterado']) #mover para create_sheet
        wb.save(f'{filepath}/Relatório de execução.xlsx') #mover para create_sheet