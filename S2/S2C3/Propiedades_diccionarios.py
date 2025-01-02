# Propiedades de los diccionarios
# La última estructura de datos que aún no has aprendido son los diccionarios.
#
# Al final de esta lección, podrás explicar qué es un diccionario, cómo usar su sintaxis y comparar y contrastar diccionarios con listas.
# En general, entender los diccionarios y cómo se diferencian de las listas te brindará una poderosa herramienta para usar en tus proyectos de programación.

# Teoría
# DICCIONARIOS
#
# Los diccionarios son una herramienta útil en la programación, ya que te permiten almacenar y organizar datos de una manera fácil de acceder 
# cuando los necesites. Un diccionario es una colección ordenada de elementos, similar a una lista. 
# Sin embargo, en un diccionario, cada elemento es un par clave-valor, donde cada clave sirve como identificador único para un valor específico. 
# Esta es la principal diferencia entre los diccionarios y las listas. En un diccionario, 
# los valores se asocian directamente con sus respectivas claves, en lugar de índices.
#
# Las listas son útiles para almacenar elementos en un orden determinado, 
# mientras que los diccionarios son convenientes para describir las propiedades individuales de los objetos.
#
# Sintaxis del diccionario
# Para usar un diccionario en Python, tienes que entender su sintaxis. 
# A diferencia de las listas, que usan corchetes para encerrar los elementos que contienen, los diccionarios usan llaves. 
# Dentro de las llaves, puedes definir tus pares clave-valor separados por dos puntos.
# Cada entrada del diccionario de Python tiene dos partes: una clave y un valor.
# 
# - Clave: un string o número que identifica el valor.
# - Valor: los datos asociados a la clave.
#
# Vamos a crear un diccionario que contenga información de vuelos. La clave será el número de vuelo, y el valor será la fecha y hora de salida:
 
schedule = {                    
    'SU2222': '12.06.18 12:30', # a la izquierda de los dos puntos está la clave,
        'SU1111': '12.06.18 14:05',    # a la derecha está el valor.
    'SU0777': '12.06.18 17:00' 
}

# Estas son las tres reglas básicas de la sintaxis del diccionario:
# 1. Los diccionarios se escriben con llaves: {}.
# 2. Las comas separan los elementos (pares clave-valor) dentro del diccionario.
# 3. Una clave y un valor dentro de un par se separan por dos puntos.
# ¡Mostremos el diccionario que creamos! Ejecuta el siguiente código para ver el resultado.

schedule = {                    
    'SU2222': '12.06.18 12:30', # a la izquierda de los dos puntos está la clave,
	'SU1111': '12.06.18 14:05',	# a la derecha está el valor.
    'SU0777': '12.06.18 17:00' 
}
print(schedule)

# Resultado: {'SU2222': '12.06.18 12:30', 'SU1111': '12.06.18 14:05', 'SU0777': '12.06.18 17:00'}

# DICCIONARIOS Y LISTAS
#
# Como ya sabes, en un diccionario, cada valor está relacionado con su clave, mientras que las listas utilizan índices. 
# Hay algunas diferencias más entre los diccionarios y las listas:

# La recuperación de datos de los diccionarios es más rápida, pero un diccionario ocupa más espacio en la memoria.
# Al igual que las listas, los diccionarios pueden almacenar datos de cualquier tipo, pero las claves solo pueden ser tipos de datos inmutables, 
# como strings y números (enteros y de coma flotante).

# ¡Pero no todo son diferencias! De manera similar a las listas, podemos pasar diccionarios a len() para obtener el número de elementos.

# clave - nombre del goleador : valor - número de goles marcados en 2019
players_result = {
    'Cristiano Ronaldo': 39,
    'Robert Lewandowski': 54,
    'Lionel Messi': 50,
    'Harry Kane': 36,
    'Karim Benzema': 35
}
print(len(players_result))

# Ejercicio
# De nuevo, es hora de practicar un poco.
# Crea un diccionario llamado movies que incluya las siguientes cuatro películas. El nombre de la película será la clave y el año de estreno será el valor:
# Her, 2013
# Big Eyes, 2014
# Taxi Driver, 1976
# The King of Comedy, 1982
# Una vez creado, muestra el diccionario en la pantalla.

# crea un diccionario
movies = {'Her': 2014, 
          'Big Eyes': 2014,
          'Taxi Driver': 1976,
          'The King of Comedy': 1982
}
print(movies)

# Resultado
{'Her': 2013, 'Big Eyes': 2014, 'Taxi Driver': 1976, 'The King of Comedy': 1982}

# Fin.