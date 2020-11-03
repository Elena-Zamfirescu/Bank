import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
googleClient = gspread.authorize(creds)
magazie = googleClient.open("Brutarie").worksheet("Magazie")
angajati = googleClient.open("Brutarie").worksheet("Angajati")
produse = googleClient.open("Brutarie").worksheet("Produse")






# print(magazie.col_values(2))
# magazie.append_row(["Seminte",230,"g"])
# lista_cu_nume=sheet.col_values(1)
# for nume in lista_cu_nume:
#     print(f"Cursantul: {nume}")

# primul_nume=sheet.cell(3,2).value
# print(primul_nume)
#
# randul1=sheet.row_values(1)
# print(randul1)
#
# print(sheet.cell(1,1))
# sheet.update_cell(1,1,"Zoe")
# print(sheet.cell(1,1))

cell=magazie.find("Apa")
print(cell)

# magazie.update('A1:B2', [[1, 2], [3, 4]])
