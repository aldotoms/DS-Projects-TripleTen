# Capítulo 1/6
# La librería Pandas

# Pandas para archivos de Excel y CSV

# En la lección anterior, creaste tu propio DataFrame a partir de un conjunto de datos almacenados en una lista anidada. 
# También sabes cómo acceder a los atributos de un DataFrame por separado o utilizando el método info().
# Antes de profundizar en cualquier análisis, es una buena idea obtener una descripción general rápida de los datos; 
# ya hemos aprendido sobre los atributos y el método info() que nos permite hacer esto. Además de estos, pandas ofrece otros métodos.
# Asimismo, en la vida real, a menudo no creamos nuestros propios datos, sino que recibimos conjuntos de datos en forma de archivos u obtenemos estos archivos de una base de datos. 
# Cuando obtenemos un archivo con datos, todo lo que tenemos que hacer es leer estos conjuntos de datos en DataFrames.

# Teoria
# En esta lección, aprenderás a leer ficheros CSV y Excel en pandas y a recuperar la primera y la última fila de tu conjunto de datos utilizando los métodos head() y tail().

# Lectura de archivos CSV

# En la lección anterior hemos utilizado un conjunto de datos simple con países y sus capitales, que contenía una pequeña cantidad de datos ya almacenados como una lista anidada. Sin embargo, al recibir un conjunto de datos en formato de archivo, este se almacena con una estructura específica que pandas puede convertir en un objeto de tipo DataFrame.
# Tratarás principalmente con archivos CSV ("comma-separated value", por sus siglas en inglés), aunque también habrá algunos archivos de Excel.
# En los archivos CSV, las comas separan los valores de diferentes columnas. Pandas lee estos archivos y transfiere los datos a un DataFrame.
# Como ya se mencionó, un DataFrame requiere datos y nombres de columna, los cuales se proporcionan en archivos CSV:
# - La primera línea contiene los nombres de las columnas.
# - Cada línea siguiente contiene los datos que corresponden a una fila de la tabla.
# A continuación, ilustramos el archivo CSV a la izquierda y cómo se convierte en un DataFrame de pandas a la derecha.

# Teoria

# En esta lección, aprenderás a leer ficheros CSV y Excel en pandas y a recuperar la primera y la última fila de tu conjunto de datos utilizando los métodos head() y tail().
# Lectura de archivos CSV
# En la lección anterior hemos utilizado un conjunto de datos simple con países y sus capitales, que contenía una pequeña cantidad de datos ya almacenados como una lista anidada. Sin embargo, al recibir un conjunto de datos en formato de archivo, este se almacena con una estructura específica que pandas puede convertir en un objeto de tipo DataFrame.

# Tratarás principalmente con archivos CSV ("comma-separated value", por sus siglas en inglés), aunque también habrá algunos archivos de Excel.
# En los archivos CSV, las comas separan los valores de diferentes columnas. Pandas lee estos archivos y transfiere los datos a un DataFrame.
# Como ya se mencionó, un DataFrame requiere datos y nombres de columna, los cuales se proporcionan en archivos CSV:
# - La primera línea contiene los nombres de las columnas.
# - Cada línea siguiente contiene los datos que corresponden a una fila de la tabla.
# A continuación, ilustramos el archivo CSV a la izquierda y cómo se convierte en un DataFrame de pandas a la derecha.

import pandas as pd
df = pd.read_csv('/datasets/music_log_chpt_11.csv') # el argumento es una ruta de archivo

Una ruta de archivo es un string que indica dónde está almacenado un archivo en una computadora. La ruta puede ser diferente dependiendo de dos factores:

# El sistema operativo que determina su forma.
#  - En Windows, la ruta suele escribirse con una barra invertida: 'C:\catalog\file.csv'
#  - En macOS y Linux, esta se escribe con una barra diagonal: '/catalog/files.csv'

# 2. Si la ruta es relativa o absoluta.
# Una ruta absoluta comienza en el directorio raíz del sistema. En Windows, es el nombre del disco ("C"): 'C:\catalog\file.csv'. 
# En Linux y macOS, la ruta se ejecuta con una "raíz" indicada por una barra antes de su nombre: '/catalog/file.csv'.
# Una ruta relativa se refiere a una ubicación que es relativa al directorio actual. Por ejemplo, 
# si un programa y un archivo se ejecutan desde el mismo directorio, la ruta será solo el nombre del archivo. 
# Si un programa se ejecuta desde un directorio superior, la ruta relativa incluirá el nombre de un subdirectorio donde se encuentre el archivo:

