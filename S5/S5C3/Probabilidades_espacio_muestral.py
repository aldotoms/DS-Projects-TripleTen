# Capítulo 3/5
# Teoría de la probabilidad

# Probabilidades del espacio muestral
# En Python, los cálculos de probabilidad simples basados en espacios muestrales como estos se pueden realizar fácilmente usando el operador lógico == y la función len().
#   ' Utilizar == identificará las filas que satisfacen tu evento.
#   ' len() proporcionará el recuento de filas que satisfacen tu evento.
# Aquí te mostramos un ejemplo.
# Has creado una lista de reproducción en la aplicación Spotify con dos columnas: 'Artist' y 'Song'.

import pandas as pd

cool_rock = pd.DataFrame(
    {
        'Artist': [
            'Queen',
            'Queen',
            'Queen',
            'Pink Floyd',
            'Nirvana',
            'AC/DC',
            'AC/DC',
            'Scorpions',
            'Scorpions',
            'Scorpions',
        ],
        'Song': [
            'The Show Must Go On',
            'Another One Bites The Dust',
            'We Will Rock You',
            'Wish You Were Here',
            'Smells Like Teen Spirit',
            'Highway To Hell',
            'Back in Black',
            'Wind Of Change',
            'Still Loving You',
            'Send Me An Angel',
        ],
    }
)
print(cool_rock)

# Suponiendo que pulses aleatorio, cada canción de la lista de artistas + canciones tiene la misma probabilidad de tocar primero. Esta lista es nuestro espacio de muestra.
# ¿Cuál es la probabilidad de que la primera canción que suene sea "Smells Like Teen Spirit"?
# Usa == para identificar los resultados que satisfacen este evento y usa len() dos veces: una para contar el número de resultados que satisfacen el evento y otra vez para contar el tamaño del espacio muestral.

print(
    len(cool_rock[cool_rock['Song'] == 'Smells Like Teen Spirit'])
    / len(cool_rock)
)

# ¡Has aprendido muchos términos nuevos! Para comprobar que lo has entendido, intenta realizar las siguientes tareas.
# Después de barajar la lista, tienes que calcular la probabilidad de que la primera canción sea del grupo 'Queen'. Escribe el código para calcularlo.
# Utiliza la variable desired_outcomes para almacenar el número de resultados deseados, total_outcomes para almacenar el número total de resultados, 
# y probability para el resultado final. Tras hacer esto, muestra probability.

# Código
import pandas as pd

cool_rock = pd.DataFrame(
    {
        'Artist': [
            'Queen',
            'Queen',
            'Queen',
            'Pink Floyd',
            'Nirvana',
            'AC/DC',
            'AC/DC',
            'Scorpions',
            'Scorpions',
            'Scorpions',
        ],
        'Song': [
            'The Show Must Go On',
            'Another One Bites The Dust',
            'We Will Rock You',
            'Wish You Were Here',
            'Smells Like Teen Spirit',
            'Highway To Hell',
            'Back in Black',
            'Wind Of Change',
            'Still Loving You',
            'Send Me An Angel',
        ],
    }
)

desired_artist = 'Queen'
desired_outcomes = len(cool_rock[cool_rock['Artist'] == desired_artist])
total_outcomes = len(cool_rock)
probability = desired_outcomes / total_outcomes
print(probability)

# ¡Bien hecho! Ahora que has aprendido los fundamentos de la teoría de la probabilidad, ya puedes sumergirte en temas más específicos.

# FIN.