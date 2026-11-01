favorite_places = {
    'Rizki': ['Candi Prambanan', 'Pantai Parangtritis'],
    'Briliant': ['Bali'],
    'Daffa': ['Gunung Bromo', 'Malioboro', 'Dieng'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")