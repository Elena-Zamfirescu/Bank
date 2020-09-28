import json
import clients
import Reports
import balance

while True:
    choise = (input("Meniu:\n1. Introduceti un client nou\n2. Verificati balanta unui client dupa ID\n3. Verificati balanta unui client dupa nume si prenume\n4. Modificati balanta unui client dupa ID\n5. Generarea extras de cont\n6. Exit\nSelectati o optiune\n>"))

    if int(choise) == 1:
         clients.adaugare_client()
    elif int(choise) == 2:
        clients.interogare_dupa_ID()
    elif int(choise) == 3:
           clients.interogare_nume_prenume()
    elif int(choise) == 5:
        Reports.report()
    elif int(choise) == 6:
        break
    elif int(choise) == 4:
        balance.modificare_sold_dupa_ID()
    else:
            print("Introduceti o optiune valida")
