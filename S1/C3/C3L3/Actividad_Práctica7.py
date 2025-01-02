# EJERCICIO 1
#
# Intentemos algo diferente. Vamos a usar la siguiente frase para extraer partes específicas de este texto:
# 'Londres es la capital del Reino Unido'
#
# Para hacerlo, asigna el texto anterior a la variable phrase (frase). 
# Segmenta la variable, utilizando únicamente la segmentación negativa, y devuelve el siguiente texto:
# La salida esperada es esta: Reino Unido

phrase = 'Londres es la capital del Reino Unido'
print(phrase[-11:])

# ----------------------------------------------------------------------------------------------------------------
# EJERCICIO 2
# Al igual que en el ejercicio anterior, utilizaremos la misma frase para extraer una parte distinta del texto.

phrase = 'Londres es la capital del Reino Unido'
print(phrase[len(phrase)-11:])

# Asigna el texto anterior a la variable phrase. Muestra la palabra capital utilizando la segmentación negativa.
# La salida esperada es esta: capital

phrase = 'Londres es la capital del Reino Unido'
print(phrase[-23:-16])

# Fin.