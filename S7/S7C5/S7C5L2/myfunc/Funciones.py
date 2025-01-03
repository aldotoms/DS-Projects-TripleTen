# Funciones
# En el curso de Python básico aprendiste sobre las funciones de Python. Esta lección tiene dos objetivos:

# Recapitular conceptos básicos relacionados con funciones, tales como el alcance de las variables y los diferentes tipos de argumentos.
# Introducir el concepto de sugerencias de tipo, su propósito y uso

# Resumen de funciones
# Alcance de la variable
# El alcance de una variable es el área dentro de un programa donde se puede acceder a la misma. Hay tres alcances a tener en cuenta cuando codificamos en Python:

# Alcance local: si haces referencia a una variable dentro de una función, el intérprete buscará primero el nombre de esa variable dentro de la definición de esa función.
# Alcance global: si el intérprete no encuentra la variable dentro del alcance local, la buscará en el alcance global (es decir, en otras partes del programa fuera de las funciones).
# Alcance integrado: por último, si el intérprete no encuentra la variable ni en el ámbito local ni en el global, la buscará en el ámbito integrado de Python.
# Veamos algunos ejemplos de cada tipo de alcance.

# Alcance local
# Vamos a crear un script que incluya una función con algunas variables:

# my_func.py
product_price = 12.0
product_qty = 5

def total_price():
    product_price = 11.0
    product_qty = 4
    print(f'Precio total: {product_price * product_qty}')

total_price()


# Observa que hay variables product_price y product_qty tanto dentro como fuera de la función. Al ejecutar un script, el intérprete utiliza los valores product_price y product_qty del alcance local (dentro de la función), aunque estas variables también existen en el alcance global (fuera de la función).

# Alcance global

# my_func.py
product_price = 12.0
product_qty = 5

def total_price():
    print(f'Precio total: {product_price * product_qty}')

total_price()

# Las variables product_price y product_qty no están definidas en el alcance local de la función, por lo que el intérprete pasa al alcance global de my_func.py para encontrarlas.

# Alcance integrado

# my_func.py
product_price = 12.0
product_qty = 5

def total_price():
    print(f'Precio total: {price * qty}')

total_price()

# Ni price ni qty existen en el alcance integrado, global o local, por lo que el intérprete lanza un error. La documentación de Python contiene las listas completas de nombres para las funciones integradas y las constantes integradas.

# Para evitar problemas de alcance en tu código, es una buena práctica escribir funciones que no dependan de variables definidas fuera de la función. Si tu función necesita usar una variable que no es su parámetro, intenta crear la variable dentro del cuerpo de esta función.

# Tipos de argumentos de función
# Argumentos posicionales
# Los argumentos posicionales son argumentos de una función que deben pasarse en un orden específico. Al llamar a una función definida con argumentos posicionales, debemos pasar los valores de los argumentos exactamente en el mismo orden en que se definieron.

# my_func.py
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
        total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, 5.1, 'A', 'B')

# De lo contrario, obtendremos un error o, según la definición y el uso de la función, un valor de retorno incorrecto. En el ejemplo anterior, 409 es dist_miles, 35 es mpg y 5.1 es el price.

# Si cambiamos el orden, es muy probable que encontremos un error.

# my_func.py
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price('A', 'B', 409, 35, 5.1)


## Argumentos de palabras clave

# Podemos llamar a una función con argumentos de palabras clave. En este caso, debemos pasar los nombres de los argumentos junto con sus valores. Esto nos obliga a escribir un poco más de código a la hora de llamar a una función, pero también nos da la flexibilidad de pasar los argumentos en el orden que queramos.

# my_func.py
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(dist_miles=409, loc_from='A', loc_to='B', mpg=35, price=5.1)

# Observa cómo llamamos a la función:

trip_price(dist_miles=409, loc_from='A', loc_to='B', mpg=35, price=5.1)

# Ahora tiene un argumento y su valor correspondiente junto a él.

# Combinación de argumentos posicionales y de palabras clave
# Podemos combinar los argumentos posicionales y de palabras clave al llamar a una función, siempre que empecemos primero por los argumentos posicionales.

# Si anteponemos un argumento de palabra clave a un argumento posicional, se producirá un SyntaxError:

# my_func.py
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(loc_from='Boston', loc_to='New York', price=5.1, 409, 35)

# Si pasamos primero todos los argumentos posicionales, el script se ejecutará sin errores:

# my_func.py
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, loc_from='Boston', loc_to='New York', price=5.1)

# Argumentos predeterminados

# Podemos establecer valores por defecto para cualquiera de los parámetros al definir nuestra función. Estos valores por defecto se utilizarán si llamamos a la función sin pasarle argumentos para esos parámetros.

# my_func.py
def trip_price(dist_miles, mpg, price, loc_from='A', loc_to='B'):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, price=3.8)

# Ten en cuenta que cuando definimos una función con parámetros cuyos valores están predeterminados, tenemos que poner todos ellos después de los parámetros que no tienen valores predeterminados en la definición de nuestra función; de lo contrario, se producirá un error:

# my_func.py
def trip_price(loc_to='B', dist_miles, mpg, price, loc_from='A'):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(409, 35, price=3.8)

# Pregunta
# ¿Qué hará el intérprete a continuación si la implementación de una función usa variables que no están presentes en el alcance local?
# R.Buscará estos nombres de variables en el alcance global.

# ¿Cuál de estas opciones no producirá ningún error al llamar a una función en Python?
# R.Pasar argumentos de palabra clave en cualquier orden.
# Sí, no dará como resultado un error. Podemos pasar argumentos de palabras clave como queramos.

# Fin.