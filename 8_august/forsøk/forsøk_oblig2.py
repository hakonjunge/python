'''livets_mening = input("Hva er meningen med livet?")
livets_mening = int(livets_mening)

while livets_mening != 42:
    if not livets_mening == 42:
        print("FEIL!")
        continue'''
'''
livets_mening = input("Hva er meningen med livet?")
livets_mening = int(livets_mening)

if livets_mening == 42:
    print("Riktig, livets mening er 42!")

else:
   print("FEIL")
   continue'''
svar = 42
close1 = 30
close2 = 50
while True:
    livets_mening = int(input("Hva er meningen med livet?"))
    if livets_mening == svar:
        print("Det stemmer, meningen med livet er 42!")
        break
    elif close1 < livets_mening < close2:
        print("Nærme, men feil")
    else:
        print("FEIL!")