# PRACTICA GUIADA
#
# Divide el string phrase en una lista de nombres de personajes Disney. 
# Guarda el resultado en la variable words y muéstralo en pantalla.
# La salida esperada es esta: ['Aladdin', 'Esmeralda', 'Hercules', 'Mulan']

phrase = 'Aladdin#Esmeralda#Hercules#Mulan'
words = phrase.split('#')  # escribe tu código aquí
print(words)

# Une los superhéroes de la lista heroes en un string utilizando el separador >. 
# Asigna el resultado a la variable comparison y muéstralo en pantalla.
# La salida esperada es esta: Spiderman>Batman>Superman>Iron Man

heroes = ['Spiderman', 'Batman', 'Superman', 'Iron Man']
comparison = '>'.join(heroes)    # escribe tu código aquí
print(comparison)

# Fin.
