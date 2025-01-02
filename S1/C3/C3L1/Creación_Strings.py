# Capítulo 3.- Propiedades básicas de los Strings

# Creación de los strings

# Comencemos creando un objeto string en Python. 
# Puedes hacerlo colocando cualquier número de caracteres entre comillas, dobles o sencillas, y asignarle una variable:

my_string_1 = ' ¡String 1, string 2, string rojo, string azul! '
my_string_2 = ' ¡String 1, string 2, string rojo, string azul! '

print(my_string_1)
print(my_string_2)

# No importa si usamos comillas simples o dobles, ambos strings serán iguales. 
# Puedes utilizar esto a tu favor si utilizas comillas dobles para los strings que tienen apóstrofos.

# Mira el siguiente string 'Let's learn about strings!' (¡Aprendamos sobre los strings!). 
# Si colocamos este string en la función print() y ejecutamos este código, se producirá un error:

print('Let's learn about strings')

# El problema aquí es que Python no puede entender por qué hay 3 apóstrofos. 
# Como humanos entendemos qué está pasando ahí. Pero Python cree que falta un apóstrofo. 
# Para corregir el error, debemos escribir Let's learn about strings! entre comillas dobles:

print("Let's learn about strings!")

# Fin.