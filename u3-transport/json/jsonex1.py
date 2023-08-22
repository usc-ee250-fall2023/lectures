import sys
import json

json_file = open(sys.argv[1], "r")
json_text = json_file.read()

# Read in JSON and convert to Python dict
person = json.loads(json_text)
print("Raw input: ")
print(person)
print("\n\n")
# Update the data using Python object syntax
person["friends"].append("Aaron")

# Convert back to JSON
new_json = json.dumps(person, indent=4)
print("Updated: ")
print(new_json)