# En este caso, estamos leyendo el archivo music_log_chpt_11.csv ubicado en la carpeta datasets, que se encuentra en el directorio raíz. 
# Si deseas volver a ver el código, aquí está:

df = pd.read_csv('/datasets/music_log_chpt_11.csv') # el argumento es una ruta de archivo ABSOLUTA


# Lectura de archivos de Excel

# Como se mencionó anteriormente, Excel tiene dificultades con archivos grandes, mientras que pandas los maneja con facilidad. 
# Por lo tanto, además de leer archivos CSV, con frecuencia necesitamos importar archivos de Excel para trabajar con ellos.
# Esta necesidad también se debe a que Excel es una forma muy popular de almacenar datos en las empresas. 
# Y estos datos son los que necesita utilizar cualquier profesional de los datos para alcanzar sus objetivos.
# El proceso de crear un DataFrame a partir de un archivo Excel es similar a lo que hicimos con los archivos CSV. 
# Pandas proporciona una función integrada read_excel() para leer archivos de Excel que también espera una ruta como argumento. 
# Así es como se hace:

import pandas as pd

df = pd.read_excel('/datasets/music_log.xlsx') # el argumento es una ruta de archivo

# El fragmento de código anterior se lee en el archivo music_log.xlsx, que es un archivo Excel. 
# Podemos identificar un archivo Excel por su extensión. Las extensiones comunes para archivos de Excel incluyen .xlsx, .xls, .xlsm, .xlsb y .xltx.
# Como resultado, obtenemos un DataFrame. Para concluir, hay varias formas de crear un DataFrame, es posible:

# - crearlo a partir de una lista, como lo hicimos previamente para los países y sus capitales;
# - leer un archivo CSV utilizando la función integrada de pandas;
# - leerlo en un archivo Excel.

# Quizás te preguntes, ¿por qué es importante almacenar nuestros datos en forma de DataFrame? 
# La respuesta está en las funciones de análisis integradas que están disponibles exclusivamente para los DataFrames. 
# Hasta el momento, has aprendido sobre los atributos y el método info(). Ahora, investiguemos qué más podemos hacer.


# Métodos head y tail

# Ya te familiarizaste con nuestro conjunto de datos music_log, que almacena información sobre las canciones reproducidas por los usuarios en una plataforma de música online. 
# Lo leímos desde un archivo CSV y lo almacenamos como un DataFrame en la variable df de esta forma:

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

# Ahora que ya tenemos nuestros datos en un nuevo conjunto de datos, ¿cuál es el siguiente paso lógico? 
# Para nosotros, la respuesta es simple: hay que evaluar el conjunto de datos, o al menos una parte de este, echándole un vistazo para tener una idea de su contenido.
# Pandas ofrece dos métodos para mostrar el principio o el final de un conjunto de datos: head() y tail(). 
# Como sugieren sus nombres, head() muestra las primeras filas de una tabla, mientras que tail() muestra las últimas filas.
# Ahora veamos estos métodos en acción. Como sabes, un método es algo que podemos aplicar a un objeto, en nuestro caso, a un DataFrame. 
# Comencemos por aplicar el método head() y mostrar el resultado.

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

print(df.head())

# Como resultado, hemos obtenido los nombres de las columnas y las primeras cinco filas de un conjunto de datos, junto con sus índices correspondientes que van de 0 a 4. 
# La función head() muestra las primeras 5 filas por defecto, pero puedes comprobar cualquier número de filas pasando un argumento que especifique el número deseado. 
# Por ejemplo, para mostrar las 3 primeras filas, utiliza el siguiente código:

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

print(df.head(3))

# Ten en cuenta que pasamos 3 como argumento y aquí está nuestro resultado:

# El método tail funciona de forma similar pero muestra las últimas filas. 
# Así es como podemos comprobar las últimas 3 filas de un conjunto de datos:

import pandas as pd

df = pd.read_csv('/datasets/music_log_chpt_11.csv')

print(df.tail(3))

# Fin.