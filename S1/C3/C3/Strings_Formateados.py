# Strings formateados
#
# Cómo incorporar variables a strings
# Si necesitas que tu programa muestre algo, utilizarás el método print(). 
# Por ejemplo, digamos que quieres que tu programa muestre el nombre, la edad y la estatura de alguien de la siguiente forma:

message = "Victoria tiene 23 años y mide 157 cm"
print(message)

# La salida es: Victoria tiene 23 años y mide 157 cm
# Este código funciona, ¿pero qué pasa si algunos atributos cambian con el tiempo? 
# En ese caso, sería difícil mantener este código actualizado.

# F-strings
# El método F-string (o cadena F) es una manera muy directa y elegante de incorporar información dinámica que puede cambiar con el tiempo. 
# Esto es lo que debes hacer:
#
# 1.-Comienza la definición de tu string con la letra ‘f’, como si dijera, "’f’ormatea" el siguiente string, antes de abrir las comillas.
# 2.-Escribe tu texto normalmente, pero reemplaza los valores con variables dentro de las llaves {}. 
#    Estas variables deben almacenar la información que finalmente querrás incorporar a tu string.
#    En un escenario más elaborado, el contenido de estas variables podría actualizarse con el tiempo.
#    Por lo tanto, quieres que tus programas se mantengan al corriente con estos cambios sin intervenciones manuales.
#
# Este es nuestro primer ejemplo convertido al formato F-string:

name = 'Victoria'
age = 23
height = 157
message = f"{name} tiene {age} años y mide {height} cm"
print(message)

# Más aún, también puedes realizar operaciones dentro de las llaves. Este es un ejemplo de una operación aritmética.

name = 'Victoria'
age = 23
message = f"El próximo año, {name} tendrá {age + 1} años"
print(message)

# Fin.