# Práctica Guiada
# Llama al método sort() para ordenar la lista movies en orden ascendente. Muestra el resultado en la pantalla.
# La salida esperada es esta: ['Fight Club', 'Harakiri', 'Pulp Fiction', 'The Good, the Bad and the Ugly']

movies = ['The Good, the Bad and the Ugly', 'Pulp Fiction', 'Fight Club', 'Harakiri']
# ordena la lista aquí
movies.sort()
# muestra la lista aquí
print(movies)

# Ordena la lista movies_duration en orden descendente utilizando el método sort(). Muestra el resultado en la pantalla.
# La salida esperada es esta: [201, 195, 178, 175, 154, 152, 142, 139]

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]
# ordena las películas aquí
movies_duration.sort(reverse=True)
# muestra el resultado aquí
print(movies_duration)

# Ordena la lista movies_duration en orden descendente, utilizando esta vez la función sorted(). 
# Almacena el resultado en la variable movies_duration_sorted y muéstralo.
# La salida esperada es esta: [201, 195, 178, 175, 154, 152, 142, 139]

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]
movies_duration_sorted = sorted(movies_duration, reverse=True) # ordena la lista movies_duration utilizando sorted()
# muestra la lista resultante aquí
print(movies_duration_sorted)

# Fin.