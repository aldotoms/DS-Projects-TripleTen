# LISTAS

# Lo que aprenderás en este capítulo
# En este capítulo, vas a explorar las listas, una estructura de datos fundamental en Python 
# que se utiliza para almacenar diversos tipos de información de manera eficiente.

# Al final de este capítulo podrás:
# - Crear listas y agregarles datos.
# - Realizar sorting (ordenación de datos), slicing (segmentación de datos) y otras modificaciones básicas en listas.
# - Trabajar con listas anidadas.
# - Utilizar métodos de lista para preprocesar strings.

# Estas habilidades serán esenciales para tu proyecto del sprint, donde las aplicarás para resolver desafíos reales 
# como los que enfrentan los profesionales de datos a diario.

# Propiedades básicas de las listas
# Entre las muchas características útiles que podemos encontrar en Python, las listas se destacan como una de las estructuras de datos más importantes y versátiles. 
# Entender cómo funcionan las listas es crucial, ya que constituyen la base para las estructuras de datos más avanzadas.
# Además, dominar el uso de las listas te permitirá realizar una gran variedad de tareas de manipulación de datos, 
# desde el almacenamiento de datos más básico hasta el preprocesamiento y análisis de datos complejos.

# Las listas de Python son colecciones ordenadas de elementos (o ítems) que pueden ser de diferentes tipos, tales como enteros, strings, booleanos o incluso otras listas. 
# Ordenadas significa que mantienen el orden en el que fueron creadas, sin ningún cambio, a menos que les agregues nuevos elementos o las redefinas.
# Las listas se definen colocando elementos dentro de corchetes [] y separándolos mediante comas.
# Aquí tienes algunos ejemplos de listas:

# Una lista vacía
my_list = []

# Una lista de enteros
numbers = [1, 2, 3, 4, 5]

# Una lista de strings
fruits = ['manzana', 'manzana', 'banana', 'cereza']

# Una lista de tipos de datos mezclados
mixed = [1, 'apple', 3.14, True]

print('Contenido de la variable my_list:',my_list)
print('Contenido de la variable numbers:',numbers)
print('Contenido de la variable fruits:',fruits)
print('Contenido de la variable mixed:',mixed)


# Una lista puede contener una mezcla de tipos de datos tal y como se define en la variable mixed (mezclada).
# Y lo que es más, una lista permite que la información se duplique, como puedes ver en la lista fruits.
# Sin importar el tipo de elementos que almacenen, descubrirás que tienen un tipo de datos específico:

print('Tipo de clase de la variable my_list:',type(my_list)) 
print ('Tipo de clase de la variable numbers:',type(numbers)) 
print ('Tipo de clase de la variable fruits:',type(fruits)) 
print ('Tipo de clase de la variable mixed:',type(mixed)) 

# Y, además, puedes comprobar la longitud de estas listas:

print('longitud de la variable my_list:', len(my_list)) 
print('longitud de la variable numbers:', len(numbers)) 
print('longitud de la variable fruits:', len(fruits)) 
print('longitud de la variable mixed:', len(mixed)) 

# Una lista también puede estar contenida en otras listas, a las que se les llama listas anidadas, de este modo:

# Lista anidada
nested_list= [0,[1, 2, 3],['manzana', 'cereza']]

print('Contenido:',nested_list)
print('Tipo de clase:',type(nested_list)) 
print('Lengitud:', len(nested_list)) 

# Observa que la longitud de la lista anidada es 3 elementos. 
# En Python, la función len() no cuenta recursivamente el número de elementos en la lista anidada, en su lugar, sólo cuenta los elementos en el nivel superior dentro de la lista.
# Como hay tres elementos de nivel superior en la variable nested_list, su longitud es 3.

# Por último, podemos hacer uso de algunas operaciones aritméticas con las listas:
# Concatenar listas:

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# 1. Repetir una lista:

a = [1, 2, 3]
print(a*2)

# Fin.