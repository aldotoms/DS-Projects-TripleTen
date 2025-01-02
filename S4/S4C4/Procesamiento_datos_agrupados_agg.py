# Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

## *Procesamiento de datos agrupados con agg()
#

# A estas alturas, ya te debería ser familiar el método groupby() de pandas. 
# Este método nos permite modificar el formato de un conjunto de datos agrupando filas en función de los valores de una o varias columnas. 
# En esta lección, revisaremos groupby() y brindaremos información más detallada sobre cómo funciona.

# Echemos otro vistazo al conjunto de datos de ventas de videojuegos, usando dropna() para excluir los valores ausentes una vez más:

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')
df.dropna(inplace=True)

print(df.head())

# Digamos que necesitamos la puntuación promedio de la crítica para cada género:

mean_score = df.groupby('genre')['critic_score'].mean()
print(mean_score)

# El índice del objeto Series mean_score es la “clave groupby()”, en este caso, los valores unívocos de la columna 'genre'. 
# Hacer una operación groupby() cambia el índice de fila de los datos a las claves por las que estamos agrupando.
# Para agrupar por varias columnas, pasamos una lista al método groupby():

grp = df.groupby(['platform', 'genre'])
print(grp['critic_score'].mean())

# Ahora tenemos la puntuación promedio de la crítica para cada género en cada plataforma. 
# Como agrupamos por dos columnas, nuestro resultado es un objeto Series de múltiples índices con dos valores de índice para cada puntuación promedio, 
# en este caso, 'platform' y 'genre'.

# Aquí la variable grp es un objeto que contiene el DataFrame agrupado antes de que procesemos cada grupo con el método mean(). 
# Se denomina objeto "en espera". Si intentamos imprimir el objeto grp, se mostrará una representación del objeto en forma de texto.

grp = df.groupby(['platform', 'genre'])
print(grp)

# Cuando imprimimos df.groupby('column_name'), no vemos la impresión de una tabla como ocurriría si imprimiéramos df. 
# En cambio, vemos el tipo de datos del objeto agrupado (DataFrameGroupBy) y una cadena (0x0000022EA82A75B0) que representa la ubicación en la memoria de la computadora donde se almacena el objeto. 
# No se mostrará ningún resultado hasta que procesemos los grupos.

## *Dividir-aplicar-combinar

# El objeto DataFrameGroubBy forma parte de un framework de procesamiento de datos llamado dividir-aplicar-combinar:
#   1. dividir los datos en grupos;
#   2. aplicar una función de agregación estadística a cada grupo;
#   3. combinar los resultados para cada grupo.
# En el código a continuación, podemos ilustrar cada uno de los tres componentes de dividir-aplicar-combinar:

grp =df.groupby(['platform', 'genre'])
mean_scores = grp['critic_score'].mean()
print(mean_scores)

# Dividimos los datos en grupos con df.groupby(['platform', 'genre']), aplicamos el método mean() y combinamos el resultado en un objeto Series grp['critic_score'].mean().
# Por supuesto, podemos omitir la creación de los objetos grp y mean_scores y hacer que pandas realice los tres pasos con una sola línea de código:

print(df.groupby(['platform', 'genre'])['critic_score'].mean())


## *El método agg()

# Hasta ahora, solo hemos aplicado una única función a nuestros grupos. Pero, ¿qué pasa si queremos calcular diferentes estadísticas de resumen para diferentes columnas? 
# Por ejemplo, tanto la puntuación promedio de los críticos como el total de ventas en Japón para cada grupo. 
# Podemos conseguirlo utilizando el método agg(), que es la abreviatura de "aggregate" (agregar).
# El método agg() usa un diccionario como entrada donde las claves son los nombres de columnas y los valores correspondientes son las funciones de agregación que quieres aplicarles:

agg_dict ={'critic_score': 'mean', 'jp_sales': 'sum'}

grp = df.groupby(['platform', 'genre'])
print(grp.agg(agg_dict))

# ¿No es increíble? ¡Incluso puedes aplicar tus propias funciones personalizadas con agg() de esta manera! Echa un vistazo:

def double_it(sales):
    sales = sales.sum() * 2 #multiplica la suma anterior por dos
    return sales

agg_dict = {'jp_sales': double_it}

grp = df.groupby(['platform', 'genre'])
print(grp.agg(agg_dict))

# RESUMEN

# Vamos a recordar todo lo que hemos estudiado en esta lección:
#   - Método groupby(): método utilizado para agrupar datos por una o varias columnas en un DataFrame.
#   - grp = df.groupby(['platform', 'genre']) agrupará por dos columnas al mismo tiempo.
#   - Método agg(): método utilizado para calcular estadísticas agregadas para cada grupo en un DataFrame agrupado. Pásale un diccionario con ítems de 'column':'function'.
#   - Framework dividir-aplicar-combinar: framework de tratamiento de datos que describe el proceso de dividir un conjunto de datos en grupos, 
#     aplicar una función a cada grupo y, a continuación, combinar los resultados en una única estructura de datos.
#   - Método mean(): método utilizado para calcular la media de un conjunto de valores.
#   - Método sum(): método utilizado para calcular la suma de un conjunto de valores.
#   - Método dropna(): método utilizado para eliminar valores ausentes (NaN) de un DataFrame.
#   - Objeto DataFrameGroupBy: objeto que contiene el DataFrame agrupado antes de que este sea procesado con una función de agregación.

# FIN.