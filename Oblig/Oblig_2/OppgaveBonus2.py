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
