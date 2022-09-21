svar = 42
close1 = 30
close2 = 50
while True:
    livets_mening = int(input("Hva er meningen med livet?"))
    if livets_mening == svar:
        print(f"Det stemmer, meningen med livet er {livets_mening}!")
        break
    elif close1 < livets_mening < close2:
        print(f"Nærme, men {livets_mening} er feil")
    else:
        print("FEIL!")
