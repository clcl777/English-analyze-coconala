import openpyxl
import re
wb = openpyxl.load_workbook("総合政策リスト.xlsx")
ws = wb["総合政策"]

#print(c1.value.isalpha())
i = 1
before = ""
for cell in ws['B']:
    if before == cell.value:
        print(cell)
        row = cell.row
        print(row)
        ws.delete_rows(row)
    before = cell.value
wb.save('総合政策リスト.xlsx')
    #print(cell.value.isascii())
    #print(str(i))
    #i = i + 1


#print(bool(re.search(r'[a-zA-Z0-9]', "aA00")))