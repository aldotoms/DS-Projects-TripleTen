# Capítulo 2/5  Sentencias condicionales
#
# Introducción
# En el capítulo anterior, al estudiar el bucle while, has visto cómo se comprobaba la condición en cada iteración del bucle. 
# En concreto, estábamos comprobando si total_weight era menor(<) que capacity y, si era así, el bucle seguía ejecutándose.
# Ahora, es el momento de aprender más sobre las declaraciones condicionales como <, que hemos utilizado en el bucle while.

# Declaraciones condicionales
# En el capítulo anterior, no solo has trabajado mucho con los bucles while, sino también en la creación de tu propia librería de películas movies_info. 
# Ya puedes hacer mucho con esta, por ejemplo, ordenar películas por distintos parámetros, agregar y eliminar entradas, acceder solo a valores específicos, etcétera.

# En este capítulo escribirás programas que tomarán decisiones con base en la entrada o los datos que reciban, con la ayuda de declaraciones condicionales. 
# Una vez que domines el uso de declaraciones condicionales, estarás listo para pasar al análisis de datos.

# Al final de este capítulo, sabrás cómo reconocer y definir expresiones lógicas; 
# utilizar expresiones condicionales para ayudar a filtrar tablas; 
# utilizar las declaraciones condicionales if y else para crear ramas en el código; 
# utilizar elif para justificar más de dos ramas posibles; formar expresiones compuestas con and, or y not; y, 
# escribir filtros que almacenen filas que cumplan criterios en una variable vacía.

# Este capítulo debería tomar de 1 a 3 horas. También veremos algunos ejemplos simples de nuestra lista anidada movies_info.

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# Fin.

datos_de_peliculas = movies_info
indice_pelicula = 0

def clasificar_pelicula(datos_pelicula):
    for indice_pelicula in range(len(datos_de_peliculas)):
        tier_de_pelicula = ""
        
    if datos_de_peliculas[indice_pelicula][-1] >= 8.8:
        datos_de_peliculas[indice_pelicula].append("alto")
        
clasificar_pelicula(movies_info)