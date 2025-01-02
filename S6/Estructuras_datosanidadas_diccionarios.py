# Capítulo 3/5
# Aprender Python más a fondo

## Diccionarios: estructuras de datos anidadas con diccionarios
# En la lección anterior, aprendiste acerca de 3 nuevos métodos: values() que extrae valores de un diccionario, keys() que extrae claves y items() que extrae tanto las claves como los valores. 
# También te mostramos cómo utilizar estos métodos en un bucle for. A continuación te mostramos un ejemplo:

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

for value in financial_info.values():
    print(value)

# En esta lección, vamos a explorar las estructuras de datos anidadas usando diccionarios. Aprenderemos cómo combinar diccionarios con listas y cómo crear e iterar sobre estas estructuras. 
# También discutiremos cómo iterar sobre diccionarios y cómo procesar una lista de diccionarios.
# A veces, los valores de un diccionario son estructuras anidadas. En el primer sprint, vimos un ejemplo de una lista de listas que representan una estructura anidada. Aquí está:

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

# Los diccionarios también pueden contener estructuras anidadas. Al final de esta lección, comprenderás mejor las estructuras anidadas con diccionarios y cómo se pueden usar para procesar datos complejos.

# Diccionarios de listas
# Una estructura de datos útil en Python es un diccionario de listas, donde cada diccionario sirve como registro o entrada en la lista. 
# Esto facilita la organización de datos de muchas maneras diferentes. Cada diccionario puede tener muchos pares clave-valor que describen diferentes atributos o propiedades del registro.
# Veamos un ejemplo de un horario de autobuses:

# En el diccionario anterior, las claves son los números de las rutas de autobuses y los valores son listas con los horarios de salida. 
# Puedes obtener el horario de una ruta determinada utilizando la clave.
# Esta es una forma de iterar sobre un diccionario de listas. Primero, examina el código a continuación y luego ejecútalo para ver el resultado.

# Código
bus_schedule = {
    '72': ['8:00', '12:00', '17:30'],
    '26': ['9:30', '15:00'],
    '17': ['7:30', '12:30', '15:30']
}

# iteramos sobre las claves y los valores del diccionario
for route, times in bus_schedule.items():
    # iteramos sobre los valores de la lista
    for time in times:
        # mostramos la ruta y su horario correspondiente
	      print(f"Ruta {route} - Hora {time}")

# Usamos el método items() para iterar sobre las claves y los valores del diccionario, y luego usamos un bucle for para iterar sobre los valores de la lista y mostrar la ruta y su horario correspondiente.
# Ahora, a practicar:
# Pregunta
# ¿Qué va a hacer el siguiente código?

bus_schedule = {
    '72': ['8:00', '12:00', '17:30'],
    '26': ['9:30', '15:00'],
    '17': ['7:30', '12:30', '15:30']
}

for route, times in bus_schedule.items():
    earliest_time = times[0]
    print(f'La primera hora para el autobús #{route} es {earliest_time}')

# Los diccionarios de listas fueron la primera estructura de datos anidada que aprendiste. A continuación, convirtamos diccionarios de listas en listas de diccionarios y veamos cuál es la ventaja de esta estructura anidada.


## Listas de diccionarios y tablas
# La última estructura de datos que veremos en esta lección es la lista de diccionarios.
# Anteriormente, utilizaste listas anidadas para reproducir tablas. A continuación te mostramos un ejemplo:

movies_table = [
    ['The Shawshank Redemption', 'USA', 'drama', 1994, 142, 9.111],
    ['The Godfather', 'USA', 'drama, crime', 1972, 175, 8.730],
    ['The Dark Knight', 'USA', 'fantasy, action, thriller', 2008, 152, 8.499]
]

# El problema con estas "tablas" es que se accede a las filas y columnas mediante índices. 
# Por ejemplo, para obtener el año de estreno de la película de la tercera fila, tenemos que acceder al elemento en el índice 3 de la sublista 2. Ejecuta el siguiente código para ver cómo funciona:

# Código
movies_table = [
    ['The Shawshank Redemption', 'USA', 'drama', 1994, 142, 9.111],
    ['The Godfather', 'USA', 'drama, crime', 1972, 175, 8.730],
    ['The Dark Knight', 'USA', 'fantasy, action, thriller', 2008, 152, 8.499]
]

print(movies_table[2][3])

# Si convertimos esta lista de listas en formato de tabla, el resultado no será tan fácil de comprender:
# # Una computadora entendería la tabla, pero un analista podría confundirse. Para obtener los datos necesarios, tendrías que memorizar el orden de las columnas, qué índice corresponde a la calificación, la duración, etc.
# Para que esta sea una tabla utilizable, necesitaríamos los nombres de las columnas:

# Las listas de diccionarios nos permiten reemplazar los números de las columnas con nombres (claves del diccionario). 
# A continuación se muestra cómo se ven los datos de las películas como una lista de diccionarios. Examina el código que aparece a continuación y ejecútalo:

# Código
movies_table = [
    {'movie_name':'The Shawshank Redemption', 'country':'USA', 'genre':'drama', 'year':1994, 'duration':142, 'rating':9.111},
    {'movie_name':'The Godfather', 'country':'USA', 'genre':'drama, crime', 'year':1972, 'duration':175, 'rating':8.730},
    {'movie_name':'The Dark Knight', 'country':'USA', 'genre':'fantasy, action, thriller', 'year':2008, 'duration':152, 'rating':8.499}
]

# ahora accedemos a la columna por su nombre:
print(movies_table[2]['movie_name'])

# Las claves de diccionario facilitan el acceso a las columnas.
# Conocer las diferentes estructuras de datos también facilita el trabajo de quienes se encargan del análisis. Además, nos sirve para seleccionar la estructura idónea para cualquier dataset. Cuando el nombre de las columnas aporta más información que su orden, es preferible aplicar una estructura con nombres.
# Una lista de diccionarios reúne las ventajas de ambas estructuras:
#   - De los diccionarios, los nombres.
#   - De las listas, la capacidad de iterar sobre elementos ordenados.
# ¡Practiquemos un poco ahora!

#Pregunta
# Aquí está la tabla movies_table que acabamos de ver en el ejemplo:

movies_table = [
    {'movie_name':'The Shawshank Redemption', 'country':'USA', 'genre':'drama', 'year':1994, 'duration':142, 'rating':9.111},
    {'movie_name':'The Godfather', 'country':'USA', 'genre':'drama, crime', 'year':1972, 'duration':175, 'rating':8.730},
    {'movie_name':'The Dark Knight', 'country':'USA', 'genre':'fantasy, action, thriller', 'year':2008, 'duration':152, 'rating':8.499}
]

# ¿Qué código no dará como resultado un error cuando se ejecute? Selecciona la opción correcta.
print(movies_table[-1]['movie_name'])

# ¡Perfecto! A continuación, veamos qué podemos hacer con una lista de diccionarios.

# FIN.  