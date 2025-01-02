# Capítulo 2/5 Sentencias condicionales
#
# Modificación de tablas

# Teoria
# Las tablas son una parte integral del procesamiento y análisis de datos. 
# En Python, las tablas suelen implementarse como listas de listas o utilizando librerías como pandas, las cuales veremos en el futuro.
# La modificación de tablas puede ser un paso crucial en el preprocesamiento de datos y los bucles son una forma eficaz de hacerlo. 
# En esta lección aprenderemos cómo modificar tablas mediante bucles en Python.

# Modificación de valores en una tabla
# La modificación de valores en una tabla es una operación común en el procesamiento de datos. 
# Podemos utilizar bucles para modificar valores en una tabla. Imaginemos que tenemos una tabla de películas con el siguiente formato:

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1994, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

# Supongamos que queremos cambiar el año de lanzamiento de "Schindler's List" de 1994 a 1993. Podemos utilizar el siguiente código:

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1994, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_name = "Schindler's List"
correct_year = 1993

for movie in movies: # haz un bucle por todas las películas
    if movie[0] == movie_name: # si el título de la película es el que queremos arreglar
        movie[1] = correct_year # asigna el valor deseado


for movie in movies: # haz un bucle por todas las películas
    print(movie)

# Recuerda que estas modificaciones son posibles porque las listas son mutables. 

# Ejercicio
# Ahora que tenemos los años correctos, intenta hacer cambios por tu cuenta con esta tarea.
# Imagina que has creado una lista de películas que te gustaría ver con tus amistades. Aquí tienes esta lista:

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1993, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

# Has enseñado la lista a tus amigos y les has preguntado qué les parecía. 
# En general, les ha gustado mucho, pero dicen que antes de ver "The Lord of the Rings: The Return of the King", 
# sería estupendo ver la primera parte de la película, que es "The Lord of the Rings: The Fellowship of the Ring".

# Les das la razón en que hay que ver primero la primera parte de la película. 
# Así que tu objetivo ahora consiste en modificar la lista de movies que has creado anteriormente. 
# En concreto, quieres sustituir "The Lord of the Rings: The Return of the King" por "The Lord of the Rings: The Fellowship of the Ring", que se estrenó en 2001. 
# El director de la película fue Peter Jackson.

# Para ello, escribe un bucle for que recorra los elementos de la lista movies. 
# Cuando llegues a una sublista con el nombre de la película "The Lord of the Rings: The Return of the King", 
# sustituye el nombre de la película por la variable new_movie y el año de estreno por la variable new_year.

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1993, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_to_change = "The Lord of the Rings: The Return of the King"
new_movie = "The Lord of the Rings: The Fellowship of the Ring"
new_year = 2001

for movie in movies:
    if movie[0] == movie_to_change: # establece una condición aquí
        movie[0] = new_movie        # sustituye el nombre de la película si la condición devuelve True
        movie[1] = new_year         # sustituye el año de estreno si la condición devuelve True

# no modifiques el código de abajo, ya que imprime el resultado
for movie in movies:
    print(movie)

# Resultado
['The Shawshank Redemption', 1994, 'Frank Darabont']
['The Godfather', 1972, 'Francis Ford Coppola']
['The Dark Knight', 2008, 'Christopher Nolan']
['12 Angry Men', 1957, 'Sidney Lumet']
["Schindler's List", 1993, 'Steven Spielberg']
['The Lord of the Rings: The Fellowship of the Ring', 2001, 'Peter Jackson']

# Fin.