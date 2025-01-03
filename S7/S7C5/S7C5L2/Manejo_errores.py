## Manejo de errores
# En esta lección cubriremos dos temas:

# Cómo manejar correctamente los errores.
# Excepciones que pueden ocurrir si un usuario, ya sea humano u otra aplicación, proporciona a nuestro programa unos valores de entrada inesperados.

# Errores
# Los programas de computadora no son tan flexibles como los humanos, si sucede algo inesperado, el flujo se interrumpe y se genera un error. En el primer sprint del programa ya hemos encontrado errores, por lo tanto, es momento de investigar más a fondo.

# Los mensajes de error (con suerte) nos muestran en qué parte de nuestro programa se detectó un error y cuál fue el problema. Volviendo a nuestro programa de rotación de imágenes anterior, imaginemos que cometemos un error al introducir el nombre de nuestro archivo de imagen, por ejemplo, tripleten_logo.jpe en lugar de tripleten_logo.jpeg:

# python image_rotator.py tripleten_logo.jpe --angle 180 output.png -i

# Como podemos ver, se lanza una excepción FileNotFoundError. En Python, hay un gran número de diferentes excepciones, o tipos de errores. Todas las excepciones pertenecen a la clase genérica Exception, pero cada tipo de excepción en concreto es un objeto único. Por ejemplo, el objeto FileNotFoundError es diferente del objeto TypeError que obtenemos cuando, digamos, sumamos una cadena a un número. Puedes visualizar todos los tipos diferentes de excepciones aquí.

https://docs.python.org/3/library/exceptions.html#Exception

# Si se está ejecutando un proceso computacional continuo o de gran envergadura, a nadie le gustaría que todo se bloqueara por un error tipográfico o de menor importancia. Detectar un error significa localizar el problema sin finalizar todo el programa. Además, la captura de errores puede ser útil a la hora de depurar el programa o hacerlo más fácil de usar, proporcionando sugerencias y soluciones.

# Try-except
# En el primer sprint, aprendimos cómo try-except puede ayudar a manejar errores. Para recapitular brevemente: la parte del código susceptible de error puede envolverse en un bloque try-except, que permite al código realizar una acción alternativa en lugar de detenerse al encontrar una excepción. Vamos a reemplazar la línea que abre un archivo con el siguiente código:

try:
    im = Image.open(args.input_file)

except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto:')

# En el bloque try, intentamos abrir un archivo con el nombre pasado a args.input_file. En el bloque except, queremos decirle a nuestro programa qué debe hacer si no puede encontrar un archivo con ese nombre, es decir, si Python lanza una excepción FileNotFoundError. Ten en cuenta que, aunque no tenemos que especificar el tipo de excepción que queremos capturar, se recomienda hacerlo siempre.

# Incluso si capturamos un error en nuestro código anterior, esto no resuelve el problema de qué hacer si el archivo no puede ser encontrado. Para mejorar la funcionalidad del programa, podemos pedirle al usuario o la usuaria que introduzca otro nombre de archivo usando la función input(). Esto le permite al usuario o la usuaria escribir la ruta a una imagen deseada desde el teclado, que luego se pasa a nuestro programa como una cadena:

try:
    im = Image.open(args.input_file)

except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto:')
    im = Image.open(input())

# Imaginemos que el archivo ha sido encontrado, pero no se carga correctamente debido a que está dañado o su tipo es incorrecto. Podemos capturar más de un tipo de excepción añadiendo varios bloques except. Vamos a utilizar el tipo genérico Exception para nuestro segundo bloque except:

try:
    im = Image.open(args.input_file)

except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto:')
    im = Image.open(input())

except Exception:
    print('Es probable que el archivo sea incorrecto, prueba con uno diferente:')
    im = Image.open(input())

# Además, podemos obtener un mensaje de error que Python mostraría si se permitiera que el código fallara. Con este fin, hay que utilizar un alias para nuestro tipo de excepción y luego imprimir ese alias en el bloque except. Echa un vistazo a la variable error_msg en el bloque Exception de abajo:

