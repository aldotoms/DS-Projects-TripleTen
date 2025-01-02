# Capítulo 3/6
# Introducción al preprocesamiento de datos y al análisis inicial

#   Procesar valores ausentes
# En la lección anterior, aprendiste cómo corregir errores estructurales en los nombres de columna y cómo, automáticamente, 
# trabajar con estos procesos programando tu propio bucle. Para que refresques tu memoria:

new_col_names = []

for old_name in celestial.columns:
    # Primero, elimina los espacios al principio y al final
    name_stripped = old_name.strip()
    # Luego, pon todas las letras en minúsculas
    name_lowered = name_stripped.lower()
    # Por último, reemplaza los espacios entre palabras por guiones bajos
    name_no_spaces = name_lowered.replace(' ', '_')
    # Agrega el nuevo nombre a la lista de nuevos nombres de columna
    new_col_names.append(name_no_spaces)

# Reemplaza los nombres anteriores por los nuevos
celestial.columns = new_col_names


# Ahora que hemos corregido los nombres de las columnas, podemos mostrarte cómo preprocesar los valores ausentes en los propios datos. 
# Al final de esta lección, podrás comprobar rápidamente qué columnas tienen valores ausentes usando el método isna(), 
# completar los valores ausentes con el método fillna() y eliminar filas o columnas con valores ausentes utilizando el método dropna().

# eoria

# ¿Por qué es importante procesar valores ausentes?
# El procesamiento de valores ausentes es fundamental. 
# Los algoritmos de aprendizaje automático no funcionan bien con los datos que contienen valores ausentes. Además, 
# os algoritmos estadísticos que pueden ayudar a las empresas a tomar decisiones informadas también sufren problemas con la información incompleta. 
# Como regla general, siempre debemos abordar los valores ausentes antes de seguir adelante. 
# Para comenzar, echemos un vistazo a las primeras 10 filas de nuestro dataset. 
# No te preocupes por que los cambios realizados en los nombres de las columnas aún no se vean reflejados. 
# Lo ideal sería que esos cambios se reflejaran aquí, pero decidimos dejar los nombres originales para centrarnos en cada paso del preprocesamiento por separado.

import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
print(df.head(10))

# Como ya hemos visto, hay algunos valores ausentes (NaN) en la columna 'Artist'. 
# ¿Recuerdas que los valores ausentes pueden aparecer por diferentes razones? 
# Por ejemplo, tal vez un usuario no proporcionó ninguna información personal. O quizá hubo problemas con la recopilación de datos automatizada. 
# A veces, los valores ausentes se insertan intencionalmente, ya que deben reemplazarse automáticamente con caracteres especiales.
# Los valores ausentes pueden aparecer de varias maneras, pero aquí hay dos de las más comunes:

# 1. Formas esperadas: None o NaN. Estos son dos valores especiales que marcan los valores ausentes:
#   - None es una instancia del objeto NoneType. En términos más sencillos, se utiliza para representar un valor nulo o la ausencia de cualquier valor.
#   - NaN significa "no es un número" (en inglés, "Not A Number") y se utiliza para representar valores ausentes en los datos. Se trata como un decimal, 
#     específicamente como un tipo float. NaN representa cualquier valor que no está definido o no se puede representar.

# 2. Formas inesperadas. Las personas pueden optar por marcar los valores ausentes de formas alternativas, tales como 0, '?', 'NN' o 'n/a'. 
#    Lo ideal es que también proporcionen documentación para los datos. Si no lo hacen, tendrás que hacer una conjetura sobre el significado de los valores ausentes.

#  Si encuentras con frecuencia un carácter especial en una tabla sin ninguna explicación, es probable que represente valores ausentes. 
# Y los tratarás del mismo modo en que tratas None o NaN, pero observa que Python solo reconoce a None y NaN como valores ausentes, 
# así que tendrás que identificarlos manualmente.


## Teoria
# Como ya hemos visto, no siempre está claro que los ceros son simples ceros.

# Procesamiento de valores ausentes
# Bien, sabemos cómo identificar valores ausentes, pero ¿cómo los podemos abordar?
# Aquí, demostraremos algunas formas de lidiar con los valores ausentes. Utilizaremos un dataset de la Organización Mundial de la Salud. 
# El registro epidemiológico de la OMS (materiales en inglés) contiene datos estadísticos sobre el cólera a partir de 2017:

import pandas as pd
cholera = pd.read_csv('/datasets/cholera.csv')
print(cholera)

