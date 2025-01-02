# Capítulo 5/6
# Visualización de datos

# Correlación
# A menudo, el principal objeto del análisis de datos es mostrar la relación entre dos variables. 
# Por ejemplo, podemos querer determinar cómo se relaciona el precio de un apartamento con su tamaño. 
# ¿Afecta a su valor la distancia desde el centro? ¿Qué impacto tiene el año de construcción o el nivel de ruido que tiene el barrio? 
# Los gráficos de dispersión nos ayudan a responder estas preguntas, ya que nos proporcionan una representación visual de estas relaciones.
# A la tendencia de una variable a cambiar en relación con el cambio en otra variable se le llama correlación.
# Los gráficos de dispersión que hicimos en la última lección muestran que la altura y el peso se correlacionan positivamente. 
# Esto tiene sentido porque un aumento en uno generalmente significa un aumento en el otro. 
# Un ejemplo de correlación negativa sería la altura y el tono de voz; generalmente, cuanto más alta sea una persona, menor será la frecuencia de su voz.

# Coeficiente de correlación
# Una cosa es mirar el gráfico, pero también necesitamos una forma numérica para describir la correlación.
# Para cuantificar cómo una variable tiende a cambiar cuando la otra variable cambia, utilizamos el coeficiente de correlación de Pearson, conocida comúnmente como el coeficiente de correlación. 
# Este coeficiente puede tomar cualquier valor entre -1 y 1.
# Un valor de -1 representa una correlación lineal negativa perfecta, mientras que un valor de 1 representa una correlación lineal positiva perfecta. 
# En general, el coeficiente de correlación funciona de este modo:

#   - Si uno de los valores incrementa junto con el otro, el coeficiente de correlación es positivo.
#   - Si uno permanece igual mientras el otro cambia, el coeficiente es 0.
#   - Si uno se reduce mientras el otro incrementa, el coeficiente es negativo.

# Cuanto más cerca esté el coeficiente de -1 o 1, más fuerte será la correlación. 
# Por otro lado, un valor de 0 puede significar que no hay correlación o que hay una conexión no lineal compleja que el coeficiente no puede reflejar.
# Para ayudarte a entender la relación entre el coeficiente de correlación y la distribución de puntos en un gráfico de dispersión, hemos incluido una gráfica interactiva. 
# Puedes cambiar el coeficiente de relación y observar cómo cambia la dispersión de los puntos de datos.
# Observa que hay diferentes gráficos de dispersión que podrían dar como resultado el mismo coeficiente de correlación; este solo es un ejemplo.

# Calcular el coeficiente de correlación
# En pandas, puedes calcular el coeficiente de correlación de Pearson usando el método corr(). 
# Para hacerlo, aplícalo a la columna con la primera variable, y pasa la columna con la segunda variable como un parámetro. 
# No importa el orden de las variables. Por ejemplo:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/datasets/height_weight.csv')

print(df['height'].corr(df['weight']))

# Resultado: 0.9165261045538688

# Con un coeficiente de alrededor de 0.9, la altura y el peso tienen una fuerte correlación positiva en este conjunto de datos. 
# Esto coincide con nuestro "sentido común" de que las personas más altas tienden a pesar más. 
# Por supuesto, hay variación en esta tendencia, por lo que no esperaríamos un coeficiente de correlación positivo perfecto de 1.
# Puede ser tentador hacer una declaración como "la altura de una persona determina su peso". 
# Sin embargo, por sí sola, la correlación no puede decirnos nada sobre causa y efecto; solo sabemos que los dos factores están correlacionados. 
# Para probar (o refutar) la causa y efecto, necesitaríamos realizar experimentos controlados. Recuerda, correlación no implica causalidad.
# Por ahora, vamos a practicar el cálculo de coeficientes de correlación para otros pares de variables en nuestro conjunto de datos.


## *Ejercicios

# Ejercicio 1
# ¿Recuerdas el gráfico de dispersión que hiciste en la última lección para las columnas 'height' y 'age'? 
# Ahora vas a calcular el coeficiente de correlación de Pearson para aquellas columnas y asigna el resultado a una variable llamada ah_corr. 
# Después muéstralo. ¿El resultado se alinea con el gráfico de dispersión?

import pandas as pd

df = pd.read_csv('Datasets/height_weight.csv')

ah_corr = df['height'].corr(df['age']) # escribe tu código aquí

print(ah_corr)

# Resultado: 0.010042046516844344

# Ejercicio 2
# Intenta llamar al método corr() en todo el DataFrame. Para ello, sigue el mismo proceso que antes, pero no pases ninguna variable al DataFrame df o al método corr(). 
# ¿Qué pasa? Imprime el resultado.

import pandas as pd

df = pd.read_csv('Datasets/height_weight.csv')

print(df.corr()) # escribe tu código aquí

# FIN.