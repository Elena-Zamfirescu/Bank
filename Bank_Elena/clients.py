import json
import ID
def adaugare_client():
    id=ID.unique_ID()
    client = {
        "ID": id,
        "nume": (input("Prenumele clientului\n>") + " " + input("Numele clientului\n>")),
        "oras": input("Orasul clientului\n>"),
        "Telefon": input("Numarul de telefon al clientului\n>"),
        "balance": input("Introduceti soldul initial in RON\n>")
    }
    read_json_file=open("Bank_E.json","r")
    convert_json_to_dict=json.load(read_json_file)
    read_json_file.close()
    poz=(len(convert_json_to_dict))
    convert_json_to_dict[poz+1]=client
    new_client=json.dumps(convert_json_to_dict, indent=4)
    rewrite_json=open("Bank_E.json","w")
    rewrite_json.write(new_client)
    rewrite_json.close()


def interogare_dupa_ID():
    read_json_file = open("Bank_E.json", "r")
    convert_json_to_dict = json.load(read_json_file)
    read_json_file.close()
    interogare_ID = (input("Introduceti ID-ul pentru care doriti sa faceti verificarea sau scrieti EXIT pentru revenire la meniu.\n>"))
    list_IDs=[]
    i=1
    while i < len(convert_json_to_dict)+1:
        list_IDs.append(convert_json_to_dict[str(i)]["ID"])
        i+=1
    # print(list_IDs)

    while True:
        if interogare_ID.lower()=="exit":
            break
        elif int(interogare_ID) not in list_IDs:
            print("ID-ul nu exista in baza de date.\nReincercati sau faceti verificarea dupa nume, selectand urmatoarea optiune din meniu.")
            break
        else:
            for i in convert_json_to_dict:
                if int(interogare_ID) == convert_json_to_dict[i]["ID"]:
                    sold=convert_json_to_dict[i]["balance"]
                    print(f"Soldul pentru interogare_ID este: {sold} RON")
            break

def interogare_nume_prenume():
    read_json_file = open("Bank_E.json", "r")
    convert_json_to_dict = json.load(read_json_file)
    read_json_file.close()
    interogare_nume_prenume = input("Introduceti numele si prenumele clientului sau scrieti EXIT pentru revenire la meniu.\n>")
    corresponding_IDs = []
    list_of_names=[]
    for i in convert_json_to_dict:
        list_of_names.append((convert_json_to_dict[str(i)]["nume"].lower()))

    for i in convert_json_to_dict:
        if (convert_json_to_dict[str(i)]["nume"].lower()) == interogare_nume_prenume.lower():
            corresponding_IDs.append(convert_json_to_dict[str(i)]["ID"])

    while True:
        if interogare_nume_prenume.lower=="exit":
            break
        elif interogare_nume_prenume.lower() not in list_of_names and interogare_nume_prenume.lower()!="exit":
            print("Numele clientului nu se afla in baza de date")
            break
        else:
            for i in corresponding_IDs:
                for j in convert_json_to_dict:
                    if i == convert_json_to_dict[j]["ID"]:
                        sold = convert_json_to_dict[j]["balance"]
                        print(f"Soldul clientului {interogare_nume_prenume} cu ID {i} este: {sold} RON")
            break


