# Sprint 5
# Análisis estadístico de datos

# *Prueba de hipótesis en Python. Valores p

# En Python, existen funciones que podemos utilizar para comprobar hipótesis. No es necesario que elijas un nivel de significación o que averigües si un valor se encuentra o no dentro de un intervalo crítico. 
# Una función devuelve la estadística de diferencia entre la media y el valor con el que lo estás comparando, y la importancia estadística de esta estadística es el valor p (de la palabra probabilidad).
# La estadística de diferencia es el número de desviaciones estándar entre los valores comparados si ambas distribuciones se convierten en una distribución normal estándar con media 0 y desviación estándar 1. 
# Este número no ayuda mucho a orientarse. Es razonable usar el valor p para decidir si aceptar o rechazar la hipótesis nula. 
# El valor p es la probabilidad de obtener un resultado al menos tan extremo como el que estás considerando, suponiendo que la hipótesis nula sea correcta. 
# El valor p está indicado como porcentaje e indica el área bajo la curva que corresponde a una probabilidad.
# Si este valor es superior al 10%, definitivamente no debes rechazar la hipótesis nula. Si el valor p es más bajo, es posible que debas rechazar la hipótesis nula. 
# Los valores de umbral convencionales son 5% y 1%.

# Si aceptas que el 5% de probabilidad es demasiado bajo y por eso rechazas la hipótesis nula, entonces cada 20 experimentos rechazarás la hipótesis no porque sea incorrecta, 
# sino porque el valor real resultó estar muy lejos del valor propuesto. Siempre depende del analista decidir qué umbral considerar suficiente.
# Si no hay muchos valores en cada muestra (no más de 20-30), la distribución correspondiente a la hipótesis nula será casi normal, solo un poco amplia. En otras palabras, 
# los datos insuficientes producen una gran variación. Esta distribución se llama Distribución de Student. Es una distribución de probabilidad similar a la distribución normal en su forma de campana, 
# pero tiene colas más gruesas. Se utiliza para estimar parámetros de población para tamaños de muestra pequeños o varianzas desconocidas.
# La distribución normal supone que se conoce la desviación típica de la población. Sin embargo, la distribución de Student no parte de este supuesto. 
# El número de valores observados (menos 1) utilizados para construir la distribución de Student se denomina oficialmente "grados de libertad" (k), que están relacionados con el tamaño de la muestra. 
# A medida que aumenta el número de grados de libertad (k), la distribución se aproxima más a una distribución normal con la misma media:

# La distribución de Student también se denomina distribución t, y la prueba estadística que la utiliza se denomina prueba t.
# Como analistas, no tenemos que preocuparnos de si la distribución t con la que trabajamos se aproxima o no a una distribución normal, ya que las funciones de la librería scipy la normalizan automáticamente, 
# por lo que se puede realizar una prueba estadística. La función scipy.stats.ttest_1samp (array, popmean) se usa para probar hipótesis del tipo "la media de la población es igual a x".
# ttest significa prueba t, del inglés t-test; 1samp significa que estamos trabajando con una muestra y comparándola con un valor dado.
# Pasamos estos parámetros a la función:
#   - array es una matriz que contiene la muestra.
#   - popmean es la media propuesta que estamos probando.

# Cuando se llama, la función devuelve la estadística de diferencia entre popmean y la media muestral de array. 
# También devolverá la significación estadística bilateral, que es la probabilidad de que la media de toda la población estadística se desvíe del valor propuesto al menos tanto como vemos en la muestra 
# (aumentando o disminuyendo en cualquier dirección). ¡Ahora veamos cómo funciona en la práctica! Tu socio comercial dice que el sitio web que creaste se ha convertido en un medio para atraer usuarios. 
# Dicen que los usuarios pasan dos horas al día en el sitio web. En otras palabras, nuestra hipótesis nula es que los usuarios pasan 2 horas en el sitio web.
# Han tomado una muestra de 200 personas de los registros de tiempo pasado en el sitio web. Vamos a comprobar la hipótesis de tu compañero realizando una prueba y comparando el valor p resultante con el umbral que fijaremos en el 5%.

