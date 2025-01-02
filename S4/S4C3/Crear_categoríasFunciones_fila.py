## *Crear categorías con funciones de fila

# Has podido realizar un análisis simplificado sobre la correlación entre la puntuación de la crítica de un juego y su éxito comercial utilizando una función creada por ti mismo y el método apply(). 
# Tu función personalizada tomó un solo argumento, así que nada más tuviste que llamar a apply() en la columna que contenía los valores que querías usar como input.
# Pero, ¿qué pasa si queremos crear categorías con base en los valores de más de una columna? 
# En ese caso, podemos escribir una función que toma una fila entera como input y extrae los valores que necesitamos para crear categorías nuevas.
# Demostraremos esto con el conjunto de datos de los videojuegos. Esta vez vamos a simplificar las cosas y primero nos vamos a deshacer de todas las filas que no tengan valores:

import pandas as pd
df = pd.read_csv('Datasets/datasets/vg_sales.csv')

df.dropna(inplace=True)
df.info()

# Hemos descartado muchas filas, pero ahora no tenemos que preocuparnos por que falten valores. 
# Además, siempre podemos agregarlas de nuevo después del análisis preliminar para ver cómo eso afecta nuestros resultados.
# Ahora, vamos a escribir una función llamada era_sales_group() que coloque los juegos en las siguientes categorías según el año de lanzamiento y las ventas totales:
#   - Los que se lanzaron antes del 2000 y que tienen menos de $1 millón en ventas irán a la categoría 'retro'.
#   - Los que se lanzaron entre el 2000 y el 2009 (inclusive) con menos de $1 millón de ventas irán a la categoría 'modern'.
#   - Los que se lanzaron antes del 2010 y que tienen $1 millón o más en ventas irán a la categoría 'classic'.
#   - Los que se lanzaron a partir del 2010 y que tienen menos de $1 millón en ventas irán a la categoría 'recent'.
#   - Los que se lanzaron a partir del 2010 y que tienen $1 millón o más en ventas irán a la categoría 'big hit'.
# Así es como se verá la función junto con el output de muestra:

def era_sales_group(row):
    """
    La función devuelve una categoría de juegos según el año de lanzamiento y las ventas totales mediante las siguientes reglas:
    —'retro'   para año < 2000 y las ventas totales < $1 million
    —'modern'  para 2000 <= año < 2010 y las ventas totales < $1 million
    —'recent'  para año >= 2010 y las ventas totales < $1 million
    —'classic' para año < 2010 y las ventas totales >= $1 million
    —'big hit' para año >= 2010 y las ventas totales >= $1 million
    """

    year = row['year_of_release']
    na_sales = row['na_sales']
    eu_sales = row['eu_sales']
    jp_sales = row['jp_sales']
    
    total_sales = na_sales + eu_sales + jp_sales
    
    if year < 2000:
        if total_sales < 1:
            return 'retro'
        else:
            return 'classic'
    if year < 2010:
        if total_sales < 1:
            return 'modern'
        else:
            return 'classic'
    if year >= 2010:
        if total_sales < 1:
            return 'recent'
        else:
            return 'big hit'

row = df.iloc[0]    # usa la primera fila como input de ejemplo

print(row)
print()
print('Este juego es', era_sales_group(row))

# Al igual que la función era_group() de la lección pasada, era_sales_group() tiene un parámetro: row. 
# Sin embargo, en este caso se espera que row sea una sola fila entera del DataFrame.
# Esta función requiere cuatro valores de la fila para hacer la categorización: uno para el año de lanzamiento y tres para calcular las ventas totales. 
# Observa que la función usa nombres de columnas de df para extraer estos valores, así que no funcionará en otro DataFrame con columnas diferentes, 
# sino que depende de los datos en vg_sales.csv.
# Usamos df.iloc[0] para tomar la primera fila de df con el objetivo de probar nuestra función, lo que produjo el output 'classic'. 
# Si revisamos las reglas de categorización, esto tiene sentido. Wii Sports fue lanzado antes del 2010 y ciertamente alcanzó más de $1 millón, ¡incluso mucho más!

