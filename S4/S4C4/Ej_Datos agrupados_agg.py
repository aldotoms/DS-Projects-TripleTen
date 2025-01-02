# Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

# Procesamiento de datos agrupados con agg()

# *Ejercicio:

# ¡Es hora de que analicemos en detalle las ventas de videojuegos de cada género!
# El precódigo crea una columna 'total_sales' como ya has hecho antes. Utilizarás estas columnas, así que apunta sus nombres.
# A continuación, el precódigo agrupa el DataFrame df por la columna 'genre' y asigna el objeto agrupado resultante a la variable grp.
# Y ahora vas a hacer lo siguiente:
#   - Crear un diccionario para calcular para cada género:
#       - Suma del total de ventas.
#       - Ventas promedio NA (Norteamérica).
#       - Ventas promedio EU (Europa).
#       - Ventas promedio JP (Japón).
#   - Asignar el diccionario a una variable llamada agg_dict con las tuplas descritas anteriormente.
#   - Asignar el resultado de agg() a una variable llamada genre.
#   - Imprimir genre.

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')

df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

grp = df.groupby('genre')

agg_dict = {'total_sales': 'sum', 'na_sales': 'mean', 'eu_sales': 'mean', 'jp_sales': 'mean'} # escribe aquí tu diccionario con cuatro tuplas, una por cada variable

genre = grp.agg(agg_dict) # utiliza aquí la función agg

print(genre) # muestra aquí los resultados

# Fin.