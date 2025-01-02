# Capítulo 2/5 · Faltan 3 lecciones - Sentencias condicionales
#
# Filtrar tablas
#
# Teoria
# En los últimos capítulos has aprendido tres conceptos importantes:
# - las listas anidadas, que pueden utilizarse para representar tablas;
# - los bucles, que pueden utilizarse para recorrer sublistas o valores dentro de ellas;
# - los operadores condicionales, que cambian el comportamiento del código en función de determinados criterios.
# Al unir estos tres conceptos obtenemos un nuevo concepto, que son los filtros.

# Uso de filtros
# Un filtro es una herramienta útil que podemos utilizar para procesar tablas, 
# seleccionando solo los datos que cumplan con una serie de condiciones y utilizando estas condiciones para crear nuevas tablas.
# Al final de esta lección, podrás explicar cómo funcionan los filtros y utilizarlos para recuperar tablas más pequeñas 
# que contengan solamente los datos relevantes, facilitando de este modo el análisis y la manipulación de tus datos.
# Volvamos a ver nuestra lista anidada de películas:

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

# Vamos a crear un filtro que almacene películas con una duración mayor a 180 minutos en una nueva lista anidada. 
# Ejecuta el código de abajo y luego lo comentaremos.

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

movies_filtered = [] # lista vacía para almacenar el resultado

for movie in movies_info: # recorre en bucle las filas de la tabla original
    if movie[4] > 180: # si una película dura más de 180 minutos
        movies_filtered.append(movie) # agrega la fila a movies_filtered
        
for movie in movies_filtered: # muestra el contenido de movies_filtered
    print(movie)

# Resultado:
["Schindler's List", 'USA', 1993, 'drama', 195, 8.818]
['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625]


# Fíjate, primero hemos creado la variable llamada movies_filtered y hemos almacenado una lista vacía en ella. 
# A continuación, hemos utilizado el bucle for para iterar sobre las sublistas de la lista movies_info. 
# La condición if movie[4] > 180 nos permite extraer la duración de una película determinada y comprobar si es superior a 180. 
# En caso afirmativo, hemos empleado el método append() que añade la película a la lista movies_filtered.
# ¿Qué es lo que acabamos de hacer? 
# Acabamos de filtrar la tabla original movies_filtered en función de la duración de las películas. 
# Acabamos de crear este filtro.
#
# Partes de un filtro
# Un filtro para una tabla consta de tres partes:
# 1. Una variable con una lista vacía para agregar filas coincidentes.
# 2. Un bucle que recorre la tabla original.
# 3. Una sentencia condicional con if. Si una sublista cumple la condición, se agregará a la variable que almacena elementos que cumplen con nuestro filtro.
# Creemos otro filtro para almacenar todas las películas japonesas en una nueva lista. Examina el código que aparece a continuación y ejecútalo para ver cuál será el resultado.
#
# Creemos otro filtro para almacenar todas las películas japonesas en una nueva lista. 
# Examina el código que aparece a continuación y ejecútalo para ver cuál será el resultado.

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

movies_filtered = [] # lista vacía para almacenar el resultado

for movie in movies_info: # recorre en bucle las filas de la tabla original
    if movie[1] == 'Japan': # si la película es de Japón,
        movies_filtered.append(movie) # agrega esta fila a movies_filtered

for movie in movies_filtered: # muestra el contenido de movies_filtered
    print(movie)

# Resultado
['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106]

# No hay muchas películas japonesas en nuestra base de datos. ¿Qué hay de las películas americanas? ¿Puedes intentar encontrarlas?


# Ejercicio
# Obtén todas las películas americanas de la tabla movies_info utilizando un filtro. 
# Guarda el resultado en movies_filtered_USA. Imprime esta lista cuando hayas terminado.

movies_filtered_USA = []
country = 'USA'

for movie in movies_info:
    if movie[1] == country:
        movies_filtered_USA.append(movie)

for movie in movies_filtered_USA:
    print(movie)

