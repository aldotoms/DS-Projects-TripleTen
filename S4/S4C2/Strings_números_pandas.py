# Teoría
## *Trabajar con tipos de datos numéricos y de string

# *Strings y números en pandas

# Cuando pandas lee datos de un archivo de texto, automáticamente convierte los datos sin procesar al tipo de datos pandas.
# Por lo general, la conversión es directa: una columna que contenga solo números en tu CSV o Excel se leerá en automático como un tipo de datos float o int. 
# Si una columna solo contiene palabras, se lee como un tipo de datos object. 
# Pandas utiliza este tipo de datos para datos string, así como también cuando una columna contiene una mezcla de tipo de datos entre sus valores.
# A veces, pandas no puede inferir el tipo de datos correcto. Cuando esto pasa, necesitamos intervenir y convertir por nuestra cuenta los valores al tipo correcto.
# Otras veces, pandas hará exactamente aquello para lo que fue diseñado, pero eso podría no ser lo que queremos.
# En esta lección, aprenderás a lidiar con estas situaciones.

# *Convertir a un tipo de datos específico

# El método astype() de pandas te permite moldear (o convertir) tipos de datos.
# Al igual que con otros métodos de pandas, existe para DataFrames y Series.
# Vamos a ilustrar cómo funciona usando un par de ejemplos con juguetes.
# Abajo, vamos a crear un DataFrame sencillo de dos columnas a partir de un diccionario de Python. Las claves del diccionario se usarán como nombres de columna en el DataFrame. Luego, mostraremos la información sobre los tipos de datos de las columnas:

import pandas as pd

d = {'col1': [1.0, 2.0], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)
print()
print('Output of fg.info():')
df.info()

# Ahora, usemos el método astype() para convertir todos los valores en strings y mostrar el DataFrame.
# Al usarlo, debes especificar entre paréntesis el tipo de datos al cual deseas convertirlo. 
# Por ejemplo, df['column'] = df['column'].astype('int') convertiría la columna 'column' al tipo de datos entero.
# Ten en cuenta que no todos los tipos de datos se pueden convertir entre sí usando astype().  
# Cualquier operación de conversión que pudiese alterar significativamente los datos originales debe hacerse con cuidado.

df_str_dtype = df.astype('str')
print(df_str_dtype)
df_str_dtype.info()

# Podemos ver que, aunque no ha cambiado lo que muestra el DataFrame, ¡sí cambió la información sobre los tipos de datos!
# También podemos usar el método astype() en columnas individuales (p. ej., objetos tipo Series). Hagamos que 'col1' sea del tipo de datos int en vez de float.

df['col1'] = df['col1'].astype('int')
print(df)

# Esta vez, en lugar del método info(), echemos un vistazo al atributo dtypes. ¿Lo recuerdas?
# Las columnas en un DataFrame pueden tener diferentes tipos de datos, o dtypes.

print(df.dtypes)

# Así como así, hemos cambiado con éxito el tipo de datos de una sola columna. 
# Fíjate que el 64 en int64 se refiere al tamaño de bits de los enteros en la memoria de la computadora. 
# También puedes ver otros tipos de enteros como int32, int16 y otros. 
# Básicamente, el tipo de 64 puede contener muchos más dígitos que los de menos bits, pero todos se comportan de forma idéntica a los tipos de datos int.


# *Cuidado con los problemas inesperados

# Digamos que cargas un conjunto de datos y parece que todos los valores flotantes en una columna en realidad deben ser enteros, pero hay demasiados para analizarlos manualmente. 
# ¿Cómo sabes que es seguro hacer la conversión de float a int o si perderás algo de información tras hacerlo?
# Para ilustrar esto, mira el siguiente ejemplo.

d = {'col1': [1.0, 2.0, 3.0, 4.0], 'col2': [5.0, 6.01, 7.0, 8.0]}
df = pd.DataFrame(data=d)
print(df)

# Si no tienes cuidado, ejecutarás df.astype('int') (que cambiará 6.01 a 6) sin darte cuenta de que acabas de cambiar los valores de tu conjunto de datos.

