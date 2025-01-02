# Capítulo 4/6 · Faltan 2 lecciones
# Trabajar con valores duplicados y ausentes

# *Gestión de duplicados
# Ahora que sabes cómo lidiar con los valores ausentes, es momento de aprender algunas técnicas para lidiar con otro problema común en la etapa de preprocesamiento de datos: los valores duplicados.
# En el sprint de Python Básico, conociste los métodos duplicated() y drop_duplicates(). En esta lección, revisaremos estos conceptos y otras formas de abordar la duplicación de datos.

# Buscar duplicados a mano
# El análisis que realizaste previamente sobre las fuentes de tráfico para el sitio de comercio electrónico online generó más preguntas en el equipo a cargo de atraer nuevos clientes. 
# Quieren saber si hay una marca popular de teléfonos móviles que no esté suficientemente representada en el sitio web, 
# así como estadísticas que comprueben qué modelos de teléfonos les interesan más a la clientela.
# Para empezar, quieren que averigües cuántas tiendas ya están vendiendo ciertos teléfonos en un mercado online.
# Para completar este análisis, utilizamos nuestro viejo amigo read_csv() para leer el conjunto de datos /datasets/phone_stock.csv, guardándolo en la variable df_stock. 
# Imprime las cinco primeras filas de la tabla.

# Código:

import pandas as pd     # escribe tu código aquí
df_stock = pd.read_csv('/datasets/phone_stock.csv')
print(df_stock.head(5))

# Resultado:

          id                     item  count
0  100480924     Apple iPhone Xr 64gb     10
1  100480924     Apple iPhone Xr 64GB     19
2  100480959     Xiaomi Redmi 6A 16GB     44
3  100480975          HUAWEI P30 lite     38
4  100480988  Samsung Galaxy A30 32GB     49

# La tabla tiene:
#   - una columna 'id' con los ID de los productos;
#   - una columna 'item' con los nombres de los modelos;
#   - una columna 'count' con el número total de teléfonos disponibles para determinados modelos.
# En las dos primeras filas ya podemos ver datos duplicados.
# En el caso del iPhone Xr 64 GB de Apple, solo debería haber una fila de datos y el recuento en esa fila debería ser 29. 
# ¿Qué pasa si los datos de algunos de los otros teléfonos también están duplicados en otra parte de la tabla? 
# Necesitamos poder analizar todo el conjunto de datos a la vez, en lugar de esperar encontrar duplicados leyendo una copia impresa de los datos.

# *Revisión: encontrar datos duplicados
# Hay dos técnicas que funcionan para encontrar datos duplicados:
# Técnica 1
# Podemos utilizar el método duplicated() junto con sum() para obtener el número de valores duplicados en una sola columna o filas duplicadas en un DataFrame. 
# Recuerda que si llamas a duplicated() sin utilizar sum(), se imprimirá una serie booleana tan larga como el DataFrame, con True donde hay un duplicado y False donde no lo hay. 
# Ejecuta el siguiente código para ver un ejemplo:

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Así es como se ve el dataset:')
print(df)
print('Así es como se ve una serie booleana devuelta:')
print(df.duplicated())
print('Así se ve el resultado de duplicated() con sum():')
print(df.duplicated().sum())

# Devuelve:

Así es como se ve el dataset:
    col_1  col_2
0     A      1
1     B      2
2     A      2
3     A      1

Así es como se ve una serie booleana devuelta:
0    False
1    False
2    False
3     True
dtype: bool

Así se ve el resultado de duplicated() con sum():
1

# Por lo tanto, para comprobar la presencia de duplicados, utiliza el método duplicated() seguido del método sum(). Por cierto, puedes visualizar los duplicados mediante un simple filtrado:

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print(df[df.duplicated()])

# Devuelve:

    col_1  col_2
3     A      1

# Obtenemos como salida la cuarta fila (la fila con índice 3) porque esta fila es un duplicado de la primera fila (la fila con índice 0).

# *Técnica 2
# Llama al método value_counts(). Este método identifica todos los valores unívocos en una columna y calcula cuántas veces aparece cada uno. 
# Podemos aplicar este método a los Series para obtener los pares valor-frecuencia en orden descendente. 
# Las entradas que se duplican con más frecuencia se encuentran en la parte superior de la lista. A continuación te mostramos un ejemplo:

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Así es como se ve el dataset:')
print(df)
print()
print('Este es el resultado de la llamada al método value_counts() para col_1:')
print(df['col_1'].value_counts())

# Devuelve:

Así es como se ve el dataset:
  col_1  col_2
0     A      1
1     B      2
2     A      2
3     A      1

Este es el resultado de la llamada al método value_counts() para col_1:
A    3
B    1
Name: col_1, dtype: int64

# La letra A aparece tres veces, mientras que la B solo aparece una vez. Sin exploración adicional, no podemos concluir que hay tres filas duplicadas en las que 'col_1' es A. 
# Sin embargo, ahora tenemos una hipótesis de que podría ser el caso. Por ejemplo, en cuanto a teléfonos, 
# hay dos filas con Apple iPhone Xr 64gb que definitivamente vamos a fusionar para tener una idea clara sobre el stock.

