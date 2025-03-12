def auto(car, model, **car_info):
    car_info['car_vendor'] = car
    car_info['model'] = model
    return car_info

auto1 = auto('Ford', 'Focus', year = 2017, price = 20000)
print(auto1)

auto2 = auto('Toyota', 'Camry', year = 2018, tow_package = True)
print(auto2)

