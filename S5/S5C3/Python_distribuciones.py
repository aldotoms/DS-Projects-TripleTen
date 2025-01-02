# Capítulo 3/5
# Teoría de la probabilidad

# *Usar Python para trabajar con distribuciones*

# Para crear datasets con varios tipos de distribución, vamos a utilizar la librería NumPy. 
# Esta librería trabaja con matrices de datos de muchas dimensiones y dispone de formas rápidas de realizar cálculos complicados con muchos números a la vez.
# Como recordarás, el objeto principal de la librería NumPy es un ndarray (array N-dimensional), que es un array multidimensional que contiene elementos del mismo tipo. 
# El tamaño de un array NumPy se determina en el momento de su creación y no puede modificarse durante la ejecución del código.
# Para crear ndarray utilizamos la función np.array(). Como argumento, debes especificar una lista de datos que deben colocarse en un array:

import numpy as np
data = np.array([1, 3, 5, 7, 11, 13, 17, 19, 23, 317])

# Puedes acceder a los elementos de un ndarray utilizando índices, igual que hacías con las listas:

print('El primer elemento:', data[0])
print('El último elemento:', data[-1])
print('Todos los elementos excepto el primero y el último:', data[1:-1])

# NumPy puede utilizarse para generar números aleatorios con una distribución especificada, mediante la función normal() del módulo random. 
# Para generar un array de 20 números que sigan una distribución normal, utiliza el siguiente código:

import numpy as np

data = np.random.normal(size = 20)
print(data)

# Ten en cuenta que estos datos, data, pueden variar ya que los números se generan aleatoriamente.
# Para generar un array con una media y una desviación estándar dadas, tenemos que especificar los valores de estos parámetros:

import numpy as np

mean = 15  # media entre 1 y 30
std_dev = 5  # desviación estándar aleatoria

data = np.random.normal(mean, std_dev, size = 20)
print(data)

# Ahora, está todo listo para trabajar con los datos. Supongamos que el array contiene los datos del peso de los paquetes comprados por los 30 primeros visitantes de la tienda. 
# ¿Cuántos visitantes se fueron con un paquete que pesaba más que la media?

# declara una variable para almacenar el número de visitantes.
# como aún no hemos empezado a contar,
# el número de visitantes con una bolsa pesada es cero.
visitors_number = 0

# crea un bucle para iterar consecutivamente sobre el peso de cada bolsa.
for weight in data:

    # si el peso de la bolsa actual es mayor que la media, aumenta el contador.
    if weight > mean:
        visitors_number += 1

# muestra el número de visitantes con bolsas pesadas.
print('Número de visitantes con bolsas pesadas:', visitors_number)

# Ahora es el momento de practicar.


# *Ejercicios*
# Ejercicio 1
# Tenemos a 30 estudiantes que realizaron un examen. Sus puntuaciones se almacenan en la variable exam_results. 
# Si un estudiante obtuvo menos de 20 puntos, reprobó el examen. Escribe un programa que cuente cuántos estudiantes reprobaron el examen y almacena el resultado en la variable failed_students. 
# Muestra el resultado.

import numpy as np

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)

failed_students = 0 # valor inicial

# código para los cálculos
for result in exam_results:
    if result < 20:
        failed_students += 1
    
print('Número de estudiantes reprobados:', failed_students)

# Ejercicio 2
# Vamos a seguir con los resultados del examen. Ahora tenemos que contar no solo a los estudiantes que reprobaron, sino también a los que obtuvieron otros resultados: 
# excelente (90 puntos o más), notable (70-89 puntos), satisfactorio (50-69) y aprobado (20-49).
# Crea un diccionario summarized_data y escribe código para rellenarlo con los datos necesarios.

import numpy as np

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)

summarized_data = {'excellent': 0, # añade el valor inicial aquí,
                   'good': 0, # añade el valor inicial aquí,
                   'average': 0, # añade el valor inicial aquí,
                   'passable': 0, # añade el valor inicial aquí,
                   'failed': 0, # añade el valor inicial aquí
                  }

# escribe aquí el código para contar el número de estudiantes para cada tipo de resultados obtenidos.
for result in exam_results:
    if result >= 90:
        summarized_data['excellent'] += 1
    elif result >= 70:
        summarized_data['good'] += 1
    elif result >= 50:
        summarized_data['average'] += 1
    elif result >= 20:
        summarized_data['passable'] += 1
    elif result < 20:
        summarized_data['failed'] += 1

# código para mostrar los resultados en pantalla. No lo cambies.
for result in summarized_data:
    print(result, '-', summarized_data[result])


# FIN.