import random

kortstokk = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
reshuffle = []

start_chips = int(input("Hvor mange chips skal du starte med? "))
chips = start_chips

print(f"\nDu starter med {chips} chips")


def delUtKort(tur):
    kort = random.choice(kortstokk)
    tur.append(kort)
    reshuffle.append(kort)
    kortstokk.remove(kort)


def beregneTotalSum(tur):
    total = 0
    bildekort = ['J', 'Q', 'K']
    for kort in tur:
        if kort in range(1, 11):
            total += kort
        elif kort in bildekort:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


while True:
    blackjack = False
    spillerIn = True
    dealerIn = True

    spiller = []
    dealer = []

    if len(kortstokk) < 5:
        kortstokk.extend(reshuffle)
        print("\nKortstokken ble omstokket")

    while True:
        bet_chips = int(input(f"\nHvor mange chips better du?\nDu har {chips} totalt "))
        if bet_chips > 0 and bet_chips <= chips:
            print(f"\nDu har bettet {bet_chips} chipper")
            break
        print("Du kan ikke bette mer enn eller mindre enn du har")

    for _ in range(2):
        delUtKort(dealer)
        delUtKort(spiller)

    print(f"Dealeren har {dealer[:-1]} og X")
    while True:
        print(f"Du har {spiller} for en total på {beregneTotalSum(spiller)}\n")
        if beregneTotalSum(spiller) == 21:
            break
        if input("1: Stå\n2: Slå til\n") == '1':
            break
        else:
            delUtKort(spiller)
        if beregneTotalSum(spiller) >= 21:
            break

    while True:
        print(f"Dealeren har {dealer}")
        if beregneTotalSum(dealer) > 17:
            break
        else:
            delUtKort(dealer)
        if beregneTotalSum(dealer) >= 21:
            break

    print(f"Du har {spiller} for en total på {beregneTotalSum(spiller)} og dealeren har {dealer} for en total på"
          f" {beregneTotalSum(dealer)}")

    if beregneTotalSum(spiller) == 21:
        print("DU VANT MED BLACKJACK")
        chips += bet_chips * 2

    elif beregneTotalSum(dealer) == 21:
        print("DEALEREN VANT MED BLACKJACK")
        chips -= bet_chips

    elif beregneTotalSum(spiller) > 21:
        print("Du tapte siden du gikk over 21")
        chips -= bet_chips

    elif beregneTotalSum(dealer) > 21:
        print("Dealeren gikk over 21, du vant")
        chips += bet_chips

    elif beregneTotalSum(dealer) > beregneTotalSum(spiller):
        print("Dealeren vant")
        chips -= bet_chips

    elif beregneTotalSum(dealer) < beregneTotalSum(spiller):
        print("Du vant")
        chips += bet_chips

    elif beregneTotalSum(dealer) == beregneTotalSum(spiller):
        print("Det ble likt")
        chips += 0

    print(f"Du har {chips} totalt")

    if chips <= 0:
        print("Du er tom for chips, du må sette inn mer penger")
        break

    if input("\nØnsker du å fortsette\n1 - Ja\n2 - Nei\n") == '2':
        break

print(f"Du er ferdig og har {chips} chipper igjen")