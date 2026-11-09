from exercise_11_01_function import city_country

def test_city_country():
    """Apakah kota dan negara seperti 'Santiago, Chile' berfungsi?"""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'