# Capítulo 3/5 · Faltan 3 lecciones
# Teoría de la probabilidad

# *Trabajar con una distribución normal*

# En esta lección, exploraremos una de las distribuciones más fundamentales en estadística: la distribución normal, a menudo referida como la campana de Gauss.
# Esta distribución se manifiesta en diversas situaciones, desde representar la altura de la población hasta determinar las tasas de falla en equipos.
# Aunque existen otras distribuciones en el mundo real, la normal se destaca por su prevalencia y relevancia teórica.

# Centro y dispersión de una distribución normal
# Una distribución normal tiene dos parámetros clave: la media y la varianza

X ∼ (μ, σ^2)

# Esta notación se puede leer como: la variable X se distribuye normalmente con una media mu (μ) y una varianza sigma al cuadrado (σ²), es decir, una desviación estándar sigma.
# Para una distribución normal, el 68% de los puntos de datos se encuentran a una desviación estándar (σ) de la media, 
# el 95% a dos desviaciones estándar de la media y el 99,7 % a las tres primeras desviaciones estándar de la media. Este concepto se denomina regla de las 3 sigmas.

# A menudo, los parámetros de distribución son conocidos y necesitas encontrar la probabilidad de que ocurra un valor en un intervalo determinado.

# Pregunta
# Supongamos que el número de horas que los clientes pasan en el gimnasio cada semana sigue una distribución normal con una media de 4 y una desviación típica de 1. 
# ¿Qué porcentaje de clientes pasa más de 6 horas a la semana en el gimnasio?
# R. menos del 3%
# El valor "más de 6 horas" es de 2 sigma por encima de la media. Sabemos que el 95% de los valores están dentro del intervalo media +/- 2σ. 
# El 5% restante se distribuye uniformemente entre dos intervalos que están fuera del intervalo media +/- 2σ. 
# A nosotros solo nos interesa el primer intervalo, que contiene la mitad del 5% restante.

# La siguiente imagen interactiva muestra la distribución normal resultante. La media (1 000) está en el centro y las otras líneas verticales están espaciadas a intervalos de una desviación estándar. 
# Los porcentajes son las probabilidades asociadas a cada intervalo.
# Intenta cambiar los valores de la media (μ) y la desviación estándar (σ) para ver cómo se verá afectada la distribución normal.

# ¿Qué ocurre con los intervalos de probabilidad cuando σ aumenta? Como puedes ver, se amplían. 
# Una desviación estándar mayor indica un rango mayor en el que puede situarse un valor dado, es decir, será más difícil saber con certeza donde puede ubicarse.


# *Calcular probabilidades en datos normalmente distribuidos con Python*
# Python puede hacer los cálculos por nosotros. Para ello nos hacen falta métodos de la librería SciPy y su módulo intermedio stats.
# SciPy es una librería Python gratuita y de código abierto que se utiliza para la computación científica y técnica. 
# Contiene módulos para optimización, álgebra lineal, integración, procesamiento de señales e imágenes y muchos otros propósitos.
# En esta lección examinaremos la función stats.norm(), que genera una distribución normal con unos parámetros dados (media y desviación estándar). 
# También estudiaremos los métodos norm.cdf y norm.ppf, que permiten buscar respuestas a preguntas concretas.
# Veamos estos métodos con más detalle. Para ilustrarlo, consideremos el siguiente ejemplo: en la India, los estudiantes mayores de edad gastan una media de 5 000 dólares para aprender una nueva profesión, 
# con una desviación típica de 1 500 dólares.

# Nombre:       La función de distribución acumulativa
# Sintaxis:     norm.cdf()
# Explicación:  Da la probabilidad de que una variable aleatoria sea menor o igual que un valor determinado
# Ejemplo:      ¿Cuál es la probabilidad de que un estudiante pueda aprender una nueva profesión por menos de 4 000 dólares?

# Nombre:       La función de punto porcentual
# Sintaxis:     norm.ppf()
# Explicación:  Da el valor de la variable aleatoria que corresponde a una determinada probabilidad
# Ejemplo:      ¿Cuál es el coste máximo de la formación para el 10% de los estudiantes que gastaron menos dinero en sus estudios?

# Veamos cómo obtener respuestas a estas preguntas utilizando Python.

from scipy import stats as st       # importamos el módulo stats.

data = st.norm(5000, 1500)      # creamos un objeto con datos distribuidos normalmente con una media de 5 000 y una desviación estándar de 1500.
desired_cost = 4000     # creamos una variable para almacenar el coste deseado.
probability = data.cdf(desired_cost)    # calculamos la probabilidad de obtener el valor desired_cost.

print(probability)

# La probabilidad es superior al 25%. ¡Al menos es posible 😉!
# Y ahora, a por la segunda pregunta:

from scipy import stats as st       # otra vez empezamos con la importación y creación de la distribución.

