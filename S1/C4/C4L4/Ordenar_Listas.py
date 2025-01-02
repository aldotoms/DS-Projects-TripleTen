# Ordenar Listas
# Hemos explorado varios métodos clave: 
# - append() para agregar un elemento, 
# - extend() para múltiples elementos, 
# - insert() para colocar elementos en cualquier lugar, y 
# - pop() para eliminarlos. 
# 
# Pero hay más: una operación fundamental para manipular los datos es ordenarlos. 
# Vamos a sumergirnos en el proceso de ordenación y a mejorar aún más nuestros conocimientos de Python.


# El Método sort()
# El método sort() ordena una lista, modificando la original. Por defecto, ordena los elementos en orden ascendente.
# Ejemplo:

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
print(years)

years.sort()
print(years)

# Dos cosas a tener en cuenta sobre nuestro resultado:
# 1) El método sort() modifica la lista original en lugar de crear una nueva.
# 2) Por defecto, este método ordena los elementos en orden ascendente, de menor a mayor.
# Para ordenar en orden descendente, utiliza el parámetro reverse=True:

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years.sort(reverse=True)
print(years)

# Al ordenar strings se sigue el orden lexicográfico (puntuación, números, A-Z, a-z, en este mismo orden de prioridad).
# Ejemplo:

movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Schindler\'s List']
movies.sort()
print(movies)

# El cambio de un string a minúsculas afecta a su posición en la lista:

movies = ['The Shawshank Redemption', 'The Godfather', 'the Dark Knight', 'Schindler\'s List']
movies.sort()
print(movies)

# Fíjate en que la película 'the Dark Knight' pasó de la segunda a la última posición.
# Utiliza reverse=True para ordenar strings en orden descendente:

movies = ['The Shawshank Redemption', 'The Godfather', 'the Dark Knight', 'Schindler\'s List']
movies.sort(reverse=True)
print(movies)


# Uso de la función sorted()
# La función sorted() de Python ordena listas y otros tipos de datos, diferenciándose de sort() en dos aspectos clave:
# - sort() es un método de lista que modifica la lista original.
# - sorted() es una función que devuelve una nueva lista ordenada.
# Aquí tienes un ejemplo con sorted():

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years_sorted = sorted(years)
print(years_sorted)

# Y un ejemplo con sort():

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years.sort()
print(years)

# Al intentar asignar el resultado de sort() a una nueva variable se obtiene None:

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years_sort = years.sort()
print(years_sort)

# Para obtener una lista ordenada asignada a una nueva variable, utiliza sorted(). 
# Para modificar una lista existente, utiliza sort().
# Ambos métodos ordenan en orden ascendente por defecto, pero pueden hacerlo en orden descendente con reverse=True:

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
years_sorted = sorted(years, reverse=True)
print(years_sorted)

# Fin.