# Capítulo 4/5 Funciones

# Ejercicio
# ¡Ahora te toca a ti probarlo! ¡Practiquemos!
# El siguiente fragmento de código contiene operaciones repetitivas. En concreto, calcula el total multiplicando el número de artículos por su precio.
# Podemos hacer un 10% de descuento si la cantidad es superior a 5. Para ello, multiplicamos el total por 0.9. 

# Calcula el total para el primer artículo
item_total_1 = item_price_1 * item_quantity_1

# Aplica el descuento del 10% si la cantidad es superior a 5
if item_quantity_1 > 5:
    item_total_1 *= 0.9

# Calcula el total para el segundo artículo
item_total_2 = item_price_2 * item_quantity_2

# Aplica el descuento del 10% si la cantidad es superior a 5
if item_quantity_2 > 5:
    item_total_2 *= 0.9

# Calcula el total para el tercer artículo
item_total_3 = item_price_3 * item_quantity_3

# Aplica el descuento del 10% si la cantidad es superior a 5
if item_quantity_3 > 5:
    item_total_3 *= 0.9


# Tu objetivo es escribir una función llamada calculate_total_price que puede eliminar la redundancia y utilizarse en los tres casos expuestos abajo.

def calculate_total_price(price, quantity):
    total = price * quantity
    if quantity > 5:
        total *= 0.9
    return total


item_price_1 = 20.0
item_quantity_1 = 20

item_price_2 = 30.0
item_quantity_2 = 1

item_price_3 = 10.0
item_quantity_3 = 6


item_total_1 = calculate_total_price(item_price_1, item_quantity_1)
item_total_2 = calculate_total_price(item_price_2, item_quantity_2)
item_total_3 = calculate_total_price(item_price_3, item_quantity_3)

print(item_total_1)
print(item_total_2)
print(item_total_3)

# Resultado
# 360.0
# 30.0
# 54.0

# En la próxima lección, aprenderás a filtrar funciones.
# Fin.