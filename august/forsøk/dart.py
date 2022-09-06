'''print("************")
print("*DART-SPILL*")
print("************")
scoringboard = []
players = int(input("Hvor mange skal spille?"))
print()
print("Resultat:")
for tall in range(players):
    import random
    tilfeldig = random.sample(range(0, 60), 3)
    print(tilfeldig)
    scoringboard.append(tilfeldig)
print()
print("Scoringboard:")
for liste in scoringboard:
    print(liste)
print("Vinneren er ")'''
