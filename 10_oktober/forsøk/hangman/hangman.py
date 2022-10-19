def hangman():
    hemmelig_ord = str.lower(input("Skriv inn et ord: "))
    antall_liv = int(input("Hvor mange liv skal du ha: "))
    antall_bokstaver_i_ord = int(len(hemmelig_ord))
    riktig_svar = 0
    while antall_liv > 0:
        gjett = str.lower(input("Skriv inn en bokstav: "))
        if gjett in hemmelig_ord:
            print("Korrekt")
            riktig_svar += 1
            print(f"Du har {riktig_svar} riktige svar")
            if riktig_svar == antall_bokstaver_i_ord:
                print(f"Du greide det! Ordet var {hemmelig_ord}")
                break
        elif gjett not in hemmelig_ord:
            print("Prøv igjen: ")
            antall_liv -= 1
            if antall_liv > 0:
                print(f"Du har {antall_liv} liv igjen")
            else:
                print("Beklager du røyk ut")
hangman()