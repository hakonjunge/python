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
    tilfeldig = random.sample(range(0, 61), 3)
    #bruker random.sample(range) fordi det gir meg mulighet å hente ut 3 tilfeldige tall samtidig
    totale_poeng = sum(tilfeldig) #Får regnet ut total
    print(f"Spiller {i}: {tilfeldig}"+f" = {totale_poeng}")
    scoringboard.append(tilfeldig)
    i += 1
print()
print("Resultat:")
sumboard = [sum(res) for res in scoringboard]
print(f"Vinneren er spiller {sumboard.index(max(sumboard))+1} med {max(sumboard)} poeng.")
#Får skrevet ut hvem som vinner ved hjelp av max() og index på den som vant
