# Capítulo 4/6
# Trabajar con valores duplicados y ausentes

# Rellenar los valores categóricos ausentes
# Antes de sumergirnos en cómo rellenar los valores ausentes, necesitamos un momento para analizar los dos tipos de variables con las que trabajarás como profesional de datos: cuantitativas y categóricas.

# *Variables cuantitativas vs. categóricas*
# Las variables cuantitativas tienen valores numéricos que podemos usar para cálculos aritméticos, por ejemplo, la altura, el peso, la edad y los ingresos. 
# En Python, estos valores tienden a almacenarse como números enteros o flotantes.
# Las variables categóricas representan un conjunto de valores posibles que puede tener una observación particular, por ejemplo, el color, la marca y el modelo de un automóvil. 
# En Python, estos valores tienden a almacenarse como cadenas, pero también pueden ser valores booleanos o incluso números enteros.
# # Algunos ejemplos de valores categóricos enteros son códigos postales o etiquetas numéricas que representan otros valores (por ejemplo, 1 = rojo, 2 = azul, etc.). 
# En cualquier caso, no tiene sentido realizar operaciones aritméticas con valores categóricos. 
# La forma en que rellenamos los valores ausentes depende de si son cuantitativos o categóricos.

# Pregunta
# En la última lección determinamos que en nuestras columnas de dirección de correo electrónico y fuente de tráfico hay valores NaN. ¿Qué tipo de variables son estas columnas?
# R. Tanto 'source' como 'email' son categóricas.
# Así es, ambas son categóricas.

# Tanto 'source' como 'email' son columnas categóricas. De hecho, cada columna en el conjunto de datos de fuente de tráfico es categórica. 
# En esta lección aprenderemos algunas formas efectivas de rellenar los valores categóricos ausentes.

# Pregunta
# Acuérdate del sprint de Python básico. Allí aprendimos un método para sustituir NaN por un valor de nuestra elección. 
# ¿Recuerdas cuál era? Escribe tu respuesta sin punto al principio pero con paréntesis al final.
# R. fillna()
# El método fillna() reemplaza NaN en el conjunto de datos con el valor que introducimos dentro del paréntesis.

# Los valores NaN en la columna 'email' sustituyen a las direcciones de correo electrónico de los usuarios y las usuarias que no se suscribieron al boletín de la tienda. 
# Ya que no hay forma de averiguar sus direcciones de correo electrónico, no podemos rellenar manualmente los valores ausentes con datos significativos.
# Pero podemos rellenarlos con un valor por defecto para representar los correos electrónicos ausentes. 
# Sustituyamos los valores ausentes en la columna 'email' por la cadena vacía '' como valor por defecto.
#   1. Utiliza el método fillna() para sustituir los valores ausentes en 'email' por cadenas vacías.
#   2.Imprime las cinco primeras filas del DataFrame.

# Código:

import pandas as pd
df_logs = pd.read_csv('/datasets/visit_log.csv')

df_logs['email'] = df_logs['email'].fillna('') # escribe tu código aquí

print(df_logs.head())

# Resultado:

      user_id   source       email  purchase
0  7141786820    other                     0
1  5644686960    email  c129aa540a         0
2  1914055396  context                     0
3  4099355752    other                     0
4  6032477554  context                     1

# Ahora, cuando imprimimos el DataFrame, no vemos nada para los valores de 'email' ausentes porque con la cadena vacía no hay nada que imprimir.

# Pregunta
# Recuerda que nuestro conjunto de datos tiene 200 000 filas y 186 047 valores ausentes en la columna 'email'. 
# Después de rellenar los valores ausentes con la cadena vacía '', 
# ¿cuántos valores no nulos encontrará info() para la columna 'email'?
# R. 200,000
# ¡Correcto!, info() solo reconoce NaN y None como valores nulos.
# Usar fillna() no es la única forma en que podemos rellenar los valores ausentes con cadenas vacías. Por cierto, también podemos hacerlo directamente al leer los datos mediante read_csv().


# *El parámetro keep_default_na=
# Si observas los datos de texto sin procesar en el archivo visit_log.csv, encontrarás que los valores ausentes están representados por la ausencia de texto. 
# En otras palabras, la ausencia de texto en visit_log.csv se interpreta como NaN. Consulta el archivo CSV en la pestaña de la lección.
# Pero podemos hacer que read_csv() lea la ausencia de texto como cadenas vacías en lugar de NaN, configurando el parámetro keep_default_na= en False. 
# Probémoslo en nuestro conjunto de datos:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)

print(df_logs.head())
print()
df_logs.info()

