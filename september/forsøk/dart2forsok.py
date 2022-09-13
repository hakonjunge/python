import random
scoringboard = []
print("*Dart Spill 2*")

players = int(input("Antall spillere: "))
attempts = int(input("Antall runder: "))
numbers = [x * i for x in range(1, 21) for i in range(1, 4)] + [0, 25, 50]
round_count = 1
print()
print("Resultat:")
for tall in range(players):
    tilfeldig = random.sample((numbers), attempts)
    print(f"Spiller {round_count}: {tilfeldig}")
    scoringboard.append(tilfeldig)
    round_count += 1

print()
print("Resultat:")
sumboard = [sum(res) for res in scoringboard]
print(f"Vinneren er spiller {sumboard.index(max(sumboard))+1} med {max(sumboard)} poeng.")