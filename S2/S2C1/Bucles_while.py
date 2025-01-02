# Capítulo 1/5 Bucles
# Bucles while
# 
# Teoría
# Hay varios tipos de bucles, incluidos los bucles for y while. 
# Cada tipo es útil para resolver diferentes problemas. 
# Como hemos visto, los bucles  for son excelentes cuando sabes de antemano que necesitarás ejecutar un conjunto de instrucciones una determinada cantidad de veces, 
# como la cantidad de elementos en una lista.
# Pero cuando no sabemos cuántas veces tendremos que repetir un fragmento de código, los bucles while vienen a ayudar. 
# Por ejemplo, esto puede resultar de gran utilidad:
# - Cuando un usuario rellena un formulario, podría haber un bucle que procese datos al tiempo que se van introduciendo. 
#   El bucle sigue iterando hasta que todos los datos se hayan ingresado correctamente.
# - Si una cámara web reacciona al movimiento, un bucle puede transmitir datos hasta que el movimiento se detenga.
#
# En los bucles while, la condición se comprueba antes de cada iteración. 
# Si esta condición es True, el algoritmo ejecuta las instrucciones dentro del cuerpo del bucle. 
# Una vez que la expresión lógica en la condición devuelva False, el bucle se detendrá.
#
# Veamos otro ejemplo. Un ascensor inteligente puede medir el peso total de las personas en su interior y compararlo con la capacidad del ascensor. 
# Cada vez que una nueva persona entra en el ascensor, el bucle while comprueba si se ha alcanzado el peso máximo.
#
# En este experimento, supondremos que el peso en kilogramos de cada nueva persona es un valor aleatorio de 30 a 120. 
# Los valores aleatorios pueden asignarse a las variables usando la función randint() de la librería random. 
# La función randint genera números enteros aleatorios dentro de un rango específico, por consiguiente declararemos el rango de 30 a 120 y simularemos el peso de una persona al azar. 
# Hablaremos de la generación de números aleatorios y las librerías con más detalle más adelante. 
# Por ahora, supongamos que podemos importar randint() desde la caja de herramientas random y usarla como herramienta para nuestras necesidades.
#
# Ejecuta el siguiente código y luego lo discutiremos en detalle.

# Los valores aleatorios pueden ser asignados a las variables utilizando la función randint() de la librería al azar 
# La función randint genera números enteros aleatorios dentro de un rango específico,
# por consiguiente declararemos el rango de 30 a 120 y simularemos el peso de una persona al azar.

from random import randint # importamos la función randint de la librería random

capacity = 400 # capacidad del ascensor en kg
total_weight = 0 # variable que almacena el peso total

while total_weight < capacity: # mientras que el peso total es menor que la capacidad máxima
    person_weight = randint(30, 120) # generamos un número aleatorio de 30 a 120
    total_weight += person_weight # el peso generado se añade a la impresión del peso total 
    print(f'Entra una persona. Carga del ascensor: {total_weight}')
    
print('¡Lo sentimos! El ascensor está lleno. Tendrás que esperar al siguiente.')

# Antes de cada paso, el bucle comprueba la variable total_weight. 
# Si está por debajo del límite de capacity, el bucle ejecutará las instrucciones de su cuerpo. 
# Luego volverá a la primera línea y comprobará de nuevo si el peso total es menor que la capacidad máxima. 
# Cuando se haya alcanzado o excedido el límite, el bucle se detendrá y se mostrará el texto que se encuentra fuera del cuerpo del bucle.
# 
# El signo < en el bucle while es un operador de comparación que comprueba si el valor de la derecha es mayor que el valor de la izquierda, al igual que el operador matemático. 
# En el contexto de un bucle while, se utiliza para comprobar si una determinada condición es True (verdadera) o False (falsa). 
# Si la condición es verdadera, se ejecutará el código dentro del bucle. Hablaremos más sobre estos operadores de comparación en el próximo capítulo.
#
# No sabemos cuántos pasos ejecutará el bucle. Eso depende de cuán rápido el peso total alcance el límite, pero cuando lo haga, el bucle finalizará.

# Uso de contadores
#
# while se puede utilizar con una variable de contador, que puede usarse para detener el bucle, 
# o puedes usar contadores simplemente para saber cuántas veces se repitió el bucle.
# Veamos de nuevo el ejemplo del ascensor, pero esta vez queremos evitar que más de 10 personas entren en el ascensor. 
# De nuevo, ejecuta el siguiente código y luego lo comentaremos.

num_people = 0 # comienza en 0 y no hay nadie dentro
capacity = 10 # variable que almacena el límite de personas

while num_people < capacity: # mientras que el número de personas es menor que la capacidad máxima
    num_people += 1 # una persona entra
    print(f'Entra una persona. Carga del ascensor: {num_people}')
    
print('¡Lo sentimos! El ascensor está lleno. Tendrás que esperar al siguiente.')

# Puedes ver que en cada iteración el código muestra la cantidad de personas en el ascensor. 
# El último número mostrado es 10. Después de eso, no se imprimen números, lo que significa que el bucle finalizó.
# Luego, vamos a ver cómo podemos determinar la cantidad de personas necesaria para que el ascensor alcance su carga máxima. 
# ¡Ejecútalo varias veces y verás la función randint() en acción!

from random import randint

capacity = 400 # capacidad del ascensor en kg
total_weight = 0 # variable que almacena el peso total
num_people= 0 # comienza en 0, no hay nadie dentro

while total_weight < capacity: # mientras que el peso total es menor que la capacidad máxima
    person_weight = randint(30, 120) # generamos un número aleatorio de 30 a 120
    total_weight += person_weight # el peso generado se agrega al peso total
    num_people += 1 # una persona entra
    print(f'Entra una persona. Carga del ascensor: {total_weight}')
    
print(f'¡Lo sentimos! El ascensor está lleno. Tendrás que esperar al siguiente. \nHay {num_people} personas dentro')


# Bucles infinitos
#
# Ten en cuenta que el uso de bucles while tiene un problema: si la comparación en el encabezado nunca devuelve False, se produce un bucle infinito. 
# Luego el cuerpo del bucle sigue ejecutándose:

sales = 1000 # establecemos el valor de sales en 1000

while sales > 100: # siempre que el valor en sales sea superior a 100,
    sales += 1 # incrementamos el valor de sales en 1
    print(sales) # y lo imprimimos

# La condición sales > 100 nunca devolverá False, por lo que terminamos con un contador descontrolado.

# Fin.