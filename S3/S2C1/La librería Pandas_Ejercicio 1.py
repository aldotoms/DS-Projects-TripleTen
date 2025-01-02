# Capítulo 1/6
#La librería Pandas

# EJERCICIOS

# Ejercicio 1

# Importa pandas para poder acceder a la librería con pd. 
# Crea una lista anidada, music, con cuatro elementos. 
# Cada sublista debe almacenar dos valores de tipo string: artista y nombre de la canción:

# 'Bob Dylan' — 'Like A Rolling Stone'
# 'John Lennon' — 'Imagine'
# 'The Beatles' — 'Hey Jude'
# 'Nirvana' — 'Smells Like Teen Spirit'

import pandas as pd

music = [
    ['Bob Dylan', 'Like A Rolling Stone'],
    ['John Lennon', 'Imagine'],
    ['The Beatles', 'Hey Jude'],
    ['Nirvana', 'Smells Like Teen Spirit'],
]

quboz = ['Artist', 'Song']
quboz_list = pd.DataFrame(data=music, columns=quboz)
print(quboz_list)

