livets_mening = input("Hva er meningen med livet?")
svar = 42
livets_mening = int(livets_mening)
close1= 30
close2 = 50
if livets_mening == svar:
    print("Det stemmer, meningen med livet er 42!")
elif close1 < livets_mening < close2:
    print("Nærme, men feil")
else:
    print("FEIL!")