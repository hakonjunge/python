while True:
    livets_mening = int(input("Hva er meningen med livet? Hint: Det er et tall. "))
    if livets_mening == 42:
        print(f"Det stemmer, meningen med livet er {livets_mening}!")
        break
    elif 30 < livets_mening < 50:
        print(f"Nærme, men {livets_mening} er feil")
    else:
        print("FEIL!")
'''Ganske rett frem, gjorde en if statement etter en input. 
gikk lei av å runne scriptet manuelt hele tiden så la utspørringen inni en while løkke
'''