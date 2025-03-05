cities={'Moscow':  
        { 'country': 'Russia',
         'population': 12000000,
         'fact': 'Moscow is the capital of Russia',
                    }
        , 'Minsk':  
        { 'country': 'Belarus',
         'population': 1900000,
         'fact': 'Minsk is the capital of Belarus',

                    }
        , 'Riga': {
            'country': 'Latvia',
            'population': 700000,
            'fact': 'Riga is the capital of Latvia',
                    }
        }
for city_name, city_info in cities.items():
    print(f"{city_name} is located in {city_info['country']} and has population of {city_info['population']}. {city_info['fact']}")