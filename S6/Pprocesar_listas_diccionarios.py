# Capítulo 3/5
# Aprender Python más a fondo

## Diccionarios: procesar listas de diccionarios

# Ahora conocemos dos estructuras de datos anidadas con diccionarios:
# Diccionarios de listas. A continuación te mostramos un ejemplo:

bus_schedule = {
      '72': ['8:00', '12:00', '17:30'],
      '26': ['9:30', '15:00'],
      '17': ['7:30', '12:30', '15:30']
  }
  
#   - Listas de diccionarios, que son excelentes para la representación de tablas.
# Ahora veamos un ejemplo concreto en el que las listas de diccionarios resultan útiles.
# Imagina que pides pizza y bebidas mediante una aplicación móvil. Los datos del pedido se envían al servidor como una lista de diccionarios donde:
#   -Cada diccionario es un elemento en el pedido.
#   - Cada clave del diccionario es un parámetro del pedido.
# Mira la lista de diccionarios order a continuación para ver cómo se envían los datos del pedido:

order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'price': 9
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'price': 2
    }
]

# Supongamos que queremos saber el pedido total. Para hacer esto, necesitamos sumar valores numéricos de los diccionarios para poder calcularlo. Sabemos lo siguiente:
#   - La lista nos permite recorrer todos los artículos del pedido utilizando un bucle.
#   - Los diccionarios nos dan acceso al precio y a la cantidad de cada elemento del pedido.
# Nuestro objetivo es multiplicar la cantidad y el precio de cada artículo del pedido. 
# El siguiente código hace exactamente esto. Primero, examínalo y luego ejecútalo para ver cuál es el resultado. 
# Presta atención a los comentarios que dejamos en el código. Explican claramente lo que está pasando.

# Código
order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'price': 9
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'price': 2
    }
]

# variable del precio total del pedido
total_price = 0 

# iterar sobre cada diccionario de la lista
for item in order: 
# añadir a la variable el precio del elemento multiplicado por la cantidad
    total_price += item['price'] * item['quantity']

print(total_price)

# Como resultado, obtuvimos 36 como nuestro total, pero ¿qué pasa si queremos calcular el total para una categoría en particular? Por ejemplo, ¿solo para pizzas?
# Mientras trabajábamos con las sentencias condicionales y la lista de listas anidadas en el primer sprint, aprendimos sobre los filtros. 
# Para aplicar un filtro, iteramos sobre una lista (por ejemplo, for movie in movies_info:), comprobamos una condición (por ejemplo, if movie[4] > 180:), y luego, 
# realizamos una acción si la condición devuelve True. Este es el código completo para un filtro aplicado a la lista de las listas anidadas:

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

movies_filtered = [] # lista vacía para almacenar el resultado

for movie in movies_info: # recorre en bucle las filas de la tabla original
    if movie[4] > 180: # si una película dura más de 180 minutos 
        movies_filtered.append(movie) # agrega la fila a movies_filtered

for movie in movies_filtered: # muestra el contenido de movies_filtered
    print(movie)

# Ahora filtremos los elementos de un diccionario anidado por categoría. ¡A ver si encuentras todas las pizzas!
#   - El bucle iterará sobre las listas de diccionarios y obtendrá el valor de la clave 'category'.
#   - Si el elemento pertenece a la categoría "pizza", el bucle añadirá el diccionario completo a la nueva lista.
# Examina el código que aparece a continuación y ejecútalo para ver qué produce.

# Código
order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'price': 9
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'price': 2
    }
]

# variable para almacenar el resultado
filtered_order = [] 

for item in order: # iterar sobre cada diccionario de la lista
	if item['category'] == 'pizza': # si la categoría es pizza...
		filtered_order.append(item) # agregamos el diccionario a la lista filtered_order

# mostramos la lista filtrada de diccionarios
print(filtered_order)

# Ahora tenemos una lista filtrada de diccionarios. ¿No es genial?
# ¡Ahora es tu momento de brillar! Mira el siguiente ejercicio.
# Volvamos al diccionario order. Halla el precio total para todas las pizzas en order y muéstralo. 
# Usa el mismo método que en los ejemplos de esta lección. Si tienes dificultades para resolverlo, consulta la pista.

# Código
order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'comment': 'Add extra cheese please!',
        'price': 9 # precio por elemento
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'comment': '',
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'comment': '',
        'price': 2
    },
    {
        'item': 'Apple juice 0.5 l',
        'category': 'beverages',
        'quantity': 1,
        'comment': '',
        'price': 1
    },
    {
        'item': 'Croissant with cheese',
        'category': 'baked foods',
        'quantity': 2,
        'comment': '',
        'price': 1
    }
]

total_price = 0

# empieza a escribir tu bucle for aquí
for item in order:
    if item['category'] == 'pizza':
        total_price += item['price'] * item['quantity']

print(total_price)

# FIN.