# PROYECTO 1: Aldo Tomás Orduña Fabila - Data Science - 22.Sep.2024
# 
# Como parte del equipo de análisis, lo primero que debes hacer es evaluar la calidad de una muestra de datos recopilados y prepararla para analizarla posteriormente. 
# Después, en la segunda parte de este proyecto en el segundo sprint, desarrollarás más tus habilidades y harás tu primer análisis completo, 
# respondiendo a las necesidades del cliente.

# Estos son los datos que el cliente nos proporcionó. Tienen el formato de una lista de Python, con las siguientes columnas de datos:

# user_id: Identificador único para cada usuario.
# user_name: El nombre del usuario.
# user_age: La edad del usuario.
# fav_categories: Categorías favoritas de los artículos que compró el usuario, como 'ELECTRONICS', 'SPORT' y 'BOOKS' (ELECTRÓNICOS, DEPORTES y LIBROS), etc.
# total_spendings: Una lista de números enteros que indican la cantidad total gastada en cada una de las categorías favoritas.

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]
​
# Paso 1
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. 
# Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. 
# Te han pedido que revises los datos recopilados y propongas cambios. 
# A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.

user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']

# Opciones:
#   1. Se debe cambiar el tipo de dato de user_id de cadena a entero.
#   2. La variable user_name contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#   3. El tipo de dato de user_age es correcto y no hay necesidad de convertirlo.
#   4. La lista fav_categories contiene cadenas en mayúsculas. En lugar de ello, debemos convertir los valores de la lista en minúsculas.

# Para cada una de las opciones, escribe en la siguiente celda markdown si la identificaste como un problema real en los datos o no. 
# Justifica tu razonamiento. Por ejemplo, si crees que la primera opción es correcta, escríbelo y explica por qué piensas que es correcta.
# Escribe tu respuesta y explica tu argumentación:

# Respuestas:
#   1R. No es necesario cambiar el "type" del 'user_id', ya que actualmente está declarado como un 'string' o cadena.
#       Eso está bien ya que no sólo pueden ser números, sino también, letras que nos indiquen un número de folio.
#       A los números de folio de un 'user_id' no se les puede aplicar operaciones aritméticas.
#   2R. Si es necesario corregir el contenido de la variable 'user_name' debido a que es un nombre propio,
#       el cual no debería estar separado por guión bajo, tener espacios al principio ni al final.
#   3R. No es correcto el tipo de dato de 'user_age', por lo que es necesario convertirlo ya que las edades se identifican con números enteros y no con decimales.
#       Se debe cambiar el tipo de 'user_age' de un 'float' a un 'integer'.
#   4R. No es tan necesario convertir los datos "strings" de la variable 'fav_categories' siempre y cuando todas sean mayúsculas; 
#       sin embargo, como buena práctica es recomendable utilizar cadenas en minúsculas, por lo que se deberá realizar el cambio.


# Paso 2
# Vamos a implementar los cambios que identificamos. 
# Primero, necesitamos corregir los problemas de la variable user_name Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; 
# tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.
# La salida esperada es: mike reed

user_name = ' mike_reed '
user_name = user_name.strip().replace('_', ' ') # escribe tu código aquí
print(user_name)


# Paso 3
# Luego, debemos dividir el user_name (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: 
# la cadena para el nombre y la cadena para el apellido.
# La salida esperada es: ['mike', 'reed']

user_name = 'mike reed'
name_split = user_name.split() # escribe tu código aquí
print(name_split)


# Paso 4
# ¡Genial! Ahora debemos trabajar con la variable user_age. 
# Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.
# La salida esperada es: 32

user_age = 32.0
user_age = int(user_age) # escribe tu código aquí
print(user_age)


# Paso 5
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de user_age no se pueda convertir en un número entero. 
# Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# Escribe un código que intente convertir la variable user_age en un número entero y asigna el valor transformado a user_age_int. 
# Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: 
# Please provide your age as a numerical value. (Proporcione su edad como un valor numérico.)
# La salida esperada es: Please provide your age as a numerical value.

user_age = 'treinta y dos'

try:
    user_age = int(user_age)
except:
    print('Please provide your age as a number value.')


# Paso 6
# El equipo de dirección de Store 1 te pidió ayudarles a organizar los datos de sus clientes para analizarlos y gestionarlos mejor.
# Tu tarea es ordenar esta lista por ID de usuario de forma ascendente para que sea más fácil acceder a ella y analizarla.

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

users.sort()    # Esta función odenará la lista por el número de 'user_id' de menor a mayor.
print(users)


# Paso 7
# Tenemos la información de los hábitos de consumo de nuestros usuarios, incluyendo la cantidad gastada en cada una de sus categorías favoritas. 
# La dirección está interesada en conocer la cantidad total gastada por el usuario.
# Calculemos este valor y despleguémoslo.
# La salida esperada es: 1280

fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]
total_amount = sum(spendings_per_category) # escribe tu código aquí
max_amount = max(spendings_per_category)
min_amount = min(spendings_per_category)
print(f"La cantidad total gastada por el usuario es de {total_amount}, la cantidad mínima es de {min_amount}, y la cantidad máxima es de {max_amount}.")


# Paso 8
# La dirección de la empresa nos pidió pensar en una manera de resumir toda la información de un usuario. 
# Tu objetivo es crear una cadena formateada que utilice información de las variables user_id, user_name y user_age.
# Esta es la cadena final que queremos crear: User 32415 is mike who is 32 years old. (El usuario 32415 es Mike, quien tiene 32 años).

user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32
user_info = 'User {i} is {n} who is {a} years old.'.format(i=user_id, n=user_name[0], a=user_age) # escribe tu código aquí
print(user_info)


# Paso 9
# La dirección también quiere una forma fácil de conocer la cantidad de clientes con cuyos datos contamos. 
# Tu objetivo es crear una cadena formateada que muestre la cantidad de datos de clientes registrados.
# Esta es la cadena final que queremos crear: Hemos registrado datos de X clientes.

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]
message = f"We have registered data on {len(users)} clients." # escribe tu código aquí
print(message)


# Paso 10
# Apliquemos ahora todos los cambios a la lista de clientes. Para simplificar las cosas, te proporcionaremos una más corta. Debes:
# Eliminar todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo.
# Convertir todas las edades en números enteros.
# Separar todos los nombres y apellidos en una sublista.
# Guarda la lista modificada como una nueva lista llamada users_clean y muéstrala en la pantalla.

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
]

users_clean = []

​# Procesa al primer usuario ' mike_reed '
user_name_1 = users[0][1].strip().replace('_', ' ').split()
user_age_1 = int(users[0][2])
user_1 = (users[0][0], user_name_1, user_age_1, users[0][3:5])
users_clean.append(user_1)

# Procesa al segundo usuario 'kate morgan'
user_name_2 = users[1][1].split()
user_age_2 = int(users[1][2])
user_2 = (users[1][0], user_name_2, user_age_2, users[1][3:5])
users_clean.append(user_2)

# Procesa al tercer usuario ' john doe '
user_name_3 = users[2][1].strip().split()
user_age_3 = int(users[2][2])
user_3 = (users[2][0], user_name_3, user_age_3, users[2][3:5])
users_clean.append(user_3)

print(users_clean)

# La salida esperada es:[
    # ['32415', ['mike', 'reed'], 32, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]], 
    # ['31980', ['kate', 'morgan'], 24, ['CLOTHES', 'BOOKS'], [439, 390]], 
    # ['32156', ['john', 'doe'], 37, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]]
    # ]

# Fin.