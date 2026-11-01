orang = [
    {
        'first_name': 'Briliant',
        'last_name': 'Ghani',
        'age': 90,
        'city': 'magelang',
        'favorite_places': ['solo', 'magelang'],
        'hobby': ['reading', 'playing games'],
    },
    {
        'first_name': 'muhammad',
        'last_name': 'daffa',
        'age': 100,
        'city': 'surakarta',
        'favorite_places': ['solo', 'UNS'],
        'hobby': ['jogging', 'swimming'],
    },
    {
        'first_name': 'Muhammad',            # ganti dengan orang ketiga
        'last_name': 'Rizki',
        'age': 20,
        'city': 'kota',
        'favorite_places': ['Batam', 'Sumber'],
        'hobby': ['reading', 'gym'],
    },
]
for person in orang:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"=== {full_name} ===")
    print(f"Age             : {person['age']}")
    print(f"City            : {person['city'].title()}")
    print(f"Favorite places : {', '.join(person['favorite_places'])}")
    print(f"Hobby           : {', '.join(person['hobby'])}")
    print()