try:
    im = Image.open(args.input_file)

except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto:')
    im = Image.open(input())

except Exception as error_msg:
    print(error_msg)
    print('Es probable que el archivo sea incorrecto, prueba con uno diferente:')
    im = Image.open(input())


## Try-except-else-finally

# Las declaraciones try-except pueden ir aún más lejos. Podemos especificar qué ocurrirá en el caso de que no se encuentre ningún error (sentencia else) o al final del bloque try, pase lo que pase (sentencia finally). A menudo utilizamos finally para realizar ciertas tareas, por ejemplo, limpiar la memoria, finalizar las conexiones de red, etc.:

# image_rotator.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('angle', help='rotación deseada', type=int)
parser.add_argument( '-i', '--info', help='muestra el tamaño de la imagen', action='store_true')
args = parser.parse_args()

angle = args.angle

try:
    im = Image.open(args.input_file)
    
except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto:')
    im = Image.open(input())

except Exception:
    print('Archivo incorrecto, intenta con uno diferente:')
    im = Image.open(input())

else:
    print("Ejecución fluida'")

finally:
    rotated = im.rotate(angle)
    im.close() # cerrar el archivo de imagen, eliminándolo de la memoria
    rotated.save(args.output_file)

if args.info:
    print('dimensiones de la imagen de entrada:', im.size)


# Ten en cuenta que, en nuestro ejemplo, los mensajes de entrada pueden provocar nuevos errores, así que esta solución no es perfecta, pero demuestra cómo podemos hacer que nuestros programas sean flexibles gracias a un manejo creativo de los errores.

# Resumen

# Cuando se encuentra un error en Python, se lanza una excepción y se termina la ejecución del programa. Los bloques Try-except se usan para envolver sentencias susceptibles de error y detectar excepciones, es decir, para manejarlas con habilidad:

try:
    something

except FileNotFoundError:
    print('archivo no encontrado')
    do this

except Exception as error_msg:
    print(error_msg)
    do that

else:
    print('ejecución fluida')

finally:
    clean up

# Dependiendo de tu programa, pueden ocurrir todo tipo de errores en cualquier parte de tu código. Pero los ejemplos más comunes son los errores que se producen al abrir archivos, al comprobar o convertir tipos de datos y al gestionar las entradas del usuario. Nunca está de más implementar el manejo de errores en todo código que realiza estas tareas.


# Pregunta

# Supongamos que trabajamos en un script que espera tres argumentos:

# una ruta a una imagen de entrada;
# una ruta a una imagen de salida;
# un nuevo tamaño para una imagen.
# El script lee una imagen de entrada, la redimensiona al tamaño especificado y guarda la imagen resultante utilizando la ruta de salida proporcionada. Así es como se ve este script:

# resizer_2.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('new_size', help='tamaño de imagen', type=tuple)
args = parser.parse_args()

im = Image.open(args.input_file)
resized = im.resize(args.new_size)
resized.save(args.output_file)
im.close()

# Es hora de probar el manejo de errores. Necesitamos verificar si es posible abrir una imagen de entrada. Si no, queremos:

# 1. Imprimir un mensaje de error.
# 2. Luego imprimir "the default image is used" ("se usa la imagen predeterminada").
# 3. En su lugar, leer el archivo default_input.png.

# Como recordatorio, podemos usar except Exception ... para detectar cualquier error al envolver la parte Image.open().
# ¿Cómo deberíamos reescribir nuestro script para que haga exactamente lo que queremos?

# resizer_2.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('new_size', help='tamaño de imagen', type=tuple)
args = parser.parse_args()

try:
    im = Image.open(args.input_file)

except Exception as error_msg:
    print(error_msg)
    print('the default image is used')
    im = Image.open('default_input.png')

resized = im.resize(args.new_size)
resized.save(args.output_file)
im.close()

# ¡Definitivamente funcionará!

