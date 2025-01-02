# Capítulo 4/6
# Trabajar con valores duplicados y ausentes

# *Ejercicios*

# Ejercicio 1
# Ahora aplica el método value_counts() a la columna 'email' y almacena el resultado en la variable email_values. 
# Esta vez, no incluyas los valores ausentes en la salida. Imprime el resultado.

# Código:
import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

email_values = df_logs['email'].value_counts(dropna=True) # escribe tu código aquí

print(email_values) # escribe tu código aquí)

# Resultado

4526cc437a    9
410a2a3c23    9
17c4fb26f9    8
5a4c033120    7
125073f731    7
             ..
a719af2824    1
be38ee0313    1
b66198ec91    1
2fca4486da    1
2338bb1a43    1
Name: email, Length: 6062, dtype: int64

# Ejercicio 2
# Ahora intentemos ordenar los resultados por índice en lugar de valores para ver si se añade algún significado a los valores de la columna 'email'. 
# Vuelve a escribir la variable email_values utilizando la ordenación e imprime el resultado.

# Código

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

email_values = df_logs['email'].value_counts(dropna=True)
email_values = email_values.sort_index() # escribe tu código aquí

print(email_values)

# Resultado

000b6d0fb5    3
000eb3c3df    4
0017c0065d    4
001c287e32    6
002020511f    1
             ..
ff953ec581    1
ffa51139e7    2
ffcef1ce43    2
ffe64c4d89    5
fffc7f0482    1
Name: email, Length: 6062, dtype: int64

# Fin.