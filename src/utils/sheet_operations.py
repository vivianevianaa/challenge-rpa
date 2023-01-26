from openpyxl import Workbook


def create_sheet(filepath):
    """
    The function create the workbook from openpyxl.
    After that, the sheet is created with the static headers.
    """

    wb = Workbook()
    sheet = wb.active

    sheet['A1'] = 'Nome do documento'
    sheet['B1'] = 'Status'

    save_sheet(wb, filepath)

    return wb, sheet


def save_sheet(wb, filepath):
    """
    Save the sheet after updates.
    """
    wb.save(f'{filepath}/Relatório de execução.xlsx')


def update_sheet(sheet, file):
    """
    Updating sheet
    """
    sheet.append([file, 'documento alterado'])


def close_sheet(wb):
    """
    Closing workbook.
    """
    wb.close()