# Recibimos una descripción de las columnas en el dataset. Esto es lo que nos indica:

'region' y 'country' indican la ubicación geográfica;
'total_cases' es el número total de casos de cólera;
'imported_cases' es la cantidad de casos importados de otros países;
'deaths' es el número de casos letales;
'case_fatality_rate' almacena la tasa de mortalidad;
'notes' contiene strings con ciertos comentarios.

## Buscar valores ausentes
# Para encontrar todos los valores ausentes en una tabla, puedes utilizar el método isna(). 
# Funciona de manera bastante sencilla: si se encuentra un valor ausente, devuelve True; si no, devuelve False.
# isna() no es tan útil por sí solo. Generalmente usamos el método isna() junto con el método sum(). 
# La función sum() cuenta todos los valores True y devuelve su suma total:

print(cholera.isna().sum())

# Por lo tanto, para cada columna del dataset, obtenemos un valor que indica la cantidad de valores ausentes en esa columna. 
# Por ejemplo, la columna 'imported_cases' contiene 6 valores ausentes y la columna 'notes' contiene 21.
# También es posible que encuentres el comando isnull() utilizado en lugar de isna(). 
# En realidad son lo mismo, por lo que tanto cholera.isna().sum() como cholera.isnull().sum() producirán el mismo resultado.
# Nuestra recomendación es que uses isna(), ya que es el que más se usa en el mercado. 
# Recuerda que tanto isna() como isnull() devuelven las formas esperadas de manejar los valores ausentes. 
# En otras palabras, solo tienen en cuenta NaN y None.
# Entonces, vemos que casi todas las columnas contienen valores ausentes. Vamos a averiguar qué hacer con ellos.

# Formas de procesar valores ausentes
# Dependiendo de los objetivos de tu investigación, puedes procesar los valores ausentes de diferentes maneras.
# - Las filas de una tabla pueden eliminarse por completo si han perdido su valor debido a los valores ausentes. A veces, un segmento de datos se vuelve inútil debido a la ausencia de valores y debe eliminarse.
# Fíjate que no hay datos sobre Europa en nuestra tabla de la OMS; la fila está llena de valores ausentes. Según la columna 'notes', no hubo casos de cólera en Europa en 2017. Así que podemos eliminar la fila sin ningún impacto en los resultados.
# - A veces, los valores ausentes se remplazan con otros valores. Esto se puede hacer cuando los valores ausentes no son muy relevantes para nuestro análisis, pero las filas o columnas aún contienen datos valiosos.
# Por ejemplo, África tuvo 179 835 casos de cólera, pero ninguno de ellos fue importado. Observa que 'imported_cases' contiene NaN. Sin embargo, si eliminamos toda la fila, perderemos algunos datos importantes.


## Sustituir valores
# Para conservar todas las filas con datos valiosos, reemplazaremos los valores NaN en la columna 'imported_cases' por ceros.
# Podemos lograr esto utilizando el método fillna(), que devuelve una copia de la columna original con todos los valores NaN reemplazados por un valor específico.

# Veamos cómo funciona en la práctica:

cholera['imported_cases'] = cholera['imported_cases'].fillna(0)
print(cholera)

# La columna 'imported_cases' ahora tiene todos sus valores ausentes reemplazados por ceros. 
# De manera alternativa, podrías haber establecido el argumento inplace=True para que no tuvieras que asignar una nueva columna en lugar de la antigua.

cholera['imported_cases'].fillna(0, inplace=True)

# El resultado será idéntico: cualquier valor que falte en la columna 'imported_cases' se reemplazará por 0.
# Por cierto, incluso puedes usar aquí el bucle for para remplazar los valores ausentes. 
# Todo lo que necesitas es crear una lista que contenga todas las columnas en donde quieres hacer el remplazo, 
# y después iterar sobre esos nombres para hacer realmente el cambio.

# recorrer nombres de columna y remplazar los valores ausentes con ceros
columns_to_replace = ['imported_cases']

for col in columns_to_replace:
    cholera[col].fillna(0, inplace=True)

# Los bucles son útiles cuando tienes varias columnas y quieres reemplazar los valores ausentes por un valor específico. 
# En este caso, solo necesitamos reemplazar los valores ausentes en la columna 'imported_cases'. 
# Por lo tanto, cholera['imported_cases'].fillna(0, inplace=True) es el método preferible.
# Ahora, inténtalo por tu cuenta.

# Fin.