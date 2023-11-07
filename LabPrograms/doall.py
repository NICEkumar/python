import json

filename = input("enter the file name:") + '.json'

with open(filename) as jfile:
    data = json.load(jfile)

print("data..")
for entry in data:
    print("Name: ", entry['name'])
    print("roll: ", entry['roll'])
    print("id: ", entry['id'])
    print("")