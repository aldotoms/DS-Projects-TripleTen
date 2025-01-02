# Capítulo 1/6 · Última lección
# La librería Pandas

# Examen del capítulo

# Has aprendido mucho en estas lecciones. 
# Antes de que continúes tu viaje de aprendizaje, recapitulemos lo que dominas hasta ahora.
# Ahora puedes importar Pandas, crear DataFrames y comprobar sus atributos dtypes, columns y shape de forma directa o con el método info():

import pandas as pd

# preparando los datos y los nombres de las columnas
atlas = [
      ['France', 'Paris'],
        ['Russia', 'Moscow'],
        ['China', 'Beijing'],
        ['México', 'Ciudad de México'],  
        ['Egypt', 'Cairo'],
]
geography = ['country', 'capital']

# creando un DataFrame
world_map = pd.DataFrame(data=atlas , columns=geography)

print(world_map.dtypes) #imprimimos el atributo dtypes
print(world_map.columns) #imprimimos el atributo columns 
print(world_map.shape) #imprimimos el atributo shape 
print(world_map.info()) #imprimimos todos los atributos a la vez

# Además, puedes crear DataFrames a partir de listas y archivos CSV y Excel, así como utilizar los métodos head() y tail():

df = pd.read_csv('/datasets/music_log_chpt_11.csv') # lee un archivo CSV
print(df.head()) # imprime las 5 primeras líneas del DataFrame

df2 = pd.read_excel('/datasets/music_log.xlsx') # read an Excel file
print(df2.tail()) # imprime las 5 últimas líneas del DataFrame

# Puedes indexar tu DataFrame utilizando tanto una notación completa como una abreviada, 
# así como aplicarle expresiones lógicas y métodos como count(), sum() y mean():

# encuentra la media utilizando la notación completa y la expresión ==
mean_duration = df[df.loc[:, 'genre'] == 'pop']['total play'].mean()

#  encuentra el recuento utilizando la notación abreviada y la expresión <=
count_duration = df[df['total play'] <= 130]['total play'].count()

# encuentra la media utilizando la notación abreviada y la expresión ==
sum_duration = df[df['genre'] == 'pop']['total play'].sum()

# Ahora que se terminó la recapitulación, ¡vayamos a los cuestionarios!
# Fin.