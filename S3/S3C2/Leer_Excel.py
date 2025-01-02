#Capítulo 2/6
# Leer y visualizar datos 

# Cómo leer archivos Excel
# No es raro recibir datos de un compañero de trabajo o un cliente en forma de hojas de cálculo de Excel en lugar de archivos CSV. En esta lección, seguiremos aprendiendo a leer archivos de Excel en Python. ¡Por suerte, pandas lo hace fácil!
# Ve el siguiente vídeo primero y luego sigue leyendo para aprender todo al respecto.

# NOTA: ¿Excel sigue siendo relevante?
# Microsoft Excel ha sido utilizado por empresas y organizaciones de todo el mundo desde finales de los ochenta. 
# Esto significa que hay una gran cantidad de datos históricos en las hojas de cálculo de Excel. 
# Hoy en día, la mayoría de las grandes organizaciones tienen sus propios centros de datos o contratos con proveedores 
# de la nube, pero, aun así, todavía se hace mucho trabajo en Excel.

# Cómo trabajar con archivos Excel
# Como ya sabes, pandas proporciona la función read_excel() para leer archivos Excel. 
# Por defecto, esta función carga la primera hoja, pero un archivo Excel puede contener varias hojas.
# Como puedes ver en la imagen siguiente, tenemos un dataset de reseñas de productos que contiene cuatro hojas: 
# reviews, reviewers, products y product_categories.

# Vamos a leer el archivo Excel utilizando únicamente la ruta de archivo /datasets/product_reviews.xlsx:

import pandas as pd
df = pd.read_excel('/datasets/product_reviews.xlsx')
print(df.head())

           id reviewer_id  product_id  review
0  2546305677    cG441617  5003186430       3
1  2603422798    cH443811  7130698135       1
2  2598103631    bF100137  4023404310       4
3  2632674394    cF786880  7130698135       4
4  2594782880    aF649317  5003186430       5

# La hoja reviews se leyó en df por defecto porque es la primera hoja del archivo Excel. 
# Para cada reseña, esta hoja contiene un ID de la reseña (columna 'id'), un ID del cliente que dejó la reseña (columna 'reviewer_id'), 
# un ID del producto reseñado (columna 'product_id') y una puntuación de la reseña entre 1 y 5 (columna 'review').


## El parámetro sheet_name=

# Si necesitas una hoja diferente a la predeterminada, debes pasar dos argumentos: 
# la ruta del archivo (una cadena) y sheet_name= con el nombre de la hoja (también una cadena). Intentemos leer la hoja reviewers.

import pandas as pd
df = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name='reviewers')
print(df.head())

         id date_joined  zipcode
0  aF195825  2012-06-21    91914
1  aF249047  2019-03-26    91915
2  aF362092  2012-01-05    91941
3  aF484180  2019-06-11    91941
4  aF539111  2011-03-04    92003

# Y eso es todo lo que hay que hacer para leer hojas de archivos de Excel en los DataFrames de pandas. 
# El método read_excel() también tiene muchos otros parámetros que puedes usar para afinar el proceso según la estructura de los datos en el archivo de Excel, 
# como el parámetro header=. Como siempre, puedes consultar la documentación (materiales en inglés) oficial para solucionar cualquier problema que puedas encontrar.
# Ahora vamos a poner en práctica tus nuevas habilidades explorando más el dataset de reseñas de productos en las tareas.

# Fin.