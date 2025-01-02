# # Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

## Combinar DataFrames con concat()

# En esta lección volveremos al conjunto de datos de ventas de videojuegos. Aquí están las primeras filas para recordarte su estructura:

import pandas as pd
df = pd.read_csv('Datasets/datasets/vg_sales.csv')
print(df.head())

# Queremos conocer algunas estadísticas generales de las distribuidoras de juegos, en particular:
#   - su puntuación promedio de la crítica;
#   - sus ventas totales.
# Como ya hemos visto, podemos hacerlo usando groupby(). Primero, obtengamos la puntuación de reseña promedio para cada distribuidora:

mean_score = df.groupby('publisher')['critic_score'].mean()
print(mean_score)

# Obtengamos también el número de ventas. La forma más sencilla de hacerlo es con un segundo groupby():

df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()
print(num_sales)

# Observa que el índice de ambos resultados es la columna 'publisher' porque agrupamos por 'publisher' en ambos casos. 
# Como ambos resultados comparten el mismo índice, podemos unir fácilmente los resultados en un DataFrame usando la función concat() de pandas:

mean_score = df.groupby('publishe')['critic_score'].mean()
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()

df_concat = pd.concat([mean_score, num_sales], axis='columns')
print(df_concat)

# En general, concat() espera una lista de objetos de tipo Series y/o DataFrame. 
# Para obtener nuestro resultado, pasamos una lista de variables de Series a concat() y configuramos axis='columns' para asegurarnos de que se combinaran como columnas.
# Ten en cuenta que los nombres de las columnas originales se conservan en el DataFrame concatenado.
# Podemos renombrar columnas utilizando el método columns. Se puede llamar en un DataFrame y pasarle una lista de nuevos nombres de columnas para reemplazar las existentes. 
# Los nuevos nombres deben pasarse en el mismo orden que los nombres originales de las columnas.
# Cambiemos el nombre de 'critic_score', ya que ahora representa un promedio:

mean_score = df.groupby('publisher')['critic_score'].mean()
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()

df_concat = pd.concat([mean_score, num_sales], axis='columns')
df_concat.columns = ['avg_critic_score', 'total_sales']
print(df_concat)

# En general, es una buena idea cambiar el nombre de las columnas después de agruparlas y procesarlas para que sean más indicativas de cómo se procesaron las columnas.
# Es posible que hayas notado que podríamos obtener el mismo resultado que antes usando agg(). Sin embargo, concat() es bastante versátil. 
# Podemos utilizarlo para concatenar DataFrames:
#   - por filas, suponiendo que tengan el mismo número de columnas;
#   - por columnas si tienen el mismo número de filas.
# Para concatenar filas de DataFrames separados, podemos usar concat() y configurar axis='index' (u omitir este parámetro, ya que axis='index' es el argumento predeterminado). 
# Alternativamente, podemos utilizar números enteros para el argumento index=, donde index=0 concatenará filas y index=1 concatenará columnas.
# Aquí hay un ejemplo en el que filtramos los datos en dos DataFrames separados según el género y luego los recombinamos en un solo DataFrame:

import pandas as pd
df = pd.read_csv('Datasets/datasets/vg_sales.csv')

rpgs = df[df['genre'] == 'Role-Playing']
platformers = df[df['genre'] == 'Platform']

df_concat = pd.concat([rpgs, platformers])
print(df_concat[['name', 'genre']])

# ¡Y así dos DataFrames se unen en uno! Recuerda que esto funciona aquí porque ambos DataFrames más pequeños tienen las mismas columnas.

# FIN-
