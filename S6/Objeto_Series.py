# Capítulo 3/5 · Faltan 3 lecciones
# Aprender Python más a fondo

## Pandas: el objeto Series

# En el segundo sprint hemos aprendido a utilizar los métodos count(), sum() y mean() para calcular datos de forma sencilla y directa. 
# También hemos aprendido a crear y manipular DataFrames en Pandas para obtener resultados sorprendentes al manipular y analizar datos.
# En esta lección conoceremos una nueva estructura de datos: el objeto Series. Un Series es básicamente una columna de un DataFrame. 
# Por ejemplo, cuando filtramos un DataFrame y extraemos una columna específica, esa columna se convierte en un Series.
# Es importante conocer la diferencia entre un DataFrame y un Series porque, por un lado, hay métodos y atributos que son exclusivos para uno u otro y, por otro, 
# algunos de los métodos que se pueden aplicar a ambos objetos se comportan de forma diferente según se trate de un DataFrame o de un Series.
# Al final de esta lección, podrás comparar y contrastar objetos DataFrames con objetos Series, así como utilizar la indexación mediante Series. 
# La indexación es una habilidad crucial para acceder a los elementos de un objeto Series, que con frecuencia se necesita para procesar los datos de alguna manera.
# Recapitulemos lo que sabemos hasta ahora. Cuando recuperas varias columnas o filas de una tabla, obtienes una nueva tabla que es un DataFrame; puedes comprobar su tipo mediante la función type. 
# Vamos a echar un vistazo:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

part_df = df[['genre', 'Artist']]
print(type(part_df))

# La tabla original tiene el mismo tipo. Échale un vistazo:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')
print(type(df))

# Como puedes ver, efectivamente tienen el mismo tipo.
# Supongamos ahora que solo deseas recuperar una columna. Puedes hacerlo fácilmente pasando el nombre de la columna entre corchetes: esto devolverá un objeto Series. 
# Observa:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

part_df = df['Artist']
print(type(part_df))
print(part_df)

# Hemos extraído la columna Artist y ahora la tenemos como objeto Series.
# Un Series es un bloque que compone una tabla; veamos cómo se estructuran.

# Cada columna en un DataFrame es un objeto Series. Como ya vimos, es posible recuperar Series separados de un DataFrame.
# Para acceder a los datos en un DataFrame se utilizan dos coordenadas (nombre de columna e índice), mientras que para acceder a los datos de un Series solo se utilizan los valores del índice. 
# Por lo tanto, nos referimos a un Series como a una estructura unidimensional.
# También, los objetos Series tienen un atributo name:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

part_df = df['Artist']
print(part_df.name)

# Cuando extraes una columna de un DataFrame a un objeto Series, el atributo name adopta el nombre de la columna, como puedes ver arriba. 
# Asimismo, cuando se construye un DataFrame a partir de Series individuales, el nombre de un objeto Series se convierte en el nombre de la columna.
# Además del nombre, un Series tiene longitud, es decir, el número total de celdas. Se puede acceder a la longitud mediante el atributo size:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

part_df = df['Artist']
print(part_df.size)

# Este Series tiene 67 963 elementos, o celdas.
# Por supuesto, existen otros atributos para Series, pero name y size son los que más utilizamos.


## Indexación en un Series
# La indexación de un Series es similar a la indexación de una lista. Para extraer un valor de una celda en función de su índice, simplemente pasa el valor del índice entre corchetes:

import pandas as pd
df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

# obtenemos un objeto Series a partir del DataFrame
artist = df['Artist']

# obtenemos una celda de un Series con una sola coordenada
print(artist[0])

# Como puedes ver, hemos extraído el primer elemento del Series al pasar el índice 0. Esto significa que, al igual que ocurre con las listas, la indexación de los objetos Series también empieza en 0.
# La indexación de Series es similar a la indexación de DataFrame en lo que respecta a la utilización del atributo loc y una notación abreviada. Consulta la siguiente tabla para ver el listado completo:

#   Tipo	                    Notación completa	                Notación abreviada
#   Un elemento	                total_play.loc[7]	                total_play[7]
#   Múltiples elementos	        total_play.loc[[5, 7, 10]]	        total_play[[5, 7, 10]]
#   Múltiples elementos 
#   consecutivos (slice)	    total_play.loc[5:10] incluyendo 10	total_play[5:10] sin incluir 10
#   Todos los elementos a 
#   partir del elemento dado    total_play.loc[1:]	                total_play[1:]
#   Todos los elementos hasta 
#   el elemento dado	        total_play.loc[:3] incluyendo 3	    total_play[:3] sin incluir 3