# Vamos a usar una nueva librería que nos ayude a lidiar con estos casos.
# * NumPy: 
# #s una poderosa librería de Python usada para computación científica. Esta introduce una nueva estructura de datos llamada array, que es parecido a una lista, pero con muchas ventajas, 
# incluyendo la habilidad para realizar operaciones vectorizadas en arrays enteros muy rápidamente. 
# NumPy también nos proporciona funciones matemáticas y herramientas que nos son útiles para trabajar con arrays, tales como ordenar, indexar y transmitir.
# Cuando estás tratando con cientos o miles (¡o más!) valores, puedes recurrir a la ayuda de la función array_equal() de la librería numpy. 
# Esta función acepta dos arrays y devuelve True si ambos tienen los mismos elementos y la misma forma, y False si es el caso contrario. Vamos a probarla con 'col1'

import numpy as np
import pandas as pd

d = {'col1': [1.0, 2.0, 3.0, 4.0], 'col2': [5.0, 6.01, 7.0, 8.0]}
df = pd.DataFrame(data=d)

# comprueba si es seguro convertir 'col1'
np.array_equal(df['col1'], df['col1'].astype('int'))
# Devuelve: True

# ¡Excelente! No hubo ningún problema. Ahora prueba con 'col2':

np.array_equal(df['col2'], df['col2'].astype('int'))
# Devuelve: False

# Ahora sabemos que no podemos convertir 'col2' de float a int sin perder algunos de los datos.
# Hay otros ejemplos de posibles problemas al considerar la conversión de tipos de datos, pero el meollo del asunto es:
# - Ten cuidado al convertir entre tipos de datos, y evalúa si la operación de conversión podría llevar a cambios significativos en tus datos.


## *Convertir strings en valores numéricos

# A veces queremos conservar los valores del string que parecen números como tipos de datos string. Los códigos postales o los ID numéricos son ejemplos comunes: son números, pero no tiene sentido realizar operaciones aritméticas con ellos.
# Sin embargo, read_csv() siempre leerá todo lo que parezca un entero como un tipo de datos int, incluso si quieres usarlos como strings.
# Otras veces, pasa lo contrario: pandas confunde los valores numéricos con strings y necesitamos intervenir un poco para hacer la conversión.
# En los casos más sencillos, el método astype() funciona de maravilla. A continuación, te mostramos cómo convertir strings que representan enteros en enteros reales:

d = {'col1': ['1.0', '2.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)
print(df.dtypes)

# convertir col2 a int
df['col2'] = df['col2'].astype('int')
print(df.dtypes)

# En otros casos, no se puede convertir los strings en números de esta forma. Mira lo que sucede cuando intentamos convertir strings que representan valores flotantes en enteros:

# convertir col1 da como resultado un error
df['col1'] = df['col1'].astype('int')

# Para solventar este problema, usaremos un método más flexible llamado to_numeric():

df['col1'] = pd.to_numeric(df['col1'])
print(df.dtypes)

# Funciona muy bien si tienes strings similares a números como '72' o '1.394'. 
# No obstante, de forma predeterminada, to_numeric() no puede convertir strings con caracteres no numéricos o decimales en números. En cambio, devuelve un error.
# Aunque hay una buena noticia: ¡to_numeric() tiene un parámetro errors=! El valor de este parámetro determina qué hará to_numeric() si encuentra un valor no válido:

# errors='raise': argumento predeterminado por el cual los valores inválidos generan errores, bloqueando la conversión a números para toda la columna.
# errors='coerce': los valores inválidos se reemplazan por NaN.
# errors='ignore': los valores inválidos simplemente se ignoran y se dejan sin cambios.

# Así es como se ve:

d = {'col1': ['1.0', 'B.0'], 'col2': ['3', '4']}
df = pd.DataFrame(data=d)

df['col2'] = df['col2'].astype('int')
df['col1'] = pd.to_numeric(df['col1'], errors='coerce')

print(df.dtypes)
print(df)

# Resumen
#   - Usa astype() para convertir un tipo de datos en otro.
#   - No todos los tipos de datos se pueden convertir entre sí usando astype(); algunas conversiones (como strings tipo float a enteros) podrían arrojar un error.
#   - Ten cuidado cuando hagas conversiones que pudieran alterar significativamente los datos originales.
#   - Al convertir los strings en números, el método to_numeric() podría ser mejor opción gracias a la flexibilidad que le brinda el parámetro errors=.