# *Gestión de duplicados
# Como ya aprendimos en el sprint de Python Básico, las filas completamente duplicadas, 
# como la primera y la última fila del DataFrame del ejemplo anterior, se pueden tratar utilizando el método drop_duplicates():

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Dataset original:')
print(df)
print()
print('Dataset con duplicados eliminados:')
print(df.drop_duplicates())

# Devuelve:

Dataset original:
  col_1  col_2
0     A      1
1     B      2
2     A      2
3     A      1

Dataset con duplicados eliminados:
  col_1  col_2
0     A      1
1     B      2
2     A      2

# Si solo deseas considerar duplicados en una (o algunas) de las columnas en lugar de filas completamente duplicadas, puedes usar el parámetro subset=. 
# Pásale el nombre de la columna (o la lista de nombres de columna) donde deseas buscar duplicados:

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print(df)
print()
print(df.drop_duplicates(subset='col_1'))

# Devuelve:

  col_1  col_2
0     A      1
1     B      2
2     A      2
3     A      1

  col_1  col_2
0     A      1
1     B      2

# Pero la naturaleza de los datos duplicados de nuestro teléfono es un poco diferente a este ejemplo de DataFrame. Echémosle otro vistazo:

import pandas as pd

stock = pd.read_csv('/datasets/phone_stock.csv')
print(stock['item'].value_counts())

# Devuelve:

Apple iPhone Xr 64gb       1
Apple iPhone Xr 64GB       1
Xiaomi Redmi 6A 16GB       1
HUAWEI P30 lite            1
Samsung Galaxy A30 32GB    1
Samsung Galaxy A30 32gb    1
Honor 8X 64GB              1
Name: item, dtype: int64

# Hay dos entradas para el Samsung Galaxy y el iPhone de Apple. La única diferencia entre las dos entradas para ambos teléfonos es gb frente a GB. 
# En realidad son duplicados, pero Python no los reconoce como tales porque las cadenas no son idénticas.

# La forma más sencilla de manejar entradas duplicadas como estas es hacer que todas las letras de las cadenas estén en minúsculas, utilizando el método lower(). 
# A continuación te mostramos un ejemplo:

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

print('Col_1 original en el dataset:')
print(df['col_1'])
print()
print('Dataset con valores reducidos en col_1')
print(df['col_1'].str.lower())

# Observa que después de df['col_1'], tenemos .str, que nos permite aplicar métodos de cadena directamente a la columna. 
# Esto es exactamente lo que hay que hacer para poder aplicar el método lower() en el siguiente paso.
# Ten en cuenta que si quieres sustituir la columna original por una nueva en la que todas las letras estén en minúsculas, tendrás que volver a hacer la asignación.

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

# sustituir la columna col_1
df['col_1'] = df['col_1'].str.lower()
print(df)

# Devuelve:

    col_1  col_2
0     a      1
1     b      2
2     a      2
3     a      1

# Debes asegurarte de que las mayúsculas no sean importantes antes de hacer que todas las cadenas estén completamente en minúsculas.
# Es posible que queramos comprobar el número de duplicados verdaderos en la columna 'col_1' después de transformar su contenido a minúsculas::

import pandas as pd
df = pd.DataFrame({'col_1': ['A', 'B', 'A', 'A'], 'col_2': [1, 2, 2, 1]})

df['col_1'] = df['col_1'].str.lower()
print(df['col_1'].duplicated().sum())

# Devuelve: 2

# Como se esperaba, obtuvimos 2 como salida. Esto se debe a que la tercera y la cuarta fila son idénticas a la primera.
# Si quieres cambiar las mayúsculas y minúsculas en solo una parte de un string, puedes usar el método replace() que aprendiste en los sprints de Python básico. 
# Por ejemplo, podrías cambiar todas las apariciones de 'GB' a 'gb' en la columna 'item' de los datos del teléfono:

import pandas as pd

stock = pd.read_csv('/datasets/phone_stock.csv')
stock['item'] = stock['item'].str.replace('GB', 'gb')

print(stock.head())

# Devuelve:

    id                  item             count
0  100480924     Apple iPhone Xr 64gb     10
1  100480924     Apple iPhone Xr 64gb     19
2  100480959     Xiaomi Redmi 6A 16gb     44
3  100480975          HUAWEI P30 lite     38
4  100480988  Samsung Galaxy A30 32gb     49


# Si no estás seguro de cuál es el mejor enfoque, siempre puedes conservar la columna original y crear una nueva columna adicional, con las cadenas modificadas. 
# Por ejemplo, podrías guardar el resultado de la sustitución en la columna 'item' en una nueva columna llamada 'item_modified':

import pandas as pd

stock = pd.read_csv('/datasets/phone_stock.csv')
stock['item_modified'] = stock['item'].str.replace('GB', 'gb')

print(stock.head())

# Devuelve:

          id                     item  count            item_modified
0  100480924     Apple iPhone Xr 64gb     10     Apple iPhone Xr 64gb
1  100480924     Apple iPhone Xr 64gb     19     Apple iPhone Xr 64gb
2  100480959     Xiaomi Redmi 6A 16gb     44     Xiaomi Redmi 6A 16gb
3  100480975          HUAWEI P30 lite     38          HUAWEI P30 lite
4  100480988  Samsung Galaxy A30 32gb     49  Samsung Galaxy A30 32gb

# Utilicemos esta técnica para arreglar nuestro conjunto de datos de existencias de teléfonos.
# Revisar Ejercicios del capitulo.

# Fin.
