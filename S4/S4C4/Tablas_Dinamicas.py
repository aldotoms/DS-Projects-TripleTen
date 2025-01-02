# Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

## *TABLAS DINÁMICAS

# A estas alturas, esperamos haberte convencido de que groupby() es una herramienta excelente para agrupar datos y realizar análisis más complejos. 
# Aunque siempre puedes usar groupby() para calcular las propiedades agregadas de tus datos, pandas también ofrece tablas dinámicas como método alternativo para agrupar y analizar datos.
# Las tablas dinámicas son una gran herramienta para sintetizar conjuntos de datos y explorar sus diferentes dimensiones. 
# Son muy populares en las aplicaciones de hojas de cálculo como Excel, pero es aún más impresionante crearlas mediante programación con pandas.
# Echemos otro vistazo a los datos de ventas de videojuegos a continuación:

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')
print(df.head())

# Supongamos que queremos determinar el total de ventas en Europa de cada género en cada plataforma. 
# Las tablas dinámicas ofrecen un método rápido y cómodo para conseguirlo. Primero, vamos a examinar el código y luego a comentarlo. 
# Para simplificar las cosas, eliminaremos las filas con valores ausentes.

df.dropna(inplace=True)

pivot_data = df.pivot_table(index='genre',
                            columns='platform',
                            values='eu_sales',
                            aggfunc='sum'
                            )

print(pivot_data)
print()
print(type(pivot_data))

# Creamos una tabla dinámica utilizando el método pivot_table(), que tiene un nombre muy apropiado. Los parámetros que utilizamos fueron:
#   - index=: la columna cuyos valores se convierten en índices en la tabla dinámica;
#   - columns=: la columna cuyos valores se convierten en columnas en la tabla dinámica;
#   - values=: la columna cuyos valores queremos agregar en la tabla dinámica;
#   - aggfunc=: la función de agregación que queremos aplicar a los valores en cada grupo de filas y columnas.

# Cada celda de la tabla dinámica de arriba contiene las ventas totales en Europa para cada combinación particular de género/plataforma. 
# También imprimimos el tipo de datos de la tabla dinámica para mostrar que es un DataFrame de pandas, que ya conocemos muy bien.
# El uso de una tabla dinámica aquí es conveniente porque nos permite fácilmente excluir todas las columnas de df que no nos interesan para nuestro análisis. 
# Además, puede ser más fácil de leer que el resultado equivalente de groupby(), como puedes ver a continuación.

groupby_data = df.groupby(['genre', 'platform'])['eu_sales'].mean()
print(groupby_data)
print()
print(type(groupby_data))

# Un formato muy diferente, ¿verdad? Observa también que el resultado de groupby() devuelve un objeto Series, mientras que pivot_table() devuelve un DataFrame. 
# Ya sea que elijas usar groupby() o pivot_table() depende de tus preferencias personales y, con el tiempo, 
# desarrollarás la intuición sobre qué herramienta es la más conveniente para la tarea en cuestión.

# FIN. 