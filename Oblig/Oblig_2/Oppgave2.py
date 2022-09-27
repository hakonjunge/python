print("Dette er en while-løkke")
i = 9
while i <= 101:
    if (i % 2) != 0:
        print(i)
    i += 1
print()
#en while løkke kan gå evig, derfor setter vi en sluttverdi, her brukte jeg "i<=101" som sluttverdi

print("Nå starter for-løkka")
for tall in range(9, 102, 2):
    print(tall)
    #en for-løkke brukes når man vet hvor lenge det skal loope