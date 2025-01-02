# Capítulo 2/5
# Estadística descriptiva

# Desviación estándar y distribución normal

# Desviación estándar y distribución normal
# Introducción a la desviación estándar
# Si los datos iniciales se midieron en, digamos, metros, usuarios o dólares, la varianza se medirá en los cuadrados de estas mismas unidades. 
# Sin embargo, esto es poco práctico para el uso diario.
# Para volver a las unidades originales, necesitamos (¡lo has adivinado bien!) sacar la raíz cuadrada de la varianza. El valor resultante se llama desviación estándar, que a veces se denomina std.
# Probablemente, ya te habrás dado cuenta de que "std" aparece en la salida del método describe(). Si no es así, aquí tienes un ejemplo:

import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 6])
s.describe()

# De las diversas métricas de dispersión, la desviación estándar es la que más se utiliza, ya que tiene las mismas unidades de medida que los datos.
# La desviación estándar se denota con sigma minúscula. Se eligió el símbolo sigma porque transmite el sonido "s", como en la palabra "standard" (estándar). 
# Así que la fórmula para la desviación estándar es:

# La desviación estándar de un dataset puede calcularse con el método std() de la librería NumPy:

import numpy as np

x = [1, 2, 3, 4, 5, 6] # dataset

standard_deviation = np.std(x)
print(standard_deviation)

# Supongamos que ya conoces la varianza de un dataset. Entonces puedes usar el método sqrt() de NumPy para calcular la desviación estándar:

import numpy as np

variance = 3.5
standard_deviation = np.sqrt(variance)
print(standard_deviation)

# Como sabemos, la distribución normal es simétrica en torno a la media o al centro del gráfico. 
# Esto significa que los datos situados cerca de la media aparecen con más frecuencia que los que están lejos de ella.
# La distribución de este tipo puede definirse mediante dos parámetros:
#   - La media (o promedio), que es el máximo del gráfico y en torno al cual el gráfico es siempre simétrico.
#   - La desviación estándar, que determina la dispersión con respecto a la media.
# Al igual que ocurre con la varianza, una desviación estándar menor (en comparación con la media) hace que el gráfico sea más empinado, 
# mientras que una desviación estándar mayor (también en comparación con la media) hace que el gráfico sea más plano:

# Si nuestros datos siguen una distribución normal, se aplica una regla importante, que es la regla de las tres sigmas. 
# Esta establece que casi todos los valores (99.7%) caen dentro de un rango determinado. Aquí tienes este rango:

(μ−3σ,μ+3σ)

# Recuerda que µ es la media y σ es la desviación estándar. 
# En otras palabras, el 99.7% de todos los valores se sitúan en un intervalo que comprende 3 desviaciones estándar a la izquierda y 3 a la derecha de la media. 
# Aquí tienes una ilustración de la regla de las tres sigmas para una distribución normal:

# Esta regla no solo nos permite encontrar un intervalo que contenga, con toda seguridad, casi todos los valores de nuestra variable, sino que también nos ayuda a detectar los valores que se encuentren fuera del mismo. 
# Estos valores se denominan valores atípicos. Merecen atención ya que su presencia en los datos puede brindar información importante sobre la variable o revelar errores de cálculo y problemas similares.

# *Ejercicios
# Ejercicio 1
# Calcula la desviación estándar del dataset data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) y guárdala en la variable standard_dev. Luego muestra los resultados.

# Código
import pandas as pd
import numpy as np

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

standard_dev = np.std(data) # escribe tu código aquí
print(standard_dev) # escribe tu código aquí

# Ejercicio 2
# El usuario promedio tarda 3 segundos en leer un mensaje en un sitio web. Esta es la media del conjunto de datos.
# Además, observamos que la varianza de los datos (que siguen la distribución normal) es de 0.25 segundos.
# Utilizando la regla de las tres sigmas descrita anteriormente, tenemos que calcular cuánto tiempo debe mostrarse un mensaje para que lo vea el 99.7% de los usuarios. 
# Para ello, sigue estos pasos:
#   1. Calcula la desviación estándar a partir de la varianza y guarda el resultado en la variable adv_std.
#   2. Dadas la media y la desviación estándar, calcula el límite superior del intervalo que representa el 99.7% de los usuarios. Almacena el valor resultante en la variable adv_time.
# Muestra tus resultados con el mensaje El tiempo de visualización del mensaje es.

# Código
import numpy as np

adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var) # calcula la desviación estándar

adv_time = adv_std * 3 + adv_mean 
print(f'El tiempo de visualización del mensaje es', adv_time) # escribe tu código aquí)

# Ejercicio 3
# Tu empresa organiza un concurso tipo trivia en un centro comercial.
# Por su experiencia en concursos similares, sabes que, por término medio, el 3% de los participantes responden correctamente a las preguntas, y que la desviación estándar es del 0.4%.
# Esperas que 6000 personas se presenten al concurso. Tienes que calcular cuántas personas podrían ganar para preparar una cantidad suficiente de premios. 
# En concreto, hay que determinar un intervalo para el número de ganadores tal que, con un 99.7% de probabilidad, el número real esté dentro de ese intervalo (es decir, entre x y y). 
# Vamos a utilizar la regla de las tres sigmas para calcular dicho intervalo.
# Una vez que lo hayas calculado, deberás imprimir los resultados de la siguiente manera: Intervalo: ... - ... (¡fíjate en los espacios alrededor del guion!)
# Para que esta tarea no sea tan abrumadora, vamos a desglosarla en pasos más sencillos:

#   1. Para empezar, calcula el promedio esperado de respuestas correctas de los participantes. 
#       Teniendo en cuenta el porcentaje medio de participantes que, como se espera, responderán correctamente (3% o 0.03) y el número previsto de participantes (6000), 
#       calcula la media y almacena el valor resultante en la variable quiz_mean.
#   2. A continuación, a partir del número total de participantes previstos (6000) y de un porcentaje dado para la desviación estándar (0.4% o 0.004), 
#       calcula la desviación estándar para el número de personas que participarán en el concurso. Este valor, σ, debe almacenarse en la variable quiz_std.
#   3. Por último, se nos pide que determinemos un intervalo para el número de ganadores. Según la regla de las tres sigmas, 
#       este intervalo comprende tres desviaciones estándar a la izquierda y 3 a la derecha de la media. Calcula los límites de dicho intervalo y 
#       guarda el límite inferior en la variable quiz_bottom_line y el límite superior en la variable quiz_top_line.
#   4. Muestra los resultados en el formato requerido.

# Código
quiz_mean = 6000 * 0.03
quiz_std = 6000 * 0.004

quiz_bottom_line = quiz_mean - 3 * quiz_std
quiz_top_line = quiz_mean + 3 * quiz_std

print(f'Intervalo:', quiz_bottom_line, '-', quiz_top_line)

# FIN.