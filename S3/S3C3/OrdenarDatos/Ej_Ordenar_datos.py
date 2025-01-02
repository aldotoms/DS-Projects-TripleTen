# Capítulo 3/6 · Faltan 2 lecciones
# Introducción al preprocesamiento de datos y al análisis inicial

# Ejercicio
# En la lección anterior, agrupaste nuestros datos music_log_processed.csv por 'genre' y calculaste el tiempo total que nuestros oyentes pasaron escuchando cada género. 
# Como resultado, en el que tenemos el tiempo de escucha total para cada 'genre'. Está almacenado en la variable time_by_genre en el precódigo.
# Ahora, ordenemos los resultados en orden descendente y veamos los 10 géneros principales que nuestros oyentes escucharon más. 
# Hazlo y guarda los resultados en la variable time_by_genre_sort.
# Toma nota que para esta tarea no necesitas especificar la columna que se va a ordenar, ya que solamente hay una columna en la variable time_by_genre.

# Código

import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

time_by_genre = df.groupby('genre')['total_play'].sum()

time_by_genre_sort = time_by_genre.sort_values(ascending=False) # escribe tu código aquí

print(time_by_genre_sort.head(10))

# Resultado
genre
dance          731069.475673
pop            727425.542459
electronic     679635.298107
rock           630434.772021
hiphop         297112.321237
classical      271098.177081
world          256630.643956
jazz           213871.653640
alternative    170130.211929
metal          154435.488092
Name: total_play, dtype: float64

# Si tienes preguntas muy precisas, como qué planeta tiene el radio más similar al de la Tierra, ¡el ordenamiento te ayudará a obtener la respuesta muy rápidamente! 
# ¡Con algo de ayuda de nuestra amiga la indexación!
# Ahora que nuestros datos ya no tienen ningún problema y están agrupados y ordenados como lo necesitamos, ¡practiquemos un poco más! 
# ¡Y eso es justo lo que haremos en la siguiente lección!

# Fin.