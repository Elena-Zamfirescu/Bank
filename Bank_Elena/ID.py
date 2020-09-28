import random
import json
lines = []

def unique_ID():

    ID = random.randint(100000, 999999)
    json_file = open("Bank_E.json", "r")
    convert_json_to_dict = json.load(json_file)
    json_file.close()

    for key, value in convert_json_to_dict.items():
        lines.append(key)

    while True:
        if str(ID) in lines:
            ID = random.randint(100000, 999999)
            continue
        else:
            break

    return (ID)

