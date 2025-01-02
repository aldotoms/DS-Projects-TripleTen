# PRÁCTICA GUIADA
#
# ¿Cómo extraerías la letra v de la variable phrase a continuación usando la indexación negativa?

phrase = 'El otro lado del rectángulo de Olivia es 2.' 

# La salida esperada es esta: v

phrase = 'El otro lado del rectángulo de Olivia es 2.'  
# escribe tu código aquí
print(len(phrase))
print(phrase[-9])

# Practiquemos el uso de la función len() utilizando algo de matemáticas. 
# Usando indexación positiva, muestra el último carácter del string almacenado en la variable phrase mediante la función len(), 
# así el índice debería ser un número positivo e imprimirá la letra g de la palabra duckling. 
# Después, muestra el primer carácter del string almacenado en la variable phrase utilizando la función len() usando la indexación negativa. 
# Esto significa que tu índice debería ser un número negativo que accede a la letra O, de Olivia.
# La salida esperada es esta:
# g
# O 

phrase = 'Olivia loves her little yellow duckling' 
print(len(phrase))      # Verificamos la longitud del string

# muestra aquí el último carácter usando la función len() y la indexación positiva
print(phrase[38])

# muestra aquí el último carácter usando la función len() y la indexación negativa
print(phrase[-39])

# Código con operaciones aritméticas
phrase = 'Olivia loves her little yellow duckling' 
print(phrase[len(phrase)-1])
print(phrase[-len(phrase)])

# Fin. 