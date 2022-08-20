import openpyxl
import re
wb = openpyxl.load_workbook("総合政策リスト.xlsx")
ws = wb["総合政策"]


i = 1
for cell in ws['B']:
    #print(cell.value.isascii())
    #print(str(i))
    #i = i + 1
    if not cell.value.isascii():
        row = cell.row
        print(cell.row)
        ws.delete_rows(row)
    """
    if not bool(re.search(r'[a-zA-Z0-9]',cell.value)):
        print(cell)
    """
wb.save('総合政策リスト.xlsx')

#print(bool(re.search(r'[a-zA-Z0-9]', "aA00")))