old_list = ['The Hobbit', 'Farmer Giles of Ham', 'Lord of the Rings: The Fellowship of the Ring',
            'Lord of the Rings: The Two Towers', 'Lord of the Rings: The Return of the King',
            'The Adventures of Tom Bombadil', 'Tree and Leaf', 'The Silmarillion', 'Unfinished Tales']
new_list = old_list[2:5]
print(new_list)
print()
books_not_lotr = []
for movies in old_list:
    if "Lord of the Rings: " in movies:
        print(movies)
print()
for books in old_list:
    if "Lord of the Rings: " not in books:
        books_not_lotr.append(books)
        print(books)
