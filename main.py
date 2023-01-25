import os

from src.utils.file_utils import get_page_number
from src.utils.sheet_operations import create_sheet, save_sheet, update_sheet
from src.utils.rpa import rpa_rename, open_adobe_reader, close_adobe_reader

filepath = 'C:\\RPA-ArtigoTeste\\' #considerar ler a partir do arquivo yml
files = os.listdir(filepath)

wb, sheet = create_sheet(filepath)
open_adobe_reader()


#Loop to filter .pdf files, apply the rpa_rename function and update the sheet'''
for file in files:
    if file.endswith('.pdf') and file[0].isdigit():
        number = get_page_number(file)

        rpa_rename(filepath, file, number)

        update_sheet(sheet, file)

close_adobe_reader()
save_sheet(wb, filepath)
