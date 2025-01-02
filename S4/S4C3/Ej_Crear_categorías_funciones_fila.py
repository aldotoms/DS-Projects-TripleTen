# Crear categorías con funciones de fila
# 2 ejercicios

# Escribe una función que se llame avg_score_group() (grupo puntuación promedio) que tenga un parámetro llamado row. 
# El parámetro row debe ser un objeto tipo Series de pandas. La función debe calcular la calificación promedio de cada juego, 
# luego devolver una cadena que coloque cada uno en una de estas categorías:
#   - valor 'low' para promedios menores de 60.
#   - valor 'medium' para promedios de 60 a 79.
#   - valor 'high' (alto) para puntuaciones mayores a 80.
# Para calcular la puntuación promedio, avg_score_group() debe tomar los valores de row con los nombres de columna 'critic_score' y 'user_score'. La fórmula para calcularlo es avg_score = (critic_score + user_score * 10) / 2.
# Te dejamos las pruebas hechas, se debe imprimir low, medium y high, en ese orden.

import pandas as pd
df = pd.read_csv('Datasets/datasets/vg_sales.csv')
df.dropna(inplace=True)

def avg_score_group(row): # escribe tu función aquí
    critic_score = row['critic_score']
    user_score = row['user_score']

    avg_score = (critic_score + user_score*10) / 2

    if avg_score < 60:
        return 'low'
    elif avg_score < 79:
        return 'medium'
    elif avg_score > 80:
        return 'high'
    
# parte de prueba a continuación, por favor no la cambies

col_names = ['critic_score', 'user_score']
test_low  = pd.Series([10, 1.0], index=col_names)
test_med  = pd.Series([65, 6.5], index=col_names)
test_high = pd.Series([99, 9.9], index=col_names)

rows = [test_low, test_med, test_high]

for row in rows:
    print(avg_score_group(row))


## Ejercicio 2
# 2. Ahora es momento de poner a prueba tu nueva función. Crea tres filas personalizadas con estos nombres de variables y valores:
#   - row_1: puntuación de la crítica de 66 y puntuación de los usuarios de 3.6.
#   - row_2: puntuación de la crítica de 72 y puntuación de los usuarios de 8.1.
#   - row_3: puntuación de la crítica de 99 y puntuación de los usuarios de 9.4.
# Cada una de las variables de fila debe ser un objeto tipo Series con valores de índice 'critic_score' y 'user_score' para que avg_score_group() 
# pueda extraer los valores correctos.
# El precódigo define la función avg_score_group() del ejercicio anterior, aunque puede que se vea distinta a tu solución. 
# Tu tarea es imprimir el resultado de llamar a avg_score_group() con cada uno de los inputs especificados.

import pandas as pd

df = pd.read_csv('Datasets/datasets/vg_sales.csv')
df.dropna(inplace=True)

def avg_score_group(row):
    critic_score = row['critic_score']
    user_score = row['user_score']
    
    avg_score = (critic_score + user_score * 10) / 2
    
    if avg_score < 60:
        return 'low'
    if avg_score < 80:
        return 'medium'
    if avg_score >= 80:
        return 'high'


# crea las filas de input de prueba aquí
row_1 = pd.Series([66, 3.6], index=['critic_score', 'user_score'])
row_2 = pd.Series([72, 8.1], index=['critic_score', 'user_score'])
row_3 = pd.Series([99, 9.4], index=['critic_score', 'user_score'])
    
# imprime los resultados de llamar a la función con los input de prueba en orden
print(avg_score_group(row_1))
print(avg_score_group(row_2))
print(avg_score_group(row_3))

# Fin.