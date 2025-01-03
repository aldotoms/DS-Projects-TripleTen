# my_func.py
# Combinación de argumentos posicionales y de palabras clave

def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

#trip_price(loc_from='Boston', loc_to='New York', price=5.1, 409, 35)

# Si pasamos primero todos los argumentos posicionales, el script se ejecutará sin errores:
trip_price(409, 35, loc_from='Boston', loc_to='New York', price=5.1)