cities = {'surakarta': {
    'country': 'indonesia',
    'population': 1000000,
    'fact': 'kota ini dikenal sebagai kota batik'
}, 'berlin': {
    'country': 'jerman',
    'population': 3000000,
    'fact': 'kota ini dikenal sebagai ibu kota jerman'
}, 'tokyo': {
    'country': 'jepang',
    'population': 13000000,
    'fact': 'kota ini dikenal sebagai ibu kota jepang'
}}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: approximately {info['population']:,}")
    print(f"  Fact: {info['fact']}")