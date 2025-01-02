# Capítulo 2/5
# Estadística descriptiva

# Medidas de posición y de variabilidad
# Medidas de posición

# En el sprint anterior, te familiarizaste con las medianas y las medias, que son valores utilizados para describir datos numéricos. 
# Estos valores también son llamados medidas de posición. Las medianas y las medias te permiten encontrar un valor aproximado que caracteriza o representa un dataset determinado.
# Tanto las medianas como las medias tienen sus propias ventajas. Para calcular una media, necesitas todos los valores del dataset. 
# Esto se debe a que cuando calculamos una media, sumamos todos los valores y dividimos la suma obtenida por el número total de valores. 
# A veces, la media también se denomina medida algebraica de posición. La mediana representa los valores situados en el centro de una distribución. 
# Vamos a repasar brevemente qué es la mediana:

import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data.mean()

# La mediana es una medida de posición estructural. Podrías cambiar casi todos los valores en el dataset y, aún así, la mediana permanecería igual. 
# A modo de ejemplo, sigamos trabajando con el dataset del cuestionario anterior y calculemos la media y la mediana usando Python.

print('La media es igual a', data.mean())
print('La mediana es igual a', data.median())

# Ahora veamos cómo se ven afectadas la media y la mediana cuando modificamos los datos. 
# Primero, divide todos los valores estrictamente menores de 5 entre 10 y luego multiplica todos los valores estrictamente mayores de 5 por 10 (el número 5 en sí debe dejarse sin cambios). 
# Encuentra la nueva mediana y la media del dataset actualizado.

data_new = pd.Series([0, 0.1, 0.2, 0.3, 0.4, 5, 60, 70, 80, 90, 100])
print('La media es igual a', data_new.mean())
print('La mediana es igual a', data_new.median())

# La media ha cambiado, pero la mediana sigue siendo la misma. No es fácil hacer que la media permanezca igual, 
# ya que cualquier alteración en un número mayor que esa media requiere de un cambio compensatorio en un número menor que esta.
# Pero si tu dataset contiene valores atípicos, necesitarás la mediana, como bien aprendiste en el sprint de Manipulación de datos. 
# Sólo hay que tener en cuenta que la media de un dataset que contiene valores atípicos puede ser engañosa. Así, cuando Bill Gates entra en un bar, 
# todas las personas que están allí se hacen millonarias, por término medio.
# Imaginemos que tienes una start-up: un sitio web de financiación colectiva. Los bloggers lo usan para recaudar donaciones para su trabajo. 
# La mayoría de la gente que suele hacer donativos no dona más de un par de dólares, pero hay varios fans que les envían a sus ídolos un par de cientos de dólares.

# Pregunta
# ¿Qué medida funcionaría mejor con fines promocionales si quisiéramos convencer a los bloggers para que utilicen el servicio? 
# ¿Qué medida revela más sobre cuánto paga la mayoría de las personas?
# - R. La donación media (la media) es mejor para la promoción de un blogger, mientras que la mediana nos informa sobre cuánto paga la gente en general.
# Correcto. La donación media será notablemente superior a la mediana, y esto es bueno para fines promocionales. 
# En cambio, la mediana sirve mejor para mostrar cuánto paga la mayoría de las personas.

# Medidas de variabilidad
# Las medidas de posición por sí solas no son suficientes para comprender los datos. 
# También querrás saber cómo están dispersos (o distribuidos) los valores en torno a la media o la mediana.
# Para nuestra medida estructural de posición, que es la mediana, también tenemos una medida estructural de dispersión. Esta medida se denomina cuartil.
# Si la mediana representa el valor en el medio de una distribución, los cuartiles representan otras posiciones importantes. ¿Cuáles son?

# - El primer cuartil (también conocido como Q1) representa el valor del percentil 25 de la distribución de datos. 
#   El percentil 25 es el valor por debajo del cual se encuentran el 25% de los datos.
# - El segundo cuartil (Q2) representa el valor del percentil 50 de la distribución de datos, que es exactamente la mediana. 
#   Al igual que el percentil 25, el percentil 50 es el valor por debajo del cual se encuentran el 50% de los datos.
# - El tercer cuartil (Q3) representa el valor en el percentil 75 de la distribución de datos.

# Así es como se ve un sencillo ejemplo de distribución por edades:
# A menudo visualizamos los cuartiles en forma de diagrama de caja y bigotes. El ejemplo anterior tendrá el siguiente aspecto:

# Esto es lo que nos dice el diagrama de caja:
# - El valor mínimo es igual a 1 año. Se encuentra al final del bigote izquierdo.
#   - Primer cuartil: 2 años.
#   - Segundo cuartil: 3 años.
#   - Tercer cuartil: 5 años.
#   - El máximo es igual a 6 años. Se encuentra al final del bigote derecho.

# La distancia entre Q1 y Q3 se denomina intervalo intercuartílico (o IQR). Mide la dispersión de los datos situados en la mitad central. En otras palabras, es el intervalo del 50% medio de la muestra.

# Para construir un diagrama de caja en Python, a menudo recurrimos a la librería Seaborn, que proporciona capacidades de visualización similares a la librería Matplotlib utilizada anteriormente, 
# pero tienen funcionalidades ligeramente diferentes. Para empezar, necesitamos importar Seaborn,

import seaborn as sns

# y luego construimos un diagrama de caja y bigotes de la siguiente manera:

import pandas as pd

dataset = pd.Series([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6])
sns.boxplot(dataset)

# Observa que para construir este diagrama de caja, utilizamos los mismos datos que cuando vimos el diagrama por primera vez. 
# Como era de esperar, el gráfico resultante es idéntico al que te hemos mostrado anteriormente, la única diferencia radica en que nuestro gráfico está orientado verticalmente.
# Pero, ¿cómo medimos la dispersión alrededor de la medida algebraica de posición, es decir, alrededor de la media?
# El primer enfoque, y el más sencillo, consiste en encontrar la distancia promedio entre la media y todos los demás valores. ¡Calculémosla ahora!

# *Ejercicios*
# Ejercicio 1
# Tus objetivos actuales son:
#   1. Encontrar la media del dataset y almacenarla en la variable mean_value, utilizando un método apropiado.
#   2. Calcular la distancia entre cada valor y la media, y almacenar el valor resultante en la variable spacing_all. 
#      Para realizar este paso, puedes utilizar operaciones aritméticas sencillas con Series de pandas. 
#      Esto dará lugar a operaciones elemento por elemento, lo que significa que se realizará una operación en cada elemento de un Series, generando otro Series.
#   3. A continuación, calcula la distancia media y almacénala en la variable spacing_all_mean.
#   4. Imprime la variable spacing_all_mean.

import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value =  data.mean() # escribe tu código aquí: busca el valor medio en el dataset
spacing_all = data - mean_value # escribe tu código aquí: para cada elemento del dataset, encuentra su distancia a la media
spacing_all_mean =  spacing_all.mean() # escribe tu código aquí: calcula la distancia media

# escribe tu código aquí
print(mean_value)
print(spacing_all)
print(spacing_all_mean)

# FIN.