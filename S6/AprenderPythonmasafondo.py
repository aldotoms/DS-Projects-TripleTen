# Capítulo 3/5
# Aprender Python más a fondo

## Diccionarios: recorrer diccionarios en bucle

# Tras haber profundizado en los entresijos de los diccionarios de Python, estás a un paso de vivir una experiencia de aprendizaje mucho más enriquecedora. 
# Ahora vamos a sumergirnos aún más en el tema de los diccionarios.
#Es importante mencionar que existen varias formas de acceder a los elementos de un diccionario. 
# Además de las formas que ya conocemos, otra forma es recorrer las claves, valores o elementos del diccionario. 
# Esto puede ser muy útil cuando necesites realizar alguna operación en cada elemento. Por ejemplo, puede que quieras actualizar los valores de ciertas claves o crear un nuevo diccionario basado en un subconjunto de claves y valores.
# En esta lección, aprenderás a usar los métodos keys(), values() e items() para recorrer elementos específicos del diccionario.

# Bucles sobre claves y valores
# Puedes usar los métodos keys() y values() para ver las claves y los valores del diccionario, respectivamente. 
# Estos métodos son útiles cuando quieres realizar operaciones solo en las claves o los valores, o cuando quieres comprobar si una clave o un valor en particular está presente en el diccionario.
# Para recorrer las claves en un diccionario, puedes usar el método keys(). Aquí te mostramos un ejemplo:

financial_info = {
    'American Express': 93.23, 
    'Boeing': 178.44, 
    'Coca-Cola': 45.15, 
    'Walt Disney': 119.34, 
    'Nike': 97.99, 
    'JPMorgan':96.27, 
    'Walmart': 130.68
}

for key in financial_info.keys():
    print(key)

# Para recorrer los valores en un diccionario, usemos el método values():

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

for value in financial_info.values():
    print(value)

# Vamos a crear un programa que recorra el diccionario financial_info y calcule el valor total de todas las acciones. 
# Esto puede resultar útil para los inversores y las inversoras que deseen obtener una visión general rápida del rendimiento de su cartera.
# Para hacer esto, necesitas utilizar un bucle for para iterar sobre el diccionario financial_info, extraer el precio de las acciones (los precios de las acciones almacenados como valores) y actualizar la variable total_value.
# Cuando termines, muestra total_value en la pantalla.

# Código
financial_info = {
    'American Express': 93,
    'Boeing': 178,
    'Coca-Cola': 45,
    'Walt Disney': 119,
    'Nike': 97,
    'JPMorgan': 96,
    'Walmart': 130
}

total_value = 0 # el valor que actualizarás en cada iteración del bucle

# escribe tu bucle for aquí. En cada iteración del ciclo, extrae el precio
for value in financial_info.values():
    total_value += value    # y actualiza la variable total_value

print(total_value)

# Acabamos de mostrarte cómo recorrer los valores en un diccionario y hacer algo con ellos. Usamos el método values() para calcular cuánto valen todas las acciones en el diccionario financial_info. 
# Puedes usar este truco para resolver todo tipo de problemas en los que tienes que hacer algo con cada elemento de un diccionario.

# Bucles sobre elementos
# Además de las claves y los valores, puedes usar el método items() para ver los pares (clave, valor) del diccionario. 
# Este método puede ser útil cuando quieres iterar sobre los pares y realizar alguna operación en cada uno.
# Así es como se hace:

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

for key, value in financial_info.items():
    print(key, value)

# Recorrer los diccionarios en Python es una habilidad útil cuando se trabaja con esta estructura de datos. 
# Al usar los métodos keys(), values() y items(), puedes recorrer fácilmente los elementos específicos de un diccionario y realizar las operaciones necesarias en ellos.
# Ahora, calculemos nuevamente el valor total de todas las acciones, pero esta vez con la ayuda del método items():

# De nuevo, vamos a crear un programa que recorra el diccionario financial_info y calcule el valor total de todas las acciones.
# Esta vez necesitas usar el método items() en lugar de values().
# Cuando termines, muestra total_value en la pantalla.

# Código
financial_info = {
    'American Express': 93,
    'Boeing': 178,
    'Coca-Cola': 45,
    'Walt Disney': 119,
    'Nike': 97,
    'JPMorgan': 96,
    'Walmart': 130
}

total_value = 0 # el valor que actualizarás en cada iteración del bucle

# escribe tu bucle for aquí. En cada iteración del ciclo, extrae el precio
for key, value in financial_info.items():
    total_value += value
# y actualiza la variable total_value

print(total_value)

# FIN.