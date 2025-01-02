# Capítulo 4/5 Funciones
#
# Uso de funciones para simplificar el código
# Funciones definidas por el usuario en la práctica
# Ahora que conoces la teoría que hay detrás de la creación de tus propias funciones destinadas a facilitar la lectura de tu código 
# y eliminar repeticiones en el mismo, es hora de ponerla en práctica. 
# Al final de esta lección, serás capaz de utilizar funciones para optimizar tu código.

# Teoria

# A continuación, vamos a estudiar un caso que utilizaremos a lo largo de esta lección. 
# Una tienda virtual necesita escribir un programa que automatice los descuentos. 
# Si un usuario gasta más de cien dólares en comprar un producto determinado, recibirá un descuento del 5% en ese producto.
# Dos variables describen cada elemento del pedido:

[number]_item_price es el precio del artículo.
[number]_item_quantity es la cantidad.

# Digamos que hay tres artículos en el carrito de un usuario.

first_item_price = 10.0
first_item_quantity = 3 

second_item_price = 51.0
second_item_quantity = 2 # El total suma más de $100. Descuento aplicado

third_item_price = 4.0
third_item_quantity = 10

# Primero, vamos a hacer este ejercicio sin crear una función.

# Sin una función definida por el usuario
# Para cada artículo del carrito:
#   - Encuentra el total.
#   - En una sentencia condicional, compara el total con 100.
#   - Si el total es superior a 100, resta el 5% del total.
# Este es el programa resultante:

first_item_price = 10.0
first_item_quantity = 3

second_item_price = 51.0
second_item_quantity = 2

third_item_price = 4.0
third_item_quantity = 10

# encuentra el total para el primer elemento
first_item_total = first_item_quantity * first_item_price
if first_item_total > 100: # si es superior a 100,
    first_item_total -= first_item_total * 0.05 # entonces resta el 5 %
print(first_item_total)

# encuentra el total del segundo artículo
second_item_total = second_item_quantity * second_item_price 
if second_item_total > 100: # si es superior a 100,
    second_item_total -= second_item_total * 0.05 # entonces resta el 5 %
print(second_item_total)

# encuentra el total del tercer artículo
third_item_total = third_item_quantity * third_item_price
if third_item_total > 100: # si es superior a 100,
    third_item_total -= third_item_total * 0.05 # entonces resta el 5 %
print(third_item_total)


# Teoria
# En un código perfecto se eliminan las repeticiones innecesarias. 
# Cuando las mismas instrucciones aparecen varias veces en el código, cada una de ellas debe tener su propia función. 
# En lugar de repetir todo el bloque de instrucciones, basta con llamar a esa función.

# En el algoritmo de descuento del 5%, las variables cambian, pero los cálculos siguen siendo los mismos. En una función definida por el usuario:
# - Las variables se convertirán en parámetros.
# - Las instrucciones de cálculo se convertirán en el cuerpo.

# Con una función definida por el usuario
# Vamos a crear una función:
#   1.- que contenga dos parámetros: el precio y la cantidad del artículo;
#   2.- en cuyo cuerpo:
#       - se calcule el precio total del artículo en el carrito;
#       - el total se compare con 100 en una sentencia condicional;
#       - se reste el 5 % si el total es superior a 100;
#   3.- que devuelva el total.

# Dеfine la función con dos parámetros: precio y cantidad
def calculate_total_price(price, quantity):
    total = price * quantity # calcula el total del artículo en el carrito
    if total > 100: # compara el total con 100
        total -= total * 0.05 # si el total es superior a 100, resta el 5 %
    return total # devuelve el total

first_item_quantity = 3
first_item_price = 10.0

second_item_quantity = 2
second_item_price = 51.0

third_item_quantity = 10
third_item_price = 4.0

# Llama a la función tres veces.
# Almacena el resultado de cada llamada en una variable.
first_item_total = calculate_total_price(first_item_price, first_item_quantity)
second_item_total = calculate_total_price(second_item_price, second_item_quantity)
third_item_total = calculate_total_price(third_item_price, third_item_quantity)

print(first_item_total)
print(second_item_total)
print(third_item_total)

# Resultado
# 30.0
# 96.9
# 40.0

# Ahora, en lugar de repetir largos segmentos de código, simplemente llamamos a la función y le pasamos los argumentos entre paréntesis. 
# El código es ahora más corto y claro.

# Al igual que con las variables, los nombres de función se escriben utilizando minúsculas y un guion bajo para separar palabras, 
# o en snake_case (por ejemplo, calculate_total_price).

# Fin.