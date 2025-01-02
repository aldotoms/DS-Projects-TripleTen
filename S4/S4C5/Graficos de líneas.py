# Capítulo 5/6
# Visualización de datos

## *Gráficos de líneas

# ¿Recuerdas cuando usamos el método plot() sin especificar un argumento para el parámetro kind=? 
# Eso nos dio un gráfico de líneas donde cada punto de datos está conectado de forma secuencial por una línea.
# Se veía más o menos así:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

df.sort_values('height').plot(x='height', y='weight')
plt.show()

# Sin embargo, un gráfico de líneas no es apropiado para estos datos porque estos gráficos implican una relación entre puntos de datos consecutivos.
# En cambio, los gráficos de líneas son excelentes cuando tienes datos que se conectan cronológicamente y cada punto de tiempo de los datos tiene alguna dependencia con el punto anterior. 
# Cosas como datos de temperatura, datos de tráfico y datos del mercado de valores son buenos candidatos para los gráficos de líneas.
# En esta lección, vamos a trabajar con datos del mercado de valores de Starbucks (SBUX) desde 2015 hasta 2019. 
# Obtuvimos este conjunto de datos de Yahoo Finanzas y lo modificamos para que contuviera solo un subconjuto de las columnas disponibles.
# Vamos a echar un vistazo a los datos:

import pandas as pd

df = pd.read_csv('Datasets/sbux.csv')

print(df.head())
print()
df.info()

# Hay cuatro columnas en el conjunto de datos:
#   - 'date': fecha en la que se registraron los datos.
#   - 'open': precio de una acción en USD en la apertura del mercado, es decir, el primer precio del día.
#   - 'close': precio de una acción en USD al cierre del mercado, es decir, el último precio del día.
#   - 'volume': número total de acciones cotizadas.

# Por ejemplo, la primera fila nos dice que el 2 de enero de 2015, el precio de apertura de las acciones de Starbucks fue de $41.06, 
# el precio de cierre fue de $40.72 y ese día se negociaron 6 866 000 acciones. 
# Cada fila representa un día de negociación cuando el mercado estaba abierto, lo que excluye los fines de semana y ciertos días festivos.
# Del resultado de info(), también vemos que 'date' tiene un tipo de datos string, las otras columnas son numéricas y no faltan valores. 
# Para nuestros propósitos, está bien representar las fechas como strings, pero más adelante en el sprint, 
# aprenderás sobre tipos de datos especiales para fechas y horarios que te facilitarán extraer información y realizar cálculos con ellos.
# Para datos temporales como este, es razonable suponer que el precio de un día tiene alguna relación con el precio del día anterior. 
# Así que avancemos y hagamos un gráfico de líneas para visualizar el precio de apertura de las acciones de Starbucks durante el ciclo de vida del conjunto de datos:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/sbux.csv')

df.plot(x='date', y='open')
plt.show()

# Todo lo que teníamos que hacer para trazar un gráfico de líneas era llamar a plot() en nuestro DataFrame sin un argumento kind= y 
# especificar qué columnas queremos trazar en los ejes X y Y, tal como ya lo hemos hecho con nuestros otros gráficos. 
# No tienes que especificar el argumento kind= como "line", puesto que ya es un valor predeterminado.
# Ahora tenemos una gran representación del precio de apertura histórico de las acciones de Starbucks. 
# Parece que el precio se dispara bastante rápido más adelante en el gráfico. ¿Alrededor de qué fecha ocurrió eso? 
# Es difícil saberlo a partir de este gráfico porque las etiquetas de marca del eje X se superponen entre sí.
# Además, para corregir la superposición de etiquetas de marca, ¿qué otras mejoras podríamos hacerle a este gráfico?


# Pregunta
# ¿Qué más harías para que la gráfica anterior sea más profesional y comunicativa? Selecciona todas las opciones que correspondan:
#   - Incluye una etiqueta del eje Y. (Sin él, no podríamos entender fácilmente de lo que estamos hablando.)
#   - Incluye un título de gráfico parecido a “Starbucks market open” ("Apertura del mercado de Starbucks" en Espanol). (Un título hace todo mejor y más fácil de entender.)
#   - Elimina la leyenda. (No deberíamos agregar cosas simplemente por tenerlas. En este caso, las leyendas no sirven.)
#   - Especifica las unidades del eje Y como "USD" (dólares de los Estados Unidos). (De esta manera nos aseguramos que todos sepan qué estamos mostrando.)

# Ahora, vamos a usar nuestras habilidades para mejorar esta gráfica como corresponde.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/sbux.csv')

df.plot(x='date',
        y='open',
        legend=False,
        title='Starbucks market open',
        xlabel='Date',
        ylabel='Share price / USD',
        rot=45)

plt.show()

# A estas alturas, todos los parámetros que usamos para este gráfico te deben resultar familiares, a excepción del último: rot=. 
# Este argumento rota las etiquetas de marca del eje X tantos grados como lo establezcas. 
# Lo usamos para que nuestras etiquetas de marca no se superpongan unas a otras, y ahora se presentan en ángulos de 45º del eje X.
# ¡Ahora es tu turno de crear algunos gráficos de líneas profesionales!

# FIN-