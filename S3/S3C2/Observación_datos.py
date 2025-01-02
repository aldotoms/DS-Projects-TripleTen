# Capítulo 2/6
# Leer y visualizar datos

# Observación de los datos

# ¿Recuerdas que en el sprint sobre Python Básico aprendimos sobre algunos atributos y métodos de DataFrame que te dan una visión general de tus datos? 
# Son muy útiles cuando empiezas a trabajar con un nuevo dataset porque te ayudan a plantear las primeras preguntas que debes explorar.
# Como son tan importantes, en esta lección vamos a repasar esas herramientas, además de presentar un nuevo método para echar un vistazo a tus datos. 
# En esta lección seguiremos utilizando la base de datos global de centrales eléctricas (materiales en inglés) modificada.

https://datasets.wri.org/dataset/globalpowerplantdatabase

## Revisión del método info()

# Nunca es mala idea llamar al método info() cada vez que empieces a trabajar con un nuevo DataFrame. 
# El método info() no devuelve nada, sino que imprime información general sobre el DataFrame (lo que significa que no es necesario utilizar print() con info()).
# Leamos de nuevo los datos de la central y llamemos a info() para ver qué información nos brinda:

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

data.info()

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

# Solo con este método, obtenemos la siguiente información:
# - el número de filas (RangeIndex: 34936 entries);
# - el número de columnas (total 7 columns);
# - el nombre de cada columna (Column);
# - el número de valores de cada columna que no están ausentes (Non-Null Count);
# - el tipo de datos de cada columna (Dtype).

# Ten en cuenta: no se puede acceder directamente a la información mostrada por info() para almacenarla en variables o utilizarla en cálculos porque info() no devuelve nada, solo muestra en la pantalla. 
# Si necesitas asignar un atributo del DataFrame a una variable para utilizarla más tarde, tendrás que acceder a ese atributo directamente.
# Si quieres almacenar el número de filas y columnas como variables, puedes utilizar el atributo shape. 
# Este atributo devuelve tanto el número de filas como el número de columnas en el dataset. Así es como puede utilizarse:

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

n_rows, n_cols = data.shape

print(f"El DataFrame tiene {n_rows} filas y {n_cols} columnas")  

# Respuesta: El DataFrame tiene 34936 filas y 7 columnas

# Observa cómo hemos utilizado una cadena f para imprimir información sobre las filas y columnas del conjunto de datos.
# La función data.shape devuelve una tupla como salida. Una tupla es un tipo de datos en Python, al igual que las listas y otros tipos. 
# En palabras sencillas, una tupla es una colección de objetos separados por comas.
# Una tupla es similar a una lista de Python en términos de indexación, objetos anidados y repetición. Sin embargo, 
# la principal diferencia entre ambas es que una tupla Python es inmutable (no puede modificarse), mientras que una lista Python es mutable.

# En el código anterior, asignamos los valores de la tupla a variables diferentes separando los nombres de las variables con una coma: n_rows, n_cols = data.shape.
# En general, puedes "desempaquetar" elementos de tuplas o listas en variables de esta manera.
# Pregunta
# Sabemos que el método info() devuelve el número de valores no ausentes. Sabiendo esto podemos calcular fácilmente el número de valores ausentes.

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

# Por ejemplo, podemos determinar el número de valores ausentes en la columna 'owner' utilizando la información del método info() 
# restando el número de valores no nulos en la columna 'owner' del número total de filas del DataFrame.
# En lugar de hacerlo manualmente, revisemos la manera de calcular el número de valores ausentes en una columna concreta utilizando pandas.


## El método sample()
# El método info() es estupendo, pero puedes obtener una visión aún más completa de tus datos combinando info() con la impresión de algunas filas de DataFrame. 
# Recuerda que podemos hacerlo con los métodos head() o tail(). Por ahora vamos a empezar con head():

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

       country                                              name capacity_mw latitude longitude primary_fuel owner   
0  Afghanistan      Kajaki Hydroelectric Power Plant Afghanistan        33.0   32.322    65.119        Hydro   NaN
1  Afghanistan                                      Kandahar DOG        10.0    31.67    65.795        Solar   NaN
2  Afghanistan                                      Kandahar JOL        10.0   31.623    65.792        Solar   NaN
3  Afghanistan     Mahipar Hydroelectric Power Plant Afghanistan        66.0   34.556   69.4787        Hydro   NaN
4  Afghanistan  Naghlu Dam Hydroelectric Power Plant Afghanistan       100.0   34.641    69.717        Hydro   NaN

# Ahora podemos ver los valores reales de nuestros datos junto con la sinopsis general proporcionada por info(). 
# Por defecto, head() imprime las 5 primeras filas. En este caso, esas filas corresponden a centrales eléctricas en Afganistán. 
# Dado que se trata de un dataset global, cabría esperar que también estuvieran representados otros países, 
# pero no podemos estar seguros de que sea así al ver solo las 5 primeras filas. Intentemos con 10 filas:

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

