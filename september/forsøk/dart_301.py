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
import random

print("*****")
print("*301*")
print("*****")

players = [301 for p in range(int(input("Antall spillere: ")))]
numbers = [x * i for x in range(1, 21) for i in range(1, 4)] + [25, 50, 0]

gameOver = False
round_count = 1

while not gameOver:
    print(f"round: {round_count}")
    for points in range(len(players)):
        tilfeldig = random.randrange(len(numbers))
        if players[points] == 301:
            if tilfeldig % 3 == 1 and not numbers[tilfeldig] in [0, 25, 50]:
                players[points] -= numbers[tilfeldig]
        elif players[points] - numbers[tilfeldig] == 0:
            if tilfeldig % 3 == 1 and not numbers[tilfeldig] in [0, 25, 50]:
                players[points] -= numbers[tilfeldig]
                gameOver = True
                break
        elif players[points] - numbers[tilfeldig] < 0 or players[points] - numbers[tilfeldig] == 1:
            continue
        else:
            players[points] -= numbers[tilfeldig]
    print(players, end="\n\n")
    round_count += 1
print(f"Vinneren er spiller {players.index(0) + 1}.")
