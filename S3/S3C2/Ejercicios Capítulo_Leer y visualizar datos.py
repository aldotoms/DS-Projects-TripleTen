# Capítulo 2/6
# Leer y visualizar datos

# Ejercicio 1
# El conjunto de datos está disponible en /datasets/letters_colors_decimals.csv. 
# Los valores en dicho dataset están separados por $, y a se utiliza como punto decimal. 

# Léelo de tal manera que:
# - La primera fila se convierta en el encabezado.
# - Las columnas estén separadas correctamente.
# - Los decimales se lean correctamente.
# Muestra el DataFrame.

# Código
import pandas as pd
df = pd.read_csv('/datasets/letters_colors_decimals.csv', sep='$', decimal='a') # escribe tu código aquí
print(df)

# Resultado
  letters  colors  decimals
0       a  yellow       1.2
1       b     red       1.3
2       c    cyan       1.4

# Fin.