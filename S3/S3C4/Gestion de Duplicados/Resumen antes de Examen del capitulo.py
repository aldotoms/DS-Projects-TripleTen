# Capítulo 4/6 · Última lección
# Trabajar con valores duplicados y ausentes

# *Examen del capítulo

# Introducción
# En este capítulo obtuviste habilidades cruciales para manejar y limpiar tus datos con Pandas. Ahora, eres capaz de:
#   - Identificar y tratar datos ausentes.
#   - Reemplazar valores ausentes de forma adecuada con base en el tipo de datos.
#   - Manejar entradas de string duplicadas prestando atención a las mayúsculas y minúsculas.
#   - Reemplazar valores de forma eficiente utilizando el método replace().
# Esta es una recapitulación rápida de lo que has aprendido:
# Puedes detectar valores ausentes en tu conjunto de datos y rellenarlos utilizando métodos adecuados para cada situación. Por ejemplo:

import pandas as pd

missing_values = df.isna().sum()    # Detectar valores ausentes

df['source'] = df['source'].replace('', 'email')    # Reemplazar strings vacíos en una columna

df['churned'].fillna(0, inplace=True)   # Rellenar valores ausentes en una columna numérica con un valor por defecto

# También ya practicaste el manejar valores duplicados y hacer tus datos de string consistentes utilizando métodos como replace() y drop_duplicates() para limpiar tu conjunto de datos:

duplicates = df.duplicated().sum()      # Comprobar si hay duplicados en los datos

df = df.drop_duplicates()       # Eliminar registros duplicados

df['city'] = df['city'].str.strip().str.title()     # Estandarizar el texto en una columna

# Estas técnicas ayudarán a garantizar que tus datos estén limpios y listos para un análisis más profundo. ¡Llegó el momento de probar tus conocimientos con los cuestionarios!


# *Práctica guiada

# *Pregunta. Cuestionario 1
# ¿Qué son los datos ausentes?
# Elige tantas como quieras
# Respuestas:
# 1) Valores desconocidos para una variable.
#    El término datos ausentes o valores ausentes significa que no sabemos nada sobre los valores reales, esta información está ausente. 
#    Los datos ausentes se codifican frecuentemente como None en un objeto DataFrame.
# 2) Valores que no tienen ningún significado para una variable.
#    Los datos ausentes pueden codificarse de forma diferente a None con valores de aspecto regular, por ejemplo, -1, 0, '', NA, que no tienen ningún significado en el contexto de esa variable específica.


# *Pregunta. Cuestionario 2
# Has leído los datos de visit_log.csv en un objeto DataFrame y has comprobado con info() que hay datos ausentes.

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200000 entries, 0 to 199999
Data columns (total 4 columns):
 #   Column    Non-Null Count   Dtype 
---  ------    --------------   ----- 
 0   user_id   200000 non-null  int64 
 1   source    198326 non-null  object
 2   email     13953 non-null   object
 3   purchase  200000 non-null  int64 
dtypes: int64(2), object(2)
memory usage: 6.1+ MB

# El método sample(10) muestra los siguientes diez registros aleatorios.

       user_id source       email  purchase
 4  5644686960  email  c129aa540a         0
11  8623045648  email  d6d19c571c         0
18  5739438900         19379ee49c         0
19  7486955288  email  09c27794fa         0
22  1397217221    NaN  79ac569f0b         0
33  7298923004  email  1fe184ed73         0
43  6034222291  email  fb58a27f03         0
49  5062457902    NaN  9ddce3a861         0
56  5690036640  email  a088a48182         0
66  9963049355         9cc43ebd15         0

# Sabes que cada visita de un usuario debe estar asociada a uno de los tres tipos de fuente: email, andoird_push, ios_push.
# ¿Cuántos valores ausentes puede haber en la columna source (dado que 200000-198326=1674)?
# R. Más de 1674 valores.
# Hay strings vacíos en source. Estos espacios vacíos son marcadores de posición para los datos ausentes. Podemos añadir estos registros a los 1674 registros con NaN que info() ya ha reconocido.


