# EJERCICIO 1
#
# El departamento de seguridad del banco nos ha solicitado una lista con los nombres de nuestros primeros clientes.
# Actualmente, esta información está disponible como un string en el que todos los nombres están separados por comas 
# y que se almacena como la variable names.
# Para ayudar, vamos a convertir el string en una lista llamada names_split, 
# donde cada elemento representa el nombre de un cliente. No olvides mostrar la lista resultante.
# La salida esperada es esta:
# ['Jack Wilson', 'Nina Brown', 'Alex Smith', 'Brian Perez', 'David Martinez', 'John Kim']

names = 'Jack Wilson,Nina Brown,Alex Smith,Brian Perez,David Martinez,John Kim'
names_split = names.split(',') # escribe tu código aquí
print(names_split)

# Resumen
# En esta lección aprendiste algunas técnicas básicas de procesamiento de texto. 
# Con el método split() ahora puedes dividir un string en secciones más pequeñas y almacenarlas en una lista. 
# En cambio, si tienes una lista de strings, puedes unirlos en un solo string utilizando el método join().

# Recursos adicionales
# División de Python: https://www.w3schools.com/python/ref_string_split.asp
# Unión de Python: https://www.w3schools.com/python/ref_string_join.asp

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# Fin.