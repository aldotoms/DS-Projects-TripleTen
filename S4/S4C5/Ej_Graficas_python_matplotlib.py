# Sprint 4
# Manipulación de datos (Data Wrangling) (continuación)

# *Crear gráficas en Python con matplotlib

## Ejercicio

# Hemos importado pandas y las librerías pyplot de Matplotlib en el precódigo proporcionado, y creamos un DataFrame llamado df. 
# Tu tarea es crear un gráfico con forma de estrellas rosas utilizando los datos en df. Para tu comodidad, todos los atributos necesarios se enumeran a continuación. 
# Sigue las instrucciones para lograr el resultado deseado. Si lo necesitas, consulta la sección de repaso para recordar los nombres de los parámetros.
#  Usando el método plot() de pandas, crea un trazo de columna 'a' frente a la columna 'c' del df que tenga los siguientes argumentos:

# 1. El título "A vs C" (el uso de mayúsculas y minúsculas es importante, así que puedes copiarlo y pegarlo).
# 2. Un estilo de marcador de estrella (puedes usar un asterisco '*' para lograrlo).
# 3. Marcadores de color rosa fuerte (utiliza el nuevo y obvio parámetro color= para hacerlo, con el argumento 'hotpink')
# 4. Tamaño de la gráfica de 5 por 5 pulgadas.
# 5. Rango del eje X de 0 a 12.
# 6. Rango del eje Y de 1 a 6.
# 7. Eje X con la leyenda "C".
# 8. Eje Y con la leyenda "A".

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25], 'c':[1, 3, 6, 10]})

df.plot(title='A vs C',
        x='c', 
        y='a', 
        style='*', 
        color='hotpink', 
        xlim=[0, 12], 
        ylim=[1, 6], 
        figsize=[5, 5], 
        xlabel='C', 
        ylabel='A') 

plt.show()
