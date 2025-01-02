# Capítulo 5/6
# Visualización de datos

## *Matrices de dispersión

# Crear matrices de dispersión
# En la lección anterior, encontramos una fuerte correlación entre la altura y el peso, pero en la vida real, las cosas rara vez son tan simples. 
# Si nos interesa explorar los factores que contribuyen al peso de las personas, hay mucho más que considerar además de la altura. 
# Por ejemplo, también podríamos querer saber cómo la edad y el sexo se correlacionan con el peso, o cómo se correlacionan entre sí.
# Desafortunadamente, es imposible trazar los cuatro parámetros en el mismo gráfico de forma coherente. 
# Sin embargo, podemos crear gráficos de dispersión para cada posible par de parámetros: altura y peso, altura y edad, peso y sexo, etcétera. 
# Este conjunto de gráficos por pares se denomina matriz de dispersión.

# En pandas, podemos construir matrices de dispersión usando la función plotting.scatter_matrix(): 

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Datasets/height_weight.csv')

pd.plotting.scatter_matrix(df, figsize=(9, 9))
plt.show()

# Cada celda de esta cuadrícula de 4x4 muestra la relación entre un par de columnas. Vamos a descomponerla. 
# Mostraremos cada gráfico debajo de la explicación, y puedes encontrarla nuevamente en la matriz, para que tú la ubiques.

#   - Las celdas diagonales no muestran las relaciones entre variables. 
#     En su lugar, existen los histogramas que muestran la distribución de valores para cada variable individual. 
#     Por ejemplo, examina la primera imagen en la parte superior. Ahí podemos ver que los adultos suelen medir entre 64 y 68 pulgadas de altura. 
#     En el último capítulo estudiaremos los histogramas con más detalle.

df = pd.read_csv('Datasets/height_weight.csv')

df.plot(x='weight', y='height', kind='hist', alpha=0.5)
plt.show()

df.plot(x='height', y='weight', kind='hist', alpha=0.5)
plt.show()

df.plot(x='weight', y='age', kind='hist', alpha=0.5)
plt.show()

df.plot(x='age', y='male', kind='hist', alpha=0.5)
plt.show()

#   - Las celdas que están justo debajo y al lado del histograma de altura muestran la conexión entre altura y peso. 
#     Ambos gráficos de dispersión de altura-peso contienen información idéntica, pero los ejes simplemente están invertidos. 
#     Vimos este gráfico de dispersión en la última lección, y determinamos que es indicativo de una fuerte correlación positiva (un coeficiente de correlación de aproximadamente 0.9).

df = pd.read_csv('Datasets/height_weight.csv')

df.plot(x='weight', y='height', kind='scatter', alpha=0.5)
plt.show()

df.plot(x='height', y='weight', kind='scatter', alpha=0.5)
plt.show()

#   - Los gráficos de dispersión para la relación edad-altura muestran una amplia dispersión de puntos sin una relación claramente discernible, 
#     como pudiste observar cuando creaste este gráfico de dispersión y calculaste el coeficiente de relación (alrededor 0.01) en las lecciones anteriores.

df = pd.read_csv('Datasets/height_weight.csv')

df.plot(x='height', y='age', kind='scatter', alpha=0.5)
plt.show()

df.plot(x='age', y='height', kind='scatter', alpha=0.5)
plt.show()

#   - Los gráficos de dispersión edad-peso también tienen una amplia dispersión de pesos para cada edad, 
#     pero parece que puede haber una tendencia ligeramente positiva para los gráficos de dispersión edad-altura.

df = pd.read_csv('Datasets/height_weight.csv')

df.plot(x='weight', y='age', kind='scatter', alpha=0.5)
plt.show()

df.plot(x='age', y='weight', kind='scatter', alpha=0.5)
plt.show()

# La última fila (y la última columna) de los gráficos de dispersión muestra la relación entre el género y las otras variables, 
# en donde un valor de 1 significa que la persona es del género masculino y 0, del femenino. 
# Estas gráficas muestran una correlación positiva en las relaciones género-altura y género-peso, pero no en género-edad.

# Con una sola línea de código creamos una matriz de dispersión que nos permitió hacer muchas deducciones sobre las relaciones entre las variables en nuestro conjunto de datos. 
# ¿No crees que sería genial si pudiéramos cuantificar todas estas relaciones también?


## *Matrices de correlación
# En un ejercicio de la última lección, llamaste al método corr() en nuestro DataFrame y obtuviste este resultado:

import pandas as pd

df = pd.read_csv('Datasets/height_weight.csv')

print(df.corr())

# La tabla devuelta se denomina matriz de correlación. Esta matriz contiene los coeficientes de correlación para cada par de columnas numéricas en el DataFrame.
# Los coeficientes en la diagonal de la parte superior-izquierda a la inferior-derecha siempre son igual a 1, ya que cualquier variable se correlaciona perfectamente consigo misma. 
# Los elementos diagonales arriba (y debajo) de la diagonal principal contienen los coeficientes para cada par de columnas. 
# En este caso, hay 6 coeficientes de correlación únicos para los posibles pares de las variables comparadas.

# Construir una matriz de correlación es una forma mucho más rápida de obtener todos los coeficientes de correlación que llamar individualmente a corr() para cada par de columnas. 
# En este caso, solo hay 6 pares, ¡pero imagina si tuviéramos docenas de columnas numéricas!


## Ejercicio:

# Obtén los coeficientes de correlación para la columna 'male' con cada una de las otras tres columnas. 
# Pero en lugar de llamar corr() en la columna 'male' tres veces por separado, crea una matriz de correlación y extrae los tres coeficientes que deseas. 
# El resultado debería ser un objeto Series con tres elementos, uno para cada coeficiente.
# Asigna la matriz de correlación a una variable llamada corr_mat y asigna el Series de coeficientes a una variable llamada male_corr. Luego, muestra male_corr.
# Usa loc[] con 'male' como el primer argumento, y una lista de los otros datos como el segundo argumento para extraer aquellos valores para la variable male_corr.

import pandas as pd

df = pd.read_csv('Datasets/height_weight.csv')

corr_mat = df.corr() # escribe tu código aquí
male_corr = corr_mat.loc['male', 'height':'age'] # escribe tu código aquí
print(male_corr)    

# FIN.