# Capítulo 4/5 · Faltan 3 lecciones - Funciones
#
# Funciones de filtro
# Ahora que tu código tiene un aspecto estupendo, es hora de ver qué otro uso puedes dar a tus funciones.

# Funciones de filtro
# Ahora que tu código tiene un aspecto estupendo, es hora de ver qué otro uso puedes dar a tus funciones.
# Anteriormente, en el primer sprint, utilizaste el bucle for y las sentencias condicionales con el fin de crear un filtro para tu tabla de películas. 
# Este filtro tenía que devolver películas con una duración superior a 180 min:

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

movies_filtered = [] # Lista vacia para almacenar el resultado

for movie in movies_info: # recorre en bucle las filas de la tabla original
    if movie[4] > 180: # si una película dura más de 180 minutos
        movies_filtered.append(movie) # agrega la fila a movies_filtered

for movie in movies_filtered: # muestra el contenido de movies_filtered
    print(movie)

# El resultado:
["Schindler's List", 'USA', 1993, 'drama', 195, 8.818]
['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625]

# Vamos a mejorar nuestra solución con la ayuda de las funciones. Para ello, podemos tomar fragmentos de código, como el de arriba, y crear una función que sirva para cualquier consulta, no para una sola.
# Vamos a hacer que nuestro código sea más simple y flexible, para que podamos manejar toneladas de consultas en el futuro sin tener que copiar y pegar o reescribir nada.
# Dividiremos el código en bloques lógicos y crearemos dos funciones:
# 1) Una para filtrar las películas.
# 2) Otra para imprimir los nombres de las películas que obtuvimos después de filtrar.

# función que devuelve una copia filtrada de una lista anidada
def filter_by_timing(data, target_duration): 
    filtered_result = []
    for row in data:
        if row[4] > target_duration:
            filtered_result.append(row)
    return filtered_result 
# devuelve los resultados filtrados

# esta función acepta la lista anidada como entrada y la muestra, sin devolver nada
def print_movie_info(data):
    for movie in data:
        print(movie)

# llamemos a la función sobre movies_info:

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

movies_filtered = filter_by_timing(movies_info, 180)
print_movie_info(movies_filtered)

# Resultado
["Schindler's List", 'USA', 1993, 'drama', 195, 8.818]
['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625]

# ¡Nuestras funciones han cumplido su objetivo según lo previsto! 
# Ahora podemos reutilizar este código para filtrar la tabla de películas de la forma que queramos e imprimirla. 
# ¡Este código versátil nos ofrece infinitas posibilidades!
# Estas funciones también han facilitado la lectura del código. ¡Ahora es el momento de practicar!


# EJERCICIOS
#
# Ejercicio 1
# En el precódigo, encontrarás las funciones que hemos creado en esta lección para filtrar y mostrar el resultado. 
# Utiliza estas funciones para filtrar las películas de más de 140 minutos de duración e imprimir el resultado.

def filter_by_timing(data, target_duration): 
    filtered_result = []
    for row in data:
        if row[4] > target_duration:
            filtered_result.append(row)
    return filtered_result 

def print_movie_info(data):
    for movie in data:
        print(movie)

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

# llama aquí a la función de filtrado
movies_filtered = filter_by_timing(movies_info, 140)

# llama a la función para mostrar los resultados aquí
print_movie_info(movies_filtered)

# Resultado
['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.73]
['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499]
["Schindler's List", 'USA', 1993, 'drama', 195, 8.818]
['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625]
['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619]
['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521]


# Ejercicio 2
# Basándote en la función anterior, escribe una nueva filter_by_year() que filtre las películas por año de estreno. 
# La nueva función debe tener dos parámetros:
data=: datos sobre las películas.
year=: criterio de filtro basado en el año.

# La función debe devolver una lista de listas que sólo contengan películas estrenadas después de year=. 
# Al final, debes imprimir el resultado de la función utilizando el año 1990 como argumento.

# esta función imprime la tabla filtrada. No modificar
def print_movie_info(data):
    for movie in data:
        print(movie)


# define tu función filter_by_year() aquí
def filter_by_year(data, year):
    filtered_result = []
    for row in data:
        if row[2] > year:
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

# A continuación tienes dos llamadas a funciones: para filtrar y para imprimir
movies_filtered = filter_by_year(movies_info, 1990)
print_movie_info(movies_filtered)

# Resultado: solo peliculas que salieron despues de 1990:
['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499]
["Schindler's List", 'USA', 1993, 'drama', 195, 8.818]
['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625]
['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619]
['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644]
['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]

# Fin.