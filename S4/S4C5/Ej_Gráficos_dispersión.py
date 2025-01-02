# Gráficos de dispersión
# ejercicios

# Para hacer el análisis más interesante y fácil de entender, usaremos el mismo conjunto de datos de antes, pero esta vez analizaremos height frente a age en lugar de weight. 
# Vas a crear un gráfico de dispersión que muestre la relación entre estas dos variables.
# Los datos de altura y peso del adulto se han leído en la variable df para ti en el precódigo. 
# Utiliza el argumento kind='scatter' para crear el gráfico de dispersión deseado. Da al gráfico los siguientes argumentos:

#   1. El título “Adult heights” ("Altura de adultos" en Espanol) (el uso de mayúsculas y minúsculas es importante).
#   2. Valor alfa de 0.36.
#   3. Tamaño de la gráfica de 8 por 6 pulgadas.
#   4. Eje X etiquetado “Age / years” (“Edad / anos“ en Espanol).
#   5. Eje Y etiquetado “Height / inches” ("Altura / pulgadas" en Espanol).

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df.plot(x='age',
        y='height',
        kind='scatter',
        title='Adult heights',
        xlabel='Age / years',
        ylabel='Height / inches',
        figsize=[8, 6],
        alpha=0.36)
        # escribe tu código aquí

plt.show()

# FIN-