## Capítulo 3/6
# Introducción al preprocesamiento de datos y al análisis inicial

# Ejercicios
# Ejercicio 1
# ¡Y ahora es tu turno para practicar!

# Primero, debes ver si algo está mal con los nombres de las columnas y qué es. 
# Así que comienza por mostrar los nombres de columna de la tabla df.

# Código
import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
# escribe tu código aquí
print(df.columns)

Index(['  user_id', 'total play', 'Artist', 'genre', 'track'], dtype='object')


## Ejercicio 2
# Debes identificar tres problemas en los nombres de las columnas '  user_id', 'total play' y 'Artist'. Adelante, corrígelos.
# Renombra las siguientes tres columnas en df:

# - ' user_id' → 'user_id'
# - 'total play' → 'total_play'
# - 'Artist' → 'artist'

# Crea un diccionario con los nombres antiguos y los nuevos, y después llama al método rename() en df y pasa a este tu diccionario.
# En el diccionario, utiliza los nombres de columna anteriores como claves y los nuevos como valores.
# Luego, muestra el atributo columns para df para confirmar que los cambios se han aplicado.

# Código
import pandas as pd
df = pd.read_csv('/datasets/music_log_raw.csv')
columns_new ={
    '  user_id': 'user_id',
    'total play': 'total_play',
    'Artist': 'artist',
}
df.rename(columns = columns_new, inplace = True)
print(df.columns)


## Teoria

# Forma automatizada de renombrar las columnas
# A veces, la cantidad de columnas en un dataset puede ser grande, por lo que es poco práctico asignar manualmente nuevos valores a los nombres de las columnas. 
# Y de hecho, podría ser difícil ver los problemas en un nombre de columna. En estos casos, los bucles y los métodos de string pueden ser muy útiles. 
# Echa un vistazo al siguiente fragmento de código que itera sobre los antiguos nombres de la columna, los cambia y guarda los resultados en la lista new_col_names, 
# que más tarde se asigna como los nuevos nombres de columna:

new_col_names = []

for old_name in celestial.columns:
    # Primero, elimina los espacios al principio y al final
    name_stripped = old_name.strip()
    # Luego, pon todas las letras en minúsculas
    name_lowered = name_stripped.lower()
    # Por último, reemplaza los espacios entre palabras por guiones bajos
    name_no_spaces = name_lowered.replace(' ', '_')
    # Agrega el nuevo nombre a la lista de nuevos nombres de columna
    new_col_names.append(name_no_spaces)

# Reemplaza los nombres anteriores por los nuevos
celestial.columns = new_col_names

# Como resultado, obtenemos un DataFrame en el que todos los nombres de las columnas se ajustan a nuestro formato deseado.
# Una cosa importante a tener en cuenta es cómo reemplazamos los nombres de columna antiguos con los nuevos a través de esta línea:

celestial.columns = new_col_names

# Vamos a explicarlo un poco más:
# - new_col_names es una lista que contiene los nombres nuevos de columna que queremos configurar.
# - Al establecer celestial.columns igual a new_col_names, hacemos el verdadero reemplazo, actualizando los nombres de columna antiguos con los nuevos almacenados en new_col_names.
# Dicho método de reemplazo resulta útil cuando tienes nombres de columna que quieres establecer en forma de lista.
# ¡Es muy claro! Recorre los nombres de tus columnas; elimina todos los espacios iniciales y finales usando el método strip(); 
# haz que todo esté en minúsculas con el método lower(); remplaza cualquier espacio entre palabras con guiones bajos aplicando el método replace(); y después agrega el nuevo nombre (más claro) a la nueva lista.
# Ahora es tu turno nuevamente. Volvamos a nuestro dataset music_log_raw.csv.


## Ejercicios

# Ejercicio 3
# Ahora queremos que hagas el mismo cambio de nombre, pero usando 3 métodos de string: strip(), lower() y replace(). 
# Coloca los nuevos nombres de columna en la lista new_col_names.
# Luego, muestra el atributo columns para df para confirmar que los cambios se han aplicado.

# Código
import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

new_col_names = []

# escribe tu código aquí
for old_name in df.columns:
    name_stripped = old_name.strip()
    name_lowered = name_stripped.lower()
    name_no_space = name_lowered.replace(' ','_')
    new_col_names.append(name_no_space)

df.columns = new_col_names
print(df.columns)


# ¡Y ahí lo tienes! ¡Un simple bucle puede hacer que todo se vea limpio y reluciente! 
# A partir de la próxima lección, vas a estudiar cómo trabajar con problemas de contenido, empezando con los valores ausentes.

# Fin.