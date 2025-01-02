# Capítulo 3/5 · Faltan 2 lecciones
# Aprender Python más a fondo

## Pandas: estadística descriptiva

# A lo largo de tu reciente viaje de aprendizaje, has profundizado en los entresijos de los diccionarios, adquiriendo conocimientos sobre cómo iterar sobre ellos, 
# cómo gestionar estructuras anidadas y cómo manejar listas de diccionarios. Además, has explorado los aspectos más potentes de las funciones, que son los parámetros, los valores por defecto y los distintos tipos de argumentos. 
# Esta exploración también ha abarcado el objeto Series de Pandas, lo que ha mejorado tus habilidades de manipulación de datos. Ahora, te espera otro capítulo fascinante en el que te sumergirás en la estadística descriptiva. 
# Este paso te ayudará a profundizar en el análisis de datos, permitiéndote sacar conclusiones significativas de la información que tienes a tu alcance.
# Hasta ahora, hemos aprendido a limpiar datos, eliminando los duplicados y los valores ausentes, a agrupar los datos con groupby() y a ordenarlos. 
# Es momento de agregar más herramientas a nuestro arsenal, que nos proporcionen lo que necesitamos para hacer el análisis.
# Al analizar datos, siempre es importante comprender las características básicas de los datos, también conocidas como estadísticas descriptivas. 
# Has estudiado algunos métodos similares en el contexto de las listas, pero pandas proporciona un conjunto de métodos que facilitan la obtención de características básicas de los datos en DataFrames.
# Al final de esta lección, serás capaz de utilizar cuatro métricas simples para comprender las propiedades básicas de los datos: los valores máximo y mínimo, la mediana y la media. 
# Saber cómo usarlas te dará un muy alto nivel de sentido de cómo es la estructura de los datos. Podrás obtener el rango de los datos, una posible indicación de valores atípicos o valores sin sentido, 
# una idea de los valores típicos y un conocimiento de la magnitud y dirección de sesgo basado en la diferencia entre la media y la mediana. ¡Así que empecemos!


## Máximo

# Encontremos los valores máximos para la cantidad de segundos que se reprodujo cada canción (esta información ahora se almacena en la columna renombrada llamada 'total_play'). 
# Para encontrar el valor máximo, usa el método max():

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_processed.csv')

print(df['total_play'].max())

# ¡La canción más larga se reprodujo durante más de dos horas! Sería interesante saber qué pista era.
# Afortunadamente, podemos averiguarlo mediante la indexación lógica. Mostramos la fila del DataFrame para la cual 'total_play' es igual al valor máximo:

print(df[df['total_play'] == df['total_play'].max()])

# Desafortunadamente, no hay información sobre esta pista, ¡pero al menos sabemos que existe!
# Intenta hallar algunos números más grandes en el ejercicio.


## Ejercicios

# Ejercicio 1
# Llevaremos a cabo un análisis parecido solo para las canciones pop. En el siguiente código, filtramos el DataFrame original para extraer todas las filas correspondientes a canciones pop. 
# Luego, como hicimos en la lección, eliminamos todas las filas donde la columna 'total_play' tiene menos de 30 segundos porque asumimos que tales pistas se saltan.
# Busquemos la reproducción más larga de una pista de pop. Calcúlala y muestra el resultado.

# Código
import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_processed.csv')

pop_tracks = df[df['genre'] == 'pop']
pop_tracks = pop_tracks[pop_tracks['total_play'] > 30]

max_dur = pop_tracks['total_play'].max() # escribe tu código aquí
 
print(max_dur)


## Mínimo

# El valor mínimo, es decir, la pista reproducida durante el tiempo más corto, se puede encontrar con el método min().
# Ahora, si se salta una canción, 'total_play' será 0. Nos interesan las canciones que no se saltaron de inmediato, pero que tampoco se reprodujeron durante mucho tiempo. 
# Busquemos la canción más corta que se escuchó durante al menos medio minuto.
# Podemos comenzar realizando un segmento de las pistas escuchadas durante más de medio minuto y encontrando el valor mínimo:

df_drop_skip = df[df['total_play'] > 30]

print(df_drop_skip['total_play'].min())

# Ahora obtendremos los nombres de las pistas que se saltaron rápidamente. Aplicaremos la indexación lógica, como cuando buscábamos el valor máximo: 

print(df_drop_skip[df_drop_skip['total_play'] == df_drop_skip['total_play'].min()])

