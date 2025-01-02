# Capítulo 2/6
# Leer y visualizar datos

# Solucionar problemas con archivos CSV

# El primer paso para trabajar con datos es acceder a ellos. 
# En el sprint de Python Básico, aprendiste a leer archivos CSV con formato estándar en DataFrames de pandas usando el método read_csv(). 
# En esta lección, aprenderás a leer datos de archivos CSV que no se ajustan al formato estándar que vimos en Python Básico.
# Ve el siguiente vídeo primero y luego sigue leyendo para aprender todo al respecto.

# Recuerda que CSV significa valores separados por comas. Sin embargo, un archivo CSV no tiene que usar solo una coma como delimitador; se puede usar cualquier carácter. 
# Por ejemplo, los valores separados por tabuladores son otro formato común. Son archivos con los valores delimitados por tabulaciones. 
# A veces pueden aparecer como archivos .tsv o .tab (también conocidos como archivos TSV) además de .csv. 

# Echemos un vistazo a los datos en un archivo CSV llamado gpp_modified.csv. 
# Este conjunto de datos es un subconjunto de la Base de datos mundial de centrales eléctricas (Global Power Plant Database) del Instituto de Recursos Mundiales (World Resources Institute) (materiales en inglés), de acceso público. 
# Los datos de gpp_modified.csv se han modificado a partir del conjunto de datos original para reducir la cantidad de datos generales e incorporar un formato no estándar para la práctica de esta lección.

# Intentemos leer el archivo usando read_csv() sin ningún argumento adicional e imprimiendo las primeras 5 filas:

import pandas as pd
data = pd.read_csv('/datasets/gpp_modified.csv')
print(data.head())

Afghanistan|Kajaki Hydroelectric Power Plant Afghanistan|33   0|32   322|65   119|Hydro|
0                                 Afghanistan|Kandahar DOG|10   0|31    67|65   795|Solar|
1                                 Afghanistan|Kandahar JOL|10   0|31   623|65   792|Solar|
2           Afghanistan|Mahipar Hydroelectric Power Plant ...   0|34   556|69  4787|Hydro|
3           Afghanistan|Naghlu Dam Hydroelectric Power Pla...   0|34   641|69   717|Hydro|
4           Afghanistan|Nangarhar (Darunta) Hydroelectric ...  55|34  4847|70  3633|Hydro|

# ¡Vaya! ¿Qué diablos está pasando aquí? No hubo ningún error de Python, pero el DataFrame es un desastre. 
# Los nombres de las columnas se parecen a los propios datos, y es difícil saber qué se supone que son los datos. 
# Esta es una gran pista que nos indica que debemos abrir el archivo en un editor de texto y examinarlo más de cerca.

# Acabas de ver cómo los valores de un archivo de texto pueden delimitarse con caracteres distintos de la coma. 
# ¿Te acuerdas de los archivos .tsv que comentamos hace poco? 
# Los valores de esos archivos se separan con pestañas (tabs) o caracteres \t en terminología informática.


## El parámetro sep=

# El archivo definitivamente tiene comas, pero parece que el delimitador es en realidad el carácter |. 
# Podemos considerar esto cuando leemos los datos utilizando el parámetro sep= en read_csv(). 
# El argumento por defecto para sep= es ',', lo que explica la estructura de columnas que hemos observado antes. 
# En su lugar, usemos '|' como argumento y veamos cómo afecta eso al DataFrame:

import pandas as pd
data = pd.read_csv('/datasets/gpp_modified.csv', sep='|')
print(data.head())

   Afghanistan       Kajaki Hydroelectric Power Plant Afghanistan   33,0   32,322   65,119  Hydro  Unnamed: 6
0  Afghanistan                                       Kandahar DOG   10,0    31,67   65,795  Solar         NaN
1  Afghanistan                                       Kandahar JOL   10,0   31,623   65,792  Solar         NaN
2  Afghanistan      Mahipar Hydroelectric Power Plant Afghanistan   66,0   34,556  69,4787  Hydro         NaN
3  Afghanistan   Naghlu Dam Hydroelectric Power Plant Afghanistan  100,0   34,641   69,717  Hydro         NaN
4  Afghanistan  Nangarhar (Darunta) Hydroelectric Power Plant ...  11,55  34,4847  70,3633  Hydro         NaN

# Otro ejemplo consiste en leer en un archivo .tsv. Para ello, necesitamos establecer el parámetro sep= en '\t'. 
# Vamos a volver al conjunto de datos de plantas y sigamos trabajando con él. ¡Ahora sí está empezando a parecerse más a un verdadero DataFrame! 
# No obstante, aún nos quedan algunos asuntos por resolver.


## Los parámetros header= y names=

# Puede que hayas notado que los nombres de las columnas no parecen correctos; parece que se ha utilizado la primera fila de datos para los nombres de las columnas. 
# Esto no es bueno, ya que no queremos perder esos datos en la primera fila, y necesitamos buenos nombres de columnas para tener claridad en nuestro trabajo.

