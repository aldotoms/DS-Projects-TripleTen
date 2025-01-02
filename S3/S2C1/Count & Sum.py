# Capítulo 1/6 · Faltan 2 lecciones
# La librería Pandas

# Vamos a contar y sumar (Count & Sum)

# Ahora que puedes acceder fácilmente a los datos de tus tablas utilizando las estrategias de filtrado que has aprendido en las lecciones anteriores, 
# es hora de ver su utilidad práctica. Como especialistas en datos, utilizamos datos para responder preguntas. 
# Al filtrar una tabla podemos encontrar respuestas a diversas preguntas y resolver distintos asuntos, 
# desde conocer las preferencias de los usuarios hasta lograr comprender las tendencias. 
# Vamos a responder algunas preguntas acerca de nuestros datos musicales.

# Aquí tenemos un ejemplo de análisis que podemos realizar. 
# Por ejemplo, si quieres saber cuánto tiempo, de promedio, reproduce un usuario una canción pop, 
# empieza por obtener una tabla filtrada que contenga solo canciones 'pop': 

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
pop_df = df[df['genre'] == 'pop']

# Ahora tenemos la variable pop_df que contiene una tabla filtrada de canciones pop. 
# Sin embargo, esta tabla es solo la mitad del trabajo. Nuestro objetivo es determinar la duración promedio. 
# Para lograrlo, necesitamos extraer la columna 'total play', que contiene la cantidad de tiempo (en segundos) que el usuario reprodujo una canción.

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
pop_df = df[df['genre'] == 'pop']

# extrae la columna total play (reproducción total) del DataFrame filtrado
pop_duration = pop_df['total play']
print(pop_duration)

# Si mostramos la variable pop_duration, veremos que esta es simplemente la columna 'total_play' extraída del DataFrame pop_df:

0         92.851388
4        193.776327
8          3.161000
11         0.000000
13         2.000000
            ...    
67921     18.554472
67937     68.495839
67952     44.200000
67958    220.551837
67961     11.529112
Name: total play, Length: 8663, dtype: float64


### Método Mean()

# Imagina que quieres calcular un promedio. Para lograrlo, simplemente aplica el método mean() y hará todo el trabajo duro por ti. 
# De esta forma:

mean_duration = pop_duration.mean()
print(mean_duration)

90.37219914513818

# Este es el código completo que escribimos para calcular y mostrar la media:

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
pop_df = df[df['genre'] == 'pop']
pop_duration = pop_df['total play']
mean_duration = pop_duration.mean()
print(mean_duration)

90.37219914513818

# La duración promedio de una canción pop es de unos 90 segundos. 
# Una parte considerable de nuestro código está dedicada solo al cálculo de este valor. 
# ¿Hay alguna forma de resolver esta tarea de una manera más directa, sin tener que declarar todas estas variables? 
# Sí, la hay. Descubre cómo puedes hacerlo:

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
mean_duration = df[df['genre'] == 'pop']['total play'].mean()
print(mean_duration)

90.37219914513818

# Ahora, veamos más detenidamente una línea de código que calcula el promedio por nosotros.

1. df[df['genre'] == 'pop'] filtra la tabla original y extrae solamente las filas con canciones pop.
2. Al agregar ['total play'], extraemos la columna 'total play' de la tabla filtrada.
3. Aplicamos el método mean() y este calcula el promedio por nosotros.
# Todo esto se logra en una sola línea de código, ¿no es genial?
# Es hora de que lo hagas tú.

# Ejercicio 1
# En escenarios de la vida real, las empresas a menudo quieren tener respuestas a preguntas específicas. 
# Por ejemplo, una empresa podría necesitar analizar los datos de un usuario cuyo 'user_id' sea igual a '5D9AAD37'.

# ¡Hagámoslo ahora! Para lograrlo, debes filtrar la tabla para extraer solo las filas relevantes para el usuario objetivo ('5D9AAD37') 
# y, luego, calcular la duración media de las canciones que este ha escuchado. Esta información se guarda en la columna 'total play'. 
# Tras calcular, guarda el resultado en la variable user_mean_dur y muéstralo.

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
user_mean_dur = df[df['user_id'] == '5D9AAD37']['total play'].mean() # escribe tu código aquí.
print(user_mean_dur)


### Método Count()

# mean() es un método que comúnmente se utiliza en el análisis de datos. 
# count() es otro método útil que hace un recuento del número de filas que cumplen un criterio particular. 
# Por ejemplo, podemos utilizarlo para calcular el número de canciones que los usuarios escucharon durante más de 3 minutos (180 segundos).

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
duration_threshold = 180
long_songs = df[df['total play'] > duration_threshold]['total play'].count()
print(long_songs)

19065

# Analicemos lo que hemos hecho:
# 1. Primero, definimos la variable duration_threshold y la establecemos como nuestro criterio.
# 2. Utilizando este criterio, filtramos el DataFrame original: Esto nos proporciona una nueva tabla que incluye solamente las canciones que duran más de 3 minutos.
# 3. De este DataFrame filtrado, podemos seleccionar cualquier columna, pero vamos a seleccionar la columna 'total_play', ya que es la que hemos utilizado para filtrar:
# 4. Por último, aplicamos el método count() para contar el número de filas en la columna 'total_play':
# Como hemos filtrado todas las pistas que duran menos de 3 minutos, este recuento representa el número de canciones que duran más de 3 minutos.
# Como resultado, ahora sabemos que 19 065 canciones de nuestra tabla original duran más de 3 minutos. ¡Ahora vamos a practicar!

# Ejercicio 2
# Escribe el código para contar el número de canciones donde 'Aura' es el artista. 
# Para ello, necesitarás la columna 'Artist'. Almacena el resultado en la variable aura_count. No olvides mostrar este número.

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
aura_count = df[df['Artist'] == 'Aura']['Artist'].count() # escribe tu código aquí
print(aura_count)

# Resultado: 5


### Método Sum()

# Finalmente, te mostraremos cómo funciona el método sum(). 
# Es parecido a los métodos mean() y count() que acabamos de analizar. 
# Este método suma los valores en una columna especificada.
# Por ejemplo, podemos utilizar el método sum() para calcular el tiempo total que pasa un usuario escuchando música. 
# Calculemos este tiempo para el usuario cuyo 'user_id' es '174C0ED6':

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
user_sum_dur = df[df['user_id'] == '174C0ED6']['total play'].sum()
print(user_sum_dur)

1003.6256215980322

# Como resultado, obtenemos el tiempo de reproducción total de nuestro usuario.
# Ahora vamos a practicar un poco.

## Ejercicio 3
# Escribe un código que calcule el número total de segundos que nuestros usuarios escucharon canciones del artista 'Zodiac'. 
# Almacena el resultado en la variable zodiac_total y muéstralo.

# Código
import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv')
zodiac_total = df[df['Artist'] == 'Zodiac']['total play'].sum() # escribe tu código aquí
print(zodiac_total)

# Resultado 501.210367

# Estos tres métodos son realmente útiles en el análisis de datos. 
# Te ayudan a obtener información sin mucho esfuerzo, así que tenlos siempre a mano a la hora de programar. 
# Teniendo esto en mente, continuemos con un poco más de teoría.

# Fin.