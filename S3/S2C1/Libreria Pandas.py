# Capítulo 1/6
# La librería Pandas

# Importación y uso de paquetes
# Ahora que conoces los conceptos básicos de la librería pandas, intentemos trabajar con ella.
# Al final de esta lección, podrás importar pandas en Python y crear tu primer DataFrame.

# Teoaría
# Importación de la librería
# El primer paso para aprovechar todas las ventajas de pandas, es importar la librería:

import pandas

# Una vez que hayas importado la librería, puedes llamar a sus métodos y funciones integradas. 
# Por lo general, pandas se importa con el alias pd, lo que facilita su referencia más adelante en el código. 
# De hecho, puedes utilizar cualquier alias que quieras, pero este es el alias más común para pandas, 
# sí que te sugerimos que te ciñas a él y que uses esta notación más adelante en tu trabajo. 
# De este modo:

import pandas as pd

# Creación de un DataFrame
# Para utilizar pandas, debes convertir tus datos a un DataFrame. Para ello puedes utilizar la clase DataFrame().
# Una clase es como una plantilla para crear objetos, y hay muchas clases en pandas. La clase DataFrame() es la que más se utiliza.
# La clase DataFrame() toma dos argumentos: data y columns.
# - data espera una lista que contenga los datos.
# - columns espera una lista de nombres de columnas que correspondan a la lista de datos.

# Imagina que tienes un conjunto de datos simple: una lista anidada que contiene los nombres de los países 
# y sus capitales. Así que tenemos una variable llamada atlas, que almacena esta información:

atlas = [  
        ['France', 'Paris'],  
        ['Russia', 'Moscow'],  
        ['China', 'Beijing'],  
        ['Mexico', 'Mexico City'],  
        ['Egypt', 'Cairo']  
]

#  Podemos utilizarla como valor para el argumento data.

pd.DataFrame(data = atlas, columns = )

# Como puedes ver, todavía debemos darle un valor al argumento columns. 
# Vamos a crear una lista que contenga los nombres de columnas 'country' y 'capital':

geografy = ['country', 'capital']

# Ahora tenemos dos argumentos y podemos convertir nuestra lista anidada en un DataFrame y almacenarlo en la variable world_map:

world_map = pd.DataFrame(data=atlas, columns=geografy)

# Como DataFrame() es una clase dentro de la librería pandas, va precedida de pd cuando la llamamos.
# El código completo se verá así:

import pandas as pd

# preparamos los datos y los nombres de las columnas
atlas = [
      ['France', 'Paris'],  
        ['Russia', 'Moscow'],  
        ['China', 'Beijing'],  
        ['Mexico', 'Mexico City'],  
        ['Egypt', 'Cairo'],
]

geografy = ['country', 'capital']

# creamos un DataFrame
world_map = pd.DataFrame(data=atlas , columns=geografy)

# mostrando el DataFrame

print(world_map)

# Hemos convertido los datos brutos de una lista anidada en un DataFrame con columnas con nombre.
# ¡Ahora te toca a ti!

# Fin.