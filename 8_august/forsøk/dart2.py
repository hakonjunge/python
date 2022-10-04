import random
print("**************")
print("*DART-SPILL 2*")
print("**************")
i = 1
umulig = [23, 29, 31, 35, 37, 41, 43, 44, 46, 47, 49, 52, 53, 55, 56, 58, 59]
scoringboard = []
players = int(input("Hvor mange skal spille? "))
arrow = int(input("Hvor mange kast skal alle kaste? 3"))
print()
print("Resultat:")
for tall in range(players):
    tilfeldig = random.sample(range(0, 60), arrow)
    print(f"Spiller {i}: {tilfeldig}")
    scoringboard.append(tilfeldig)
    i += 1
print()
print("Resultat:")
sumboard = [sum(res) for res in scoringboard]
print(f"Vinneren er spiller {sumboard.index(max(sumboard))+1} med {max(sumboard)} poeng.")
