# Capítulo 2/6
# Leer y visualizar datos

### Ejercicios

# Ejercicio 1
# El precódigo ya incluye código para imprimir las 5 primeras filas del conjunto de datos de la central eléctrica utilizando el método head(). 
# Escribe código que:
# 1. muestrea 5 filas aleatorias del dataset y las almacena en la variable sample. Utiliza random_state=543210 en el muestreo.
# 2. imprime la variable sample.

import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

print(data.head())
print()

sample = data.sample(5, random_state=543210) # escribe tu código aquí
print(sample) # escribe tu código aquí)

# Resultado
       country  ... owner
0  Afghanistan  ...   NaN
1  Afghanistan  ...   NaN
2  Afghanistan  ...   NaN
3  Afghanistan  ...   NaN
4  Afghanistan  ...   NaN

[5 rows x 7 columns]

                        country  ...                         owner
24993  United States of America  ...  CVI CleanCapital Solar 4 LLC
1978                     Brazil  ...                           NaN
1190                     Brazil  ...                           NaN
5430                      China  ...                           NaN
16218                     Italy  ...                           NaN

[5 rows x 7 columns]


# Ejercicio 2
# Ahora que ya tenemos una idea de cómo son los datos de cada columna, comprueba la información general de este conjunto de datos llamando al método info(). 
# Hemos incluido el código del último ejercicio para que puedas comparar las filas de muestra con la salida de info().

# Código
import pandas as pd

column_names = [
    'country',
    'name',
    'capacity_mw',
    'latitude',
    'longitude',
    'primary_fuel',
    'owner'
]
data = pd.read_csv(
    '/datasets/gpp_modified.csv',
    sep='|',
    header=None,
    names=column_names,
    decimal=',',
)

sample = data.sample(5, random_state=543210)
print(sample)
print()

data.info()

# Resultado
                        country  ...                         owner
24993  United States of America  ...  CVI CleanCapital Solar 4 LLC
1978                     Brazil  ...                           NaN
1190                     Brazil  ...                           NaN
5430                      China  ...                           NaN
16218                     Italy  ...                           NaN

[5 rows x 7 columns]

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 34936 entries, 0 to 34935
Data columns (total 7 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   country       34936 non-null  object 
 1   name          34936 non-null  object 
 2   capacity_mw   34936 non-null  float64
 3   latitude      34936 non-null  float64
 4   longitude     34936 non-null  float64
 5   primary_fuel  34936 non-null  object 
 6   owner         20868 non-null  object 
dtypes: float64(3), object(4)
memory usage: 1.9+ MB

# Fin.