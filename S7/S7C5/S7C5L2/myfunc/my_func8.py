# my_func.py
# Ten en cuenta que cuando definimos una función con parámetros cuyos valores están predeterminados, tenemos que poner todos ellos después de los parámetros que no tienen valores predeterminados en la definición de nuestra función; de lo contrario, se producirá un error:

def trip_price(loc_to='B', dist_miles, mpg, price, loc_from='A'):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, price=3.8)