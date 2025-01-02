# Capítulo 2/5 Sentencias condicionales
# 
# Sentencias if y else
#
# Teoria
# En resumen, existen dos tipos principales de expresiones lógicas:
# - Expresiones que contienen operadores de comparación: ==, !=, >, <, >=, <=
# - Expresiones que contienen operadores lógicos: and, or, not
#
# Además de esto, también hemos aprendido sobre las funciones de predicado que se pueden aplicar a las cadenas. Estas son islower(), isdigit() y isalpha().
# Ahora que puedes reconocer e identificar expresiones lógicas que devuelven True o False, es hora de aprender sobre los operadores condicionales.
# Al final de esta lección podrás utilizar las sentencias if y else para crear ramas en tu código.
# ¿Recuerdas el ejemplo de la lección anterior? Esta es una versión más simple:
# 
# Una sentencia if es un operador condicional que permite ejecutar un bloque de código solo si cierta condición es verdadera; si la condición es falsa, se omitirá el bloque de código.
# Veamos cómo programar esta lógica en Python:
# Una sentencia condicional en Python contiene un encabezado y un cuerpo:

# - el encabezado contiene la condición (una expresión lógica);
# - el cuerpo contiene instrucciones (ramas de código) con una indentación de cuatro espacios.
# Si la expresión lógica devuelve True, la sentencia if ejecutará el código en el cuerpo de la condición.
# # Experimenta con el siguiente código cambiando el valor de la variable weather para ver cómo funciona.

# cambia el estado del clima para ver cómo afecta el condicional

weather = 'lluvia'

# condicional
if weather == 'lluvia':
    print('llevar paraguas')

print('¡vamos!')

# Como no está lloviendo, Python nos recomendó llevar un sombrero, ¡tal como se lo pedimos! Bien, ahora hazlo por tu cuenta.
# 
# Ejercicio
# Bien, ¡ahora vamos a escribir algo de código!
# Utiliza una sentencia condicional para comprobar la calificación de la película The Godfather, que se te facilita en el precódigo. Se almacena en la variable movie_rating.
# Si es mayor o igual a 8.5, muestra el mensaje 'High rating' ("calificación alta"). Si no, muestra 'Average rating' ("puntuación media").

movie_rating = 8.73 # Puntuación de The Godfather
if movie_rating >= 8.5:
    print('High rating')
else:
    print('Average rating') # escribe tu código aquí

# Teoria
# Comprobación de subcadena
# En Python, puedes utilizar el operador in para determinar si existe una subcadena dentro de una cadena más grande. 
# Esta es una herramienta increíblemente útil que se puede utilizar en múltiples contextos. 
# Por ejemplo, puedes utilizar este operador para comprobar si una determinada palabra aparece en una oración o 
# para identificar si una secuencia de caracteres específica está presente en un archivo de texto.
# Para utilizar este operador, simplemente escribe la subcadena que estás buscando, seguida del operador in, 
# seguido de la cadena más grande dentro de la cual deseas buscar. Si la subcadena está presente dentro de la cadena más grande, 
# el operador devolverá True; de lo contrario, devolverá False. 
# Dicen que "No hay yo en el equipo"; vamos a comprobarlo:

if "estoy" in "el equipo":
    print("Aquí estoy yo en el equipo.")
else:
    print("Es verdad, no hay yo en el equipo.")

# Es verdad, no hay yo en el equipo.
# Probemos de nuevo con un ejemplo más complicado. Esta es una cita conocida escrita por George Bernard Shaw, busquemos algo divertido en ella:

quote = "El progreso es imposible sin cambio y aquellos que no pueden cambiar de opinión no pueden cambiar nada."
if "ogres" in quote:
    print("Donde hay progreso, ¡hay queso!")
else:
    print("¡Aquí no, pequeño bromista!")

# Donde hay progreso, ¡hay queso!
# Con if y else podemos crear un algoritmo bidireccional. 
# Pero ¿qué pasa si queremos considerar más de dos posibilidades? Lo descubriremos en la próxima lección; por ahora, ¡vamos a practicar!

# Fin.