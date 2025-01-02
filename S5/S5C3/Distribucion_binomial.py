# Capítulo 3/5
# Teoría de la probabilidad

# *Trabajar con una distribución binomial*
# Calcular el número de k éxitos de n pruebas

# Como recordarás, tenemos que encontrar la manera de calcular de cuántas formas podemos obtener k éxitos de n pruebas sin necesidad de compilar una tabla con todos los resultados posibles. 
# Es posible con la ayuda de la siguiente fórmula:

P = n! / (k! * (n-k)!) * pk * q(n-k)
P = factorial(n) / (factorial(k) * factorial(n-k)) * p**k * q**(n-k)

# Si aplicamos esta fórmula al ejemplo de los clics en el banner, podemos considerar n como el número total de usuarios y k como el número de clics en el banner. 
# La fórmula nos ayudará a calcular de cuántas formas podemos seleccionar un grupo de k usuarios del total de n usuarios que hagan clic en el banner y no en otro enlace.
# Por ejemplo, el número de formas en que 7 de cada 10 usuarios harán clic en el banner es:

# Para encontrar el mismo resultado en Python podemos utilizar el código:

from math import factorial

c = factorial(10)/(factorial(7)*factorial(3))
print(c)

# Escribe el código para encontrar el número de formas en las que 90 de cada 100 usuarios hacen clic en el banner. Guarda el resultado en la variable c.
# Código

from math import factorial

c = factorial(100) / (factorial(90)*factorial(10)) # escribe tu código aquí

print(c)


# *Ejercicios*
# Ejercicio 1

# Los portátiles de Pineapple son caros, pero siguen siendo populares entre los geeks de la informática: 
# el 60% de los clientes están dispuestos a comprarse una computadora portátil de esta marca si acuden a la tienda. 
# Los portátiles de Banana son más baratos, pero no tan populares: solo el 20% de los visitantes de la tienda están dispuestos a comprarlos.
# Supongamos que la tienda solo tiene a la venta equipos de Pineapple. ¿Cuál es la probabilidad de que 50 de cada 80 clientes realicen una compra en un día?
# Guarda el resultado en la variable probability y muéstralo.
# No olvides que en Python se utiliza el signo ** para la exponenciación.

# Código
from math import factorial

p = 60/100 # la probabilidad de que un cliente realice una compra
q = 1 - p # la probabilidad de que un cliente NO realice una compra
n = 80 # el número total de visitantes
k = 50 # el número de visitantes que esperamos que realicen una compra

probability = factorial(n) / (factorial(k) * factorial(n-k)) * p**k * q**(n-k) # escribe aquí el código para realizar los cálculos

print(probability)


# Ejercicio 2
# Supongamos que, al lado de una tienda de hardware Pineapple, hay un gran centro comercial con otra tienda que vende computadoras Banana. 160 clientes visitan esa tienda durante el día. ¿Cuál es la probabilidad de que 50 de esos visitantes se compren una computadora portátil?
# Recuerda que solo el 20% de los usuarios están dispuestos a comprar un portátil de la marca Banana.
# Guarda el resultado en la variable probability y muéstralo.

# Código
from math import factorial

p = 20/100 # la probabilidad de que un cliente realice una compra
q = 1 - p # la probabilidad de que un cliente NO realice una compra
n = 160 # el número total de visitantes
k = 50 # el número de visitantes que esperamos que realicen una compra

probability = factorial(n) / (factorial(k) * factorial(n-k)) * p**k * q**(n-k) # escribe aquí el código para realizar los cálculos

print(probability)

# FIN.