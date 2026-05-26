import streamlit as st

films = [
    {"title": "Hoppers", "genre": ["comedy"], "type": "movie", "duration": "short", "year": "2026"},
    {"title": "Titanic", "genre": ["romance","drama"], "type": "movie", "duration": "long", "year": "1997"},
    {"title": "Zombies", "genre": ["fantasy"], "type": "movie", "duration": "short", "year": "2018"},
    {"title": "Brave citizen", "genre": ["action"], "type": "movie", "duration": "long", "year": "2023"},
    {"title": "Me before you", "genre": ["romance"], "type": "movie", "duration": "long", "year": "2016"},
    {"title": "Barbie", "genre": ["comedy", "fantasy"], "type": "movie", "duration": "long", "year": "2023"},
    {"title": "Parasite", "genre": ["thriller"], "type": "movie", "duration": "long", "year": "2019"},
    {"title": "Exhuma", "genre": ["horror"], "type": "movie", "duration": "long", "year": "2024"},
    {"title": "20th Century girl", "genre": ["romance", "drama"], "type": "movie", "duration": "long", "year": "2022"},
    {"title": "Last Holiday", "genre": ["romance"], "type": "movie", "duration": "long", "year": "2006"},
    {"title": "Dead poets society", "genre": ["drama"], "type": "movie", "duration": "long", "year": "1989"},
    {"title": "10 things I hate about you", "genre": ["romance"], "type": "movie", "duration": "long", "year": "1999"},

    {"title": "Stranger Things", "genre": ["horror"], "type": "series", "duration": "long", "year": "2016", "seasons": 5},
    {"title": "Pursuit of jade", "genre": ["fantasy"], "type": "series", "duration": "long", "year": "2026", "seasons": 1},
    {"title": "9-1-1", "genre": ["action"], "type": "series", "duration": "long", "year": "2018", "seasons": "9"},
    {"title": "The Rookie", "genre": ["action"], "type": "series", "duration": "long", "year": "2019", "seasons": 8},
    {"title": "Taxi Driver", "genre": ["action"], "type": "series", "duration": "long", "year": "2018", "seasons": 3},
    {"title": "Fatma", "genre": ["period", "drama"], "type": "series", "duration": "short", "year": "2026","seasons": 1},
    {"title": "Weak Hero Class", "genre": ["action", "thriller"], "type": "series", "duration": "long", "year": "2022","seasons": 2},
    {"title": "Dear X", "genre": ["thriller"], "type": "series", "duration": "short", "year": "2025","seasons": "1"},
    {"title": "Twinkling Watermelon", "genre": ["fantasy", "romance"], "type": "series", "duration": "long", "year": "2023","seasons": 1},
    {"title": "Alchemy Of Souls", "genre": ["period","fantasy", "romance"], "type": "series", "duration": "long", "year": "2022","seasons": 2},
    {"title": "A Shop for Killers", "genre": ["action", "thriller"], "type": "series", "duration": "short", "year": "2024","seasons": 1},
    {"title": "Welcome to Samdal-ri", "genre": ["romance", "comedy"], "type": "series", "duration": "long", "year": "2023","seasons": 1},
    {"title": "Dr. Romantic", "genre": ["romance", "drama"], "type": "series", "duration": "long", "year": "2016","seasons": 3},
    {"title": "Hometown Cha-Cha-Cha", "genre": ["romance", "comedy"], "type": "series", "duration": "long", "year": "2021","seasons": 1},
]

st.title("🎬 Film Expert System")

genre = st.selectbox("Choose genre", sorted(list({g for f in films for g in f["genre"]})))
type_ = st.radio("Type", ["movie", "series"])
duration = st.radio("Duration", ["short", "long"])
period = st.selectbox("Period", ["old", "modern", "recent"])

def match_year(year, period):
    year = int(year)
    if period == "old":
        return year < 2000
    elif period == "modern":
        return 2000 <= year <= 2015
    else:
        return year > 2015

if st.button("Get Recommendations"):
    results = []

    for film in films:
        if (
            genre in film["genre"] and
            film["type"] == type_ and
            film["duration"] == duration and
            match_year(film["year"], period)
        ):
            results.append(film)

    if results:
        st.subheader("Recommendations")
        for r in results:
            if r["type"] == "series" and "seasons" in r:
                st.write(f"🎥 {r['title']} ({r['seasons']} seasons)")
            else:
                st.write(f"🎬 {r['title']}")
    else:
        st.warning("No match found.")