data = st.norm(5000, 1500)
target_level = 0.1      # establecemos el valor de la probabilidad. Buscaremos el umbral del coste de los estudios para el 10% de los estudiantes que gastaron menos dinero.
cost = data.ppf(target_level)       # encontramos el importe que no supere los gastos del 10% de estudiantes que gastaron menos dinero.

print(cost)

# Ahora sabemos que ese 10% de estudiantes no gastaron más de 3 077 dólares en su formación. ¡Sí que saben ahorrar dinero!

# Pregunta
# La puntuación media en el examen del Certificado de análisis de datos es 1000 y la desviación estándar es 100. Hay que encontrar la probabilidad de obtener entre 900 y 1 100 puntos en el examen.
# ¿Qué código se debe utilizar para ello?

st.norm(1000, 100).cdf(1100) - st.norm(1000, 100).cdf(900)

# Para responder a la pregunta, tenemos que calcular la probabilidad de que el valor que buscamos sea inferior a 1 100 y restarle la probabilidad de que sea inferior a 900. 
# Esto es exactamente lo que hace este código.


# *Ejercicios*

# Ejercicio 1
# El número de visitantes mensuales de una tienda virtual tiene una distribución normal con una media de 100 500 y una desviación estándar de 3 500.
# Encuentra la probabilidad de que en el próximo mes el sitio web del outlet tenga:
#   - menos de 92 000 visitantes;
#   - más de 111 000 visitantes.
# Completa el código siguiendo los comentarios y utiliza las sentencias print() del precódigo para mostrar tus resultados.

# Código
from scipy import stats as st

mu = 100_500 # ¿cuál es la media de la distribución?
sigma = 3_500 # ¿cuál es la desviación estándar de la distribución?

more_threshold = 111_000 # ¿Cuál es el límite superior del número de visitantes?
fewer_threshold = 92_000 # ¿Cuál es el límite inferior del número de visitantes?

p_more_visitors = 1-st.norm(mu, sigma).cdf(more_threshold) # calcula la probabilidad de que el número de visitantes sea superior al umbral superior
p_fewer_visitors = st.norm(mu, sigma).cdf(fewer_threshold) # calcula la probabilidad de que el número de visitantes sea inferior al umbral inferior

print(f'Probabilidad de que el número de visitantes sea superior a {more_threshold}: {p_more_visitors}')
print(f'Probabilidad de que el número de visitantes sea inferior a {fewer_threshold}: {p_fewer_visitors}')

# ¡Exactamente! Este tipo de predicciones son muy importantes para los equipos de ventas y marketing.


# Ejercicio 2
# Otra tienda online, Fancy Pants, vende productos de regalo a un público muy limitado de clientes corporativos. 
# Las ventas semanales en la tienda de conjuntos de ajedrez de lujo fabricados con colmillo de mamut tienen una distribución normal con una media de 420 y una desviación estándar de 65.
# El equipo de inventario está decidiendo cuántos conjuntos pedir. Quieren que la posibilidad de venderlos todos la próxima semana sea del 90%. ¿Cuántos deben pedir?

# Código
from scipy import stats as st

mu = 420 # escribe tu código aquí: ¿cuál es la media?
sigma = 65 # escribe tu código aquí: ¿cuál es la desviación estándar?
prob = 0.9 # escribe tu código aquí: ¿cuál es la probabilidad requerida de vender todos los artículos?

n_shipment = st.norm(mu, sigma).ppf(1-prob) # escribe tu código aquí: ¿cuántos artículos se deben pedir?

print('Cantidad de artículos a pedir:', int(n_shipment))

# ¡Bien hecho! Por un lado, si compras demasiado inventario, el negocio puede fracasar. Por otro lado, si compras muy poco, no maximizarás los ingresos.


# Ejercicio 3
# Los precios de los pedidos realizados en una tienda virtual tienen una distribución normal con una media de 24 dólares y una desviación estándar de 3.20 dólares.
# Algunos clientes eligen la entrega rápida por mensajería, que tiene un precio fijo independientemente del valor del pedido.
# Los clientes tienden a molestarse cuando el costo de la entrega es igual al costo del pedido. 
# ¿Cuánto debería costar el envío por mensajería para que no supere el precio del pedido en el 75% de los casos?

# Código
from scipy import stats as st

mu = 24 # coloca tu código aquí: ¿cuál es la media de la distribución?
sigma = 3.20 # coloca tu código aquí: ¿cuál es la desviación estándar de la distribución?
threshold = 0.75 # coloca tu código aquí: ¿qué porcentaje de pedidos debería costar más del doble del costo de envío?

max_delivery_price = st.norm(mu, sigma).ppf(1-threshold) # coloca tu código aquí: el costo máximo de envío

print('Costo máximo de envío por mensajería:', max_delivery_price)

# ¡Ya está! Si la entrega cuesta 21.84 dólares, el 75% de los clientes estarán satisfechos.

# FIN.