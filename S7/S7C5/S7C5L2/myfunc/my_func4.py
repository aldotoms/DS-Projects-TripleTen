# my_func.py
# argumentos posicionales

def trip_price(dist_miles, mpg, price, loc_from, loc_to):
        total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, 5.1, 'A', 'B')