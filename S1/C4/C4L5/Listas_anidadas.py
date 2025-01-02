# LISTAS ANIDADAS
#
# Las listas anidadas son, básicamente, listas dentro de listas donde el primer nivel de anidación corresponde a la lista principal, 
# cuyos elementos son listas independientes (sublistas). 
# Los elementos de estas sublistas son objetos más simples, como números o strings.
#
# Gracias a estas estructuras, puedes crear, almacenar y mostrar información organizada en Python, por ejemplo, tablas. 
# El hecho de almacenar información en forma de tabla puede facilitar y acelerar el análisis, así como mejorar los procesos de toma de decisiones. 
# Como especialista en datos, te encontrarás con tablas muy a menudo.
# Veamos un ejemplo concreto:

movies_info = [
            ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
            ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730]
]

print(movies_info)

# Puedes ver que tenemos una lista principal llamada movies_info.
# Dentro de ella, puedes ver 2 películas diferentes.
# Cada una de estas películas tiene su propia información en otra lista.
# Como resultado, se obtienen listas dentro de una lista: listas anidadas.
#
# Aunque la salida de la función print() puede ser difícil de leer a primera vista, debería quedar claro que hemos agrupado los elementos en sublistas.
# En otras palabras, la información de cada película está almacenada en su propia sublista y la de todas las películas en la lista principal.

# Recuperación de datos de una lista anidada
# Cuando una tabla se representa como una lista de listas, el primer índice indica una fila (o sea, una sublista concreta);
# y el segundo, una columna (es decir, un índice concreto de una sublista). 
# Podemos utilizar estas dos coordenadas para acceder a cualquier elemento individual.

example = [10,20,30,['a','b','c'],50]
print(example[3][1])
# 3 porque es donde está almacenada la segunda lista
# 1 porque es donde está almacenada 'b'

# Volvamos al ejemplo de las películas. Si queremos ver el primer elemento de la lista principal y también el último: 

print(movies_info[0]) # recuperamos la primera fila
print(movies_info[-1]) # recuperamos la última fila

# Ahora vamos a acceder a los elementos particulares de estas sublistas colocando el segundo índice entre corchetes:

print(movies_info[0][2]) # recuperamos el tercer valor (año) de la primera fila
print(movies_info[-1][0]) # recuperamos el primer valor (título) de la última fila

# La anidación puede llegar aún más lejos con listas de listas de listas. 
# Este tipo de estructura es muy común en la ciencia de datos. 
# Así es que es muy importante que entiendas cómo acceder a ellas.

# Fin.
