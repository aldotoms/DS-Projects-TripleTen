# SPRING 2 - BUCLES
# Operadores de asignación aumentada y funciones integradas
#
# Teoria

# Antes de profundizar en los bucles, nos gustaría presentar dos conceptos que se usan con frecuencia junto con los bucles para simplificar y optimizar el código: 
# la asignación aumentada y las funciones integradas como min(), max() y sum().
# Mediante el uso de la asignación aumentada, puedes actualizar fácilmente el valor de una variable sin tener que duplicar su nombre, 
# mientras que las funciones integradas brindan soluciones preparadas para realizar cálculos y operaciones comunes. 
# Comprender estos conceptos te ayudará a escribir un código de Python más eficiente y eficaz.
# Al final de esta lección, podrás modificar los valores almacenados en las variables usando la asignación aumentada y calcular el mínimo, 
# el máximo y la suma usando las funciones integradas.
# ¡Vamos!

# Actualizar valores
# Rara vez usamos Python como una calculadora simple para sumar o restar números. 
# En cambio, los valores a menudo están vinculados a variables cuyos valores pueden cambiar a medida que recibimos y procesamos más datos. 
# Por ejemplo, la cantidad de hablantes de diferentes idiomas definitivamente cambiará cada año.
# Tomemos el número total de hablantes de francés (284.9 millones de personas) y almacenémoslo en la variable fr_speakers. 
# Supongamos que las cosas han cambiado y ahora 2.5 millones de personas más hablan francés. Tenemos que actualizar la variable.
# Por supuesto, podemos simplemente sobrescribirla:

fr_speakers = 284.9
fr_speakers = 284.9 + 2.5
print(fr_speakers)

# El resultado: 287.4
# Pero esa no es la mejor solución. La actualización de valores a mano puede conducir fácilmente a un error humano. 
# Por ejemplo, si tu código es grande y el valor cambió muchas veces en el código, no sabrás qué valor tiene cuando necesites cambiarlo.
# Después de todo, solo necesitamos agregar 2.5 al valor actual usando la propia variable:

fr_speakers = 284.9
fr_speakers = fr_speakers + 2.5
print(fr_speakers)

# El resultado: 287.4
# ¡Obtenemos el mismo resultado!


# Asignación aumentada
# Por supuesto, incluso con el método anterior, aún estás duplicando el nombre de la variable y haciendo posible que ocurra un error humano. 
# Solo un error tipográfico y fr_speakers puede convertirse en fi_speakers, ¡y te resultará difícil averiguar por qué desaparecieron todos esos hablantes de francés! 
# ¡Tal vez fue el invierno finlandés y no un error tipográfico!
# Para ayudarte a evitar esos errores, existe un método más corto y útil llamado asignación aumentada. En Python, se ve así:

fr_speakers = 284.9
fr_speakers += 2.5
print(fr_speakers)

# ¡Lo conseguimos de nuevo! Los operadores de asignación aumentada funcionan de la misma manera que otros operadores aritméticos. 
# Compruébalo por tu cuenta. Ejecuta el siguiente código para ver cómo las asignaciones aumentadas cambian el valor original de items.

items = 10

items += 5 # igual que items = items + 5
print(items)

items -= 5 # igual que items = items - 5
print(items)

items *= 3 # igual que items = items * 3
print(items)

items /= 5 # igual que items = items / 5
print(items)

# ¡Menos tecleo, mismos resultados!

# Ejercicio 1
# Pruébalo por tu cuenta en la siguiente tarea.
# Cambia el valor de it_speakers: agrégale 5 utilizando la asignación aumentada. Muestra el nuevo valor.

it_speakers = 67.8
it_speakers += 5    # actualiza aquí el valor de la variable
print(it_speakers)  # imprime aquí el valor de la variable

# Resultado: 72.8


# Funciones integradas
#
# Una gran ventaja de Python son las funciones integradas. 
# Los analistas y las analistas a menudo necesitan encontrar la suma o los valores mínimo y máximo de sus datos, 
# por lo que los desarrolladores y las desarrolladoras han creado funciones preparadas para estos cálculos.
#  - La función sum() toma una lista como argumento y devuelve la suma de sus elementos.
# - La función max() se usa para encontrar el valor máximo.
# - La función min() se usa para encontrar el valor mínimo de la lista.
#
# Observa cómo funcionan ejecutando el siguiente código:

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139, 133, 126]

total_duration = sum(movies_duration) #suma todos los elementos de la lista
max_duration = max(movies_duration) #obtiene el elemento más grande en la lista
min_duration = min(movies_duration) #obtiene el elemento más pequeño en la lista

print(total_duration)
print(max_duration)
print(min_duration)

# Resultado:
# 1595
# 201
# 126

# En conclusión, las funciones integradas de Python son increíblemente útiles para simplificar operaciones y cálculos complejos. 
# Los analistas pueden aprovechar estas funciones para calcular métricas importantes de forma rápida y sencilla a partir de sus datos. 
# ¡Las utilizarás mucho en tu futura profesión!
# Ahora pasemos al tema principal de este capítulo: los bucles.

# Fin.