# SyntaxError - TypeError - NameError
# Los errores más comunoes
# ¿Cómo manejar los errores adecuadamente cuando surgen.

# Los errores son una parte completamente normal del proceso de escribir código. 
# Al implementar mecanismos de manejo de errores evitamos que nuestros programas dejen de funcionar, lo que aumenta su fiabilidad.
# Dado que los errores pueden surgir de diferentes fuentes, repasaremos los tres motivos más comunes que los provocan:
# 1. Sintaxis incorrecta
# 2. Operaciones Prohibidas
# 3. Referencia a variables no válidas

# 1.-Error de Syntaxis
# Este tipo de error ocurre cuando tu código no se apega a las reglas del lenguaje de programación. 
# Un ejemplo de ello es cuando olvidamos un paréntesis en la función print(), lo que genera un SyntaxError.
print('Hola'
      
# 2.-Error de Operación
# Esto ocurre como resultado de una operación no válida. Por ejemplo, dividir entre cero. Echa un vistazo a este código:
print(777 / 0)

# Otro ejemplo sería agregar texto a un número. Revisa el siguiente código y observa qué error arroja:
numbers = 'uno dos tres cuato' + 5
print(numbers)

# Errores de espacio de nombres
# Esto ocurre si tratas de utilizar una variable que no se ha creado. Aquí te mostramos un ejemplo:
apple_price = 1.25
banana_price = 0.99
print("Precio Total", apple_price + banana_price + kiwi_price)

# ¿Cómo podemos manejar un error durante la ejecución del código?
# Para manejar estas situaciones, Python utiliza el bloque try-except. 
# El bloque try ejecuta el código con normalidad; si ocurre un error, el bloque except lo detecta, lo que permite que el programa continúe ejecutándose.
# Observa que tanto try como except van seguidos de dos puntos. 
# En las siguientes líneas están escritas las instrucciones para cada bloque, y cada línea dentro de estos bloques está indentada de la siguiente manera:
try:
    print(777 / 0)
except:
    print("¡No es posible dividir entre ceros")
    print("¡Sigamos adelante")