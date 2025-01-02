# Sprint 4
# Manipulación de datos (Data Wrangling) (continuación)

# Teoría
# Crear gráficas en Python con matplotlib

# Python tiene varias librerías populares para crear gráficos a partir de tus datos. Tal vez, la librería más común es Matplotlib. 
# Así que probablemente encontrarás muchas referencias a esta librería en la web cuando busques cómo solucionar problemas de trazado en Python.
# Más recientemente, se han creado otras librerías de trazado que son más "fáciles de usar", utilizando Matplotlib como base. 
# En particular, Seaborn y Plotly son opciones comunes. Plotly incluso tiene una librería más novedosa llamada Plotly Express, 
# la cual es muy amigable con el usuario y suele producir gráficos atractivos desde el principio.
# Sin embargo, para muchos tipos de gráficos simples ¡no necesitamos para nada una librería de gráficos externa! 
# Los buenos y confiables pandas tienen sus propios métodos para hacer gráficos a partir de objetos Series y DataFrames. 
# En esta lección, aprenderás cómo hacer diagramas usando pandas y cómo mostrarlos usando Matplotlib.

## *El método plot() y plt.show()

# Comencemos aprendiendo sobre el método plot() de pandas y el método show() de la biblioteca pyplot de Matplotlib. 
# Aquí hay un ejemplo de cómo podemos llamar plot() para crear una gráfica en pandas y después usar show() para mostrar claramente una gráfica.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})
print(df)

df.plot()
plt.show()

# Para dibujar esta gráfica, hemos importado tanto pandas como pyplot desde las librerías matplotlib. Una convención popular es usar plt como el alias para la librería pyplot. 
# El método plot() de pandas prepara la imagen con los datos, mientras que la función show() de pyplot presenta la imagen al usuario.
# Por defecto, el método plot() crea una gráfica en donde todas las columnas numéricas en el DataFrame se trazan en los mismos ejes. 
# Los índices están en el eje X y los valores de las columnas están en el eje Y.
# Si es necesario, también puedes trazar solamente una columna individual.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df['b'].plot()
plt.show()

# En algunos entornos de desarrollo, como Jupyter notebooks, no necesitas usar plt.show() para mostrar tu gráfica. 
# Pero es una buena práctica incluir siempre plt.show() para que tus gráficas se muestren en cualquier entorno en el que otra persona pueda ejecutar tu código.
# Otra opción que podrías necesitar es escribir código que almacena nuestras gráficas como archivos de imagen. 
# Por ejemplo, podemos almacenar la gráfica anterior en formato PNG usando la función savefig() de matplotlib:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df['b'].plot()
plt.savefig('myplot.png')

# Si ejecutas este código en tu máquina local, debes tener un archivo PNG llamado myplot.png en cualquier directorio en el que se encuentre tu script de Python o Jupyter notebook. 
# Python sabe en qué formato guardar el archivo según la extensión en tu entrada de string para savefig().


## Personalización de gráficas con parámetros plot()
# Tal vez notaste que los gráficos que hemos hecho hasta ahora son bastante básicos y no cumplen con las buenas prácticas que aprendiste anteriormente en este capítulo. Bueno, plot() tiene muchos parámetros adicionales que podemos usar para arreglar esto.

# Títulos. Los títulos de los gráficos se pasan al parámetro title= como strings:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B')
plt.show()

# ¡Ahora tenemos un buen título para complementar nuestro gráfico! Aunque nos gustaría elegir algo más descriptivo que "A y B" si se tratara de datos reales, claro.


## *Estilos de línea
# Nuestra gráfica no es tan mala, pero un gráfico de líneas podría no ser lo mejor aquí, ya que implica que tenemos puntos de datos a lo largo de toda la línea cuando, de hecho, sólo tenemos cuatro. 
# Para que le resulte obvio a cualquiera que mire el gráfico, sería mejor usar un estilo de marcado distinto para los puntos de datos.
# Para cambiar el estilo de marcador del gráfico, puedes usar el parámetro style=. Vamos a pasarle un argumento de 'o' para que cada valor se marque como un punto.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B', style='o')
plt.show()

# También hay otros estilos de marcador; por ejemplo, style='х' marca cada punto con una x:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B', style='x')
plt.show()

