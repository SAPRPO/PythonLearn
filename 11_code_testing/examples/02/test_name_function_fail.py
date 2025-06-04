from name_function_updated import get_formatted_name

def test_first_last_name(): #name from test_!!!!
    """support names 'Jaa Kaa'?"""
    formatted_name = get_formatted_name('laa','jaa')
    assert formatted_name == 'Laa Jaa'

def test_first_middle_last_name(): #name from test_!!!!
    """support names 'Wolfgang Amadeus Mozart'?"""
    formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
