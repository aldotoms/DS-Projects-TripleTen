# Capítulo 3/6
# Introducción al preprocesamiento de datos y al análisis inicial

# Procesamiento de valores duplicados
# En las lecciones anteriores, aprendiste a renombrar las columnas y manejar los valores ausentes en tus datos.
# Para ello, usamos tres métodos: isna() para encontrar los valores ausentes; fillna() , para llenarlos; y dropna() para deshacernos de las filas con datos no necesarios.

# Teoria
# En esta lección, nos centraremos en cómo manejar los datos duplicados.
# Usaremos el dataset music_log_raw.csv en su versión sin procesar, sin ningún cambio en los nombres de las columnas ni valores ausentes. 
# En la vida real, no empezaríamos por tratar de eliminar los duplicados. Más bien, primero cambiaríamos el nombre de las columnas, 
# luego procederíamos a eliminar los valores NaN y finalmente puliríamos nuestro conjunto de datos eliminando los duplicados, lo que aprenderás a hacer en esta lección.
# Al final de esta lección, podrás usar los métodos duplicated(), drop_duplicates(), reset_index(), unique() y nunique() para trabajar con duplicados en tus datos.

# Detección de casos obvios
# Recuerda esos duplicados que vimos al principio del capítulo:

# Este dataset nos proporciona un ejemplo de una fila completamente duplicada que puede detectarse fácilmente usando el método duplicated(). 
# Este método funciona de manera similar al método isna(): devuelve True si se duplica un valor y False en caso contrario.
# Para contar estos valores, se puede combinar con el método sum():

import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
print(df.duplicated().sum())

5313

# Esos son muchos valores duplicados. Averigüemos cómo eliminarlos. Pero antes, intenta por tu cuenta encontrar algunos duplicados en el siguiente ejercicio.

# Fin.