# *Pregunta. Cuestionario 3
# Ahora consideras los strings vacíos en el campo source como valores ausentes y quieres rellenarlos con el valor de email (después de hablar con el departamento de marketing, parece el reemplazo obvio). 
# ¿Qué método utilizarás para este ejercicio?
# R. replace()
# La función replace() al ser llamada en una columna de nuestro DataFrame nos permite cambiar un valor por otro. Recuerda que la sintaxis es replace(old_value, new_value).


# *Pregunta. Cuestionario 4
# Tienes datos sobre la clientela de un operador de telefonía móvil, que contienen una columna numérica llamada churned con 1.0 para los clientes y las clientas que terminaron sus contratos y NaN para el resto. 
# ¿Qué valor utilizarás para sustituir NaN?
# Elige tantas como quieras
# R1. 0  Establecer churned en 0 para los clientes que no se fueron parece razonable. Puede tratarse como un análogo de False.
# R2. Cualquier número entero distinto de 1.    Establecer churned a cualquier otro valor numérico parece válido, ya que nos permite diferenciar dos tipos de clientes. Lo clásico sería fijar el valor en 0. 


# *Pregunta. Cuestionario 5
# Tienes datos sobre la clientela del banco. Lo malo es que hay valores ausentes en la columna income. ¿Qué estadística utilizarías para completar los valores ausentes con un valor representativo?
# R. median()   La mediana es una buena estimación del valor esperado cuando los datos están muy sesgados. La razón es que no está tan distorsionada por los valores atípicos como la media.


# Pregunta. Cuestionario 6
# Tienes 15 millones de registros sobre las visitas online de la clientela de un sitio y te gustaría estudiar la duración habitual de una visita. 
# Debido a problemas técnicos en el pasado, hay 3348 registros en los datos con valores de client_id desconocidos. ¿Qué vas a hacer?
# R1. Eliminar los registros.   Dado el pequeño porcentaje de los registros, parece bastante seguro.
# R2. No eliminar los registros, sino excluirlos del análisis.  Dado el pequeño porcentaje de los registros, parece bastante seguro. 
#     También podemos eliminarlos por completo para evitar la necesidad de filtrarlos de alguna manera en los pasos posteriores del análisis.


# Pregunta. Cuestionario 7
# Estás comprobando los datos para ver si hay registros duplicados. Quieres obtener la lista de valores únicos y su recuento. ¿Qué función vas a utilizar?
# R. value_counts()     Esta función identifica todos los valores unívocos en una columna y calcula cuántas veces aparece cada uno. Los registros con más duplicados se encuentran al inicio de la lista.


# Pregunta. Cuestionario 8
# Vamos a trabajar un poco más con los duplicados a partir de un nuevo ejemplo. Ahora estás analizando los datos de las ventas de carros Bentley para diferentes clientes y quieres clasificarlos por ciudades. 
# La función value_counts() de la columna city devuelve lo siguiente:

New Your    1034
London      543
Paris       345
LONDON      32
 London     1

# R. Recorta el espacio de London (el que tiene un espacio al principio) y convierte todos los "London" a mayúscula inicial.
#    Convertir London, LONDON y London  (con un espacio al principio) a mayúscula inicial es la estrategia correcta. En este caso, tener el mismo nombre de city tiene sentido sin tener duplicados. 


# Siguientes pasos
# ¡Bien hecho! Hiciste un muy buen trabajo con todos estos valores ausentes y duplicados y ahora es momento de resumir lo que aprendiste.
# Ahora eres capaz de:
#   - Identificar y contar los valores ausentes utilizando técnicas diferentes.
#   - Filtrar los datasets para extraer las filas con valores ausentes.
#   - Distinguir entre valores categóricos y cuantitativos.
#   - Rellenar los valores categóricos y cuantitativos ausentes.
#   - Identificar, eliminar e incluso fusionar valores duplicados.
# En el siguiente capítulo, elevarás tu experiencia en el manejo de datos mediante el dominio de técnicas avanzadas de indexación y filtrado. 
# Aprenderás cómo utilizar la indexación para acceder y manipular datos de forma más eficiente, aplicar filtros sofisticados basados en consultas y combinar el filtrado con el reemplazo de valores.

# Fin.