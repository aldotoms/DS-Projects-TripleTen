# Capítulo 1/5 Bucles

# Cuestionario del capítulo
# Introducción
# Ya has visto lo poderosos que pueden ser los bucles for y while. 
# Por ejemplo, los bucles for nos permiten iterar sobre una tabla (una lista de listas) 
# y modificar los valores en filas y columnas particulares como esta:

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

for row in movies_info:
    runtime = row[4]
    runtime /= 60
    print(runtime)

# La salida esperada es:
# 2.3666666666666667
# 2.9166666666666665
# 2.533333333333333
# 3.25
# 3.35
# 2.566666666666667
# 2.966666666666667
# 2.316666666666667
# 2.216666666666667
# 2.1

# Los bucles while, por otro lado, son increíblemente útiles cuando no sabemos de antemano cuantas iteraciones necesitamos. 
# Al igual que en el ejemplo de los ascensores, hacemos un bucle hasta llegar al límite.

# Siguientes pasos
# 
# En este capítulo, has explorado las potentes capacidades de los bucles en Python. 
# A continuación te mostramos un resumen de lo que aprendiste:
#
# Bucles for
# Nos permiten iterar sobre secuencias tales como listas, lo que nos permite acceder a los elementos y modificarlos de manera eficiente. 
# Has aprendido cómo procesar cada elemento en una secuencia y realizar operaciones, como convertir valores o calcular métricas.
#
# Bucles while
# Estos son perfectos para situaciones en las que no sabes de antemano cuantas iteraciones necesitas. 
# Continúan ejecutándose en tanto una condición especificada siga siendo verdadera. 
# Esto resulta útil para escenarios en los que la condición final depende de factores dinámicos.

# Con tus nuevos conocimientos sobre bucles, ya cuentas con todas las herramientas para enfrentarte al siguiente tema: sentencias condicionales en Python. 
# Las sentencias condicionales te permitirán introducir la toma de decisiones en tus programas, lo que te permitirá ejecutar diferentes bloques de código con base en diversas condiciones.

# ¡Lo estás haciendo muy bien! Y cada nuevo concepto que aprendes se basa en el anterior. 
# ¡Sigue esforzándote y prepárate para sumergirte en el mundo de los condicionales!

# ¿Todo listo para explorar los condicionales? ¡Vamos a ello!

# Fin.