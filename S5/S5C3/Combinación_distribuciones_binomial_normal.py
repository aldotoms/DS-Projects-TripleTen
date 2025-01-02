# Capítulo 3/5 · Faltan 2 lecciones
# Teoría de la probabilidad

# *Combinación de las distribuciones binomial y normal*

# Valor esperado
# Digamos que tenemos una variable aleatoria. Puede tomar ciertos valores y cada valor tiene una probabilidad asociada. 
# El valor esperado de la variable aleatoria es el valor "típico" que asociamos con esta variable aleatoria. Para encontrar este valor, 
# necesitamos repetir el experimento muchas veces para aproximar las probabilidades de cada valor y, luego, encontrar el promedio ponderado.
# Un experimento binomial consta de n pruebas de un ensayo simple (de Bernoulli) con dos resultados. 
# Si el número de pruebas es lo suficientemente alto, la distribución binomial se puede modelar mediante la distribución normal. En esta lección, te mostraremos cómo funciona.

# Ejemplos de valor esperado
# Te presentamos a Archie. Archie es un ingeniero de software y escribe 50 fragmentos de código cada día. Una de cada cinco veces, el fragmento se ejecuta perfectamente a la primera (p = 0.2).
# Esto significa que todos los días Archie ejecuta un experimento binomial. 
# Para un experimento binomial, el valor esperado puede calcularse multiplicando el número de intentos (n) por la probabilidad de éxito (p), o n ⋅ p. En nuestro caso, será 50 ⋅ 0.2 = 10. 
# En cuanto a la varianza, para una distribución binomial, puede calcularse como n ⋅ p ⋅ (1 − p). Utilizando esta fórmula, obtenemos 50 ⋅ 0.2 ⋅ 0.8 = 8 (es decir, con un desviación estándar de √8 = 2√2).)
# ¡Esto no significa que escriba 10 fragmentos de código perfectos todos los días! Un día, podría estar cansado y escribir solo cinco; otro día, podría sentirse genial y escribir 15.
# Pero con el tiempo, el número promedio diario se aproximará a diez y alrededor del 99% de los valores estarán dentro de 10 ± 3 ⋅ 2√2. 
# En un día cualquiera, puede esperar que entre 2 y 18 fragmentos se ejecuten perfectamente en el primer intento.

# Pregunta
# Para acceder al tablón de anuncios para especialistas en estadística, los usuarios y las usuarias deben superar un examen de acceso. Es difícil y solo el 5% lo aprueba. 
# Además, solo 100 usuarios al día pueden realizar el examen y hay una lista de espera con 1000 nombres.
# Los moderadores están estudiando cómo llegan nuevos usuarios. Quieren modelar la afluencia como un experimento binomial.
# ¿Qué parámetros deberían usar?
# R. p = 0.05, n = 100
# Cien personas participaron en un experimento con dos resultados posibles: aprobar o suspender el examen. Esto significa que n = 100, y la probabilidad de éxito es del 5%, o 0.05. 
# (Nota: la lista de espera es irrelevante).


# *Aproximación normal a la distribución binomial*
# Si hay 50 intentos o más, los resultados de un experimento binomial pueden mostrarse como datos con una distribución normal. 
# Combinar dos tipos de distribuciones de probabilidad tan diferentes puede parecer confuso, así que veamos esta idea con más detalle. 
# Consideremos una distribución binomial con n = 50 y p = 0.8. Al aplicar la fórmula para la probabilidad de obtener k éxitos de n pruebas, obtendremos los siguientes resultados:
#   - La probabilidad de obtener 30 éxitos de 50 pruebas es de 0.0006.
#   - La probabilidad de obtener 35 éxitos de 50 pruebas es de 0.0299.
#   - La probabilidad de obtener 40 éxitos de 50 pruebas es de 0.1398.
#   - La probabilidad de obtener 45 éxitos de 50 pruebas es de 0.0295.
# Si calculamos los resultados para cada número de éxitos y creamos un gráfico basado en ellos, obtendremos un gráfico muy parecido a la curva de distribución normal.

# ¿Por qué es útil? Porque la distribución normal tiene características útiles y predecibles, como la regla de las tres sigmas.

# Ejemplo
# Una empresa ha decidido anunciarse online. El servicio de publicidad dice que, de promedio, el 15% de los usuarios hacen clic en sus anuncios. Eso es 750 visitas por cada 5000 vistas.
# La empresa coloca anuncios, compra 5000 impresiones (vistas) y solo obtiene 715 visitas. ¡El equipo de marketing está disgustado! ¿No les habían prometido 750 visitas? 
# Usaremos argumentos estadísticos para calmarlos.
# En resumen: cuando un usuario ve el anuncio, hay un 15% de posibilidades de que haga clic en él. Esto nos da una distribución binomial con n = 5000 y p = 0.15.
# Utilizaremos la distribución normal para aproximar la distribución binomial y calcular la probabilidad de obtener 715 clics o menos.
# Piensa: tenemos nuestro valor del eje X y queremos la probabilidad de obtener ese número o menos. ¿Qué método necesitamos?
# ¿Ya lo tienes? Necesitamos norm.cdf():

# importamos las librerías necesarias
from scipy import stats as st
import math as mt

# establecemos los valores de los parámetros
binom_n = 5000
binom_p = 0.15
clicks = 715

# calculamos el valor esperado de éxitos y sigma
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

# calculamos la probabilidad de obtener 715 visitas o menos
p_clicks = st.norm(mu, sigma).cdf(clicks)
print(p_clicks)

# La probabilidad de conseguir 715 visitas en lugar de 750 no es muy alta, alrededor del 8.3%. Sin embargo, no es lo suficientemente pequeña como para que este evento casi nunca suceda.
# Teniendo en cuenta esta probabilidad, podemos afirmar que por cada 100 empresas que pusieron anuncios con el servicio de publicidad, ocho recibirán 715 clics o menos. 
# Resulta que este no es un evento raro en absoluto y que la queja del equipo de marketing no es razonable.


# *Ejercicios*
# Ejercicio 1
# Una empresa envía a sus clientes un boletín electrónico mensual con novedades y ofertas de los socios. Sabemos que el 40% de los clientes abre el boletín.
# Uno de los socios está planeando una campaña publicitaria y espera llegar a unos 9000 clientes. 
# Calcula la probabilidad de que se cumplan las expectativas del socio si el boletín se envía a 23 000 personas.
# En el ejemplo anterior, hemos creado una variable llamada clicks. Aquí, crea otra llamada threshold y guarda el valor 9000 en ella. 
# Que el tamaño de la población sea binom_n y que la probabilidad de que se abra el boletín sea binom_p.
# Guarda la probabilidad de que se cumplan las expectativas del socio como p_threshold y muéstrala.

# Código
from scipy import stats as st
import math as mt

# establecemos los valores de los parámetros
binom_n = 23_000
binom_p = 0.40
threshold = 9_000

# calculamos el valor esperado de éxitos y sigma
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

# calculamos la probabilidad de llegar a 9,000 clientes o menos
p_threshold = 1-st.norm(mu, sigma).cdf(threshold)
print(p_threshold)

# Parece que el socio ha tomado la decisión correcta.

# FIN.