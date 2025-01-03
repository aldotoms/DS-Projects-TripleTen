# Comprobación de tipo y sugerencias de tipo

# Python es un lenguaje de tipado dinámico. En pocas palabras, el intérprete de Python no comprueba la validez de ninguna operación hasta que dicha operación se ejecuta. Python no sabe de antemano si una operación está permitida o no porque desconoce los tipos de datos de los valores hasta que los usa.

# Los siguientes ejemplos lo demuestran:

# subtract.py
def subtract(a=10, b='5'):
    return a - b
   
subtract()
print('Hola de parte de subtract.py')

# Como era de esperar, se ha producido un error porque no podemos restar una cadena de un número. Sin embargo, si solo definimos la función pero no la llamamos, el intérprete no tiene ningún problema:

# subtract.py
def subtract(a=10, b='5'):
    return a - b

print('Hola de parte de subtract.py')

# A diferencia de Python, los lenguajes de tipado estático (como Java o C++) tienen un comportamiento diferente: si hay un problema con los tipos de datos, el programa no compilará (es decir, no generará un archivo ejecutable), incluso antes de que este se ejecute.
# Cada paradigma tiene sus ventajas y desventajas. Si deseas obtener más información, consulta esta discusión en StackOverflow.


## Sugerencias de tipo

# Las sugerencias de tipo son una solución para indicar estáticamente el tipo de datos de un valor en nuestro código Python.
# Las podemos considerar como una forma de obtener algunas características (y beneficios) de un lenguaje de tipado estático en Python. Las sugerencias de tipo se especificaron en PEP 484 y se introdujeron en Python 3.5.

https://peps.python.org/pep-0484/

# Aquí tenemos un ejemplo de cómo se utilizan las sugerencias de tipo en nuestra función. Anotamos los argumentos y el valor de retorno:

def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

# La sintaxis text: str indica que el argumento text debe ser de tipo str. Del mismo modo, el argumento opcional sep también debe ser de tipo str (el valor por defecto es " "). Finalmente, la notación -> list especifica que list_of_words() devolverá una lista.

# En cuanto al estilo, PEP 8 recomienda lo siguiente:
https://peps.python.org/pep-0008/#other-recommendations

# utiliza las reglas normales para los dos puntos, es decir, ningún espacio antes y un espacio después de los dos puntos: texto: str.
# usa espacios alrededor del signo = al combinar una anotación de argumento con un valor predeterminado: sep: str = " ".
# usa espacios alrededor de la flecha >: def list_of_words(...) -> list.
# Ten en cuenta que añadir sugerencias de tipo a nuestras funciones no cambiará su comportamiento cuando las llamemos. Para el intérprete de Python, las sugerencias de tipo no cambian nada. Eso significa que las dos versiones de la función a continuación tendrán un comportamiento idéntico durante el tiempo de ejecución.

# Sin sugerencias de tipo:

def list_of_words(text, sep):
    return text.split(sep)

# Con sugerencias de tipo:

def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

# Veamos qué sucede cuando pasamos None al argumento opcional sep= cuando su sugerencia de tipo dice que debería ser str.

# list_of_words.py
def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

print(list_of_words("María tenía un pequeño cordero", sep=None))

# Aunque nuestra sugerencia de tipo dice que sep debería ser de tipo str, al intérprete no le importa que hayamos pasado None a sep.  Y como None es un argumento válido para el método split(), el programa se ejecuta sin errores.

# De ahí, podemos deducir que las sugerencias de tipo pueden ser útiles a los programadores y a las programadoras para saber qué es qué en su código, especialmente si se trata de equipos de desarrollo que trabajan en la misma base de código. Pero las sugerencias de tipo no cambian el comportamiento real del intérprete de Python.

# Comprobación de tipo
# Aunque el intérprete de Python no implementa las sugerencias de tipo, hay herramientas cuyo único propósito es realizar la comprobación de tipos. La más conocida es mypy.
https://mypy-lang.org/

# Podemos instalarla simplemente con pip:

pip install mypy

# ¡Y mypy nos dice exactamente qué falla en nuestro código!
# Ahora podemos arreglar el error:

# list_of_words.py
def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

list_of_words("María tenía un pequeño cordero", sep="a")
print("Hola de parte de list_of_words.py")

# Y volver a ejecutar mypy:

mypy list_of_words.py 

# ¡Ahora nuestro código se ve bien! Observa que mypy solamente revisó nuestro script en busca de incumplimientos de los tipos de datos, pero no lo ejecutó. Podemos decir esto porque no vemos ninguna salida de la sentencia print() en nuestro script.

# Pregunta
# Este es el resultado que verás en la Terminal al ejecutar python greetings.py:

# greetings.py
def greetings(name: int) -> str:
    return f"Hola {name}!"

print(greetings(10))

# R. Hola 10!
# Sí, exactamente así se verá la salida.

# FIN.