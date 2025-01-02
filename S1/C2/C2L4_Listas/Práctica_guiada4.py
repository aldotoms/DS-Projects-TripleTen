# PRáctica guiada
# A continuación, verás un fragmento de código que produce un error. ¿Puedes adivinar qué está mal?
# Se genera un error debido a que el nombre de la variable comienza con un número. 
# Tu objetivo es corregir el error para que podamos mostrar el texto 'Mary'. Crea un nuevo nombre de tu elección.

# La salida esperada es esta: Mary
2_name = 'Mary'
print(2_name)

_name = 'Mary'
print(_name)

# A continuación se muestra el código que genera un error. 
# Trata de encontrar un error. Si lo encuentras, corrígelo. 
# De lo contrario, ejecuta el código, lee el mensaje de error e intenta corregir el error nuevamente.

# La salida esperada es esta: 
# Precio total: 3.7300000000000004

apple_price = 1.25
banana_price = 0.99
kiwi_price = 1.49

total_price = apple_price + banana_price + kiwi_price
print("Precio total:", total_pirce)

# Código corregido es:
apple_price = 1.25
banana_price = 0.99
kiwi_price = 1.49

total_price = apple_price + banana_price + kiwi_price
print("Precio total:", total_price)

# Primero, ejecuta el programa de abajo para asegurarte de que se produzca el error ZeroDivisionError.

ja_total_speakers = 0
ja_native_speakers = 128.2
print((ja_total_speakers - ja_native_speakers) / ja_total_speakers)

# Después, cambia el código para que contenga un bloque try-except. Si hay un error, muestra el mensaje '¡División entre cero!'.
# No es necesario cambiar los valores de las variables.
# La salida esperada es esta: ¡División entre cero!

try:
    ja_total_speakers = 0
    ja_native_speakers = 128.2
    print((ja_total_speakers - ja_native_speakers) / ja_total_speakers)
except:
    print('¡División entre cero!')