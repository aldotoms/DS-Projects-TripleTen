# Capítulo 2/5 Sentencias condicionales 
#
# Creación de múltiples ramas con else y elif
# 
# Teoria
# Bien, ya sabemos cómo comprobar una condición mediante if y else, pero ¿y si necesitamos comprobar varias condiciones? ¿Cómo podemos hacerlo en Python?
#
# Condiciones múltiples 
# Las sentencias condicionales múltiples son muy comunes en Python. La sentencia elif es una abreviatura de "else if" y permite comprobar condiciones adicionales después de una sentencia if inicial.
# Al final de esta lección podrás utilizar la función elif en tu código para crear cualquier número de ramas.
# Perfeccionemos nuestro algoritmo para lidiar con el clima y agreguemos algunas opciones más:
# - Si llueve, lleva un paraguas.
# - Si hay sol, lleva gafas de sol.
# - Si nieva, ponte un gorro y una bufanda.
# - En caso contrario, no lleves nada.

# Como puedes ver en el diagrama, Python comprueba las condiciones de forma secuencial, una tras otra.
# En el caso de un algoritmo tan complejo, la estructura simple else-if no será suficiente. 
# Puedes comprobarlo por tu cuenta ejecutando el código del siguiente ejemplo.

weather = 'lluvia'

if weather == 'lluvia':
    item_to_take = 'paraguas'
if weather == 'sol':
    item_to_take = 'sombrero'
if weather == 'nieve':
    item_to_take = 'gorro y bufanda'
else:
    item_to_take = 'nada'

print(weather)
print(item_to_take)

# La variable weather del código anterior almacena el clima actual, 
# mientras que item_to_take almacena el objeto que debemos ponernos o llevar con nosotros.
# El programa no funciona como debería: nos dice que no llevemos nada cuando el valor es 'lluvia' o 'sol'. 
# ¿Por qué pasa esto? Veamos cómo funciona el código anterior si el valor de weather es 'lluvia':

# 1. if weather == 'lluvia': establece item_to_take como 'paraguas' y esto es exactamente lo que queremos.
# 2. if weather == 'sol': no hace nada, ya que esta condición devuelve False.
# 3. if weather == 'nieve': devuelve False y, luego, dentro de la sentencia else, 'nada' se establece como valor de item_to_take.

# Podemos resolver este problema fácilmente utilizando la palabra clave elif. 
# Nos permite unir varias condiciones en una sola estructura: if-elif-else. 
# Vamos a reescribir nuestro código utilizando la declaración elif:

weather = 'lluvia'

if weather == 'lluvia':
    item_to_take = 'paraguas'
elif weather == 'sol':
    item_to_take = 'sombrero'
elif weather == 'nieve':
    item_to_take = 'gorro y bufanda'
else:
    item_to_take = 'nada'

print(weather)
print(item_to_take)

# Output: lluvia
#         paraguas

# ¡Ya está! Ahora el programa se ejecuta correctamente. 
# Confírmalo por tu cuenta reemplazando el código anterior con esta versión que contiene elif.
# El uso de la palabra clave elif nos permite agregar cualquier número de ramas. Sin embargo, 
# solo se ejecutará una rama: aquella cuya condición se cumpla primero. Todas las demás ramas serán ignoradas.
# Por eso es importante ordenar correctamente las ramas, con las condiciones más específicas primero 
# y las más generales al final. Al hacer esto, podemos asegurarnos de que el código se comporte como esperamos 
# y que se cubran todos los casos posibles.

# Condiciones con el bucle for
# En combinación con un bucle for, las sentencias condicionales se convierten en una herramienta indispensable para los especialistas en datos; 
# con ellas puedes comprobar cada elemento de la lista para una condición.
# Echa un vistazo a la lista years, que almacena los años de estreno de películas. 
# Mostraremos la década correspondiente a cada año. Para hacerlo, revisaremos varios rangos que cubren los años desde 1960 hasta 2009:

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

for year in years: 
    if 1960 <= year <= 1969: 
        print('La película se estrenó en la década de 1960.') 
    elif 1970 <= year <= 1979:
        print('La película se estrenó en la década de 1970.') 
    elif 1980 <= year <= 1989: 
        print('La película se estrenó en la década de 1980.') 
    elif 1990 <= year <= 1999: 
        print('La película se estrenó en la década de 1990.') 
    elif 2000 <= year <= 2009:
        print('La película se estrenó en la década de los 2000.') 
    else: 
        print('Tiempo no definido.')

# Así obtuvimos toda la información que necesitábamos sobre cada elemento de la lista.


# Ejercicio 1
# ¡Ahora inténtalo por tu cuenta!
#
# En el precódigo, tienes una lista de countries en la que se almacenan los países donde se estrenaron determinadas películas. Escribe un bucle for que itere sobre los elementos de la lista of countries y que imprima el mensaje correspondiente para cada uno de sus elementos:
#
# Para EE. UU., imprimamos 'The movie was released in the USA.'
# Para Francia: 'Le film est sorti en France.'
# Para Italia: 'Il film e stato rilasciato in Italia.'
# Para cualquier otro país: 'Country not defined.' ('País no definido.')

# - Para EE. UU., imprimamos 'The movie was released in the USA.'
# - Para Francia: 'Le film est sorti en France.'
# - Para Italia: 'Il film e stato rilasciato in Italia.'
# - Para cualquier otro país: 'Country not defined.' ('País no definido.')

countries = ['Francia', 'Italia', 'Nueva Zelanda', 'Italia', 'Francia', 'EE. UU.']
# empieza a escribir tu bucle for aquí
for value in countries:
    if value == 'EE. UU.':
        print('The movie was released in the USA.')
    elif value == 'Francia':
        print('Il film est sorti en France.')
    elif value == 'Italia':
        print('il film e stato rilasciato in Italia')
    else:
        print('Country not defined.')

# Resultado
# Le film est sorti en France.
# Il film e stato rilasciato in Italia.
# Country not defined.
# Il film e stato rilasciato in Italia.
# Le film est sorti en France.
# The movie was released in the USA.

# Ejercicio 2
# Las puntuaciones de las películas se almacenan en la variable ratings (puntuaciones). 
# Te pedimos que conviertas estas calificaciones de un sistema de 100 puntos a un sistema de 5 puntos. 
# Para ello, debes iterar sobre la lista original de ratings y utilizar sentencias condicionales para convertir 
# la escala original al sistema de 5 puntos siguiendo la siguiente lógica:

# - imprime 2 si la calificación original se encuentra en un intervalo de 0 a 59 puntos, ambos incluidos;
# - imprime 3 si la calificación original se encuentra en un intervalo de 60 a 72 puntos, ambos incluidos;
# - imprime 4 si la calificación original se encuentra en un intervalo de 73 a 84 puntos, ambos incluidos;
# - imprime 5 si la calificación original se encuentra en un intervalo de 85 a 100 puntos, ambos incluidos.

ratings = [91, 35, 65, 89, 78, 93]
# empieza a escribir tu bucle for aquí
for value in ratings:
    if 0 <= value <= 59:
        print(2)
    elif value >= 60 and value <= 72:
        print(3)
    elif value >= 73 and value <= 84:
        print(4)
    elif value >= 85 and value <= 100:
        print(5)
    else:
        print()

# En las próximas lecciones, te mostraremos cómo se pueden utilizar las sentencias condicionales para modificar y filtrar datos en tablas.
# Fin.