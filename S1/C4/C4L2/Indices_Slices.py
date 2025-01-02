# Índices y slices
#
# Ya sabemos cómo crear listas. Pero, además de crear listas, hay muchas otras operaciones que podemos realizar con ellas. 
# Debes aprender cómo tomar o seleccionar ciertos elementos de las listas. ¿Suena interesante, no es así?
# En esta lección, vamos a ver:
# - Indexación.
# - Slicing (segmentación de datos).

# Indexar listas
# Al igual que un string, una lista es una colección ordenada de elementos. 
# Esto significa que cada elemento tiene un "lugar en la fila", es decir, un índice. 
# La indexación de listas comienza en 0 y se incrementa en 1 por cada elemento subsiguiente.

# Acceder a un elemento
# Para acceder a un elemento en un índice determinado, 
# hay que poner el número de índice entre corchetes después de la lista (al igual que lo hicimos con los strings):

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[0])        # Muestra el primer elemento de la lista
print(type(movie_info[0]))  # Muestra el tipo de datos del primer elemento de la lista

# Hemos seleccionado el primer elemento de la lista (es decir, el del índice 0) y lo confirmamos mostrando su valor y su tipo de dato.
# Veamos qué sucede si mostramos el índice 2:

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[2])        # Muestra el tercer elemento de la lista
print(type(movie_info[2]))  # Muestra el tipo de datos del tercer elemento de la lista


# Slicing
# Podemos utilizar el “slicing” para tomar varios elementos a la vez.
# La sintaxis general que se usa al segmentar una lista es poner el primer y último valor de índice del slice después de la lista, 
# separándolos con dos puntos y colocándolos entre corchetes.

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[1:4])        # muestra el segundo, tercer y cuarto elemento
print(type(movie_info[1:4]))
print(len(movie_info[1:4]))

# Acabamos de hacer un slice de la lista movie_info del índice 1 al 4. El resultado nos muestra algunos aspectos a tener en cuenta:

# - El elemento en el índice superior no está incluido en la lista (es decir, movie_info[1:4] 
#   mostrará los elementos hasta el índice 3).
# - El tipo de datos de un slice de la lista es también una lista (observa <class 'list'>).
# - La longitud del slice es igual a la diferencia del índice superior e inferior 
#   (es decir, movie_info[1:4] ⇒ 4 - 1 = 3 = len(movie_info[1:4])).

# Podemos incluir un índice superior que esté fuera del rango del índice sin que nos dé un error; en su lugar, 
# obtendremos todos los elementos hasta el final de la lista (incluyendo el último elemento):

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[2:100])
print(len(movie_info[2:100]))

# Existe una notación abreviada para esto. Si omitimos el índice superior, 
# obtendremos todos los elementos de la lista empezando por el índice inferior:

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[1:])
print(len(movie_info[1:]))

# Lo contrario también es cierto. Podemos omitir el límite inferior para obtener todos los elementos, 
# empezando desde el principio de la lista, hasta llegar al elemento situado en el índice superior, pero sin incluirlo.
# Para resumir: Al igual que los strings, los elementos de una lista se pueden indexar de forma positiva o negativa.

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]

print(movie_info[4])
print(movie_info[-1])

# Para obtener un slice de una lista, debemos pasar el límite inferior y el límite superior que queremos incluir.

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]
print(movie_info[2:4])

# El límite superior puede incluso eliminarse si lo que queremos es incluir todos los elementos, 
# comenzando por el límite inferior:

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]
print(movie_info[2:])

# Lo mismo funciona también para el límite inferior.
# Fin.
