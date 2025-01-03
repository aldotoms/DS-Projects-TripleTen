# my_func.py
# Argumentos predeterminados

def trip_price(dist_miles, mpg, price, loc_from='A', loc_to='B'):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, price=3.8)