films = [
    {"title": "Hoppers", "genre": "comedy", "type": "movie", "duration": "short", "year": "2026"},
    {"title": "Titanic", "genre": "romance", "type": "movie", "duration": "long", "year": "1997"},
    {"title": "Zombies", "genre": "fantasy", "type": "movie", "duration": "short", "year": "2018"},
    {"title": "Brave citizen", "genre": "action", "type": "movie", "duration": "long", "year": "2023"} ,  
    {"title": "Me before you", "genre": "romance", "type": "movie", "duration": "long", "year": "2016"},
    {"title": "Barbie", "genre": "comedy", "type": "movie", "duration": "long", "year": "2023"}, 
    {"title": "Parasite", "genre": "thriller", "type": "movie", "duration": "long", "year": "2019"},
    {"title": "Exhuma", "genre": "horror", "type": "movie", "duration": "long", "year": "2024"},
    {"title": "20th Century girl", "genre": "romance", "type": "movie", "duration": "long", "year": "2022"},
    {"title": "holiday", "genre": "romance", "type": "movie", "duration": "long", "year": "2006"},
    {"title": "Dead poets society", "genre": "drama", "type": "movie", "duration": "long", "year": "1989"},
    {"title": "10 things I hate about you", "genre": "romance", "type": "movie", "duration": "long", "year": "1999"},
    {"title": "Stranger Things", "genre": "horror", "type": "series", "duration": "long", "year": "2016"},
    {"title": "Pursuit of jade", "genre": "fantasy", "type": "series", "duration": "long", "year": "2026"},
    {"title": "9-1-1", "genre": "Action", "type": "series", "duration": "long", "year": "2018"},
    {"title": "The rookie", "genre": "Action", "type": "series", "duration": "long", "year": "2019"},
    {"title": "Taxi driver", "genre": "Action", "type": "series", "duration": "long", "year": "2018"},
    {"title": "Fatma", "genre": "Drama", "type": "series", "duration": "short", "year": "2026"},
    {"title": "weak hero class", "genre": "Action", "type": "series", "duration": "long", "year": "2022"},
]
    
print(" Welcome to the Film Expert System\n")

# User input
genre = input("Choose a genre (action, comedy, romance, horror, drama, fantasy, thriller): ").lower()
type_ = input("Movie or series: ").lower()
duration = input("Duration (short, long): ").lower()
period = input("Choose period (old / modern / recent): ").lower()

results = []

#rules
for film in films:
    film_year = int(film["year"])

    #  Year classification
    if period == "old" and film_year < 2000:
        match_year = True
    elif period == "modern" and 2000 <= film_year <= 2015:
        match_year = True
    elif period == "recent" and film_year > 2015:
        match_year = True
    else:
        match_year = False

    # Final rule combination
    if (film["genre"].lower() == genre and
        film["type"].lower() == type_ and
        film["duration"].lower() == duration and
        match_year):
        results.append(film["title"])

# Output
if results:
    print("\n Recommendation:")
    for r in results:
        print("-", r)
else:
    print("\n No exact match found.")