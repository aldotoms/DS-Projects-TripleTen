# PRÁCTICA GUIADA - "LISTAS"
#
# A continuación se muestran algunas variables (title, year, genre, etc.) que almacenan información sobre la película "Fight Club". 
# En vez de tener esta información en forma de variables, queremos que crees una lista que almacenará toda esta información.

movie_info = []

# Hemos creado una variable llamada movie_info. 
# Tu objetivo es rellenarla de tal manera que esta lista tenga el siguiente orden de elementos: título, año, género, duración y calificación.
# Una vez creada, muestra la lista en la pantalla.
# La salida esperada es esta: ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

title = 'Fight Club'
year = 1999
genre = ['thriller', 'drama', 'crime']
duration = 139
rating = 8.644

# añade elementos a la lista movie_info:
movie_info = [title, year, genre, duration, rating]
# muestra la lista
print(movie_info)

# Fin.