# Longitud del string.
# La longitud del string es igual al número de caracteres que tiene (observa que estamos contando caracteres, no palabras).
# Python tiene una función llamada len() que podemos usar para calcular fácilmente la longitud de cualquier string.
# Aquí está len() en acción:

name = "Stephen"
print(name)         # muestra el contenido del nombre
print()             # muestra una linea en blanco
print(len(name))    # muestra la longitud de name

# Como la palabra ‘Stephen’ tiene 7 caracteres, len(name) = 7
# Aumentemos ahora la complejidad:

sonnet = "Que la ruda mano del invierno no deshaga,\nEn ti el verano, antes tú debes ser destilado:\nEndulza algún pomo, en algún lugar atesórate\nCon el tesoro de la belleza antes que ella a sí se mate.\nNo es usura prohibida hacer pagar,\nA quien feliz paga por lo que debe;\nEso sería para ti engendrar otro tú,\nO diez veces más feliz, sea un diez por uno;\nDiez veces más feliz serás de lo que eres,\nSi diez de ti diez veces te figuran:\nPues, ¿qué podría hacer la muerte si partes,\nDejándote vivo, con descendencia?\nNo seas egoísta, tu belleza es mucha para conquista\nDe la muerte, que a los gusanos tus herederos haría."

print(sonnet)
print() # imprime una línea en blanco
print(len(sonnet))

# Con len(), podemos saber fácilmente que el soneto contiene 607 caracteres.
# Es importante tener en cuenta que los caracteres de escape y los espacios también cuentan como un carácter para la longitud del string:

string_1 = "HolaAdios"
string_2 = "Hola Adios"
string_3 = "Hola\nAdios"
print(len(string_1))
print(len(string_2))
print(len(string_3))

# Finalmente, debemos mencionar el string vacío: a menudo aparece como un marcador de posición para los valores ausentes en tablas y archivos de datos. 
# Este es un string especial con longitud cero que se puede crear utilizando comillas simples o dobles sin caracteres entre ellas:

print(len(''))
print(len(""))

# Fin.