# Ahora vamos a practicar la indexación de Series.
# Extrae la columna 'track' del DataFrame original y almacénala en la variable tracks. Este será tu Series. 
# A continuación, obtén los primeros 20 elementos de este Series y guárdalos en la variable top20. Muestra la variable.

# Código
import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

tracks = df['track'] # escribe tu código aquí
top20 = tracks[0:20] # escribe tu código aquí

print(top20)


# Filtrado de un Series
# La indexación lógica funciona también para Series y es más simple que la de DataFrames. 
# En un Series, no es necesario indicar la columna de la que proceden los datos, basta con indicar una sola condición lógica. 
# A continuación, se muestra un ejemplo en el que comprobamos, utilizando una notación abreviada, que el valor de 'total play' sea inferior a 20:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

total_play = df['total play']
lower_20 = total_play < 20

print(lower_20)

# El resultado muestra el índice de cada canción del Series junto con el valor booleano que puede ser True, si la canción ha sido reproducida durante menos de 20 segundos, o False, en caso contrario.
# Si solo necesitas analizar una columna de la tabla, puede ser una buena idea almacenar esta columna en una variable separada (como lo hicimos con la variable total_play); 
# de esta forma, no necesitarás indicar el nombre de la columna cada vez que desees analizarla.
# Es interesante que ahora podemos utilizar este nuevo Series con valores booleanos para filtrar el DataFrame original. Así es como puedes hacerlo:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

total_play = df['total play']
lower_20 = total_play < 20

df_lower20_only = df[lower_20]

print(df_lower20_only)

# Como resultado, la tabla original ahora se filtra de forma que solo contenga filas en las que los valores de la columna 'total play' sean inferiores a 20. 
# Y aquí tenemos 33 868 canciones de las 67 963 que figuran en nuestro conjunto de datos. Eso significa que casi la mitad de nuestras canciones no han sido prácticamente escuchadas.
# Otra opción sería filtrar el Series y obtener solo los valores que cumplan con tus criterios. 
# Por ejemplo, cuando obtenemos un Series con valores booleanos, podemos utilizarlo para filtrar el Series original total_play:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

total_play = df['total play']
lower_20 = total_play < 20

series_lower20_only = total_play[lower_20]

print(series_lower20_only)

# Mediante este proceso de filtrado, recuperamos solamente los valores que cumplen con nuestros criterios; en otras palabras, obtenemos un Series en el que todos los valores son menores que 20.
# Ahora vamos a practicar el filtrado de un Series.

# Tu objetivo ahora es filtrar el DataFrame original extrayendo solo las canciones pop. ¿Cómo lo harías?
# En primer lugar, extrae la columna 'genre' del DataFrame original y almacénala en la variable genre. De este modo se creará un Series. Ahora comprueba que los valores del Series sean iguales a 'pop'. 
# Esta comprobación de igualdad es un poco contraintuitiva, así que consideremos otro ejemplo en el que necesitamos comprobar que los valores del Series 
# para el nombre de la canción sean iguales a 'Andrew Paul Woodworth'. Así es como se hace:

import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

tracks = df['track']
track_check = tracks == 'Andrew Paul Woodworth'

print(track_check)

# Esperamos que este ejemplo sea suficiente para ilustrar cómo comprobamos la igualdad. Ahora, volvamos a nuestra tarea anterior.
# Entonces, el primer paso consiste en extraer la columna 'genre' del DataFrame original y almacenarla en la variable genre. 
# A continuación, teniendo en cuenta el ejemplo anterior, hay que comprobar que los valores del Series sean iguales a 'pop'. 
# El resultado de esta comprobación se almacena en la variable pop_genre_check. 
# Finalmente, utiliza la variable pop_genre_check para filtrar el DataFrame original df para incluir solo las canciones pop. 
# Almacena este DataFrame filtrado en la variable pop_df y muéstrala.

# Código
import pandas as pd

df = pd.read_csv(r'C:\Users\aldot\TripleTen_DS_Local\datasets\music_log_chpt_11.csv')

genre = df['genre'] # escribe tu código aquí
pop_genre_check = genre == 'pop' # escribe tu código aquí
pop_df = df[pop_genre_check] # escribe tu código aquí

print(pop_df)

# Y ahora la librería pandas está bajo tu dominio, ¡con todas las herramientas que necesitas para domar a esta bestia!

# FIN.