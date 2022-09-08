import random
print("************")
print("*DART-SPILL*")
print("************")
i = 1
scoringboard = []
players = int(input("Hvor mange skal spille? "))
print()
print("Resultat:")
for tall in range(players):
    tilfeldig = random.sample(range(0, 60), 3)
    print(f"Spiller {i}: {tilfeldig}")
    scoringboard.append(tilfeldig)
    i += 1
print()
print("Resultat:")
sumboard = [sum(res) for res in scoringboard]
print(f"Vinneren er spiller {sumboard.index(max(sumboard))+1} med {max(sumboard)} poeng.")
