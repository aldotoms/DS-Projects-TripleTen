# Capítulo 2/5  Sentencias condicionales
#
# Expresiones lógicas y operadores de comparación
#
# Teoria
# Hasta ahora has estado creando programas simples, en los que las líneas de código simplemente se ejecutan una tras otra; sin embargo, a veces debemos agregar flexibilidad al comportamiento del programa. Podemos hacer esto mediante sentencias condicionales.
# Digamos que es otoño. Estás tratando de averiguar si necesitas llevar un paraguas para salir de casa.

# Si está lloviendo, llevarás un paraguas; si no está lloviendo, llevarás un sombrero.

# El resultado de comprobar la condición (¿está lloviendo?) determina qué rama del algoritmo se ejecutará (con paraguas o sin paraguas).
# La estructura básica de cualquier sentencia condicional es: 
# IF <statement is True>, THEN <do this> (SI <la sentencia es True>, ENTONCES <haz esto>).
# Para definir la primera parte de la sentencia condicional utilizamos expresiones lógicas.

# Expresiones lógicas
# Hay varios tipos de expresiones en Python que devuelven True o False:
# - Expresiones que contienen operadores de comparación: ==, !=, >, <, >=, <=.
# - Expresiones que contienen operadores lógicos: and, or, not.
# - Funciones de predicado.
# Operadores de comparación
# Digamos que queremos comprobar si la película 'The Shawshank Redemption' se estrenó después de 'Titanic':

shawshank_release_year = 1994
titanic_release_year = 1997

shawshank_release_year > titanic_release_year

# El resultado: False

# ¡'The Shawshank Redemption' se estrenó unos años antes!
# Esta es una lista de los operadores lógicos que se utilizan en Python:

# Operador	Significado	Ejemplo	Resultado
# ==	Igualdad	5 == 5	True
# !=	Desigualdad	5 != 2	True
# >	Mayor que	5 > 2	True
# <	Menor que	5 < 2	False
# >=	Mayor o igual que	5 >= 2	True
# <=	Menor o igual que	5 <= 5	True

# Al usar operadores de comparación, es importante saber que no podemos comparar tipos de datos completamente diferentes.
# Cuando usamos operadores de comparación, podemos comparar float con int. De hecho, 
# Python puede convertir int en float de forma automática cuando sea necesario, pero no puedes comparar tipos de datos completamente diferentes. 
# Por ejemplo, no puedes comparar números con cadenas.


# Operadores lógicos
# Los operadores lógicos son herramientas increíblemente útiles en programación, ya que permiten combinar y evaluar múltiples condiciones en una expresión lógica. 
# En Python existen tres operadores lógicos de uso común ("and", "or" y "not") que se pueden utilizar para crear sentencias condicionales más complejas que pueden manejar múltiples condiciones.

# El operador "and" se utiliza para comprobar si las dos condiciones en una sentencia son verdaderas. 
# Si las dos condiciones son verdaderas, la sentencia completa también es verdadera; por el contrario, si una o ambas condiciones son falsas, 
# entonces la sentencia completa es falsa.

# El operador "or", por otro lado, comprueba si una o ambas condiciones en una sentencia son verdaderas. 
# Si al menos una de las condiciones es verdadera, entonces la sentencia completa es verdadera. 
# La sentencia solo será falsa si las dos condiciones son falsas.

# Finalmente, el operador "not" es un operador unario que se utiliza para revertir el valor verdadero de una condición. 
# Esto significa que si una condición es verdadera, entonces "not" la hará falsa, y viceversa.

# Estos operadores se pueden utilizar en combinación con otras sentencias condicionales y bucles para crear programas más complejos y dinámicos. 
# Cuando entiendes cómo se utilizan los operadores lógicos, puedes crear un código más eficiente y efectivo que pueda manejar una amplia gama de situaciones.

# Esta tabla muestra los operadores lógicos que se utilizan en Python:

# Operador	Significado	Ejemplo	Resultado
# and	Ambas condiciones deben ser verdaderas	5 > 2 and 3 < 5	True
# or	Al menos una condición debe ser verdadera	5 > 2 or 3 > 5	True
# not	Revierte el valor verdadero de una condición	not (5 > 2)	False

# Volvamos a nuestra base de datos de películas y comprobemos si 'Fight Club' se estrenó entre 1996 y 1998. 
# Fíjate en el código de abajo que lo hace y, luego, ejecútalo para ver cuál será la salida.

movie_info = ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644]
print(movie_info[2] > 1996 and movie_info[2] < 1998)

# Resultado:    False

# El código devolvió False porque una de las condiciones no se cumplió (Fight Club Release date < 1998).
# En caso de que desees comprobar si solo una de las condiciones es True, puedes utilizar or en lugar de and. 
# Así es como se verá nuestro código si sustituimos and por or. No dudes en ejecutarlo para ver el resultado.

movie_info = ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644]
print(movie_info[2] > 1996 or movie_info[2] < 1998)

# Como era de esperar, el resultado es True. Esto se debe a que movie_info[2] > 1996 ha devuelto True.
# ¡Ahora vamos a practicar!

# Teoría: ¿Qué pasa si quieres revertir el resultado que obtuvimos primero? Para hacerlo podemos utilizar not:
# Resultado
# False
# True

movie_info = ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644]
print(movie_info[2] > 1996 and movie_info[2] < 1998)
print(not(movie_info[2] > 1996 and movie_info[2] < 1998))

# El código devolvió False porque una de las condiciones no se cumplió (Fight Club Release date < 1998) y luego la convertimos en True.
# Ahora vamos a practicar el uso de not.

# Cuestionario 3
# Ahora vamos a practicar el uso de not.
# Pregunta: ¿Qué crees que mostrará este código?

movie_info = ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644]
print(not(movie_info[-1] > 8 and movie_info[-1] < 9))

# Teoria
# Funciones de predicado
# Una función de predicado es cualquier función que devuelve True o False. 
# Por ejemplo, estos son algunos métodos de cadena que comprueban si los caracteres de una cadena cumplen ciertas condiciones:

# - islower() devuelve True si todos los caracteres alfabéticos de la cadena están en minúsculas;
# - isdigit() devuelve True si una cadena contiene solo números;
# - isalpha() devuelve True si una cadena contiene solo letras. Si una cadena contiene signos de puntuación o espacios, devolverá False.

# A continuación se muestran cadenas y funciones de predicado. 
# Modifica las cadenas, ejecuta el código y observa cómo cambia el resultado.

print('hola'.islower()) 
print('777'.isdigit()) 
print('lacadenacontieneespaciosasícomosignosdepuntuación'.isalpha())

# Cuestionario 4
# ¡Ahora es tu momento de brillar! Completa el cuestionario que tienes a continuación.
# Pregunta: ¿Qué crees que mostrará este código?

print('Me encanta python'.islower()) 
print('doce'.isdigit()) 
print('Las declaraciones condicionales son fantásticas'.isalpha())

# Las sentencias condicionales son fundamentales para crear programas que puedan tomar decisiones con base en distintas entradas o datos. 
# Además, permiten escribir programas más flexibles y potentes que pueden manejar una amplia gama de situaciones. 
# ¡Practica la escritura de tu primera condición en la próxima lección!

# Fin.