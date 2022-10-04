import random

print(""*10+"\nDART-SPILL\n"+""*10)
players = int(input("Antall spillere: "))

scoringboard = [random.sample(range(0, 60), 3) for tall in range(players)]
print("\nResultat:")
for player in range(players):
    print(f"player {player+1}, {scoringboard[player]}")


print("\nScoringboard:")
sumboard = [sum(res) for res in scoringboard]
print(f"Vinneren er player {sumboard.index(max(sumboard))+1} med {max(sumboard)} poeng.")


'''
el Plan:
Ha to lister, en liste for
'''
'''import random
scoringboard = []

print("************")
print("*DART-SPILL*")
print("************")

i = 301
o = 1
list1_20 = range(1, 20)
list25_50 = [0, 25, 50]
print()
print("Resultat:")
start = random.randint(0, 1)
if start == 1:
    tilfeldig = random.choice(list1_20)
    verdi = random.randrange(1, 4)
    forste_forsok = verdi*tilfeldig
    i -= forste_forsok
    print(f"Kast {o}: {tilfeldig} * {verdi} = {forste_forsok}")
    print(i)
    o += 1
    if verdi == 2:
        while i > 0:
            tilfeldig = random.randint(0, 20)
            tilfeldig2 = random.randint(1, 3)
            kast = tilfeldig2 * tilfeldig
            print(f"Kast {o}: {tilfeldig} * {tilfeldig2} = {kast}")
            scoringboard.append(tilfeldig)
            i -= kast
            o += 1
            print(i)
else:
    print("feil")'''