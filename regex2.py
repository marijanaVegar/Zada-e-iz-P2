import re

# Regex za provjeru e-maila
regex_email = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'

# Regex za provjeru eduId-a
regex_eduid = r'^i[a-zA-Z]+(\d*)@sum\.ba$'

# Unos e-maila od korisnika
email = input("Unesite e-mail: ").strip()

# Unos eduId-a od korisnika
eduid = input("Unesite eduId: ").strip()

# Provjera e-maila
if re.match(regex_email, email):
    print("E-mail je u ispravnom formatu.")
else:
    print("E-mail nije u ispravnom formatu.")

# Provjera eduId-a
if re.match(regex_eduid, eduid):
    print("EduId je u ispravnom formatu.")
else:
    print("EduId nije u ispravnom formatu.")
