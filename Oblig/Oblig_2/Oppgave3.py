books = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King",
         "The Adventures of Tom Bombadil", "Tree and Leaf"]

print(books[0])
print(books[1])
print(books[-2])
print(books[-1])
print()
books.append("The Silmarillion")
books.append("Unfinished Tales")
print(books)
#Kunne nok gjort dette på en kortere måte

trilogi = "Lord of the Rings: "
for number in range(2, 5):
    books[number] = trilogi + books[number]
    continue
'''Det sto mellom å bruke books[2] = "Lord of the Rings: og så tittel på bok", flere ganger
 men valgte å lage en for-løkke som kun henter ut index 2, 3 og 4'''

print()
print(books)
print()
print()

for liste in books:
    print(liste)
    #skriver ut lista med bøkene