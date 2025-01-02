# Capítulo 3/6
# Introducción al preprocesamiento de datos y al análisis inicial

## Ejercicios

# Ejercicio 1
# Escribe código que sume la cantidad de valores ausentes en todas las columnas del dataset. 
# Guarda el resultado en la variable mis_val y muéstralo.

# Código
import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
mis_val = df.isna().sum() # escribe tu código aquí
print(mis_val)

# Resultado
  user_id        0
total play     564
Artist        8316
genre         3302
track         3159
dtype: int64


## Teoria

# Eliminar filas
# Para eliminar filas con valores ausentes en un DataFrame de pandas, usa el método dropna(). 
# Este método elimina las filas con al menos un valor ausente. 
# También puedes especificar una lista de columnas en su parámetro subset= para que elimine filas con valores nulos solo en esas columnas.

# Así es como funciona:
cholera = cholera.dropna(subset=['total_cases', 'deaths', 'case_fatality_rate'])
print(cholera)

# Y ahora, la fila con datos de Europa ya no está.
# Ahora eliminemos toda la columna 'notes', que consiste casi en su totalidad en valores ausentes.
# Usaremos el método dropna() de nuevo, pero esta vez agregaremos otro argumento: axis=. 
# Este argumento nos permite especificar si queremos eliminar filas o columnas. Si pasamos el string 'columns' a axis=, 
# eliminará las columnas que tengan valores ausentes. Dado que 'notes' es la única columna que contiene valores ausentes, 
# podemos usar esta opción de forma segura para eliminarla.

cholera = cholera.dropna(axis='columns')
print(cholera)

# Debes saber que si tienes varias columnas con valores ausentes, cholera.dropna(axis='columns') las eliminará todas. 
# No es siempre lo que queremos. En su lugar, puedes usar el método drop() para controlar qué columnas quieres eliminar. 
# Esto es lo que debes hacer si solo quieres eliminar la columna 'notes' utilizando el método drop():

cholera = cholera.drop(labels=['notes'], axis='columns')

# Tanto drop() como dropna() admiten el argumento inplace=, lo que nos permite realizar la operación localmente sin reasignación. 
# Este es un ejemplo de cómo utilizar drop() para realizar un reemplazo localmente:

cholera.drop(labels=['notes'], axis='columns', inplace=True)

# Ahora que limpiamos los datos, serán más fiables para nuestro análisis.
# Si detectas valores ausentes, siempre es una buena idea discutirlos con quienes te proporcionaron los datos. 
# Es mejor hacer una pausa, saber por qué faltan datos y después abordar el problema. Luego puedes reanudar tu análisis.
# ¡Y ahora es tu turno para eliminar las filas no necesarias! Así que aquí tienes dos ejercicios más para que practiques.


## Ejercicio 2
# Escribe código para recorrer las columnas genre, Artist y track del DataFrame df y reemplaza cualquier valor ausente con el string 'no_info'. 
# La lista de columnas a reemplazar se almacena en la variable columns_to_replace.
# Después de realizar los reemplazos, comprueba la cantidad de valores ausentes nuevamente usando isna().sum()

# Código
import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

columns_to_replace = ['genre', 'Artist', 'track']

for col in columns_to_replace:
	# escribe tu código aquí
    df['genre'].fillna('no_info', inplace=True)
    df['Artist'].fillna('no_info', inplace=True)
    df['track'].fillna('no_info', inplace=True)

print(df.isna().sum())

# Resultado
Resultado
  user_id       0
total play    564
Artist          0
genre           0
track           0
dtype: int64


## Ejercicio 3
# Ahora, eliminemos los NaNs en la columna total play remplazándolos con 0.
# Después de realizar los reemplazos, comprueba la cantidad de valores ausentes nuevamente usando isna().sum()

# Código
import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
# escribe tu código aquí
df['total play'].fillna(0, inplace=True)
print(df.isna().sum())

# Resultado
  user_id        0
total play       0
Artist        8316
genre         3302
track         3159
dtype: int64

# Ahora ya puedes eliminar las filas no necesarias de tu dataset, y también trabajar con los datos ausentes de manera que realmente sirvan para tu análisis, en lugar de arruinarlo.
# En la siguiente lección continuaremos nuestro viaje para resolver problemas de contenido aprendiendo cómo procesar valores duplicados.

# Fin. 