# Preferimos que nuestras listas de reproducción sean mezcladas, no revueltas. Según nuestros datos, podemos concluir que la duración de las canciones está dentro del rango de 30.004 a 4133.616327 segundos, 
# excluyendo las canciones saltadas. Sin embargo, no sabemos mucho sobre los valores que se encuentran entre estos extremos.
# Para obtener información sobre los valores en el medio, podemos calcular los valores de la mediana y la media. Echémosles un vistazo más de cerca.


## Mediana

# En estadística, la mediana es una medida que indica el valor central de un conjunto de datos. 
# Divide el conjunto en dos partes iguales: una parte tendrá valores menores que la mediana y la otra tendrá valores mayores que la mediana.

# Aquí hay algunos ejemplos simples para ilustrar cómo funciona la mediana:
# Número impar de valores. Supongamos que tienes el siguiente conjunto de números: [6, 3, 5, 9, 8]. Para encontrar la mediana, primero ordena los números: [3, 5, 6, 8, 9]. 
# Dado que este dataset contiene una cantidad impar de valores, la mediana es simplemente el valor medio, que es 6.
# Número par de valores. Vamos a añadir un valor más a nuestro dataset: [3, 5, 6, 8, 9, 12]. Dado que este conjunto contiene un número par de valores, 
# la mediana es el promedio de los dos valores centrales, que son 6 y 8. Así que la mediana de este conjunto de datos será (6+8)/2 = 7.
# Para resumir: si hay un número impar de valores, la mediana será el valor que se encuentra exactamente en el centro de la muestra ordenada. 
# Si hay un número par, la mediana se encuentra como la media de los dos valores vecinos en el medio de la muestra.
# Para calcular la mediana en pandas, puedes usar el método median(). Al igual que min() y max(), se puede aplicar a toda la tabla, una columna o datos agrupados.

print(df['total_play'].median())

# Ahora podemos aplicar la mediana a todos los valores de duración de escucha en nuestra tabla, excepto a las pistas escuchadas durante menos de 30 segundos, que consideramos saltadas.

df_drop_skip = df[df['total_play'] > 30]
print(df_drop_skip['total_play'].median())


## Media

# La media ("promedio" o "media aritmética") representa el valor promedio de un conjunto de datos.
# Ahora busquemos el promedio de todos los valores usando el método mean(). Para obtener este valor manualmente, sumaríamos todas las duraciones de las pistas y las dividiríamos entre el número de pistas.

print(df_drop_skip['total_play'].mean())

# ¡Bastante cerca de la mediana! Si la media fuera mucho mayor o menor, eso podría indicar la presencia de valores atípicos. Los valores atípicos son valores demasiado grandes o pequeños en comparación con el resto de los datos. 
# Hablaremos de los valores atípicos más adelante en el programa, así que no te preocupes por ellos por ahora.
# Por ejemplo, si descubrimos que alguien escuchó una canción durante más de 3 horas, se considerará un caso atípico y sospechoso. 
# Bueno, podría ser una canción en repetición (y probablemente la mejor canción de la historia), pero rara vez escuchamos una pista durante unas 3 horas.

# Sigamos hablando de los valores atípicos y cómo afectan la diferencia entre la media y la mediana. 
# Como mencionamos anteriormente, los registros que muestran que algunas personas escuchan una canción durante mucho tiempo se consideran atípicos. 
# Sin embargo, ¿qué pasa si tenemos muchas filas con duraciones similares en nuestros datos? 
# Si la proporción de tales filas es significativa, esto moverá la media y la hará más grande en comparación con la mediana.
# Así que nuestro mensaje clave aquí es que si ves una diferencia significativa entre la media y la mediana, esta indica que hay muchos valores atípicos en la columna que estás analizando. 
# ¡Recuerda, esto te será útil más adelante!

## Ejercicios

# Ejercicio 2
# Ya habíamos encontrado el valor máximo en el ejercicio anterior. Tu objetivo es calcular los valores medios y medianos para la columna 'total_play' e imprimirlos.

# Código
import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_processed.csv')

pop_tracks = df[df['genre'] == 'pop']
pop_tracks = pop_tracks[pop_tracks['total_play'] > 30]

pop_mean = pop_tracks['total_play'].mean() # escribe tu código aquí
pop_median = pop_tracks['total_play'].median() # escribe tu código aquí
 
print(pop_mean)
print(pop_median)

# ¡Y eso es todo, amigos! ¡Ya tienes todo lo que necesitas para ir a tu proyecto integrado!

# FIN.