from exercise_11_02_function import get_city_country


def test_city_country():
    result = get_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'


def test_city_country_population():
    result = get_city_country('santiago', 'chile', population=5000000)
    assert result == 'Santiago, Chile - population 5000000'