print(data.head(10))

       country                                               name capacity_mw  latitude  longitude primary_fuel owner
0  Afghanistan       Kajaki Hydroelectric Power Plant Afghanistan       33.00   32.3220    65.1190        Hydro   NaN
1  Afghanistan                                       Kandahar DOG       10.00   31.6700    65.7950        Solar   NaN
2  Afghanistan                                       Kandahar JOL       10.00   31.6230    65.7920        Solar   NaN
3  Afghanistan      Mahipar Hydroelectric Power Plant Afghanistan       66.00   34.5560    69.4787        Hydro   NaN
4  Afghanistan   Naghlu Dam Hydroelectric Power Plant Afghanistan      100.00   34.6410    69.7170        Hydro   NaN
5  Afghanistan  Nangarhar (Darunta) Hydroelectric Power Plant ...       11.55   34.4847    70.3633        Hydro   NaN
6  Afghanistan            Northwest Kabul Power Plant Afghanistan       42.00   34.5638    69.1134          Gas   NaN
7  Afghanistan  Pul-e-Khumri Hydroelectric Power Plant Afghani...        6.00   35.9416    68.7100        Hydro   NaN
8  Afghanistan   Sarobi Dam Hydroelectric Power Plant Afghanistan       22.00   34.5865    69.7757        Hydro   NaN
9      Albania                                         Bistrica 1       27.00   39.9116    20.1047        Hydro   NaN

# ¡Ajá! Ahora también podemos ver los datos de una central eléctrica en Albania. 
# Probablemente, los países aparecen en orden alfabético (puedes comprobarlo utilizando unique(), que devuelve los valores en el orden en que aparecen).
# No es raro que los datasets tengan el mismo valor en una columna durante muchas filas consecutivas, incluso durante cientos o miles de filas. 
# En estas situaciones, puede ser más útil utilizar sample() en lugar de head() o tail().
# El método sample() selecciona filas aleatorias del DataFrame en lugar de filas consecutivas del principio o del final del DataFrame. 
# Vamos a utilizarlo para imprimir 5 filas de nuestros datos:

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

print(data.sample(5))

                        country                         name  capacity_mw  latitude  longitude primary_fuel                   owner 
5208                      China  Bayanur Wuliji Wind Phase 2         49.0   41.5333   106.4167         Wind                     NaN  
29010  United States of America          J Robert Massengale         84.0   33.6039  -101.8408          Gas  City of Lubbock - (TX) 
611                   Australia        Mugga Lane Solar Park         13.0  -35.3989   149.1460        Solar       Maoneng Australia
5350                      China           Changli Datan Wind         48.0   39.5050   119.1797         Wind                     NaN
4419                     Canada                       Rawdon          2.5   46.0458   -73.7294        Hydro         Algonquin Power

# Ahora tenemos una vista previa de filas más diversa de la que teníamos usando solo head() o tail(). 
# A diferencia de head() y tail(), sample() selecciona 1 fila por defecto, por lo que tuvimos que especificar que queríamos 5 filas. 
# Fíjate en que sample() también conserva los valores del índice del DataFrame original, para que puedas ver de dónde proceden las filas. 
# La salida del fragmento de código anterior muestra que se han muestreado las filas con los índices 5208, 29010, 611, 5350 y 4419.
# Si ejecutaras el código anterior en el sandbox de la plataforma o localmente en tu propia máquina, es casi seguro que obtendrías un resultado diferente al que hemos mostrado arriba. 
# Y el resultado cambiará cada vez que vuelvas a ejecutar el código. Es porque sample() selecciona las filas "de forma aleatoria".
# Si quieres usar sample() y obtener el mismo resultado cada vez que ejecutes tu código, necesitas usar el parámetro random_state= 
# y establecerlo en algún valor entero de tu elección (cualquier número entero entre 0 y 4294967295). Aquí tienes un ejemplo:

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

print(data.sample(5, random_state=1369))

                        country                 name  capacity_mw  latitude  longitude primary_fuel                         owner 
10818                    France             Curières      1.13499   44.6495     2.8924        Solar                           NaN
1513                     Brazil  Cachoeira Caldeirão    219.00000    0.8533   -51.2917        Hydro                           NaN
1030                    Belgium              AWIRS 4     95.00000   50.5851     5.4180      Biomass                           NaN
31250  United States of America    Paragould Turbine     13.90000   36.0243   -90.5092          Gas  Paragould Light & Water Comm
20126               South Korea             Yeongnam    400.00000   35.5141   129.3835         Coal          Korea Southern Power

# Si ejecutas este código con random_state=1369 obtendrás siempre el mismo resultado. 
# Puede que quieras establecer un estado aleatorio particular para la reproducibilidad de tu código, comparando el código con otros y probando los errores.

# Fin.