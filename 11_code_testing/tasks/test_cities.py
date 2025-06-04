from city_functions import get_city_country

def test_city_country():
    result = get_city_country('amsterdam','holland')
    assert result == 'Amsterdam, Holland'

def test_city_country_population():
    result = get_city_country('amsterdam','holland', '1100000')
    assert result == 'Amsterdam, Holland - Population 1100000'