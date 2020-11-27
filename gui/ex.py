import json

with open('colors.json', 'r') as read_file:
    data = json.load(read_file)

print(data)
