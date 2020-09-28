import json
def modificare_sold_dupa_ID():
    ID = int(input(
            "Introduceti ID-ul clientului\n(In cazul in care nu cunoasteti ID, utilizati optiunea 3 pentru aflarea acestuia)\n>"))
    operatiune = int(input("Selectati operatiunea:\n1. Introducere suma\n2. Retragere suma\n"))
    add = int(input("Introduceti suma:\n>"))
    read_json_file = open("Bank_E.json", "r")
    convert_json_to_dict = json.load(read_json_file)
    if operatiune == 1:
        for i in convert_json_to_dict:
            if convert_json_to_dict[i]["ID"] == ID:
                sold_actual=int(convert_json_to_dict[i]["balance"])+(add)
                print("Valoarea a fost adaugata.")
                convert_json_to_dict[i]["balance"]=str(sold_actual)
            new_client = json.dumps(convert_json_to_dict, indent=4)
            rewrite_json = open("Bank_E.json", "w")
            rewrite_json.write(new_client)
            rewrite_json.close()
    elif operatiune == 2:
        for i in convert_json_to_dict:
            if convert_json_to_dict[i]["ID"] == ID:
                sold_actual=int(convert_json_to_dict[i]["balance"])-(add)
                print("Valoarea a fost scazuta din sold")
                convert_json_to_dict[i]["balance"]=str(sold_actual)
            new_client = json.dumps(convert_json_to_dict, indent=4)
            rewrite_json = open("Bank_E.json", "w")
            rewrite_json.write(new_client)
            rewrite_json.close()
    else:
        print("Selectati 1 sau 2.")
