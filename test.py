import re

telephone_formats = re.compile(r'\(?\d{3}\)?[ -]?\d{3}[-]?\d{4}')

text = "Contact me at (123) 456-7890,(123)-456-7890, 555-555-5555, or (111)2223333,1112223333."

matches = telephone_formats.findall(text)

for match in matches:
    print(match)