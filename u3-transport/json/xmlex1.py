import xml.etree.ElementTree as ET
import sys

# Parse
xml_person = ET.parse(sys.argv[1])

# Get root element
e = xml_person.getroot()

# Get a certain child
friends = e.find("friends")

# Get attribute tuples (everything is a string)
for f in list(friends):
    print(f.text)

# Iterate over child elements
scores = e.find("scores")
for score in list(scores):
    print(score.get("id"), score.text)

