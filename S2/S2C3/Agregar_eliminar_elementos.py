# Agregar y eliminar elementos.
#
# Anteriormente vimos que los valores se pueden extraer de un diccionario, 
# ya sea especificando el nombre de la clave (por ejemplo, financial_info['Coca-Cola']) 
# o con la ayuda del método get() (por ejemplo, financial_info.get('Coca-Cola'))
# Ahora aprendamos cómo agregar y eliminar elementos de los diccionarios.

# Añadir elementos
# Recuerda que se pueden agregar elementos al final de una lista con el método append(). 
# El método insert() se puede utilizar para elegir el lugar para un nuevo elemento en una lista.
# Añadir un nuevo elemento a un diccionario en Python es aún más sencillo. 
# Escribe el nombre del diccionario seguido de la clave entre corchetes y luego configúralo igual al valor que elijas. 
# Por ejemplo, si queremos agregar el precio de las acciones de Walt Disney a nuestro diccionario financial_info, 
# hacemos lo siguiente:

financial_info['Walt Disney'] = 119.34

# Y ya está, agregamos un nuevo par al final del diccionario financial_info con el precio de las acciones de Disney. 
# Comprobemos el resultado imprimiendo el diccionario financial_info:

print(financial_info)

{'American Express': 93.23, 'Boeing': 178.44, 'Coca-Cola': 45.15, 'Nike': 97.99, 'JPMorgan': 96.27, 'Microsoft': 213.67, 'Walmart': 130.68, 'Walt Disney': 119.34}

# A veces, antes de añadir un elemento a un diccionario, queremos comprobar si la clave que queremos utilizar 
# ya existe en el diccionario. Si la clave no existe, la agregamos. Sin embargo, si la clave ya existe, puede que queramos actualizar su valor. 
# Hagámoslo con 'Walt Disney':

if financial_info.get('Walt Disney') == None: # comprobamos si Walt Disney existe
    financial_info['Walt Disney'] = 119.34 # si no, la agregamos
else: # si existe
    financial_info['Walt Disney'] += 3.2 # actualizamos el valor

# El código anterior comprueba si 'Walt Disney' está en la variable financial_info. 
# Para ello, compara el resultado del método get() con None. 
# Si el resultado es None, significa que 'Walt Disney' no está en financial_info. 
# En este caso, agregamos 'Walt Disney' a financial_info y establecemos su precio. 
# Si 'Walt Disney' ya está en financial_info, actualizamos el precio actual incrementándolo en 3.2.

# Ejercicio
# 
# Añade un nuevo elemento al diccionario financial_info. 
# Usa 'Microsoft' como clave y 208.35 como valor. 
# Cuando termines, muestra financial_info en la pantalla.

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}
financial_info['Microsoft'] = 208.35
# agrega un nuevo par aquí
financial_info['Aeromexico'] = 210.85

print(financial_info)

# Resultado {'American Express': 93.23, 'Boeing': 178.44, 'Coca-Cola': 45.15, 'Walt Disney': 119.34, 'Nike': 97.99, 'JPMorgan': 96.27, 'Walmart': 130.68, 'Microsoft': 208.35}

# Teoria

# Eliminar elementos
# Puedes usar el comando del para eliminar un elemento de un diccionario. 
# Para hacerlo, especifica la clave del elemento que quieres eliminar después de la palabra clave del. A continuación te mostramos un ejemplo:

del financial_info['Nike']
print(financial_info)

{'American Express': 93.23, 'Boeing': 178.44, 'Coca-Cola': 45.15, 'Walt Disney': 119.34, 'JPMorgan': 96.27, 'Microsoft': 208.35, 'Walmart': 130.68}

# Al ejecutar el código anterior, eliminaremos el elemento con la clave 'Nike' del diccionario financial_info.

# De forma similar a las listas, también puedes usar el método pop() para eliminar un elemento de un diccionario 
# y acceder a su valor al mismo tiempo. El método pop() toma un argumento, que es la clave del elemento que quieres eliminar.

walmart_price = financial_info.pop('Walmart')
print(walmart_price)
print(financial_info)

# Resultado> 130.68
# {'American Express': 93.23, 'Boeing': 178.44, 'Coca-Cola': 45.15, 'Walt Disney': 119.34, 'JPMorgan': 96.27, 'Microsoft': 208.35}

# El método pop() devuelve el valor del elemento eliminado, que en este caso es el precio de las acciones de Walmart.
# ¡Y con eso concluye nuestra exploración de los conceptos básicos de los diccionarios en Python! Teniendo esto en cuenta, vamos a la práctica.

# Fin.