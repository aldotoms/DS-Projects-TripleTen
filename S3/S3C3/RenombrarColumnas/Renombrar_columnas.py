# Capítulo 3/6
# Introducción al preprocesamiento de datos y al análisis inicial

# Renombrar columnas
# En la lección anterior, estudiaste los problemas que puedes encontrar en tus datos con mayor frecuencia. 
# Y estaban divididos en errores de contenido y estructurales.
# Los errores de contenido que vimos son:
# - Valores ausentes, cuando una celda no está llena por alguna razón.
# - Valores duplicados, cuando dos o más filas son exactamente iguales.
# Y el problema estructural que vimos es el nombramiento incorrecto de columnas. En esta lección, aprenderemos cómo corregir este problema estructural.
# Algunos problemas típicos con los nombres de columna incluyen:
# - Nombres de columna que contienen espacios. Pueden ser fáciles de pasar por alto y crear problemas al intentar acceder a una columna. 
# Es mejor utilizar snake_case al nombrar columnas y variables.
# - Falta de claridad en los nombres de columna. Puede ser difícil saber qué representan los datos en una columna.
# Al final de esta lección, podrás identificar errores comunes en la denominación de columnas y utilizar el método rename() para corregirlos. 
# Saber cómo cambiar los nombres de las columnas para reflejar mejor los datos facilitará mucho el trabajo con los datos.

## Por dónde empezar
# El primer paso es comprobar si realmente tienes en tus columnas un problema con la asignación de nombres. 
# Recomendamos empezar con el método info() para obtener una idea general sobre el dataset.
# Recordemos cómo usarlo:

print(df.info())

# Este método muestra no solo los nombres de las columnas, sino también información sobre los tipos de datos en la tabla 
# y la cantidad de objetos no nulos en cada columna. Es un excelente punto de partida.
# Como alternativa, puedes usar el atributo .columns que solo muestra los nombres de las columnas y nada más.
# Para ilustrar cómo funciona el atributo .columns, creemos una tabla que contenga las distancias entre la Tierra y varios cuerpos celestes. 
# Crearemos un DataFrame a partir de estos datos.

import pandas as pd

# las medidas se almacenan en una lista de listas
measurements = [['Sun', 146, 152],
                                ['Moon', 0.36, 0.41], 
                                ['Mercury', 82, 217], 
                                ['Venus', 38, 261],
                                ['Mars', 56, 401],
                                ['Jupiter', 588, 968],
                                ['Saturn', 1195, 1660],
                                ['Uranus', 2750, 3150],
                                ['Neptune', 4300, 4700],
                                ['Halley\'s comet', 6, 5400]]

# los nombres de las columnas se almacenan en la variable header
header = ['Celestial bodies ','MIN', 'MAX'] 

# guardar el DataFrame en la variable celestial
celestial = pd.DataFrame(data=measurements, columns=header)

# Para revisar los nombres de las columnas, vamos a mostrar el atributo columns del DataFrame.

print(celestial.columns)

Index(['Celestial bodies ','MIN', 'MAX'], dtype='object')

# Aquí tenemos tres problemas:

# 1. 'Celestial bodies ' contiene dos espacios: entre las palabras y al final.
# 2. 'MIN' y 'MAX' se escriben en mayúsculas, mientras que en 'Celestial bodies ' solo se escribe con mayúscula el primer carácter. 
#     Este tipo de inconsistencia puede causar problemas.
# 3. Los nombres 'MIN' y 'MAX' no son muy descriptivos. Necesitamos nombres más explícitos para transmitir con claridad su significado.

# Corregir los problemas
# Debemos corregir estos problemas, así que cambiemos el nombre de las columnas:
# - Vamos a cambiar 'Celestial bodies ' a 'celestial_bodies', para respetar el estilo snake_case, y de esta manera resolvemos los problemas del nombre de esta columna.
# - Remplazaremos 'MIN' y 'MAX' por 'min_distance' y 'max_distance', y de esa manera también respetaremos el estilo snake_case 
#   y agregaremos significado al nombre de las columnas, lo que hace que su contenido se entienda más fácilmente.

# Para cambiar el nombre de las columnas, llama al método rename() con un diccionario como su argumento columns. 
# Las claves del diccionario deben ser los nombres anteriores de las columnas, y los valores correspondientes deben ser los nuevos nombres. 
# De este modo:

# Declara un diccionario con el nombre anterior de la columna como claves
# y los nombres nuevos de la columna como los valores
columns_new ={
    "Celestial bodies ": "celestial_bodies",
    "MIN": "min_distance",
    "MAX": "max_distance",
    }

# Llama al método rename y pasa
# el diccionario como un argumento al parámetro columns
celestial = celestial.rename(columns = columns_new)
print(celestial.columns)

Index(['celestial_bodies', 'min_distance', 'max_distance'], dtype='object')

# Antes te mostramos cómo cambiar los nombres de las columnas y reasignar la variable celestial para reflejar los cambios. 
# Si no reasignas la variable, los nombres de las columnas no cambiarán.
# Sin embargo, hay una forma más elegante de renombrar columnas que no requiere reasignación como hicimos anteriormente. 
# Solo necesitamos especificar el parámetro inplace y establecerlo en True.

# Declara un diccionario con el nombre anterior de la columna como claves
# y los nombres nuevos de la columna como los valores
columns_new ={
    "Celestial bodies ": "celestial_bodies",
    "MIN": "min_distance",
    "MAX": "max_distance",
    }

# Llama al método rename y pasa el diccionario como un argumento al parámetro columns y True como un argumento al parámetro inplace
celestial.rename(columns = columns_new, inplace = True)
print(celestial.columns)

Index(['celestial_bodies', 'min_distance', 'max_distance'], dtype='object')

# Como puedes ver, logramos los mismos resultados sin hacer ninguna asignación directa.

# Fin.