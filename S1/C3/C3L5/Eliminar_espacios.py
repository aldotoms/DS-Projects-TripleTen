# Eliminar espacios en blanco
#
# A veces, cuando los datos se exportan entre sistemas, puede ser que  objetos como espacios iniciales 
# y finales se introduzcan en los nombres de las columnas. 
# Esto puede dificultar la escritura y el intercambio de código que utiliza los mismos datos.
# El método strip() elimina todos los espacios en blanco al principio y al final de un string; 
# se conservan todos los espacios en blanco dentro del resto del string. 
# Por espacios en blanco, nos referimos a caracteres como espacios, tabulaciones y saltos de línea.
# Aquí tienes un ejemplo:

column_name = '     purchase date  '

print(column_name)                # muestra en pantalla column_name
print(len(column_name))           # muestra en pantalla la longitud actual de column_name
print()                           # muestra en pantalla una línea vacía
print(column_name.strip())        # elimina espacios en blanco desde el principio y muestra en pantalla
print(len(column_name.strip()))   # muestra en pantalla la nueva longitud de column_name 

# Podemos ver que se eliminan los espacios en blanco en ambos extremos, 
# lo que se refleja en las diferentes longitudes de los strings con y sin llamar a strip().


# Te han dado un string sentence que tiene espacios extra antes del texto. 
# Utiliza el método strip() para eliminar estos espacios. Cuando se hayan eliminado, 
# reemplaza todos los espacios en el string con -.
# Asigna el string modificado a una nueva variable llamada new_sentence y muéstrala.
# La salida esperada es esta:
# Python-es-un-lenguaje-de-programación-interpretado,-de-alto-nivel-y-de-propósito-general.

sentence = "   Python es un lenguaje de programación interpretado, de alto nivel y de propósito general.   "
new_sentence = sentence.strip() # primero, elimina los espacios innecesarios
new_sentence = new_sentence.replace(' ', '-') # segundo, reemplaza los espacios con guiones (-)
print(new_sentence) # finalmente, imprime tu string resultante aquí

# Fin.