# Capítulo 2/5 · Faltan 2 lecciones -Sentencias condicionales
#
# Operadores lógicos y filtros
# 
# Teoria

# Como ya sabemos, un filtro para una tabla consta siempre de tres partes:
# 1. Una variable con una lista vacía para agregar filas coincidentes.
# 2. Un bucle que recorre la tabla original.
# 3. Una sentencia condicional con if. Si una sublista cumple la condición, se agregará a la variable que almacena elementos que cumplen con nuestro filtro.

# Operadores lógicos y filtros
#
# Para crear un algoritmo de filtrado más sofisticado, puedes utilizar múltiples condiciones unidas por operadores lógicos. 
# Al hacerlo, puedes filtrar datos en función de más de un criterio.
# En esta lección aprenderás cómo combinar varias condiciones mediante operadores lógicos.
# Vamos a comprobar dos condiciones para obtener las películas que se estrenaron en los EE. UU. después de 1990. 
# Examina el código que aparece a continuación y ejecútalo. Lo comentaremos enseguida.

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

movies_filtered = [] 

for movie in movies_info: # un bucle sobre cada película
    if movie[2] > 1990 and movie[1] == 'USA': # si la película se estrenó después de 1990 y en los EE. UU.,
        movies_filtered.append(movie) # la agregamos a la nueva lista

for movie in movies_filtered:
    print(movie)

# La línea clave del código anterior es if movie[2] > 1990 and movie[1] == 'USA'. Analicemos lo que hace, ya que así es como un filtro comprueba una condición. 
# Para empezar, vemos claramente que consta de dos partes:
movie[2] > 1990
movie[1] == 'USA'
# Y estas dos partes se unen mediante un operador lógico and.
# Si tanto la condición movie[2] > 1990 como movie[1] == 'USA' devuelven True, entonces, 
# toda la línea (if movie[2] > 1990 and movie[1] == 'USA') devolverá True debido a que tenemos and como operador lógico. 
# Como resultado, ejecutamos movies_filtered.append(movie) y la película se añade a la lista movies_filtered. 
# Parece que te estás convirtiendo en una persona experta en filtrar películas. Sigue explorando y filtrando películas para encontrar tus favoritas.

# Ejercicio
# Ahora inténtalo por tu cuenta.
# Crea una lista vacía llamada movies_filtered. 
# A continuación, añade a movies_filtered las películas que fueron estrenadas en 1994 o que tienen una calificación inferior a 8.5.

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

# crear una lista vacía llamada movies_filtered
movies_filtered = []

# escribe tu código aquí
for movie in movies_info:
    if movie[2] == 1994 or movie[-1] < 8.5:
        movies_filtered.append(movie)

# no modifiques el código de abajo ya que imprime el resultado final
for movie in movies_filtered:
    print(movie)

# Fin.
