# En este ejercicio, utilizaremos la información resumida en una tabla.
# Esta tabla muestra una comparación entre diversos idiomas con base en su prevalencia en internet y el número de hablantes. 

# Ejercicio 1
# Observa la columna "Hablantes del idioma (millones)" arriba.
# Toma el valor para el inglés y asigna este valor a la variable english_speakers(hablantes de inglés). 
# Haz lo mismo con el ruso, asignando el valor a la variable russian_speakers (hablantes de ruso).

english_speakers = 1121.0
russian_speakers = 264.3

# Cuando hayas asignado los valores para inglés y ruso, crea una nueva variable llamada total_speakers; 
# suma english_speakers y russian_speakers y almacena el resultado de la suma en la nueva variable total_speakers.

total_speakers = english_speakers + russian_speakers

# Por último, muestra esta variable. 
# La salida esperada es esta: 1385.3

print(total_speakers)

# Ejercicio 2
# Encuentra la proporción de hablantes de italiano que son hablantes nativos. 
# Para hacerlo, asigna los valores a las variables que se proporcionan en el precódigo. En concreto:
# Asigna cuántas personas (millones) hablan italiano a la variable total_italian.

total_italian = 67.8

# Asigna cuántos hablantes nativos (millones) hablan italiano a la variable native_italian.

native_italian = 64.8

# Luego, realiza los cálculos y asigna el resultado a una variable llamada share_native. Muestra la variable.
# La salida esperada es esta: 0.9557522123893806

share_native = native_italian / total_italian
print(share_native)
