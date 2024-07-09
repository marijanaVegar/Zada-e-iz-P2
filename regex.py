import re

regex = r'^[A-Z][a-z]*\d[0-5]\s.*[A-Z][a-z]*$'

test_strings = [
    "J2 neki tekst D",
    "A4 bilo koji tekst S",
    "T0 ovaj string G",
    "A neki tekst S",
    "A6 ovaj string S",
    "T2 tekst bez prezimena"
]

for test_string in test_strings:
    if re.match(regex, test_string):
        print(f"'{test_string}' - Podudaranje")
    else:
        print(f"'{test_string}' - Ne podudaranje")
