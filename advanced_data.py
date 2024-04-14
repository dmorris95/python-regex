#Task 1

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
extraction = re.findall(r"Occupation: (.+?);", text)
print(extraction)
