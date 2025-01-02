# PRÁCTICA GUIADA
#
# Vamos a modificar la lista shawshank_movie añadiéndole el nombre del director de esta película al final de la lista. 
# Su nombre es  'Frank Darabont'.
# La salida esperada es esta: ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111, 'Frank Darabont']

shawshank_movie = ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
shawshank_movie.append('Frank Darabont') # escribe tu código aquí
print(shawshank_movie)

# Vamos a modificar la lista godfather_movie ampliando la información almacenada sobre la película. 
# Tienes que añadir el nombre del director, Francis Ford Coppola, y el del compositor de la banda sonora, Nino Rota. Mantén el orden de aparición al enumerar estos nombres.
# La salida esperada es esta: ['The Godfather', 'USA', 1972, 'Francis Ford Coppola', 'Nino Rota']

godfather_movie = ['The Godfather', 'USA', 1972]
# añade los nombres del director y del compositor al final de la lista
godfather_movie.extend(['Francis Ford Coppola', 'Nino Rota']) # tu código
print(godfather_movie)

# El nombre del director ('James Camron') se añadió antes del género de la película, pero tiene un error tipográfico. 
# Tenemos que corregir este error. Para ello, primero tenemos que eliminar el nombre del director.
# La salida esperada es esta: ['Titanic', 'USA', 1997, 'drama', 194]

titanic_movie = ['Titanic', 'USA', 1997, 'James Camron', 'drama', 194]
removed_item = titanic_movie.pop(3)
# elimina el nombre del director de la lista
print(titanic_movie)
print(removed_item)

# Fin.