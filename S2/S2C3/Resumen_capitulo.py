# Capítulo 3/5 · Última lección
# Diccionarios

# Cuestionario del capítulo

# ¡Esperamos que tengas todo listo para poner a prueba tus conocimientos de Python! 
# En este capítulo de prácticas, repasaremos todo lo que has aprendido sobre los diccionarios. 
# Recapitulemos brevemente lo que hemos aprendido hasta ahora:
# - Para obtener un valor de una lista, necesitamos pasar la clave correcta a un par de corchetes o al método get():

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

walmart_price_1 = financial_info['Walmart']
walmart_price_2 = financial_info.get('Walmart')

print(walmart_price_1)
print(walmart_price_2)

# Resultado:
# 130.68
# 130.68

# # Agregar un nuevo par clave-valor a una lista se puede hacer así de fácil:

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

financial_info['Walt Disney'] = 119.34
print(financial_info)

# {'American Express': 93.23, 'Boeing': 178.44, 'Coca-Cola': 45.15, 'Nike': 97.99, 'JPMorgan': 96.27, 'Walmart': 130.68, 'Walt Disney': 119.34}

# Es una buena práctica comprobar si una clave ya se encuentra en un diccionario. 
# Si es así, normalmente nos interesa modificar su valor. 
# De lo contrario, agregamos una nueva clave y el valor correspondiente. 
# A continuación te mostramos un ejemplo:

# comprobamos si Walt Disney existe
if financial_info.get('Walt Disney') == None: 
    financial_info['Walt Disney'] = 119.34 # si no, la agregamos
else: # si existe
    financial_info['Walt Disney'] += 3.2 # actualizamos el valor 

# Por último, pero no menos importante, del o pop() se utilizan para eliminar elementos de un diccionario:

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

del financial_info['Nike']
boeing_price = financial_info.pop('Boeing')
print(financial_info)

# {'American Express': 93.23, 'Coca-Cola': 45.15, 'JPMorgan': 96.27, 'Walmart': 130.68}

# Fin.