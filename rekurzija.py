def ispisi_string_rekurzivno(string):
    if not string:  
        return
    else:
        print(string[0]) 
        ispisi_string_rekurzivno(string[1:]) 

ulazni_string = "Rekurzija"
ispisi_string_rekurzivno(ulazni_string)
