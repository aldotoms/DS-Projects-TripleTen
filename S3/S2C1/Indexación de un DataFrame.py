#Capítulo 1/6
# La librería Pandas

# Indexación de un DataFrame

# Ahora que sabes cómo obtener información general sobre las tablas, que conoces bien el método info() y los atributos que muestra, 
# como columnas y dtypes, y que también has aprendido a construir tus propios DataFrames a partir de listas y archivos externos, 
# ha llegado la hora de aprender acerca de la indexación con DataFrames.
# Al final de esta lección, podrás utilizar la indexación para extraer solamente los datos que te interesen.


# Indexación por coordenadas

# La indexación permite acceder a una celda determinada de la tabla utilizando dos coordenadas: el número de la fila y el nombre de la columna.
# Para acceder a los valores de una tabla en un DataFrame, tenemos a nuestra disposición el atributo loc[]: df.loc[row, column]. 
# La row (fila) y la column (columna) del valor en cuestión deben especificarse entre corchetes después de loc.
# Por ejemplo, para obtener el contenido de la celda situada en la quinta fila de la columna 'genre', utiliza df.loc[4, 'genre']. 
# Observa que la indexación comienza en 0, como es habitual.

# Ejecuta el código que aparece a continuación y compruébalo por tu cuenta.

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')
result = df.loc[4, 'genre']
print(result)

# Respuesta: pop


# Ejercicio 1
# Escribe código que devuelva el nombre de la canción de la octava fila del conjunto de datos. 
# Los nombres de las canciones se ubican en la columna 'track'. Asigna el valor recuperado a la variable result y muéstralo.

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

#escribe tu código aquí
result = df.loc[7, 'track']
print(result)