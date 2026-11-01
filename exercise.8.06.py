def city_country(city, country='Indonesia'):
    """Return a string in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"

print(city_country('jakarta'))
print(city_country('bandung'))
print(city_country('berlin', country='germany'))