# Capítulo 3/5
# Aprender Python más a fondo

## Funciones: parámetros y valores predeterminados

# Muy bien, acabas de aprender cómo recorrer diccionarios en bucle, cómo crear estructuras anidadas utilizando diccionarios y cómo procesarlos. 
# Es hora de profundizar en las funciones y aprender algunas técnicas más emocionantes y potentes que las utilizan.
# En el segundo sprint, escribiste una función de filtro e imprimiste los resultados. Recapitulemos y veamos de nuevo las funciones que escribiste:

# función que extrae el año y lo compara
def filter_by_year(data, year):
    filtered_result = []
    for row in data:
        if row[2] > year:
            filtered_result.append(row)
    return filtered_result

# función que imprime solamente el nombre de la película
def print_movie_info(data):
    for movie in data:
        print(movie)

# La función filter_by_year requiere dos parámetros: data y year. En el cuerpo de la función creamos una lista vacía llamada filtered_result (resultado del filtrado). 
# El bucle for recorre las listas anidadas de películas, y si el año de una película es superior al parámetro year, toda la lista anidada se añade a filtered_result. 
# Después, utilizamos la palabra clave return para devolver los resultados del filtrado.
# Ahora es el momento de ver cómo puedes utilizar los valores por defecto de los parámetros para mejorar tus funciones. 
# Recuerda que el parámetro es lo que pasamos entre los paréntesis de una función cuando la creamos. Ya hemos mencionado que en la función anterior filter_by_year hay dos parámetros: data y year.
# Para empezar con los valores predeterminados de los parámetros, vamos a intentar ejecutar de nuevo la función omelet que escribimos en uno de los sprints anteriores. 
# Como siempre, primero examina el código y luego ejecútalo.

# Código
def omelet(eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    return result

print(omelet())

# ¡Error! Verás, es necesario pasar un argumento para eggs_number. Sin él, la función no puede convertir eggs_number en una cadena al llamar a  str().
# Si no queremos que esto ocurra, tenemos que proporcionar un valor de parámetro predeterminado al definir la función. 
# Al final de esta lección, serás capaz de hacerlo.

# Valores predeterminados de los parámetros
# Mira el video a continuación, ¡pero no olvides continuar leyendo para obtener una comprensión sólida de este tema!
# https://www.youtube.com/watch?time_continue=98&v=8awzQgjxMnQ&embeds_referring_euri=https%3A%2F%2Ftripleten.com%2F&embeds_referring_origin=https%3A%2F%2Ftripleten.com&source_ve_path=MTM5MTE3LDI4NjY2


# Imagina que estás en una cafetería y te pides un omelet, ¿crees que el camarero se confundirá si no especificas cuántos huevos quieres? Lo más probable es que te tomen el pedido con un número "estándar" de huevos. Esto es lo mismo que un parámetro por defecto.
# Así es como podemos agregar un valor predeterminado a este parámetro para nuestro código:

# añade un valor por defecto para eggs_number al parámetro
def omelet(eggs_number=2):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    return result

print(omelet())

# Al definir una función, puedes establecer un valor por defecto para cualquier parámetro utilizando =. En este ejemplo, hemos escrito eggs_number=2.
# Los parámetros con valores predeterminados también se denominan parámetros opcionales. Si no especificas su valor al llamar a la función se utilizarán los valores predeterminados.

# ¡Importante!
# Al definir una función, los parámetros opcionales deben ir después de los obligatorios, aquellos que no tienen un valor por defecto asignado. En caso contrario, obtendrás un error cuando llames a la función.

# Veamos cómo debería ser en el ejemplo siguiente, que tiene dos parámetros:
#   - cheese (queso), que es un parámetro obligatorio.
#   - eggs_number (número de huevos), que es un parámetro opcional. Tiene un valor predeterminado de 2.

# Código
# añade un valor por defecto para eggs_number al parámetro
def omelet(cheese, eggs_number=2):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    if cheese == True:
        result = result + ', con queso'
    else:
        result = result + ', sin queso'
    return result

print(omelet(False))

# Siempre tendrás que decir si quieres queso o no, ya que es un parámetro obligatorio, pero si no indicas cuántos huevos quieres, ¡serán dos! 
# ¡Llegó el momento de practicar!

# Volvamos a nuestro ejemplo de las películas. Ahora, tienes como objetivo escribir una función, filter_by_genre(), con dos parámetros:
#   - genre=: el nombre del género, por defecto 'drama'.
#   - data=: datos sobre las películas, sin valor por defecto.
# La función debe devolver una lista de listas que solamente contengan películas con el género pasado en el parámetro genre=.

# Código
# esta función imprime las tablas filtradas. No modificar
# esta función imprime la tabla filtrada

def print_movie_info(data):
    for movie in data:
        print(movie)


def filter_by_genre(data, genre='drama'):
    filtered_result = []
    for row in data:
        if genre in row[3]:
            filtered_result.append(row)
    return filtered_result


movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

movies_filtered = filter_by_genre(movies_info)
print_movie_info(movies_filtered)

# FIN.