# ÍNDICES
#
# En programación, cada string, sin importar si está lleno o vacío, tiene una longitud que podemos comprobar fácilmente utilizando la función len(). A
# hora, ¡analicemos cómo podemos interactuar con cada carácter en un string y las cosas increíbles que podemos hacer con ellos!
# 
# Introcucción a los índices
# En Python, podemos pensar en los strings como una secuencia de caracteres, en donde a cada carácter se le da un índice cuya longitud va de cero (al inicio) 
# hasta menos uno (al final).
# Un índice es un número que identifica la posición de dicho carácter en el string, y en Python, aunque parezca extraño, 
# el primer carácter tiene un índice 0 en lugar de 1. Este es un comportamiento que hallarás en muchos otros lenguajes de programación.
#
# Acceder a los carácteres de un string
# Puedes acceder a cualquier carácter determinado haciendo referencia a su índice. 
# Todo lo que tienes que hacer es colocar el índice entre corchetes después de la variable que contiene el string. 
# Pero, presta atención: tal y como se muestra en la imagen anterior, el índice comienza desde cero. Veamos un ejemplo:

word = 'carácter'
letter = word[5] # Extraer el sexto carácter del string.
print(letter)

# Aquí, obtuvimos el sexto carácter en la palabra (recuerda que comenzamos a contar desde cero):
# c a r a c t e r 
# 0 1 2 3 4 5 6 7
#
# Como en 5 tenemos una t, cuando print(letter) ves una t.


# INDEXACIÓN NEGATIVA
#
# Python también nos brinda una forma práctica de indexar comenzando desde el final del string.
# Esto se llama indexación negativa y se hace utilizando números negativos como índice.
# El último carácter del string asume -1 como índice, el anterior tiene -2 como índice, y así sucesivamente hasta llegar al primer carácter del string. 
# Echa un vistazo al siguiente código para ver cómo funciona la indexación negativa.

word = 'caráter'
last_letter = word[-1]      # Extraer la última letra
third_from_end = word[-3]   # Extraer el tercer carácter del final
print(last_letter, third_from_end)

# Aquí obtuvimos el último (-1) y el antepenúltimo (-3) caracteres del string. 
# Es importante tener en cuenta que aunque la indexación positiva comienza desde 0, la indexación negativa comienza desde -1. 
# Piénsalo de esta manera: no existe el cero negativo.
#
#  c a  r  a  c  t  e  r
# -8 -7 -6 -5 -4 -3 -2 -1
#
# Veamos otro ejemplo. ¿Cómo extraerías la letra i de la siguiente variable word usando la indexación positiva?
# 
word = 'side'
#
# Ya sabes que Python comienza desde 0. Puedes hacer lo siguiente: 

word = 'side'
print(word[1])

# ¿Qué pasa si queremos utilizar indexación negativa?

word = 'side'
print(word[-3])

# Como puedes ver, obtenemos el mismo resultado utilizando indexación positiva o negativa. 

# ERRORES DE INDICE
#
# Si intentas acceder a un carácter fuera del rango del índice del string, obtendrás un IndexError:

word = 'palabra'
print(word[8])

# Puedes asegurarte de que tu código no intentará acceder a un carácter que no existe si siempre te mantienes entre 0 y la longitud del string, menos 1.
# Revisa el último ejemplo: len('word') te daría 7, pero el último carácter tiene 6 como índice porque comenzó desde 0.
# Lo mismo sucede en la indexación negativa, pero ahora, el primer carácter tendrá el índice -len('word'). ¡Así de fácil!


# CAMBIAR EL STRING
#
# Si intentas acceder a un carácter del string por su índice y reasignar el carácter, obtendrás otro error:

word = 'bbc'
word[0] = 'a'

# Esto es así porque el string es un tipo de dato inmutable. Solo puedes reemplazar un string anterior por uno nuevo:

word = 'bbc'
word = 'abc'

# Fin.