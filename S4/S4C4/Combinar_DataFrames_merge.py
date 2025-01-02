# Sprint 4: Manipulación de datos (Data Wrangling) (continuación)

## Combinar DataFrames con merge()

# Acabas de aprender a combinar DataFrames concatenándolos por filas o columnas usando concat().
# La concatenación de DataFrames conserva la cantidad total de datos. 
# Por ejemplo, combinar un DataFrame que tiene dos columnas y tres filas con otro DataFrame que tiene las mismas dos columnas y cinco filas da como resultado 
# un DataFrame con dos columnas y ocho filas. El número total de celdas antes y después de la concatenación es dieciséis.
# En esta lección, aprenderás a combinar DataFrames utilizando el método merge() de forma que afecte a la cantidad de datos con los que estás trabajando.

# Considera el siguiente ejemplo: dos estudiantes de literatura acuerdan que uno escribirá la mitad de la lista de lectura de verano de la pizarra mientras el otro mira YouTube. 
# Después el primero irá a la cafetería, mientras que el segundo copia el resto de la lista. Finalmente, los dos combinarán las listas. ¡Trabajo en equipo! Vamos a ver cómo les fue:

import pandas as pd

first_pupil_df = pd.DataFrame(
    {
        'author': ['Alcott', 'Fitzgerald', 'Steinbeck', 'Twain', 'Hemingway'],
        'title': ['Little Women',
                  'The Great Gatsby',
                  'Of Mice and Men',
                  'The Adventures of Tom Sawyer',
                  'The Old Man and the Sea'
                 ],
    }
)
second_pupil_df = pd.DataFrame(
    {
        'author': ['Steinbeck', 'Twain', 'Hemingway', 'Salinger', 'Hawthorne'],
        'title': ['East of Eden',
                  'The Adventures of Huckleberry Finn',
                  'For Whom the Bell Tolls',
                  'The Catcher in the Rye',
                  'The Scarlett Letter'
                 ],
    }
)

print(first_pupil_df)
print()
print(second_pupil_df)

# Unión interna
# Usemos el método merge() para combinar entradas que tienen los mismos autores. E
# l nombre de la columna en la que se realizará la fusión se pasa al parámetro on=, en este caso, 'author':

both_pupils = first_pupil_df.merge(second_pupil_df, on='author')
print(both_pupils)

# El resultado contiene solo aquellos autores que están presentes en ambos DataFrames originales.
# El DataFrame fusionado incluye todas las columnas de los DataFrames originales, pero solo se conservan las filas con autores compartidos. 
# Ya que ambos DataFrames originales tienen una columna llamada 'title', pandas agregó los sufijos _x y _y para diferenciarlas en el DataFrame fusionado. 
# Cabe destacar que el DataFrame fusionado solo tiene 9 celdas, frente a las 20 celdas de los DataFrame originales: ¡la cantidad de datos ha cambiado!
# Este modo de fusionar se denomina unión interna (inner merge). Existen otros tipos de fusiones, que pueden especificarse con el parámetro how= de merge(). 
# Pero 'inner' es el argumento por defecto para how=, así que no necesitamos incluirlo arriba.


## Unión externa

# Una unión externa (outer merge) se diferencia de una unión interna en que todos los valores en la columna especificada se conservan de ambos DataFrames originales, 
# pero el DataFrame fusionado tiene valores ausentes donde no hay ninguna coincidencia. Lo mejor es ilustrar esto con un ejemplo:

both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='outer')
print(both_pupils)

# Hay 7 autores únicos en ambos DataFrames originales, cada uno se representa con una fila en el DataFrame fusionado. 
# Para los autores en el primer DataFrame que no están también en el segundo (es decir, 'Alcott' y 'Fitzgerald'), 
# hay valores NaN en la columna que proviene del segundo DataFrame (es decir, 'title_y'), y viceversa. Además, observa que ahora tenemos 21 celdas de datos.

