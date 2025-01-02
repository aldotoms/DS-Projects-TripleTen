# Sprint 4
# Manipulación de datos (Data Wrangling) (continuación)

## *Histogramas

# Ahora que sabemos cómo los gráficos de dispersión, los gráficos de líneas y los gráficos de barras nos ayudan a comprender y analizar las relaciones entre variables 
# en nuestros datos, aprenderemos a trazar una distribución para una sola variable.

# Es hora de que conozcas los histogramas.
# Histogramas: Un histograma es un gráfico que muestra la frecuencia con la que aparecen diferentes valores para una variable en tu conjunto de datos. 
# Aunque puede parecerse a los gráficos de barras, existen algunas diferencias clave entre los dos tipos:
#   - Los gráficos de barras se utilizan para comparar valores de variables discretas; los histogramas se utilizan para trazar distribuciones de variables numéricas continuas.
#   - El orden de las barras en los gráficos de barras puede modificarse para efectos de estilo o de comunicación. Sin embargo, el orden de las barras en los histogramas no puede cambiarse.
# En un histograma, el eje X representa la variable y su rango de valores. El eje Y representa la frecuencia de ocurrencia para cada valor. Y es por ello que no tiene sentido cambiar el orden de las barras.

# Este histograma representa una variable que toma valores en el rango de 1 a 9, siendo los valores alrededor de 4 y 7 los más frecuentes.
# Debido a que la variable puede tomar cualquier valor en el rango, contar cada valor único y graficar las frecuencias no es útil. 
# n su lugar, un histograma parte el rango de valores en secciones llamadas contenedores. En la gráfica anterior, uno de los contenedores está resaltado para ilustrar los tamaños de los contenedores.
# Cada contenedor tiene el mismo ancho; la altura de un contenedor corresponde al número de observaciones que están dentro del rango de ese contenedor. 
# Por lo tanto, la apariencia de un histograma depende del número de contenedores que decidamos que debe tener.
# El histograma anterior tiene 25 contenedores. Veamos qué pasa si trazamos los mismos datos utilizando tan solo 10 contenedores.

# El gráfico con 10 contenedores no tiene suficientes detalles, y el de 100 contenedores tiene demasiados. 
# Elegir el número correcto de contenedores puede ser más un arte que una ciencia, pero con la práctica lograrás dominarlo.
# Si deseas tener una mejor idea de cómo el tamaño del contenedor afecta a un histograma, puedes usar esta herramienta interactiva para cambiar la cantidad de contenedores y ver qué sucede. ¡Pruébala a continuación!

## *Trazar histogramas de DataFrames
# En pandas, hay dos formas de trazar histogramas:
#   1. El método hist().
#   2. El método plot() con el argumento kind='hist'.
# Examinemos hist() primero:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')
df.hist()

plt.show()

# Si se llama a hist() en un DataFrame sin ningún argumento, crea un gráfico separado para cada columna numérica. 
# ¿Estos histogramas te parecen familiares? ¡Eran los gráficos en la diagonal de nuestras matrices de dispersión!
# Ahora intentemos llamar a plot() en nuestro DataFrame para hacer histogramas:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df.plot(kind='hist')

plt.show()

# El comportamiento predeterminado de plot() difiere considerablemente del de hist(). 
# Usando plot() podemos trazar cada histograma en el mismo gráfico. Sin embargo, esto no tiene sentido para estos datos, 
# ya que cada una de las cuatro columnas representa una cantidad física distinta. Por tanto, no es adecuado trazarlas todas a lo largo del mismo eje.


## *Trazado de histogramas de columnas
# A menudo, querrás explorar una variable a la vez. 
# Podemos trazar un histograma para una sola columna usando hist() pasando el nombre de la columna como un argumento para el parámetro column=. 
# Echemos un vistazo más de cerca a la columna 'height' (altura):

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df.hist(column='height')
plt.show()  