# Incluso se pueden combinar diferentes estilos. Por ejemplo, cuando queremos mostrar tanto líneas como puntos, podemos usar style='o-':

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(title='A y B', style='o-')
plt.show()

# Existen muchas otras opciones de estilo de marcador (materiales en inglés), ¡así que siéntete libre de jugar con ellas y explorarlas!

df.plot(title='A y B', style="o-")
plt.show()


## *Ejes

# En todos los gráficos que has visto hasta ahora, el eje horizontal contiene los valores del índice DataFrame. 
# Pero, ¿qué sucede si deseas trazar dos columnas una frente a la otra? Podemos usar los parámetros x= y y= para lograr esto:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b', y='a', title='A vs B', style='o')
plt.show()

# Aquí, la columna 'a' está en el eje Y y la columna 'b' está en el eje X. 
# Observa que pandas ha cambiado automáticamente el nombre del eje horizontal 'b' y la leyenda predeterminada ahora se refiere solo a la columna 'a'. 
# Para cambiar las etiquetas de los ejes, podemos usar los parámetros xlabel= y ylabel= del método plot():

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b',
        y='a',
        title='A vs B',
        style='o',
        xlabel="Hola, soy B",
        ylabel="Hola, soy A")

plt.show()

# Es importante mencionar que hay una forma alternativa de configurar las etiquetas, para ambos ejes X y Y. 
# En lugar de especificar xlabel= y ylabel= en el método plot(), podemos configurar las etiquetas a través de plt.xlabel() y plt.ylabel(). Así es como se hace:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b',
        y='a',
        title='A vs B',
        style='o',
        legend=False)

plt.xlabel("Hola, soy B") # configurando la leyenda x
plt.ylabel("Hola, so A") # configurando la leyenda y
plt.show()

# A continuación, también podemos establecer los límites de los ejes usando los parámetros xlim= y ylim=. 
# Estos toman un número o una lista de dos números como sus argumentos. Si pasas un solo número, será el valor mínimo mostrado para el eje correspondiente. 
# Si pasas una lista de dos números, el primer número será el valor mínimo y el segundo número será el máximo.
# Ampliemos el rango del eje horizontal de 0 a 30, y establezcamos el valor mínimo del eje vertical en 0:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b', y='a', title='A vs B', style='o', xlim=[0, 30], ylim=0)
plt.show()


## *Otras opciones de personalización

# Puedes agregar otras características a tus gráficos si crees que los harán más fáciles de leer. 
# Agreguemos líneas de cuadrícula para ayudar a que el ojo capte qué valores estamos trazando. 
# Para hacerlo, establece el parámetro grid= en True (de manera predeterminada, este parámetro está establecido en False):

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

df.plot(x='b', y='a', title='A vs B', style='o', grid=True)
plt.show()

# También podemos gestionar el tamaño de nuestra gráfica con el parámetro figsize= (tamaño de la gráfica). 
# El ancho y el alto en pulgadas se pasan como una lista: figsize=[width, height]. Comparemos dos gráficas de diferentes tamaños:

import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25]})

# construir una gráfica pequeña
df.plot(x='b', y='a', style='o', xlim=[0, 30], figsize=[2, 2])

# construir una gráfica grande
df.plot(x='b', y='a', style='o', xlim=[0, 30], figsize=[10, 4])

plt.show()


## *Repaso

# Aquí tienes un resumen de todos los métodos y funciones que hemos mencionado en esta lección:

#   - plot(): método de pandas que prepara la imagen con los datos.
#   - show(): función de la librería pyplot de Matplotlib que presenta la imagen al usuario.
#   - savefig(): función de Matplotlib que almacena la gráfica como un archivo de imagen.
#   - title=: parámetro para establecer el título del gráfico.
#   - style=: parámetro para cambiar el estilo de marcador del gráfico.
#   - x= y y=: parámetros para trazar dos columnas, una frente a la otra.
#   - xlabel= y ylabel=: parámetros para establecer las etiquetas de los ejes.
#   - xlim= y ylim=: parámetros para establecer los límites de los ejes.
#   - grid=: parámetro para agregar líneas de cuadrícula.
#   - figsize=: parámetro para agregar el tamaño de la gráfica.
#   - legend=: parámetro para agregar o eliminar la leyenda.

# FIN.