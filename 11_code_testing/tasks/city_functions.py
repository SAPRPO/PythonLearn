def get_city_country(city, country, population=''):
    if population:
        full_string = f"{city}, {country} - population {population}"
    else:
        full_string = f"{city}, {country}"
    return full_string.title()

