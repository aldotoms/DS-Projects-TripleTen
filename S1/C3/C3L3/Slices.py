# SLICES
#
# “Slicing”te permite extraer una parte de un string, en lugar de utilizar todo el contenido o un solo carácter. 
# Además, es más rápido y eficiente.
# 
# Para segmentar un string, se utiliza la indexación para especificar el rango que se desea del string.
# En otras palabras, debes indicar el punto de inicio y el punto final (índices) dentro de un par de corchetes 
# y separarlos mediante dos puntos, de este modo:

city = 'Río de Janeiro, Brasil'
substring = city[7:14]
print(substring)    # El extracto es "Janeiro"

# Observa que al segmentar la variable city, no se devolvió el carácter en el índice 14.
# Esto se debe a que, al segmentar, el intérprete de Python deja fuera el último índice por defecto. 
# Además, no olvides que los índices comienzan en 0.

# Así que, no olvides:
# "el número de caracteres que se muestran al segmentar un string será siempre igual al índice final menos el índice inicial"

# Algo que debemos recordar de la última lección es que indexar un string fuera de su rango arroja un error. 
# Ahora bien, con la segmentación, el rango puede exceder la longitud del string sin producir un error,
# ya que Python ignora los valores de índice que no están dentro del rango real.
# Veamos algunos ejemplos:

city = 'Rio de Janeiro, Brasil'

print(city[4:1000])     # El substring city[4:1000] contendrá los caracteres desde el índice 4 hasta el final del string.
print(city[-15:500])    # city[-15:500] contendrá el substring, comenzando en J, que tiene el índice 15, hasta el final del string.
print(city[4:0])        # En el caso de city[4:0], dado que el primer índice es mayor que el segundo, el slice devolverá un string vacío.

# Finalmente, para segmentar un substring comenzando desde el primer carácter, o hasta el final, 
# puedes dejar el índice de este modo:

city = 'Rio de Janeiro, Brazil'
print(city[:14])  # en lugar de city[0:14]
print(city[16:])  # en lugar de city[16:22]

# Fin.