import random

scoringboard = []
print("*Dart Spill 2*")

players = int(input("Antall spillere: "))
attempts = int(input("Antall runder: "))
numbers = [x * i for x in range(1, 21) for i in range(1, 4)] + [0, 25, 50]
#her er nesten alt likt bortsett fra at jeg lagde en one-liner for å bestemme hvilke poeng-range man skal få
round_count = 1
print()
print("Resultat:")
for points in range(players):
    tilfeldig = random.sample((numbers), attempts)
    #henter poeng fra numbers-variablen og kjører det så mange ganger som man bestemte i attempts-inputen
    print(f"Spiller {round_count}: {tilfeldig}")
    scoringboard.append(tilfeldig)
    round_count += 1

print()
print("Resultat:")
sumboard = [sum(res) for res in scoringboard]
print(f"Vinneren er spiller {sumboard.index(max(sumboard)) + 1} med {max(sumboard)} poeng.")
