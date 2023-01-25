from openpyxl import Workbook

#Creating workbook and sheet with the static headers
def create_sheet(filepath):
    wb = Workbook()
    sheet = wb.active

    sheet['A1'] = 'Nome do documento'
    sheet['B1'] = 'Status'

    wb.save(f'{filepath}/Relatório de execução.xlsx')

    return (wb, sheet)