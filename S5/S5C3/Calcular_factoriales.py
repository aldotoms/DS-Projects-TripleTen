# Capítulo 3/5
# Teoría de la probabilidad

# Calcular factoriales
# Calcular factoriales en Python

# Cuando el valor de n es pequeño, n! puede calcularse mentalmente. Para valores mayores de n, resulta más cómodo automatizar el proceso. 
# Para ello, puedes utilizar la función factorial() del módulo math de la librería estándar de Python.

# importa la función factorial del módulo matemático
from math import factorial

# define el número necesario de cursos
courses_amount = 3

# calcula el factorial de 3 (el valor de la variable courses_amount)
result = factorial(courses_amount)

# muestra el resultado
print(result)

# Ahora ya estás preparado para resolver por tu cuenta la tarea relativa al número de opciones de entrevista por tu cuenta.
# Se seleccionaron cinco candidatos para el proyecto. La responsable de RRHH quiere entrevistar a cada uno de ellos, pero no puede decidir en qué orden va a llamar a los candidatos. 
# Completa el siguiente código que calculará cuántas opciones de listas se pueden hacer, en las que cinco candidatos están ordenados en un orden diferente.
# Guarda el resultado de los cálculos en la variable lists_amount. Muestra la variable.

# Código
from math import factorial

candidates_amount = 5

lists_amount = factorial(candidates_amount) # agrega aquí tu código
print(lists_amount)

# A la responsable de RRHH se le ha ocurrido una nueva idea: ¿qué pasaría si, en lugar de seleccionar candidatos individuales, buscara directamente al equipo perfecto? 
# Para ello, la responsable debe comprender cuántas maneras hay de formar equipos de tres personas, seleccionándolas entre cinco candidatos. 
# Esto le permitirá programar los horarios de entrevistas para los equipos. ¿Puedes ayudar a resolver este problema?


# *Combinaciones*

# Esta es una nueva tarea para ti, y antes de resolverla, tenemos que aprender una nueva fórmula: la fórmula para calcular el número de combinaciones de k elementos de n opciones posibles. 
# La fórmula es la siguiente:
# Por ejemplo, si una cafetería vende 10 tipos de helado y quieres comprar tres diferentes, tienes:
# Lo mismo puede calcularse en Python:

from math import factorial

# define los valores para las variables n y k
n = 10
k = 3

# realiza los cálculos
combinations = factorial(n) / (factorial(k) * factorial(n-k))
print(combinations)

# Ahora estás listo para ayudar a la responsable de RRHH y determinar el número de franjas horarias necesarias para entrevistar a todas las posibles formaciones del equipo.
# Completa el siguiente código para determinar el número de maneras para formar equipos de tres personas seleccionándolas entre cinco candidatos.
# Guarda el resultado de los cálculos en la variable combinations e imprímela.

# Código
from math import factorial

n = 5 # define aquí el número de candidatos
k = 3 # define aquí el número necesario de compañeros de equipo

combinations = factorial(n) / (factorial(k) * factorial(n-k)) # realiza aquí los cálculos principales
print(combinations)


# *Uso de fórmulas combinatorias para calcular probabilidades*

# Tu capacidad para contar los posibles resultados de eventos complejos te permite determinar las probabilidades de distintos resultados o combinaciones de resultados.
# Para completar todos los ejercicios siguientes, tendrás que utilizar fórmulas para calcular permutaciones o combinaciones y determinar el número total de resultados posibles. 
# A continuación, puedes dividir el número de resultados deseados entre este resultado para determinar la probabilidad.

# *Ejercicios
# Ejercicio 1
# Estás desarrollando con tus amigos un juego de búsqueda que consta de 10 tareas diferentes. 
# Las tareas pueden realizarse en cualquier orden, pero solo una secuencia de todas las existentes permite a los jugadores ganar el superpremio. 
# ¿Cuál es la probabilidad de ganar el superpremio, suponiendo que la probabilidad de elegir cada tarea en cualquier fase de la búsqueda es la misma?
# Completa el código siguiente para calcular la probabilidad. Utiliza las siguientes variables:

#   - tasks: para almacenar el número de tareas.
#   - permutations: para almacenar el número de permutaciones.
#   - probability: para almacenar la probabilidad de elegir la única secuencia de tareas que permite a los jugadores ganar el superpremio.

# Código
from math import factorial

tasks = # introduce aquí el número de tareas
permutations = # calcula aquí el número total de secuencias de tareas posibles
probability = # calcula aquí la probabilidad de seleccionar la única combinación ganadora

print(probability)


# *Ejercicios*
# Ejercicio 1

# Estás desarrollando con tus amigos un juego de búsqueda que consta de 10 tareas diferentes. Las tareas pueden realizarse en cualquier orden, 
# pero solo una secuencia de todas las existentes permite a los jugadores ganar el superpremio. 
# ¿Cuál es la probabilidad de ganar el superpremio, suponiendo que la probabilidad de elegir cada tarea en cualquier fase de la búsqueda es la misma?
# Completa el código siguiente para calcular la probabilidad. Utiliza las siguientes variables:
#   - tasks: para almacenar el número de tareas.
#   - permutations: para almacenar el número de permutaciones.
#   - probability: para almacenar la probabilidad de elegir la única secuencia de tareas que permite a los jugadores ganar el superpremio.

# Código
from math import factorial

tasks = 10 # introduce aquí el número de tareas
permutations = factorial(tasks) # calcula aquí el número total de secuencias de tareas posibles
probability = 1 / permutations # calcula aquí la probabilidad de seleccionar la única combinación ganadora

print(probability)

# Ejercicio 2
# Como los clientes no estaban satisfechos con la dificultad de ganar el superpremio, cambiaste las reglas. Ahora, los jugadores pueden elegir las tres tareas con las que quieren empezar el juego. 
# El orden de las tareas no importa, lo importante es la combinación. Si los jugadores consiguen adivinar la "combinación secreta", recibirán un código promocional de descuento.
# Para garantizar la equidad, debes calcular la probabilidad de obtener el código promocional utilizando las siguientes variables:
#   - tasks: número total de tareas disponibles.
#   - chosen: número de tareas elegidas al principio del juego.
#   - combinations: número total de combinaciones posibles de 3 tareas de las 10 disponibles.
#   - probability: probabilidad final de obtener el código promocional.
# Implementa un programa que calcule la probabilidad de obtener el código promocional utilizando las variables anteriores.

# Código
from math import factorial

tasks = 10 # introduce aquí el número total de tareas
chosen = 3 # introduce aquí el número de tareas a elegir

combinations = factorial(tasks) / (factorial(chosen) * factorial(tasks-chosen)) # calcula el número de combinaciones disponibles
probability = 1 / combinations # calcula aquí el resultado final

print(probability)


# FIN.