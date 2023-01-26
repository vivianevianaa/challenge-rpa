import os
from src.utils.sheet_operations import create_sheet, update_sheet, save_sheet, close_sheet
from src.utils.file_utils import get_page_number
from src.rpa import rpa_rename, open_adobe_reader, close_adobe_application

# Set the challenge folder and list the files
filepath = 'C:\\RPA-ArtigoTeste\\'
files = os.listdir(filepath)

# Create the sheet and open the Adobe Reader application
wb, sheet = create_sheet(filepath)
open_adobe_reader()

# The loop that will filter valid .pdf files, apply the rpa_rename function and update the sheet.
for file in files:
    if file.endswith('.pdf') and file[0].isdigit():
        number = get_page_number(file)

        rpa_rename(filepath, file, number)

        update_sheet(sheet, file)

# Closing the Adobe Reader application, saving and closing the sheet.
close_adobe_application()
save_sheet(wb, filepath)
close_sheet(wb)
