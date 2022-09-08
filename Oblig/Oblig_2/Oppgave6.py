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
for ord in valg:
    print(ord)
i = 1
valg_lower = []
for ord in valg:
    valg_lower.append(ord.lower())

print('\nÅ skrive "stopp" vil stoppe loopen og skrive ut en ferdig liste')

while True:
    kommando = str(input("\nHva vil du legge til i lista di? ").lower())
    if kommando in valg_lower:
        pakkeliste.append(kommando)
        print(f"Du har lagt til {kommando} i lista di")
        print(pakkeliste)
    elif kommando == "stopp":
        print(f"Du har valgt {kommando}")
        print("\nLista di er som følger:")
        for ord in pakkeliste:
            print(f"{i}. {ord}")
            i += 1
        break
    if kommando == "slett":
        slett = (str(input("Hva ønsker du å slette? ")).lower())
        pakkeliste.remove(slett)
        print(pakkeliste)
        continue

    if kommando not in valg_lower:
        print(f"{kommando} er ikke mulig")
