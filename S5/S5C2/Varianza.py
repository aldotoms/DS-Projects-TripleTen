# Capítulo 2/5
# Estadística descriptiva

# Varianza

# En la lección anterior, calculamos la distancia promedio entre cada valor y la media, y nos salió 0. ¿Cómo puede ser eso si todos los valores del dataset son diferentes? 
# Aquí tienes el dataset como recordatorio: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. La media de este dataset era igual a 5.
#  Esto ocurrió porque calculamos la distancia para cada elemento del dataset respecto a la media. Lo hacemos restando la media de cada valor del dataset. Así es como se hace:

0 - 5 = -5
1 - 5 = -4
2 - 5 = -3
…
8 - 5 = 3
9 - 5 = 4
10 - 5 = 5

# Al calcular la distancia media, sumamos todas las diferencias. Algunas de estas distancias eran positivas y otras negativas, por lo que se anulaban entre sí, dando como resultado una suma de 0.
# Ahora vamos a deshacernos de los signos y a hacer que todos los valores sean positivos elevándolos al cuadrado:

(0 - 5)² = -5² = 25
(1 - 5)² = -4² = 16
(2 - 5)² = -3² = 9
…
(8 - 5)² = 3² = 9
9 - 5 = 4² = 16
10 - 5 = 5² = 25

# Los nuevos valores ya no representan la distancia media entre los valores del dataset y la media. En su lugar, representan el promedio del cuadrado de la distancia. 
# Si sumamos estos valores y los dividimos por su número total, obtendremos una métrica llamada varianza. Se calcula mediante la siguiente fórmula:
# En la fórmula anterior:
#   - σ² es la varianza.
#   - Σ es el símbolo de la suma.
#   - Xᵢ representa un valor del dataset.
#   - µ es la media.
#   - n es el número de valores del dataset.

# Se eligió el símbolo sigma (σ² ) para la varianza porque transmite el sonido "s", como en la palabra "standard". 
# En la próxima lección aprenderás que la raíz cuadrada de la varianza es la desviación estándar.
# Entonces, ¿qué nos dice la varianza? Muestra el grado de dispersión del conjunto de datos. Cuanto más dispersos estén los datos, mayor será la varianza en relación con la media.
# Observa el siguiente gráfico. Hay 3 distribuciones con diferentes varianzas.

# Como puedes ver, cuanto mayor sea la dispersión en el dataset, mayor será la varianza.

# Pregunta
# ¿En qué caso la varianza es igual a cero?
# R. Cuando todos los valores del dataset son iguales.
# Solo cuando todos los valores sean iguales, todas las distancias entre la media y los valores serán iguales a cero, y la suma de sus cuadrados, también. 
# En todos los demás casos, habrá una varianza distinta de cero, aunque sea pequeña.


# *Covarianza
# En muchas ocasiones nos puede interesar saber cómo depende una variable de otra. Por ejemplo, cómo depende el precio de una casa de su tamaño.
# Para comprobar si existe esta relación, podemos calcular la covarianza entre dos variables multiplicando sus diferencias por la media. La covarianza es una medida de su relación lineal.
#   - Siguiendo con nuestro ejemplo, xᵢ representa el tamaño de una casa en metros cuadrados, mientras que yᵢ representa su precio en USD.
#   - n es el número de valores del dataset (el número de casas y sus precios).
#   - Σ es el símbolo de la sumatoria.
#   - x̄ es el tamaño medio de las casas del dataset.
#   - ȳ es la media de los precios de las casas del dataset.

# Si la covarianza es cero, indica que no existe una relación direccional clara entre las variables. El valor de la covarianza puede tomar cualquier valor entre infinito negativo e infinito positivo. 
# Un valor negativo indica una relación inversa, mientras que un valor positivo indica una relación directa.

# Pregunta
# ¿Qué indica la covarianza negativa? Selecciona todas las opciones correctas.
# R. Cuanto más lejos esté el valor de la covarianza del 0, mayor será la dependencia entre dos variables. / Correcto. Y cuando la covarianza es 0, no hay dependencia en absoluto.
# R. Los valores negativos y cercanos a 0 indican una relación negativa débil. / ¡Correcto! Cuanto más se acerque el valor a 0, más débil será la dependencia entre las variables.

# Implementación en Python
# Para calcular la varianza en Python, necesitaremos la librería NumPy, el hermano mayor de pandas que ya conoces y amas.
# Mientras que la librería pandas va bien para estructuras, NumPy se usa para funciones matemáticas complejas. Puede ser importada de la siguiente manera:

import numpy as np

# La varianza de un conjunto de datos se puede encontrar mediante el método var():

x = [1, 2, 3, 4, 5, 6] # dataset

variance = np.var(x)
print(variance)

# Y así es como calculamos la covarianza:

x = [1, 2, 3, 4, 5, 6] # dataset 1
y = [41, 62, 89, 96, 108, 115] # dataset 2

covariance_matrix = np.cov(x,y) # calculamos la matriz de covarianza
covariance = covariance_matrix[0][1] # extraemos la covarianza como valor
print(covariance)

# La función cov() de NumPy devuelve una matriz 2D en la que el valor del índice [0][1] es la covarianza entre x y y.

# *Ejercicios*
# Ejercicio 1
# Calcula la varianza del dataset data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]). Muestra los resultados.
# Código

import pandas as pd
import numpy as np

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

variance = np.var(data)   # calcula la varianza aquí
print(variance)  # escribe tu código aquí

# FIN.