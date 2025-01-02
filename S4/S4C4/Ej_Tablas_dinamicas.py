# Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

## *TABLAS DINÁMICAS

# Ejercicio:

# Hemos filtrado el conjunto de datos de videojuegos para que solo contenga juegos que se lanzaron en el 2000 o después. 
# Crea una tabla dinámica a partir del conjunto de datos filtrados que contenga el valor promedio para las ventas en Japón para cada combinación de género y año de lanzamiento.
#   - Los géneros servirán de índice.
#   - Las columnas de la tabla dinámica serán los años de lanzamiento.
#   - Utiliza la columna correspondiente como valores a ser agregados.
#   - Utiliza la función de agregación apropiada.
# Asigna el resultado a una variable llamada df_pivot y luego muéstralo.

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')
df = df[df['year_of_release'] >= 2000]

df_pivot = df.pivot_table(index='genre',
                          columns='year_of_release',
                          values='jp_sales',
                          aggfunc='mean'
                          ) # escribe tu código aquí

print(df_pivot) # escribe tu código aquí

# FIN.