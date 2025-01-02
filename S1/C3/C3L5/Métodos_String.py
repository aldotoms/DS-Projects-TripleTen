# MÉTODOS DE STRING
# En la lección anterior nos divertimos aprendiendo acerca del método format() 
# específico de los strings y cómo podemos llamarlo en objetos de string para resolver el problema de incorporar variables en nuestros strings. 
# Resulta que los strings vienen con muchísimos métodos, cada uno diseñado para procesar strings de manera diferente (qué genial, ¿no?).
#
# Al final de esta lección, podrás utilizar los siguientes métodos como parte de tu código:
# upper() convierte todos los caracteres a mayúsculas;
# lower() convierte todos los caracteres a minúsculas;
# replace() reemplaza partes de un string por otro string;
# strip() elimina los espacios al principio y al final del string.

# Estandarizar mayúsculas y minúsculas
# Python considera los strings 'Hola', 'hola' y 'HOLA' como valores diferentes.
# Como un paso importante de las fases de limpieza y procesamiento de datos de nuestro trabajo, 
# debemos estandarizar el uso de mayúsculas en nuestros strings, lo que quiere decir hacer todas las letras minúsculas o mayúsculas. 
# De esa forma, es mucho más fácil encontrar valores duplicados o agrupar datos de texto por categorías únicas.
#
# Tenemos dos métodos para lograr esto: upper() y lower().
# El método upper() convierte todas las letras en mayúsculas
# y el método lower() convierte todas las letras en minúsculas.
#
# Aquí hay un ejemplo para upper():

message = "¡Hola, me llamo Han Solo!"
print(message)
message_new = message.upper()
print(message_new)

# La salida esperada es esta:
# ¡Hola, me llamo Han Solo!
# ¡HOLA, ME LLAMO HAN SOLO!
#
# NOTA: El método lower() funciona de la misma manera que upper().

message = "¡Hola, me llamo Han Solo!"
print(message)
message_new = message.lower()
print(message_new)

# Fin.