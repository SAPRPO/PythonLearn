def describe_city(city, country='Canada'):
    print(f'{city.title()} is situated in {country}')

describe_city('toronto')
describe_city('montreal')
describe_city('vancouver')
describe_city(city='washington', country='USA')