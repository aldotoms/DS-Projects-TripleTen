# Capítulo 5/6
# Visualización de datos

## Ejercicios

# Ejercicio 1
# Crea un gráfico de líneas para el volumen comercial del conjunto de datos de acciones de Starbucks. Haz que tu gráfico se adhiera a lo siguiente:

#   1. Titulado "Historic SBUX volume" ("Volumen histórico de SBUX”) (la distinción entre mayúsculas y minúsculas es importante).
#   2. Eje X con la leyenda “Date” ("Fecha").
#   3. Eje Y con la leyenda “Volume” ("Volumen").
#   4. Leyendas de marca del eje X rotadas 50 grados.
#   5. El límite del eje Y de 1 millón a 70 millones (puedes usar 1e6 y 7e7 como los límites superior e inferior, respectivamente, 
#      para evitar los ceros. 1 000 000 = 1e6, es decir, 1 elevada a la 6a).
#   6. Sin leyenda.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/sbux.csv')

df.plot(x='date',
        y='volume',
        title='Historic SBUX volume',
        xlabel='Date',
        ylabel='Volume',
        ylim=[1e6, 7e7],
        legend=True,
        rot=45
       )

plt.show()


## Ejercicio 2
# Crea un gráfico de líneas que incluya tanto el precio de apertura como el de cierre. 
# Para hacer esto, puedes pasar la lista de nombres de columna, cols, proporcionada en el precódigo como tu argumento para y=. 
# Dado que tendrás dos variables diferentes en el mismo gráfico, asegúrate de incluir una leyenda esta vez. Haz que tu gráfico también cumpla con lo siguiente:

#   1. Titulado “Historic SBUX price” ("Precio histórico de SBUX") (la distinción entre mayúsculas y minúsculas es importante).
#   2. Eje X con la leyenda “Date” ("Fecha").
#   3. Eje Y con la leyenda “Share price / USD” ("Precio de la acción / USD").
#   4. Leyendas de marca del eje X rotadas 50 grados.

# No olvides incluir plt.show().

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/sbux.csv')
cols = ['open', 'close']

df.plot(x='date',
        y=cols,
        title='Historic SBUX price',
        xlabel='Date',
        ylabel='Share price / USD',
        legend=True,
        rot=50
       )

plt.show()

# FIN.