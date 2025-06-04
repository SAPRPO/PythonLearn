from name_function import get_formatted_name

def test_first_last_name(): #name from test_!!!!
    """support names 'Jaa Kaa'?"""
    formatted_name = get_formatted_name('laa','jaa')
    assert formatted_name == 'Laa Jaa'