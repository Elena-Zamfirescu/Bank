import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
googleClient = gspread.authorize(creds)
angajati = googleClient.open("Brutarie").worksheet("Angajati")


def adaugare_angajat:
    angajati.append_row([input("Nume:\n>"),input("Prenume:\n>"),input("Functie:\n>")])

