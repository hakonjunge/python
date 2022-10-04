'''
file = open("txt/Heisenberg.txt")
print(file.read())
file.close()

print(file.read())
'''

try:
    with open("txt/Heisenberg.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("LEMAO FILÅ FINNS IKKJE")

with open("txt/Heisenberg.txt") as file:
    print(file.readline().rstrip())
    print(file.readline())

with open("txt/my_novel.txt", "w") as file:
    user_input = input(": heihei")
    file.write(user_input)

