# PRÁCTICA GUIADA
#
# Usa lower() para convertir la siguiente lista de compras a minúsculas. 
# Reasigna la variable shopping_list a continuación con la lista convertida.
#La salida esperada es esta:

shopping_list = '''MANZANAS
naranjas
leche
Manzanas
pan
helado
manzanas
ACEITE DE OLIVA
Pan'''

shopping_list = shopping_list.lower()   # convierte la variable shopping_list a minúsculas aquí
print(shopping_list)

# Usa replace() para reemplazar todas las ocurrencias de 'manzana' por 'naranja' en el siguiente string y asigna el string modificado a la variable new_string. Muestra new_string.
# La salida esperada es esta: Yo tengo una naranja, ella tiene una naranja, él tiene una naranja, todos tenemos naranjas.

old_string = "Yo tengo una manzana, ella tiene una manzana, él tiene una manzana, todos tenemos manzanas."
new_string = old_string.replace('manzana', 'naranja')    # escribe tu código aquí
print(new_string)

# Te han dado un string sentence que tiene espacios extra antes del texto. 
# Utiliza el método strip() para eliminar estos espacios. 
# Cuando se hayan eliminado, reemplaza todos los espacios en el string con -.
# Asigna el string modificado a una nueva variable llamada new_sentence y muéstrala.
# La salida esperada es esta:
# Python-es-un-lenguaje-de-programación-interpretado,-de-alto-nivel-y-de-propósito-general.

sentence = "   Python es un lenguaje de programación interpretado, de alto nivel y de propósito general.   "
new_sentence = sentence.strip()     # primero, elimina los espacios innecesarios
new_sentence = sentence.replace(' ', '-')       # segundo, reemplaza los espacios con guiones (-)
print(new_sentence)     # finalmente, imprime tu string resultante aquí