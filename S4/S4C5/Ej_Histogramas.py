# Sprint 4
# Manipulación de datos (Data Wrangling) (continuación)

## *Ejercicio 1/2

# 1. Investiga la distribución del peso para diferentes grupos de edad. Haremos esto en dos pasos. Para comenzar, divide el conjunto de datos en tres DataFrames filtrando df y asígnalos a las siguientes variables:
#   1. df_20s: solo las filas donde 'age' es menor a 30.
#   2. df_30s: solo las filas donde 'age' es mayor o igual a 30 y menor a 40.
#   3. df_40s: solo las filas donde 'age' es mayor o igual a 40 (incluye 50 años).

# Para verificar que filtraste correctamente, muestra los siguientes resultados:
#   1. La suma de las longitudes de los tres DataFrames (debe haber 10 000 filas en total).
#   2. El valor mínimo y máximo en la columna 'age' de df_20s
#   3. El valor mínimo y máximo en la columna 'age' de df_30s
#   4. El valor mínimo y máximo en la columna 'age' de df_40s

# El precódigo ya contiene una plantilla para que muestres tus resultados, solo completa el código.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

# separa df en dataframes separados según la edad
df_20s = df[df['age'] < 30] # inserta el filtro aquí]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]# inserta el filtro aquí) & (# inserta el filtro aquí)]
df_40s = df[df['age'] >= 40]  # inserta el filtro aquí]

# print out the results
print("La suma de las longitudes del dataframe:", len(df_20s) + len(df_30s) + len(df_40s)) # termina esta línea con la suma)
print("Edad mínima y máxima para df_20s:", df_20s['age'].min(), df_20s['age'].max()) # termina esta línea con mínimo y máximo)
print("Edad mínima y máxima para df_30s:", df_30s['age'].min(), df_30s['age'].max()) # termina esta línea con mínimo y máximo)
print("Edad mínima y máxima para df_40s:", df_40s['age'].min(), df_40s['age'].max()) # termina esta línea con mínimo y máximo)


## *Ejercicio 2/2

# 2. Y, para el segundo paso, vas a crear un histograma para cada grupo de edad, todos en la misma gráfica. Para esto, haz lo siguiente:

# Llama plot() en la columna 'weight' de df_20s
#   - Establece el número de contenedores a 20.
#   - Título de la gráfica “Weight / lbs” ("Peso / lbs").
#   - Etiqueta el eje Y “Frequency” ("Frecuencia").

# Llama plot() en la columna 'weight' de df_30s
#   - Establece el número de contenedores a 20.
#   - Establece el valor de alpha a 0.6.

# Llama plot() en la columna 'weight' de df_40s
#   - Establece el número de contenedores a 20.
#   - Establece el valor de alpha a 0.3.

# Finalmente, usa la función legend() de matplotlib para etiquetar cada histograma como "20s", "30s" y "40s", respectivamente.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

df_20s['weight'].plot(kind='hist', title='Weight / lbs', ylabel='Frequency', bins=20) # escribe tu código aquí
df_30s['weight'].plot(kind='hist', bins=20, alpha=0.6) # escribe tu código aquí
df_40s['weight'].plot(kind='hist', bins=20, alpha=0.3) # escribe tu código aquí

plt.legend(['20s', '30s', '40s']) # escribe tu código aquí
plt.show()

# FIN.