# *Probar la función con filas personalizadas
# Hemos probado era_sales_group() para el caso de 'classic', ¿pero qué pasa con las otras cuatro categorías? 
# Sería una tarea tediosa buscar en los datos las filas correspondientes a cada caso. 
# Afortunadamente, podemos crear nuestras propias filas con los valores que queramos al convertir una lista de nombres de columna y una lista de valores de fila en un objeto tipo Series:

column_names = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']
row_values = [2000, 0.1, 0.25, 0]

row = pd.Series(row_values, index=column_names)

print(row)
print()
print('Este juego es', era_sales_group(row))

# Otra ventaja de probar la función de esta manera es que no necesitamos incluir valores para las columnas que no use nuestra función. 
# En este caso, nuestra fila solo tiene valores para las columnas 'year_of_release', 'na_sales', 'eu_sales' y 'jp_sales'.
# Para terminar las pruebas, vamos a usar la función con varios valores de input que nosotros creemos:

cols = ['year_of_release', 'na_sales', 'eu_sales', 'jp_sales']

row_1 = pd.Series([1989, 0, 0, 0.6], index=cols) # expect 'retro'
row_2 = pd.Series([1989, 1, 2, 0], index=cols)   # expect 'classic'
row_3 = pd.Series([2006, 0.3, 0, 0], index=cols) # expect 'modern'
row_4 = pd.Series([2020, 0, 0.4, 0], index=cols) # expect 'recent'
row_5 = pd.Series([2020, 1, 1, 1], index=cols)   # expect 'big hit'

print(row_1, row_2, row_3, row_4, row_5, sep='\n\n')
print()

rows = [row_1, row_2, row_3, row_4, row_5]

for row in rows:
    print('Este juego es', era_sales_group(row))

# ¡Parece que la función de categorización dio el resultado esperado! Para el último paso, vamos a usar la función para crear una columna nueva.

## *Crear una columna
# Ahora que has comprendido mejor cómo trabajan las funciones, vamos a aprender a usarlas junto con apply() para crear nuevas columnas.
# En este caso, queremos crear una columna llamada 'game_category' que categorice cada juego según el output de nuestra función era_sales_group(). 
# Al igual que en la lección anterior, llamaremos al método apply(). No obstante, esta vez hay dos diferencias importantes:
#   1. El método apply() se llama en el DataFrame df entero en vez de en una sola columna.
#   2. Necesitamos usar el parámetro axis= al llamar al método apply().
# De forma predeterminada, el parámetro axis= está en 0, lo que significa que apply() le pasa valores de columna a la función que se usa como input. 
# En cambio, si queremos que apply() pase los valores de fila de la función, necesitamos configurar axis=1.
# Entonces, se puede crear la nueva columna 'game_category' así:

def era_sales_group(row):
    """
    La función devuelve una categoría de juegos según el año de lanzamiento y las ventas totales mediante las siguientes reglas:
    —'retro'   para año < 2000 y las ventas totales < $1 million
    —'modern'  para 2000 <= año < 2010 y las ventas totales < $1 million
    —'recent'  para año >= 2010 y las ventas totales < $1 million
    —'classic' para año < 2010 y las ventas totales >= $1 million
    —'big hit' para año >= 2010 y las ventas totales >= $1 million
    """

    year = row['year_of_release']
    na_sales = row['na_sales']
    eu_sales = row['eu_sales']
    jp_sales = row['jp_sales']
    
    total_sales = na_sales + eu_sales + jp_sales
    
    if year < 2000:
        if total_sales < 1:
            return 'retro'
        else:
            return 'classic'
    if year < 2010:
        if total_sales < 1:
            return 'modern'
        else:
            return 'classic'
    if year >= 2010:
        if total_sales < 1:
            return 'recent'
        else:
            return 'big hit'

df['game_category'] = df.apply(era_sales_group, axis=1)
print(df.sample(5, random_state=321))

# Ahora vemos que logramos crear la nueva columna y podemos comenzar el análisis. 
# Por ejemplo, podemos recurrir al método value_counts() para obtener el número de juegos que pertenecen a cada categoría:

print(df['game_category'].value_counts())

# Esperamos que aprecies el poder y la versatilidad de las funciones personalizadas con apply(). 
# ¡No dejes de cultivar tus habilidades para crear columnas en los ejercicios!

# Fin.