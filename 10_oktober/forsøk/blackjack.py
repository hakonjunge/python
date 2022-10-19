import random

spiller_onsker_a_spille = True
spillerIn = True
dealerIn = True
bet = False

kortstokk = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
reshuffle = []
symbol = ['ruter', 'hjerter', 'spar', 'kløver']

spiller = []
dealer = []
chips = 0

start_chips = int(input("Hvor mange chips skal du starte med? "))
chips += start_chips
print(f"\nDu starter med {chips} chips")

while spiller_onsker_a_spille:
    blackjack = False
    spillerIn = True
    dealerIn = True

    if len(kortstokk) < 5:
        kortstokk.extend(reshuffle)
        print("\nKortstokken ble omstokket")

    bet_chips = int(input(f"\nHvor mange chips better du?\nDu har {chips} totalt "))
    while bet_chips <= 0 or bet_chips > chips:
        print("Du kan ikke bette mer enn eller mindre enn du har")
        bet_chips = int(input(f"\nHvor mange chips better du?\nDu har {chips} totalt "))
    else:
        print(f"\nDu har bettet {bet_chips} chipper")


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


    def dealerSinTur():
        if len(dealer) == 2:
            return dealer[0]
        elif len(dealer) > 2:
            return dealer[0], dealer[1]


    for _ in range(2):
        delUtKort(dealer)
        delUtKort(spiller)

    while spillerIn or dealerIn:
        print(f"Dealeren har {dealerSinTur()} og X")
        print(f"Du har:")
        for elm in spiller:
            print(elm)
        print(f"for en total på {beregneTotalSum(spiller)}\n")

        if beregneTotalSum(spiller) == 21:
            break
        if spillerIn:
            ståEllerSlåtil = input("1: Stå\n2: Slå til\n")
        if beregneTotalSum(dealer) > 17:
            dealerIn = False
        else:
            delUtKort(dealer)
        if ståEllerSlåtil == '1':
            spillerIn = False
        else:
            delUtKort(spiller)
        if beregneTotalSum(spiller) >= 21:
            break
        elif beregneTotalSum(dealer) >= 21:
            break

    print()

    if beregneTotalSum(spiller) == 21:
        print(f"Du har {spiller} for en total på {beregneTotalSum(spiller)} og dealeren har {dealer} for en total på"
              f" {beregneTotalSum(dealer)}")
        print("DU VANT MED BLACKJACK")
        chips += bet_chips * 2
        print(f"Du har {chips} totalt")
        blackjack = True

    if beregneTotalSum(dealer) == 21:
        print(f"Dealeren har {dealer} for en total på {beregneTotalSum(dealer)} og du har {spiller} for "
              f"en total på {beregneTotalSum(spiller)}")
        print("DEALEREN VANT MED BLACKJACK")
        chips -= bet_chips
        print(f"Du har {chips} totalt")
        blackjack = True



    elif beregneTotalSum(spiller) > 21 and blackjack is False:
        print(f"Du har {spiller} for en total på {beregneTotalSum(spiller)} og dealeren har {dealer} for en total på"
              f" {beregneTotalSum(dealer)}")
        print("Du tapte siden du gikk over 21")
        chips -= bet_chips
        print(f"Du har {chips} totalt")



    elif beregneTotalSum(dealer) > 21 and blackjack is False:
        print(f"Dealeren har {dealer} for en total på {beregneTotalSum(dealer)} og du har {spiller} for "
              f"en total på {beregneTotalSum(spiller)}")
        print("Dealeren gikk over 21, du vant")
        chips += bet_chips
        print(f"Du har {chips} totalt")



    elif 21 - beregneTotalSum(dealer) < 21 - beregneTotalSum(spiller) and blackjack is False:
        print(f"Dealeren har {dealer} for en total på {beregneTotalSum(dealer)} og du har {spiller} for "
              f"en total på {beregneTotalSum(spiller)}")
        print("Dealeren vant")
        chips -= bet_chips
        print(f"Du har {chips} totalt")


    elif 21 - beregneTotalSum(dealer) > 21 - beregneTotalSum(spiller) and blackjack is False:
        print(f"Du har {spiller} for en total på {beregneTotalSum(spiller)} og dealeren har {dealer} for en total på"
              f" {beregneTotalSum(dealer)}")
        print("Du vant")
        chips += bet_chips
        print(f"Du har {chips} totalt")

    elif beregneTotalSum(dealer) == beregneTotalSum(spiller) and blackjack is False:
        print("Det ble likt")
        chips += 0
        print(f"Du har {chips} totalt")

    spiller = []
    dealer = []
    if chips <= 0:
        break

    fortsette = input("\nØnsker du å fortsette\n1 - Ja\n2 - Nei\n")
    if fortsette == '2':
        spiller_onsker_a_spille = False

if chips <= 0:
    print("Du er tom for chips, du må sette inn mer penger")

print(f"Du er ferdig og har {chips} chipper igjen")
