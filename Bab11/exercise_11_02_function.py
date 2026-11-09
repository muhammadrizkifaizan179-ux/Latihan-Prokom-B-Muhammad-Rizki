def get_city_country(city, country, population):
    return f"{city.title()}, {country.title()} - population {population}"

def get_city_country(city, country, population=''):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"