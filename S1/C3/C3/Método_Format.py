# El método format()
#
# De manera similar al método F-string, el método format() puede utilizarse como alternativa para obtener los mismos resultados. 
# Esta es la sintaxis:
#
# 1.-Define tu string como siempre, utilizando comillas.
# 2.-Dentro de las comillas, escribe tu string reemplazando la información dinámica solo con llaves.
# 3.-Llama al método format(), coloca en el string dinámico todas las variables involucradas en orden de aparición y separadas por comas. 
#    No olvides agregar . entre tu string y el método format().
#
# Este es nuestro primer ejemplo convertido al método format().
# message = "{} tiene {} años y mide {} cm" .format(name, age, height)
#
# Observa que las llaves están vacías, lo que quiere decir que las variables serán sustituidas en el orden en que aparezcan.
# Si quieres especificar qué variable sustituye a cada llave, también puedes hacerlo.
# Veamos cómo hacerlo en nuestro ejemplo:

name = 'Victoria'
age = 23
height = 157

message = "{n} tiene {a} años y mide {h} cm" .format(h=height, n=name, a=age)
print(message)

# Fin.