# Bucles for
#
# Teoría
# La automatización ahorra tiempo (y cordura)
# Supongamos que tienes una lista de 1000 elementos y quieres realizar la misma operación con cada uno de ellos. 
# Hacerlo a mano llevaría una eternidad. Por ejemplo, si queremos mostrar elementos de la lista film_genres uno por uno, 
# necesitaremos usar print() para cada uno de ellos:

film_genres = ['scifi','drama','thriller','comedy','action']
print(film_genres[0])
print(film_genres[1])
print(film_genres[2])
print(film_genres[3])
print(film_genres[4])

# El resultado: 
#   scifi
#   drama
#   thriller
#   comedy
#   action

# No parece muy eficiente, ¿verdad? 
# Afortunadamente, Python nos ayuda a evitar eso mediante el uso de bucles, una herramienta que nos permite repetir las instrucciones tantas veces como queramos.
# Al final de esta lección, podrás explicar qué es un bucle for, describir la estructura de los bucles y escribir tus propios bucles for.

# Bucles for en Python
# El tipo de bucle más común en Python es el bucle for, que comienza con la palabra clave for. 
# Recorre los elementos en una secuencia y realiza operaciones similares en cada uno de ellos.

# La secuencia que usamos puede ser cualquier objeto ordenado, como listas o strings.
# Volvamos a la lista film_genres y escribamos un bucle corto que imprima sus elementos:

film_genres = ['scifi','drama','thriller','comedy','action']
for value in film_genres:
    print(value)

# El resultado: 
#   scifi
#   drama
#   thriller
#   comedy
#   action
#
# ¡Es un juego totalmente nuevo!

# Componentes del bucle
# Echemos un vistazo a la estructura de un bucle y desglosémosla:

# - La palabra clave for.
# - Nuestra variable de bucle element. En cada iteración del bucle toma el valor de un elemento de la secuencia y te permite realizar algunas operaciones en él. 
#   Puedes usar cualquier nombre para esta variable, pero es mejor asegurarse de utilizar uno que sea claro y significativo.
# - La palabra clave in.
# - La lista your_list. El nombre de la lista que está siendo procesada por el bucle.
# - Los dos puntos : son un elemento esencial que separa las dos partes del bucle.
# - La función print(element). Esto constituye el cuerpo del bucle. El cuerpo contiene comandos que el bucle ejecuta en cada iteración del bucle. 
#   Cada comando en el cuerpo del bucle está precedido por una indentación de cuatro espacios, 
#   lo que indica que el comando debe ejecutarse dentro del bucle, separado del resto del código.

# Es fácil de recordar, se puede leer como si estuviera escrito en un libro. Para cada elemento de la lista que te estoy dando: haz todas estas acciones.

# Ejercicio 1
# Pruébalo. Escribe un bucle que muestre todos los elementos de la lista payers en la pantalla.

payers = [56, 65, 64, 63]
# escribe tu código aquí
for value in payers:
    print(value)

# Teoría
# Errores de sintaxis
# No te olvides de incluir la indentación y los dos puntos. La sintaxis es crucial: omite un solo elemento y el programa no se ejecutará.

# Ejercicio 2
# Esa es la situación con la que nos enfrentamos en el siguiente código. Estudia el mensaje de error y corrige el código para que se ejecute correctamente.

actors = ['John Travolta', 'Bonnie Hunt', 'Jason Bateman', 'Idris Elba']
for actor in actors:
    print(actor)

# Ejercicio 3
# Diferentes listas
# Los bucles funcionan con todo tipo de listas. Escribe un bucle que imprima todos los elementos de la lista elements.

elements = [42, 'hello', 0.5, -999, 'world']
for element in elements:    # escribe tu código aquí
    print(element)


# Teoría
# Bucles con strings
# También puedes utilizar bucles for con strings. Los bucles pueden iterar sobre cada carácter del texto, tal como lo hacen sobre cada elemento de la lista:

review = 'The Emoji Movie dejó mucho que desear. Dos estrellas muy generosas, como máximo.'
for symbol in review:
    print(symbol)

# Ejercicio 4
# Crea un bucle que muestre todos los caracteres del string message_japanese uno por uno.

message_japanese = '機械翻訳は通常良くありません'
for symbol in message_japanese:     # escribe tu código aquí
    print(symbol)


# ¡Bien hecho! Con los bucles en tu haber podrás automatizar muchas operaciones que de otro modo serían tediosas.
# En la próxima lección, aprenderás a usar bucles con listas anidadas.

# Fin.