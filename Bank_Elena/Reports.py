import json
from reportlab.pdfgen.canvas import Canvas
# from datetime import datetime
# local_dt = datetime.now()
def report():
    print("Select client: ")
    print("-" * 20)
    json_clinet_file = open("Bank_E.json", "r")
    client_dict = json.load(json_clinet_file)
    json_clinet_file.close()

    for i in client_dict:
        print(f"{i}. ID: {client_dict[i]['ID']} - {client_dict[i]['nume']}")

    while True:
        option = input("Selectati numarul coresponzator:\n>")
        if option.lower() == "exit":
            break
        # elif sa caute daca id-ul exista
        else:
            canvas = Canvas(f"./{client_dict[option]['nume']}.pdf")
            canvas.setFont("Courier-Bold", 15)
            canvas.drawString(20, 800, "raport bancar".upper())
            canvas.drawString(20, 770, "-" * 20)
            # canvas.drawString(20, 770, local_dt)
            canvas.drawString(20, 750,
                              f"Soldul pentru clientul: {client_dict[option]['nume']} este {client_dict[option]['balance']}")
            canvas.setFont("Courier-Bold", 10)
            canvas.drawString(450, 200, "Python Bank app")
            print("File generated")
            canvas.save()
            break


