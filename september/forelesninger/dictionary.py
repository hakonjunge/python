movie = {'title': 'Lord of The Rings: The Fellowship of the Ring',
         'year': 2001,
         'duration': 178,
         'score': 8.8
}
print(movie['title'])
movie['director'] = 'Peter Jackson'
print()
print(f"{movie.get('title')} was directed by {movie.get('director')} and has a IMBD score of {movie.get('score')}")
for key, value in movie.items():
    print(f"{key} - {value}")