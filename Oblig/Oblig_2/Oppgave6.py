pakkeliste = []
valg = ["Regntøy",
        "Vindjakke",
        "Turbukse",
        "Undertøy",
        "Sokker",
        "Ullgenser",
        "Ulljakke",
        "Dunjakke",
        "Lue",
        "Ullvotter",
        "Innesko",
        "Fjellstøvler",
        "Shorts",
        "T-skjorte",
        "Ryggsekk",
        "Sovepose",
        "Solbriller",
        "Kart",
        "Kompass",
        "Drikkeflaske"]
for item in valg:
    print(item)
i = 1
valg_lower = []
for item in valg:
    valg_lower.append(item.lower())

print('\nÅ skrive "stopp" vil stoppe loopen og skrive ut en ferdig liste')

while True:
    kommando = str(input("\nHva vil du legge til i lista di? ").lower())
    if kommando in valg_lower:
        pakkeliste.append(kommando)
        print(f"Du har lagt til {kommando} i lista di")
        print(pakkeliste)

    elif kommando == "stopp":
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

    if kommando not in valg_lower:
        print(f"{kommando} er ikke mulig")
