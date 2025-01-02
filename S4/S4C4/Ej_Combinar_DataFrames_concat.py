# # Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

## Combinar DataFrames con concat()


### *Ejercicio 1 de 2:

# 1. Leímos los datos, creamos una columna 'total_sales' y calculamos las ventas totales para cada plataforma en la variable total_sales.
# Tienes que calcular el número total de distribuidoras que crearon un juego en cada plataforma, utilizando nunique(). Asigna el resultado a una variable llamada num_pubs y luego muéstralo.

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()

num_pubs = df.groupby('platform')['publisher'].nunique() # escribe tu código aquí
print(num_pubs) # imprime aquí


### ### *Ejercicio 2 de 2:

# 2. Combina total_sales y num_pubs por columnas en un DataFrame llamado platforms usando concat(). 
# Cambia los nombres de las columnas en platforms a 'total_sales' y 'num_publishers', respectivamente, luego imprime platforms.

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()
num_pubs = df.groupby('platform')['publisher'].nunique()

platforms = pd.concat([total_sales, num_pubs], axis='columns') # escribe tu código aquí

platforms.columns = ['total_sales', 'num_publishers'] # cambia los nombres de las columnas aquí
print(platforms) # muestra tu resultado

# FIN.