# Capítulo 3/5 - Diccionarios
#
# EXTRAER VALORES DE DICCIONARIOS
#
# Ahora que has creado tu primer diccionario, exploremos cómo podemos recuperar y agregar valores. 
# Antes de continuar, recapitulemos que existen tres reglas básicas para la sintaxis del diccionario:
# - Los diccionarios se escriben con llaves: {}.
# - Las comas separan los elementos (pares clave-valor) dentro del diccionario.
# - Una clave y un valor dentro de un par se separan por dos puntos.
# Con esto en mente, vamos a aprender cómo recuperar valores de un diccionario.

# Teoria
# Recuperación de valores del diccionario
# Hay dos formas de acceder a un valor: usando la clave directamente y usando el método get(). 
# Usaremos un diccionario en el que las claves son los nombres de las empresas y los valores son los respectivos precios de sus acciones.

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

# Usar la clave
# Puedes especificar la clave del diccionario entre corchetes para extraer su valor. 
# Por ejemplo, si queremos recuperar el precio de Coca-Cola, hacemos lo siguiente:

# accedemos al valor de la clave 'Coca-Cola' del diccionario
coca_cola_price = financial_info['Coca-Cola']
print(coca_cola_price)

# La salida es> 45.15

# El procedimiento es muy parecido al de obtener un elemento de una lista a partir del índice: 
# solo tenemos que poner la clave entre los corchetes en lugar del índice.
# La mayor ventaja es que permite el uso de claves más descriptivas y significativas, 
# lo que hace que tu código sea más legible y fácil de entender a largo plazo.

# Ejercicio 1
# ¡Ahora practiquemos la extracción de valores!
# Recupera el precio de las acciones de 'Walmart' accediendo al valor correspondiente del diccionario usando la clave 
# y luego asígnalo a la variable walmart_price. Muestra walmart_price cuando se extraiga el precio.

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

walmart_price = financial_info['Walmart']   # escribe tu código aquí
print(walmart_price)

# Resultado: 130.68

# Teoria
# Ejercicio 2
# ¿Por qué se desplomó el mercado de valores? ¡Porque nadie pudo encontrar las acciones en el diccionario! 
# Pero en serio, ¡es hora de practicar!
# Accede al precio de las acciones de 'Nike' del diccionario usando el método get(). 
# Al llamar a get(), None debe ser el valor devuelto si 'Nike' no se encuentra como clave.

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

nike_price = financial_info.get('Nike') # escribe tu código aquí
print(nike_price)

# Resultado: 97.99

# Fin.