# Si vuelves a mirar las líneas que mostramos del archivo CSV, verás que la primera línea del archivo son sólo datos. 
# En otras palabras, el archivo no tiene un encabezado (la línea al principio del archivo que contiene los nombres de las columnas). 
# Afortunadamente, read_csv() puede manejar archivos sin cabeceras si utilizamos el argumento correcto para el parámetro header=.

# El argumento por defecto es header='infer', que le dice a pandas que intente adivinar los nombres de las columnas. 
# En nuestro caso, pandas adivinó que la primera fila de datos supuestamente son los nombres de las columnas. 
# Podemos arreglarlo pasando header=None de la siguiente manera:

import pandas as pd
data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None)
print(data.head())

             0                                                  1      2        3        4      5    6    
0  Afghanistan       Kajaki Hydroelectric Power Plant Afghanistan   33,0   32,322   65,119  Hydro  NaN
1  Afghanistan                                       Kandahar DOG   10,0    31,67   65,795  Solar  NaN
2  Afghanistan                                       Kandahar JOL   10,0   31,623   65,792  Solar  NaN
3  Afghanistan      Mahipar Hydroelectric Power Plant Afghanistan   66,0   34,556  69,4787  Hydro  NaN
4  Afghanistan   Naghlu Dam Hydroelectric Power Plant Afghanistan  100,0   34,641   69,717  Hydro  NaN

# Ahora todos nuestros datos se encuentran donde deberían estar. Como el archivo no tiene nombres de columnas, y no especificamos ninguno, 
# pandas simplemente utiliza números enteros consecutivos (0, 1 , 2 ….) para nombrar las columnas. 
# Sería una mala práctica para nosotros proceder sin dar a nuestras columnas nombres descriptivos. 
# Para ello, podrías consultar el dataset documentación para averiguar qué representan las columnas, 
# pero en este caso te proporcionaremos una lista de buenos nombres de columnas.

# Podríamos renombrar las columnas después de leer los datos usando el atributo columns del DataFrame o el método rename(), 
# pero también podemos definir los nombres mientras leemos los datos usando el parámetro opcional names= en read_csv(). 
# Si pasas una lista de nombres de columnas al parámetro names=, pandas asignará esos nombres a las columnas en el orden en que aparecen en la lista.

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
data = pd.read_csv('/datasets/gpp_modified.csv', sep='|', header=None, names=column_names)
print(data.head())

       country                                              name capacity_mw latitude longitude primary_fuel owner     
0  Afghanistan      Kajaki Hydroelectric Power Plant Afghanistan        33,0   32,322    65,119        Hydro   NaN
1  Afghanistan                                      Kandahar DOG        10,0    31,67    65,795        Solar   NaN
2  Afghanistan                                      Kandahar JOL        10,0   31,623    65,792        Solar   NaN
3  Afghanistan     Mahipar Hydroelectric Power Plant Afghanistan        66,0   34,556   69,4787        Hydro   NaN
4  Afghanistan  Naghlu Dam Hydroelectric Power Plant Afghanistan       100,0   34,641    69,717        Hydro   NaN

# ¡Ahora tenemos un DataFrame con el que realmente podemos trabajar! 
# Sin embargo, ahora que sabes lo que representan las columnas numéricas, es posible que hayas notado otro problema que debemos solucionar.


## El parámetro decimal=

# Los valores de capacidad de megavatios, latitud y longitud utilizan comas en lugar de puntos para el separador decimal. 
# La convención estándar en muchos países europeos es utilizar la coma decimal, pero Python requiere que se utilice el punto decimal en los números de punto flotante. 
# Si compruebas los tipos de datos de esas columnas, encontrarás que pandas los lee como cadenas.

# En read_csv() podemos usar el parámetro decimal= y pasarle ',' como argumento. Por defecto, read_csv() utiliza decimal='.', 
# por lo que no reconoció los valores numéricos de nuestro conjunto de datos como números de coma flotante.

# Para ponerlo todo en orden, leamos el conjunto de datos por última vez:

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

# Con solo una lista de nombres de columnas y una línea de código, pudimos leer nuestro archivo CSV no estándar en un DataFrame que está listo para el futuro análisis.


## Resumen

# Como siempre, puedes conocer todos estos parámetros de read_csv() y más en la documentación (materiales en inglés) oficial. 
# Tu entorno de trabajo también podría proporcionar esta información. 
# Por ejemplo, en un cuaderno Jupyter, puedes escribir el nombre de un método y presionar $\mathtt {Shift+Tab}$ para mostrar la documentación. 
# Así es como se ve:

https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

# Esto es lo que llamamos docstring. Cuando se abre, puedes desplazarte hacia abajo para ver todos los parámetros, sus valores por defecto y breves descripciones.
# ¡Ahora vamos a poner en práctica tus nuevas habilidades!

# Fin.