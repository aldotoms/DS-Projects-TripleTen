# Capítulo 1/6
#La librería Pandas

# EJERCICIOS

# Ejercicio 2

# Crea una lista llamada entries que tenga dos elementos: 
# los nombres de las columnas 'artist' y 'track'. 
# Luego, utiliza DataFrame() para crear una tabla a partir de las listas music y entries. 
# Guarda el resultado en la variable playlist y luego muéstralo.

import pandas as pd

music = [
    ['Bob Dylan', 'Like A Rolling Stone'],
    ['John Lennon', 'Imagine'],
    ['The Beatles', 'Hey Jude'],
    ['Nirvana', 'Smells Like Teen Spirit'],
]

# escribe tu código aquí
entries = ['artist', 'track']
playlist = pd.DataFrame(data=music , columns=entries)
print(playlist)

# Fin.