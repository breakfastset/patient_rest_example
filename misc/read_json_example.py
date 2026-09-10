import json

json_file = open("persons.json", "r")

json_data = json.load(json_file)

print(json_data["people"])

json_file.close()