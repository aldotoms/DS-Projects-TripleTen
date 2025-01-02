# Sprint 4
# Manipulación de datos (Data Wrangling) (continuación)

## *Gráficos de barras

# Hasta ahora hemos estado aprendiendo cómo visualizar relaciones entre variables numéricas en nuestros datos, pero ¿qué pasa con las variables categóricas? 
# La mayoría de los conjuntos de datos con los que trabajarás tienen una combinación de datos numéricos y categóricos.
# Los gráficos de barras son una gran herramienta para comparar categorías definidas por un valor numérico.
# Así que, en esta lección, haremos gráficos de barras para visualizar datos tomados de la Oficina del Censo de los Estados Unidos sobre niveles históricos de población en 
# California, Oregón y Washington. Los gráficos de barras son una excelente opción aquí porque nos permitirán comparar propiedades numéricas (población) entre categorías (estados).
# Comencemos mostrando información general sobre el conjunto de datos:

import pandas as pd

df = pd.read_csv('Datasets/west_coast_pop.csv')
df.info()

# ¡Solo 10 filas! También podemos mostrar todo el DataFrame, entonces:

import pandas as pd

df = pd.read_csv('Datasets/west_coast_pop.csv')
print(df)

# Tenemos datos de población de California, Oregón y Washington, tomados cada 10 años desde 1920 hasta 2010, en unidades de millones de personas.
# Comparemos la población de cada estado por año. Para visualizar estos datos en un gráfico de barras, llamamos al método plot() en el DataFrame y especificamos kind='bar' 
# como un argumento. Pero necesitamos especificar que queremos la columna 'year' en el eje X, de lo contrario, el gráfico no tendrá mucho sentido:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/west_coast_pop.csv')

df.plot(x='year', kind='bar')
plt.show()

# Tal como se esperaba: un conjunto de tres barras, una para cada estado, para cada año en el conjunto de datos.
# Si no especificas ninguna columna para el parámetro y=, pandas creará automáticamente una barra para cada columna en el DataFrame que no esté en el eje X; 
# en este caso, una barra para cada población del estado.
# El gráfico de barras facilita sacar ciertas conclusiones sobre los datos. 
# Por ejemplo, podemos ver que la población de California es consistentemente mucho mayor que la de otros estados. 
# También vemos que la población ha crecido constantemente en todos los estados.
# Sin embargo, si queremos presentar estos datos a otras personas, necesitamos que se vean más profesionales:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/west_coast_pop.csv')

df.plot(x='year',
        kind='bar',
        title='West coast USA population growth',
        xlabel='Year',
        ylabel='Population (millions)')

plt.legend(['CA', 'OR', 'WA'])
plt.show()

# ¡Mucho mejor!

# Para mejorar nuestra gráfica, usamos una nueva función de Matplotlib llamada legend(). 
# Esta función nos permite especificar manualmente las etiquetas de leyenda pasando una lista de nombres de etiquetas en lugar del comportamiento predeterminado de usar los nombres de columna del DataFrame.
# La audiencia a la que presentamos esta gráfica probablemente no esté familiarizada con los aspectos técnicos de nuestro conjunto de datos, por lo que nombres como 'ca_pop' podrían no tener sentido para dicha audiencia. 
# Es mucho mejor usar etiquetas conocidas como CA, OR y WA.
# Observa que el orden de las etiquetas de la leyenda en la lista corresponderá al orden de las columnas en el DataFrame, por lo que es importante ordenar las etiquetas correctamente. 
# Además, plt.legend() tiene que venir después de que llamemos a plot() en nuestro DataFrame.
# Ahora es el momento de explorar más este conjunto de datos en las tareas.


## Ejercicio:

# La población de California es mucho mayor que la de Oregón y Washington, por lo que es difícil hacerse una idea de los datos de esos dos estados a partir del gráfico que hicimos. 
# Crea un gráfico de barras que muestre solo las poblaciones de Oregón y Washington para cada año en el conjunto de datos. 
# Hazlo llamando a plot() en df con argumentos que le den a tu gráfica las siguientes propiedades:

#   1. Incluye solo datos para Oregón y Washington especificando nuestro eje Y, tal como hicimos en la lección anterior.
#   2. Título: “Pacific Northwest population growth” (“Crecimiento de la población del noroeste del Pacífico“). La distinción entre mayúsculas y minúsculas es importante.
#   3. El eje X etiquetado: “Year” ("Año").
#   4. El eje Y etiquetado: “Population (millions)” ("Población (millones)").
#   5. Leyenda con etiquetas "OR" y "WA" para las poblaciones de Oregón y Washington, respectivamente.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/west_coast_pop.csv')

df.plot(x='year',
        y=['or_pop', 'wa_pop'],
        kind='bar',
        title='Pacific Northwest population growth',
        xlabel='Year',
        ylabel='Population (millions)')

plt.legend(['OR', 'WA'])
plt.show()

# FIN.