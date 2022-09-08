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