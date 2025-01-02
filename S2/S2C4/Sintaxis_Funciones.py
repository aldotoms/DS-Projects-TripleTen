# Capítulo 4_Sp2
# 
# Capítulo 4/5 Funciones

# Introducción
# En este capítulo hablaremos de las funciones, que son básicamente pequeños programas utilizados para automatizar operaciones rutinarias. 
# En el capítulo anterior, mientras trabajabas con diccionarios, escribiste un código que convirtió una lista de clientes en un diccionario. 
# ¿Y qué pasa si quieres reutilizar este código cuando llegue una nueva solicitud? 
# Sería genial poder obtener resultados con un solo clic. Para eso están las funciones.
# Al final de este capítulo, podrás:

# - crear tus propias funciones;
# - optimizar el código para que puedas trabajar con grandes cantidades de datos;
# - entender cuáles son las diferencias entre las variables globales y las locales;
# - utilizar la palabra clave return para definir el valor devuelto por una función tras su ejecución.

# ¡Muchas cosas por aprender!
# Estudiar este capítulo te llevará entre 1.5 y 3 horas. ¡Buena suerte!

# Sintaxis de funciones
# Ya has escrito mucho código y, probablemente, ya has tenido que escribir las mismas cosas varias veces.
# Para crear un sistema que funcione eficazmente, los desarrolladores de software utilizan un enfoque modular, 
# escribiendo fragmentos de código que se pueden reutilizar para el mismo propósito en múltiples situaciones. 
# La función es una parte fundamental del código reutilizable. Incluso más que en matemáticas, 
# en Python una función es una forma de estandarizar y compartir tu código con otras personas. 
# Así es como los analistas de datos y los científicos pueden asegurarse de que su trabajo pueda ser utilizado en un sistema 
# de mayor alcance.

# SINTAXIS DE FUNCIONES
#
# Ya has escrito mucho código y, probablemente, ya has tenido que escribir las mismas cosas varias veces.
# Para crear un sistema que funcione eficazmente, los desarrolladores de software utilizan un enfoque modular, 
# escribiendo fragmentos de código que se pueden reutilizar para el mismo propósito en múltiples situaciones. 
# La función es una parte fundamental del código reutilizable. Incluso más que en matemáticas, 
# en Python una función es una forma de estandarizar y compartir tu código con otras personas. 
# Así es como los analistas de datos y los científicos pueden asegurarse de que su trabajo pueda ser utilizado 
# en un sistema de mayor alcance.

# Teoria
# Las funciones son como un robot de cocina
# Supongamos que estás haciendo un omelet por primera vez, siguiendo cada línea de una receta, 
# leyendo y llevándola a cabo paso a paso. Sin embargo, al cabo de un tiempo, si eres un programador 
# que come omelets todos los días, es posible que se te pase por la cabeza: 
# "¡Ah! ¡Quiero un robot de cocina para hacer omelets! Poner dentro los huevos y sacar un omelet hecho".


# Sintaxis de funciones
# Ahora que hemos hablado de lo que es una función, es hora de intentar construir una.
# 
# 1.- Primero viene el encabezado de la función.
#   - La palabra clave def se utiliza para especificar el nombre de la función.
#   - Los parámetros se especifican entre paréntesis.
#   - El encabezado termina con dos puntos.
# 2.- A continuación, se define el cuerpo espaciando cada instrucción en cuatro espacios. 
#   El cuerpo es el lugar donde se realizan las manipulaciones concretas que le pedimos a una función.
# 3.- La palabra clave return indica el valor que devolverá la función cuando esta haya hecho lo que se le pidió.


# Parámetros de una función
# Volvamos a nuestro robot de cocina y a los omelets. Para preparar uno, siempre hay que seguir unos pasos básicos. 
# Pero hay algunas cosas que puedes cambiar si quieres. Tu omelet se puede hacer con un número diferente de huevos, 
# con o sin queso. Poder modificar ciertos aspectos de las instrucciones resulta de gran ayuda.
# 
# En Python, el comportamiento de las funciones se controla con parámetros, que son variables que están disponibles dentro de las funciones. 
# Los parámetros son como los ajustes de una máquina que, al alterarse, influyen en el comportamiento de la función. 
# 
# Cuando Python ejecuta una función, reemplaza los parámetros por argumentos, que son valores concretos pasados a la función cuando es llamada. 
# Volviendo a nuestro robot de cocina para hacer omelets, este puede tener muchos parámetros, tales como el número de huevos a utilizar, añadir queso o no, etc.
# 
# Por ejemplo, si le dices al robot: "Hazme un omelet de dos huevos y sin queso", los parámetros de la máquina serán sustituidos por los argumentos: 
# dos huevos y sin queso.

# El resultado de una función puede asignarse a una variable como cualquier otro valor. 
# Para definir el resultado de una función, utiliza el comando return dentro de la misma. 
# El valor delante del comando return será el resultado que se devuelve cuando se llama a la función.
# Veamos el ejemplo que viene a continuación:

def omelet(eggs_number):
    result = '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    return result

# llamada a la función con 2 huevos, su resultado se asigna a la variable omelet_type
omelet_type = omelet(2)
print(omelet_type) # imprime el resultado de la instrucción anterior
print(omelet(3)) # imprime el resultado de una nueva llamada con 3 huevos

# Resultado
# ¡El omelet está listo! Huevos utilizados: 2
# ¡El omelet está listo! Huevos utilizados: 3

# Vamos a resumir:
#Los cuatro componentes principales de una función son:
#   1) el nombre de la función;
#   2) los parámetros que cambian el comportamiento de la función;
#   3) las instrucciones que se ejecutan cuando se llama a la función (también llamadas el cuerpo de la función);
#   4) el resultado que devuelve la función.


# Teoria
# La palabra clave return
# Si queremos que nuestra función devuelva un valor en lugar de imprimir cualquier cosa, debemos utilizar la palabra clave return.
# Cuando usamos la palabra clave return en una función, indicamos a la misma la salida que queremos que nos devuelva al ser llamada. 
# Por ejemplo, podemos escribir una función para realizar cálculos y el resultado de estos cálculos es lo que queremos devolver. 
# Esto es justamente lo que vimos en el cuestionario anterior cuando se utilizó la palabra clave return para devolver el valor elevado al cuadrado. 
# Aquí tenemos de nuevo la misma función:

def square(x):
    return x ** 2

# La palabra clave return es especial porque hace que la función finalice inmediatamente y devuelva el valor especificado a su invocador. 
# Esto significa que cualquier código posterior a la ejecución de un comando return no se ejecutará, ya que la función ya ha finalizado su trabajo. 
# Es importante tener esto en cuenta al escribir funciones, ya que cualquier código que quieras ejecutar después de la sentencia return debe colocarse antes de ella.

# Vamos a pasar a la siguiente lección, en la que aprenderás cómo las funciones pueden ayudarte a optimizar tu código y cómo se diseñan buenas funciones. 
# También tendrás la oportunidad de practicar escribiendo tus propias funciones.

# Fin.
