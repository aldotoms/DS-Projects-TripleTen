# PRÁCTICA GUIADA
#
# Ahora es tu turno de practicar con los F-strings. 
# Ordena las variables en el siguiente código y despliega el mensaje Hace cinco años, Olivia tenía 20 años.
#
# Observa que la variable age almacena 25 como valor, pero en el string anterior que te pedimos mostrar se lee 20. 
# Usa una operación aritmética dentro del F-string para calcular la edad.
#
# La salida esperada es esta: 
# Hace cinco años, Olivia tenía 20 años

name = 'Olivia'
age = 25

# completa el siguiente código
message = f"Hace cinco años, {name} tenía {age-5} años"
print(message)

# Ahora practiquemos utilizando el método format() para mostrar el siguiente mensaje:
# La salida esperada es esta:
# Olivia tiene 25 años

name = 'Olivia'
age = 25

# crea un string formateado más adelante
message = "{n} tiene {a} años".format(a=age, n=name)
print(message)

# Fin.