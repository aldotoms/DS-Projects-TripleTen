# Capítulo 3/6 · Última lección
# Introducción al preprocesamiento de datos y al análisis inicial

# Examen del capítulo
# Introducción:

# Durante este sprint has aprendido muchas técnicas muy útiles; y pronto te mostraremos el conocimiento práctico en el proyecto.
# Esta es una recapitulación rápida de lo que has aprendido:
# Puedes renombrar columnas en un DataFrame utilizando rename(), identificar valores ausentes con isna() e isnull() y llenar o eliminar valores ausentes cuando se requiera. Por ejemplo:

import pandas as pd

df = df.rename(columns={'old_name': 'new_name'})    # Renombrar columnas en el DataFrame

missing_values = df.isna().sum()    # Identificar valores ausentes

df['my_column'].fillna(0, inplace=True)     # Llenar valores ausentes con 0

# También ya aprendiste a trabajar con los duplicados detectándolos y eliminándolos y exploraste el uso de unique() y nunique() para manejar distintos datos

duplicates_count = df.duplicated().sum()       # Comprobar si hay duplicados

df = df.drop_duplicates()       # Eliminar duplicados

unique_values = df['my_column'].unique()       # Recuperar valores únicos y su recuento
unique_count = df['my_column'].nunique()

# Por último, ahora puedes agrupar datos de manera efectiva utilizando groupby() para separar, aplicar funciones y combinar datos:

grouped_df = df.groupby('category_column')['value_column'].sum()        # Agrupar datos por columna y calcular la suma

# Nos entusiasma mucho ver lo que has progresado. Pero por ahora, puedes refrescar tu memoria con algunos ejercicios.

# Siguientes pasos

# Luchaste y ganaste tu primera batalla contra los problemas más comunes con los datos: los valores ausentes y los datos duplicados. 
# ¡Bien hecho! Saber cómo trabajar con valores ausentes y duplicados, así como con agrupación y ordenamiento, te ayudará mucho en tus futuros análisis.
# Ahora eres capaz de:

#   - Usar el método rename() para cambiar el nombre de las columnas.
#   - Utilizar isnull(), fillna() y dropna() para identificar, llenar y eliminar valores ausentes.
#   - Utilizar los métodos duplicated(), reset_index(), unique() y nunique() para trabajar con duplicados.
#   - Explica qué es la agrupación, las etapas de la agrupación y cómo agrupar en pandas.
#   - Ordena los datos usando el método sort_values().

# En el próximo capítulo, llevarás tus habilidades de limpieza de datos al siguiente nivel aprendiendo cómo manejar diferentes tipos de inconsistencias de datos. 
# Explorarás técnicas para distinguir entre datos categóricos y cuantitativos, manejar valores ausentes con enfoques específicos del contexto y lidiar con datos de string duplicados.

# Fin.