# Obtenemos:

      user_id   source       email  purchase
0  7141786820    other                     0
1  5644686960    email  c129aa540a         0
2  1914055396  context                     0
3  4099355752    other                     0
4  6032477554  context                     1

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200000 entries, 0 to 199999
Data columns (total 4 columns):
 #   Column    Non-Null Count   Dtype 
---  ------    --------------   ----- 
 0   user_id   200000 non-null  int64 
 1   source    200000 non-null  object
 2   email     200000 non-null  object
 3   purchase  200000 non-null  int64 
dtypes: int64(2), object(2)
memory usage: 6.1+ MB

# En la impresión podemos ver que los valores ausentes son cadenas vacías. 
# Ahora info() ya no detectará ningún valor nulo, esto significa que depende de nosotros reconocer que '' representa un valor ausente a medida que avanzamos con nuestro análisis.
# Ten en cuenta que establecer keep_default_na=False convierte todos los valores ausentes en cadenas vacías, incluso para columnas numéricas. 
# Esto hace que las columnas numéricas se lean como cadenas cuando tienen valores ausentes. 
# Así que asegúrate de usar solo keep_default_na=False cuando desees que todos los valores ausentes en cada columna se lean como cadenas vacías.
# En el caso de visit_log.csv, nos conviene hacer esto porque todas nuestras columnas son categóricas. 
# ¡Pudimos leer los datos y reemplazar todos los valores ausentes con tan solo una pequeña línea de código!
# Debido a que no podemos conocer las direcciones de correo electrónico de los visitantes que nunca proporcionaron una, tiene sentido usar la cadena vacía para esos valores ausentes. 
# Pero, ¿qué pasa con los valores de fuente de tráfico ausentes?
# Basándonos en los resultados de la lección anterior, sin duda, los valores ausentes en la columna 'source' realmente son visitas de enlaces de correo electrónico. 
# Puede que algo haya fallado en el seguimiento de estas visitas. Sea cual sea el caso, tenemos que cambiarlos manualmente.
# Lee los datos usando keep_default_na=False y luego imprime todos los valores únicos en la columna 'source'.

# Código:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)

df_sources = df_logs['source'].unique()
print(df_sources)

# Resultado:
['other' 'email' 'context' '' 'undef']

# Tenemos 5 valores distintos para la categoría de fuente de tráfico, y los valores ausentes ahora se representan con ''. 
# El valor para las fuentes de correo electrónico de marketing es la cadena 'email'. De acuerdo con nuestro análisis, queremos convertir todos los valores de '' a 'email'.

# Pregunta:
# Acuérdate del sprint de Python básico. Hemos aprendido un método para sustituir un valor por otro en una columna de un DataFrame. 
# ¿Recuerdas cuál era? Escribe tu respuesta sin punto al principio pero con paréntesis al final.
# R. replace()
# El método replace() al ser llamado en una columna de nuestro DataFrame nos permite cambiar un valor por otro. Recuerda que la sintaxis es replace(old_value, new_value).

# ¡Genial! ¡Ahora vamos a arreglar nuestros valores ausentes!
#   1. Utiliza replace() para reemplazar los valores ausentes en la columna 'source' por la cadena 'email'.
#   2. Verifica tu trabajo llamando al método unique() en la columna 'source' e imprime los resultados.

# Código:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)

df_logs['source'] = df_logs['source'].replace('', 'email') # escribe tu código a continuación

print(df_logs['source'].unique()) # escribe tu código a continuación)

# Resultado
['other' 'email' 'context' 'undef']

# Ahora que hemos rellenado los valores ausentes, podemos calcular la tasa de conversión para cada fuente. 
# Para ello, tendremos que utilizar la función groupby() para la agregación. Vamos a repasar rápidamente cómo utilizarlo.

# Pregunta:
# Tienes un DataFrame almacenado en la variable df_logs. Quieres agrupar los datos por la columna 'source' y extraer los valores de la columna 'user_id'. ¿Cómo lo harías?
# R. df_logs.groupby('source')['user_id']
# Así es. Es exactamente lo que queremos.

# Pregunta:
# Ahora que has repasado tus conocimientos sobre la agrupación, vamos a resumir los métodos que se pueden aplicar a los datos agregados. 
# En la prueba anterior, agrupaste los datos por la columna 'source' y extrajiste la columna 'user_id'. Ahora necesitas contar el número de repeticiones de cada valor en esa columna. 
# ¿Cómo completarías el código para obtener este recuento?
# R. df_logs.groupby('source')['user_id'].count()
# Así es. Es exactamente lo que queremos.

