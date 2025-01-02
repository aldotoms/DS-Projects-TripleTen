# Capítulo 4/6
# Trabajar con valores duplicados y ausentes

# **Contar valores ausentes**

# En las próximas lecciones, trabajaremos con un conjunto de datos de marketing de una empresa de comercio electrónico. 
# Los datos están en un archivo CSV llamado visit_log.csv y cada fila representa una visita al sitio web de una empresa. Hay cuatro columnas:
# 1.- 'user_id': identificador único para cada persona que visita el sitio web.
# 2.- 'source': fuente de tráfico de la visita al sitio web. Aquí nos interesan tres categorías para la fuente:
#       - Visitas desde enlaces de marketing por correo electrónico: 'email'
#       - Visitas de anuncios contextuales en línea: 'context'
#       - Visitas de cualquier otra fuente: 'other'
# 3.- 'email': dirección de correo electrónico encriptada asociada con la persona que visita el sitio.
# 4.- 'purchase': indica si la persona compró algo en esa visita (1 en caso afirmativo, 0 en caso negativo).

# Tu objetivo es determinar la tasa de conversión para cada fuente, que es la proporción de visitas en las que se realizó una compra con respecto al número total de visitas en general. 
# Comparar la tasa de conversión para cada fuente te permitirá determinar cuál de ellas genera la mayor cantidad de ventas.
# Pero antes de profundizar en los cálculos, necesitamos revisar el conjunto de datos para buscar valores ausentes y decidir qué hacer con ellos.

# *Buscar valores ausentes*

# Una buena manera de empezar a comprobar los valores ausentes es llamar al método info() de tu DataFrame, tal y como hicimos en el último capítulo.

# El método info() imprime el número de valores que no son ausentes en cada columna. Los valores nulos son valores ausentes, mientras que los no nulos son valores no ausentes. 
# Recuerda que info() solo reconocerá valores ausentes "verdaderos" como nulos (None o NaN), mientras que los valores ausentes representados por cualquier otra cosa no se considerarán como ausentes.
# Algunos ejemplos de valores ausentes de marcador de posición son el número 0, la cadena vacía '' u otras cadenas como 'None' (distinta al tipo None de Python).
# Nunca es una mala idea llamar a info() en un nuevo conjunto de datos. Echemos un vistazo a nuestro DataFrame de registros de visitantes, el cual hemos asignado a una variable llamada df_logs:

# Código
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

df_logs.info() # escribe tu código aquí

# Resultado:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200000 entries, 0 to 199999
Data columns (total 4 columns):
 #   Column    Non-Null Count   Dtype 
---  ------    --------------   ----- 
 0   user_id   200000 non-null  int64 
 1   source    198326 non-null  object
 2   email     13953 non-null   object
 3   purchase  200000 non-null  int64 
dtypes: int64(2), object(2)
memory usage: 6.1+ MB

# La salida info() muestra que nuestro conjunto de datos tiene 200 000 filas, pero las columnas 'source' y 'email' tienen menos de 200 000 valores no nulos. 
# ¡Esto significa que ambas columnas tienen valores ausentes! Aunque info() señala que tenemos valores ausentes, si nuestro objetivo es contar valores ausentes, entonces hay una mejor opción.

# Pregunta
# ¿Qué método aprendimos en el sprint de Python básico para encontrar y contar valores ausentes?

df.isna().sum()     # Sí, df.isna().sum() devuelve el número total de valores ausentes.
df.isnull().sum()   # Sí, df.isnull().sum() devuelve el número total de valores ausentes.

# Probemos esto en nuestro conjunto de datos:

# Código
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs.isna().sum()) # escribe tu código aquí)

# Resultado:

user_id          0
source        1674
email       186047
purchase         0
dtype: int64

# ¡Son bastantes! Pero hay otra forma de encontrar los valores ausentes.

# *Contar los valores ausentes con value_counts()*

# En vez de sumar los valores obtenidos con isna(), podemos contar los valores ausentes con el método value_counts(). 
# Al llamarlo en una sola columna (es decir, un Series), devuelve la cantidad de veces que cada valor único aparece en esa columna.
# Este método tiene un parámetro llamado dropna=, que se establece por defecto en True. Esto significa que value_counts() excluirá los valores None o NaN a menos que establezcas dropna=False.
# Utilicémoslo en la columna 'source' de nuestro DataFrame, asegurándonos de incluir los valores ausentes:

# Código:
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs['source'].value_counts(dropna=False))

# Resultado:

other      133834
context     52032
email       12279
NaN          1674
undef         181
Name: source, dtype: int64

# Podemos ver que la columna 'source' contiene valores para las fuentes de tráfico que nos interesan, que son:
# 'context' para anuncios contextuales, 'email' para correos electrónicos de marketing y # 'other' para todo lo demás. 
# También vemos que tenemos 1674 valores ausentes de la columna 'source', lo cual representa aproximadamente el 1% de los datos. 
# También está el valor 'undef', pero todavía no sabemos a qué se refiere.
# Como puedes ver, cuando imprimimos df_logs['source'].value_counts(dropna=False), la salida se ordena en orden descendente según el recuento de cada valor. 
# Alternativamente, podemos ordenar la salida alfabéticamente según los nombres de los valores. Para hacerlo, podemos utilizar el método sort_index().

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')
print(df_logs['source'].value_counts(dropna=False).sort_index())

# Obtenemos:

source
context     52032
email       12279
other      133834
undef         181
NaN          1674
Name: count, dtype: int64

# Acabas de utilizar el método value_counts() seguido del método sort_index(). En el mundo de los datos, es habitual aplicar varios métodos de manera consecutiva. 
# Más adelante en este sprint, verás muchas otras aplicaciones de esta técnica.

# Resumen
# Hay muchas formas de encontrar y contar valores ausentes en pandas. En esta lección aprendiste tres maneras:
#   - Llamar a info() en un DataFrame.
#   - Llamar a isna().sum() en un DataFrame o un Series.
#   - Llamar a value_counts(dropna=False) en un Series.
# Antes de pasar a cómo lidiar con los valores ausentes, vamos a investigar los valores ausentes en la columna 'email' en los ejercicios.

# Fin.