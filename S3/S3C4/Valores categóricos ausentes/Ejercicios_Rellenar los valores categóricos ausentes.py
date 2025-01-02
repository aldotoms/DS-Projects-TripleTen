# Capítulo 4/6
# Trabajar con valores duplicados y ausentes

# *Ejercicios*

# Ejercicio 1
# Para calcular la tasa de conversión de cada fuente de tráfico, primero determina cuántas visitas hubo de cada fuente.
# Para encontrar el número total de visitas de cada fuente de tráfico, utiliza groupby() para agrupar los datos por la columna 'source', luego cuenta el número de valores en la columna 'user_id' del DataFrame agrupado. Asigna el resultado en la variable visits y luego imprímelo.
# El precódigo ya contiene el trabajo que realizaste para rellenar los valores ausentes.

# Código:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count() # escribe tu código aquí
print(visits) # escribe tu código aquí)

# Resultado:

source
context     52032
email       13953
other      133834
undef         181
Name: user_id, dtype: int64


# Ejercicio 2
# A continuación, determina el número de visitas en las que se realizó una compra para cada fuente, calculando la suma de la columna 'purchase' para cada grupo de fuente. 
# Posteriormente, asigna los resultados a la variable purchases e imprímelos.

# Código:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

purchases = df_logs.groupby('source')['purchase'].sum() # escribe tu código aquí
print(purchases) # escribe tu código aquí)

# Resultado:

source
context    3029
email      1021
other      8041
undef        12
Name: purchase, dtype: int64

# Ejercicio 3
# Calcula la tasa de conversión para cada fuente de tráfico, guarda los resultados en conversion, e imprímelos. 
# La tasa de conversión es la proporción de visitas en las que se realizó una compra. El precódigo contiene las visitas y compras de tu trabajo previo.

# Código:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count()
purchases = df_logs.groupby('source')['purchase'].sum()

conversion = purchases / visits # divide el número de compras entre el número de visitas
print(conversion) # escribe tu código aquí)

# Resultado:

source
context    0.058214
email      0.073174
other      0.060082
undef      0.066298
dtype: float64

