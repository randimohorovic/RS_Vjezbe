def provjera_lozinke(lozinka):
   
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova.")
        return


    veliko = any(slovo.isupper() for slovo in lozinka)
    broj = any(slovo.isdigit() for slovo in lozinka)

    if not veliko or not broj:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
        return

    
    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
        return

    
    print("Lozinka je jaka!")


unos = input("Unesite lozinku: ")
provjera_lozinke(unos)
