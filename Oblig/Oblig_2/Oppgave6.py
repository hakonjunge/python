pakkeliste = []
i = 1
print('\nÅ skrive "stopp" vil stoppe loopen og skrive ut en ferdig liste')
print('Å skrive "slett" vil gi deg mulighet å slette noe fra lista di')
print('Å skrive "legge til" vil gi deg mulighet å legge noe til i lista di')

while True:
    kommando = str(input("\nHva ønsker du å gjøre? ").lower())
    if kommando == "legge til":
        legge_til = str(input("\nHva vil du legge til i lista di? ").lower())
        pakkeliste.append(legge_til)
        print(f"Du har lagt til {legge_til} i lista di")
        print(pakkeliste)
        continue

    if kommando == "stopp":
        print("Du har valgt stopp")
        print(("\nDu har ikke lagt til noe i listen"
               if len(pakkeliste) == 0
               else "\nLista di er som følger:"))
        for item in pakkeliste:
            print(f"{i}. {item}")
            i += 1
        break

    if kommando == "slett":
        slett = (input("Hva ønsker du å slette? ")).lower()
        if slett in pakkeliste:
            pakkeliste.remove(slett)
            print(pakkeliste)
            continue
        else:
            print(f"{kommando} er ikke mulig")

    else:
        print(f"{kommando} er ikke mulig")

#det som var viktig her var å bruke en while loop. sånn at en kommando kunne stoppe loopen
#Jeg brukte if statements fordi hvis for eksompel "legge til" ikke ble oppfattet så ble du sendt videre ned til neste if
