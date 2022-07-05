import openpyxl
path = "C:/Users/LGIT/Desktop/test P\DB-B\C3152\C3152_HM_Error.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row =3, column =1)
print(cell_obj.value)

