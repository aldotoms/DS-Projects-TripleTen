# Capítulo 4/5 · Faltan 2 lecciones - Funciones
#
# Variables globales y locales
# Muy bien, acabas de aprender cómo escribir una función de filtro e imprimir los resultados. 
# Volvamos a las funciones que has escrito:

# función que extrae el año y lo compara
def filtered_by_year(data, year):
    filtered_result []
    for row in data:
        if row[2] > year:
            filtered_result.append(row)
        return filtered_result

# función que imprime solamente el nombre de la película
def print_movie_info(data):
    for movie in data:
        print(movie)

# La función filter_by_year requiere dos parámetros: data y year. 
# En el cuerpo de la función creamos una lista vacía llamada filtered_result (resultado del filtrado). 
# El bucle for recorre las listas anidadas de películas y, si el año de una película es superior al parámetro year, 
# toda la lista anidada se añade a filtered_result. 
# Después, utilizamos la palabra clave return para devolver los resultados del filtrado.

# Y ya conocemos las variables. Además, las utilizamos mucho ahora. 
# Pero algo que aún no hemos abordado son las diferencias entre los distintos tipos de variables. 
# Sí, al igual que los argumentos, las variables también pueden ser diferentes.

# En Python, existen dos tipos de variables, las globales y las locales, que se utilizan para almacenar valores.

# TEORIA
# Al escribir funciones en Python es importante entender la diferencia entre las variables locales y las globales. 
# Las variables locales permiten organizar el código y evitar conflictos de nombres. 
# Las variables globales, en cambio, pueden ser útiles cuando necesitas compartir datos entre diferentes partes de tu código.

# Variables locales
# Las variables locales se definen dentro de una función y pueden accederse únicamente dentro de la misma. 
# Se crean cuando se llama a la función y se destruyen cuando esta termina de ejecutarse. 
# Las variables locales solo se pueden acceder dentro del alcance de la función en la que están definidas. 
# Esto significa que si una variable se define dentro de una función, es imposible acceder a ella fuera de esa función.
# Aquí está nuestra función omelet que utiliza variables locales:

def omelet(cheese, eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    return result

print(omelet(True, 3))

# En este ejemplo, result es una variable local. 
# Se define dentro de la función omelet y solo se puede acceder a ella dentro de esa función. 
# Cuando se llama a omelet, se crea result y se le asigna una cadena. La función devuelve el valor de result. 
# Si intentas imprimirlo desde fuera de la función, se producirá un error NameError: name 'result' is not defined:

def omelet(cheese, eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    return result

omelet(True, 3)
print(result)

# Traceback (most recent call last):
  File "main.py", line 11, in <module>
NameError: name 'result' is not defined


# Variables globales
# En cambio, se puede acceder a las variables globales desde cualquier parte del código, incluso desde dentro de las funciones. 
# Se definen fuera de cualquier función y pueden utilizarse en todo el programa. 
# Se puede acceder a las variables globales y modificarlas desde cualquier parte del programa. 
# Sin embargo, es importante utilizar las variables globales con precaución, ya que pueden dificultar la comprensión y el mantenimiento del código.
# Hagamos un omelet "global" con 50 ml de leche "global":

milk = 50 #declarada como una variable global

def omelet(cheese, eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    result = result + ' y leche (ml): ' + str(milk) #accedemos a la variable global
    print(result)

omelet(True, 3)

# Resultado: ¡El omelet está listo! Huevos utilizados: 3, con queso y leche (ml): 50

# En este ejemplo, milk es una variable global. 
# Está definida fuera de la función omelet, pero podemos acceder a ella desde dentro de la función. 
# La sentencia print dentro de omelet muestra el valor de result, que contiene el valor de milk.


# Uso conjunto de variables locales y globales
# Es posible utilizar variables locales y globales con el mismo nombre dentro de la misma función. 
# En este caso, la variable local tiene prioridad sobre la variable global.

result = '¡El omelet está listo!' #declarada como una variable global

def omelet(cheese, eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    print(result)

omelet(True, 3)
print(result)

# Resultado:
# ¡El omelet está listo! Huevos utilizados: 3, con queso
# ¡El omelet está listo!

# En este ejemplo, la función omelet define la variable local result que tiene prioridad sobre la variable global result. 
# Cuando llamamos a la función omelet, esta devuelve el valor de la variable local result. 
# La sentencia print fuera de la función muestra el valor de la variable global result.

# Al escribir funciones en Python es importante entender la diferencia entre las variables locales y las globales. 
# Las variables locales permiten organizar el código y evitar conflictos de nombres. 
# Las variables globales, en cambio, pueden ser útiles cuando necesitas compartir datos entre diferentes partes de tu código.

# Fin.