# De manera alternativa, podríamos trazar el mismo histograma llamando hist() sólo en la columna 'height':

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df['height'].hist()
plt.show()

# Por defecto, hist() utiliza 10 contenedores. Sin embargo, para estos datos, 10 contenedores parecen demasiado bajos para captar el nivel de detalle que deseamos. 
# Para resolverlo, podemos usar el parámetro bins= para ajustar el número de contenedores usados:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df.hist(column='height', bins=30)
plt.show()

# ¡Mucho mejor!
# Podemos hacer el mismo histograma usando plot() llamándolo sólo en la columna 'height':

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df['height'].plot(kind='hist', bins=30)
plt.show()

# El histograma es el mismo, pero el formato predeterminado de las gráficas difiere entre métodos. S
# i deseas ver un histograma para una sola variable, te recomendamos usar plot() porque hist() no es compatible con todas las palabras clave de formato que has aprendido, 
# como title=, xlabel=, ylabel=.


## *Comparación de histogramas para subconjuntos de datos
# La altura del histograma trazado arriba muestra dos picos de valores más frecuentes. 
# Esto podría deberse a las diferencias en la distribución de la estatura de hombres y mujeres. 
# Para investigar esta cuestión, podemos trazar los histogramas de altura para hombres y mujeres por separado en la misma gráfica.
# Todo lo que tenemos que hacer es filtrar el DataFrame por sexo, y luego llamar a plot() en la columna 'height'. 
# Si hacemos esto dos veces (una para cada sexo), pandas automáticamente trazará ambos en el mismo gráfico, con el segundo histograma delante del primero:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df[df['male'] == 1]['height'].plot(kind='hist', bins=30)    # esto mostrará el gráfico de hombres
df[df['male'] == 0]['height'].plot(kind='hist', bins=30, alpha=0.8) # esto mostrará el gráfico de mujeres e incluye un valor alpha para que podamos ver ambos histogramas por completo

plt.legend(['Male', 'Female']) # leyenda, que sigue el mismo orden trazado anteriormente
plt.show()

# Colocar ambos histogramas en el mismo gráfico hace mucho más fácil ver que la distribución de las alturas para hombres se desplaza hacia la derecha en comparación con la de las mujeres. 
# Por ejemplo, un hombre promedio es probablemente más alto que una mujer promedio. Es por eso que el histograma combinado para el conjunto de datos completo tiene dos picos.
# Observa que, en este caso, tiene sentido trazar ambos histogramas en el mismo gráfico, ya que ambos representan la misma variable: height. 
# Sin embargo, en otros casos podría no tener sentido, y debes ser consciente de ello.
# Si lo necesitas, puedes usar el índice para dividir tu histograma usando la misma lógica que para el filtro que utilizaste con la variable 'male'. 
# Para ello, ordena la variable y reinicia los índices para que la mujer sea la primera en el DataFrame. Después, corta el DataFrame a la mitad para poder ver la mitad de abajo de los datos.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df = df.sort_values('male').reset_index(drop=True)

df = df[df.index < 5000]

df.hist(column='height', bins=50)

plt.show()

# Resumen
# Los histogramas nos dan una idea de cómo se distribuyen nuestros datos. Al visualizar la distribución, podemos obtener información clave tales como los valores más frecuentes y la presencia de valores atípicos.
#   - Podemos usar el método hist() o plot() para hacer histogramas para nuestras cuatro columnas numéricas.
#   - Llamar a hist() en un DataFrame crea un histograma por separado para cada columna numérica.
#   - Llamar a plot() con kind='hist' traza un histograma para cada columna numérica , todas en el mismo gráfico.
#   - Llamar a cualquier método varias veces trazará también cada nuevo histograma en el mismo gráfico. Esto es útil para comparar distribuciones entre diferentes subconjuntos de datos, como la altura de hombres y mujeres.
# Ahora es tu turno de practicar cómo hacer histogramas.

# FIN.