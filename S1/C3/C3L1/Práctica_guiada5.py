# Práctica guiada No. 5

# Descripción
# Modifica el código para que pueda mostrarse sin errores. La salida esperada es esta:
# Let's become proficient in Python

print('Let's become proficient in Python')

# Código corregido:

print('Let\'s become proficient in Python')

# Descripción
# Ejecuta el siguiente código y examina el mensaje de error. 
# A continuación, usa caracteres de escape para corregir la sintaxis. La salida esperada es esta:

print("Y después dijo: "¡hey, eso es todo!", antes de agarrar la cola del gato.")

# Código corregido:
print('Y después dijo: "¡hey, eso es todo!", antes de agarrar la cola del gato.')

# Descripción
# Modifica el siguiente código para tener la misma frase en 5 líneas distintas.
# La salida esperada es esta:
# Mi lista de compras: 
# 2 cartones de leche, 
# cereal, 
# huevos, 
# pan

print("Mi lista de compras: 2 cartones de leche, cereal, huevos, pan")

# Código corregido_Opción 1:
print("Mi lista de compras: \n2 cartones de leche, \ncereal, \nhuevos, \npan")

# Código corregido_Opción 2:
print("""Mi lista de compras: 
      2 cartones de leche, 
      cereal, huevos, 
      pan""")

# Descripción
# Usa len() para calcular la longitud del string y asigna el resultado a una variable llamada length. 
# Luego, muestra el valor de length. La salida esperada es esta:

string = 'Olivia needs Kate\'s help.'

# escribe tu código aquí

string = 'Olivia needs Kate\'s help.'
length = len(string)
print(length)

# Fin.