from scipy import stats as st
import numpy as np
import pandas as pd

time_on_site = pd.read_csv('Datasets/user_time.csv')

interested_value = 120 # tiempo transcurrido en el sitio web

alpha = .05 # la significancia estadística crítica (umbral)

# realizar una prueba
results = st.ttest_1samp(
    time_on_site, 
    interested_value)

# imprimir el valor p resultante
print('valor p: ', results.pvalue)

# comparar el valor p con el umbral
if (results.pvalue < alpha):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

# El valor p resultante es 0.27702871, es decir, 27.7%. Esto representa la probabilidad de obtener un tiempo medio igual a 2 horas. 
# Dado que esta probabilidad es bastante alta, parece que los usuarios pasan realmente unas dos horas en el sitio web. 
# Utilizamos una prueba bilateral porque no nos importaba si el valor que obteníamos era superior o inferior al que proponía tu pareja (es decir, si era inferior o superior a 2 horas).
# Presta atención a cómo presentas tus resultados. Al principio de la lección dijimos que los datos nunca pueden probar o confirmar una hipótesis. Esto es de vital importancia. 
# Si solo tenemos una muestra no sabemos nada sobre toda la población estadística con certeza. Si lo supiéramos, no necesitaríamos una prueba estadística.
# Solo podemos hacer suposiciones sobre una población estadística y calcular la probabilidad de obtener una muestra dada si nuestras suposiciones fueran correctas. 
# Si la probabilidad es relativamente alta, los datos no nos dan motivos para rechazar una suposición. 
# Si la probabilidad es baja, entonces a partir de los datos proporcionados podemos concluir que nuestra suposición probablemente fue incorrecta (pero no podemos rechazarla o probar lo contrario).


# Ejercicio

# Eres el dueño de una cadena de estaciones de alquiler de patinetes llamada Scooters Get You There. 
# Hay 20 locales en el centro de la ciudad y cada uno tiene un máximo de 50 patinetes eléctricos. 
# Quieres probar la hipótesis de que en el último mes hubo un promedio de 30 patinetes disponibles en cualquier estación durante el día. 
# Un grupo urbano llamado 'Squirrel' destacó la importancia de este número en su estudio de la movilidad de los residentes. 
# Si hay menos patinetes en la estación, los usuarios pensarán que no podrán alquilar uno cuando lo necesiten, pero cuando haya más, 
# la gente pensará que no podrán aparcar su patinete después de un viaje porque no habrá aparcamiento.
# Cada hora, cada estación envía el número de patinetes disponibles al servidor. Has descargado los números de 13:00 a 16:00 durante los últimos 30 días. 
# Prueba tu hipótesis usando esta muestra. Establece un umbral de 5% para la significación estadística.

from scipy import stats as st
import pandas as pd

scooters = pd.Series([15, 31, 10, 21, 21, 32, 30, 25, 21,
28, 25, 32, 38, 18, 33, 24, 26, 40, 24, 37, 20, 36, 28, 38,
24, 35, 33, 21, 29, 26, 13, 25, 34, 38, 23, 37, 31, 28, 32,
24, 25, 13, 38, 34, 48, 19, 20, 22, 38, 28, 31, 18, 21, 24,
31, 21, 28, 29, 33, 40, 26, 33, 33,  6, 27, 24, 17, 28,  7,
33, 25, 25, 29, 19, 30, 29, 22, 15, 28, 36, 25, 36, 25, 29,
33, 19, 32, 32, 28, 26, 18, 48, 15, 27, 27, 27,  0, 28, 39,
27, 25, 39, 28, 22, 33, 30, 35, 19, 20, 18, 31, 44, 20, 18,
17, 28, 17, 44, 40, 33,])

optimal_value = 30 # escribe tu código aquí

alpha = 0.05 # establece la significación estadística crítica

results = st.ttest_1samp( # realiza la prueba t
    scooters,
    optimal_value)

print('valor p: ', results.pvalue) # extrae el valor p de los resultados de la prueba)

if (results.pvalue < alpha): # compara el valor p con el umbral alpha
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")

# FIN.