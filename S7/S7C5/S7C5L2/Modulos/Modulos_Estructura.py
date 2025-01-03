## Módulos y estructura del proyecto

# Imaginemos que eres un astrónomo o una astrónoma que escribe código en Python para analizar sus datos de observación. Después de meses de trabajo, empiezas a darte cuenta de que muchas veces utilizas el mismo código en tus scripts. Al principio, copiabas y pegabas de un script a otro, pero luego se te ocurrió que hay una solución mejor: ¡crear tu propio módulo! Así que colocaste todas las variables, funciones y clases que utilizabas con más frecuencia en un script y lo llamaste astro.py. Ahora, cuando analices un nuevo lote de datos, importa astro.py al principio de tu código, de la misma forma que importas Pandas. Entonces, tendrás todas las herramientas necesarias disponibles. Y aún mejor, ¡puedes compartir astro.py con todos tus colegas para facilitarles el trabajo!

# Librerías, paquetes y módulos
# El archivo teórico astro.py se llama módulo. A veces los términos librería, paquete, o módulo se usan de forma más o menos indistinta. Pero estrictamente hablando, los módulos son bloques de construcción más pequeños, o sea, archivos .py separados. Un paquete es un conjunto de varios módulos, y una librería puede significar lo mismo o incluso un conjunto más amplio de paquetes. Las librerías de gran utilidad generan comunidades, se amplían y establecen normas en los campos correspondientes. En este curso, dependemos en gran medida de pandas, que también es una librería/paquete.

# Agregar módulos es tan fácil como hacer clic en ladrillos LEGO. Python espera ver la extensión .py, por lo que se omite esta parte:

# myscript.py
import astro # importar nuestro módulo teórico

# Los módulos pueden mejorar considerablemente el conjunto de herramientas de nuestro programa sin necesidad de complicar demasiado nuestro código, permitiéndonos abordar tareas complejas con tan solo unas pocas líneas de código. Por ejemplo, ya has visto cómo la librería PILque hemos usado antes nos permite leer, girar y guardar una imagen sin sumergirnos en píxeles, bytes, etc.:

from PIL import Image

im = Image.open('myimage.png')
im.rotate(90)
im.save('output.png')

# Python fomenta la modularidad, y esta representa el nivel más alto en la arquitectura de programas. Para usar un módulo, simplemente hay que importarlo con import. Al importar un script este se ejecuta, y todos los objetos definidos en él quedan al alcance del entorno que lo importó:

# module.py
print("¡Hola! Soy un módulo")

# myscript.py
import module
print("Ejecutando el programa principal")

# En la práctica, los módulos no suelen mostrar ninguna salida cuando los importamos. En su lugar, nos proporcionan muchas variables, funciones y clases para que las utilicemos en nuestro código.

# Es importante señalar que, en el ejemplo anterior, myscript.py solo puede importar correctamente module si module.py se encuentra en el mismo directorio que myscript.py.


## Obtener nuevos paquetes

# Python viene instalado con muchos paquetes incorporados, pero es fácil descargar e instalar otros si es necesario. Hay un repositorio de paquetes online llamado PyPI. Si un paquete está listado allí, es posible instalarlo a través del administrador de paquetes integrado Pip ("PIP" significa "Paquetes de instalación de Pip").
# Para obtener e instalar una librería para el usuario actual, utiliza la siguiente plantilla de comando:
# pip install --user package_name

# Este es un ejemplo de cómo instalar la librería PIL que estuvimos usando:
# pip install --user Pillow


## Espacios de nombres

# Ahora descansemos y repasemos algunos fundamentos. Si en una parte de nuestro código asignamos una variable myvar = 123 y luego la usamos en otra parte, Python sabe de alguna manera a qué nos referimos. Eso se debe a que cada script en ejecución tiene su propio espacio de nombres, que es una especie de diccionario oculto donde podemos encontrar todos los objetos creados por el script y que son accesibles desde el alcance actual. Obviamente, al principio cada script individual no tiene ni idea del contenido de otros archivos. Importar módulos es como construir túneles para piezas de código adicionales. Los objetos (funciones, variables, etc.) que viven en el espacio de nombres de un módulo se denominan atributos.


## Maneras de importar cosas

# Cuando se importa un módulo, su espacio de nombres (junto con todos sus atributos) pasa a estar disponible. Para acceder a los atributos de un módulo, utilizamos la notación de puntos:

# module2.py

import re

def check_email(string: str):
    '''
    usa expresiones regulares para comprobar el formato de la dirección de correo electrónico
    el patrón es "algo@algo.algo"
    '''
    if re.match('[.\w]+@\w+[.]\w+', string):
        print('correcto')
    else:
        print('comprobar dirección de correo electrónico')

def check_age(age: int):
    if age >= 50:
        print('acceso permitido')
    else:
        print("eres demasiado joven")


# myscript2.py

import module2

email = input()

module2.check_email(email)


# En el ejemplo anterior, accedimos a la función check_email() desde module.py llamándola mediante la notación de puntos module.check_email(email).
# Si solo necesitamos un atributo y no queremos utilizar la larga notación module.attribute, podemos importar atributos individuales de un módulo:

# myscript.py

from module2 import check_email

email = input()
check_email(email)

# El peligro de importar atributos específicos reside en que pueden compartir su nombre con un objeto que ya existe en el espacio de nombres actual, o que se crearán más adelante en nuestro script. En este caso, esta última asignación anula la anterior, así que hay que tener cuidado.
# Si somos lo suficientemente valientes como para desempaquetar todos los atributos en nuestro espacio de nombres actual, usamos *:

# myscript4.py

from module2 import *

email = input()
check_email(email)

# Ten en cuenta que no queremos que ninguno de los nombres importados coincida con el nombre de otros objetos en nuestro programa. Es difícil saber los nombres de cada objeto que importamos, por eso recurrir a import * se considera a menudo una mala práctica en ingeniería de software.


## Comprobar if main

# Los scripts que escribimos suelen tener dos finalidades: o bien son el script principal que ejecuta el código de nuestro programa, o bien pueden importarse como módulo para que lo use otro script. Es posible que un script contenga algún código que necesitamos cuando se ejecuta como script principal de nuestro programa, pero que no queremos que se ejecute cuando se importa a otro lugar.

# Por ejemplo, digamos que astro.py contiene código que procesa y analiza un conjunto de datos, además de todas sus declaraciones de variables, funciones y clases. Cuando ejecutamos astro.py por sí mismo, queremos que el código ejecutado analice los datos. Pero cuando importamos astro.py en otro script, queremos que solo se ejecute el código responsable de crear variables y definir funciones y clases.

# Para asegurarnos de que ciertas partes del código de un módulo nunca se ejecuten al importarlo, debemos colocar ese código en un bloque especial if, donde comprobaremos si la variable __name__ tiene el valor '__main__'. Este bloque if a menudo se denomina punto de entrada. Aquí tienes un ejemplo sencillo:

# module_1.py

def useful_function():
    print('funcionando')

if __name__ == '__main__':
    print('probando función...')
    useful_function()

# Estarás pensando, ¿qué es esta variable __name__ y de dónde ha salido? Cada vez que ejecutamos un script, Python crea entre bastidores unas variables especiales, tanto para el script principal que ejecutamos, como para todos los módulos importados por el script principal. Una de estas variables es __name__. La variable __name__ del script principal que ejecutamos siempre tiene el valor de cadena '__main__', mientras que las variables __name__ de los módulos importados por el script principal tienen valores de cadena, que no son más que el nombre del módulo.

# Si ejecutamos el script module_1.py, del ejemplo anterior, desde la línea de comandos, ocurrirá lo siguiente:
# $ python module_1.py
# probando función...
# funcionando

# Vemos la salida del código en el bloque de punto de entrada porque module_1.py fue el script principal que ejecutamos con el comando python.
# Ahora vamos a escribir otro script, module_2.py:

# module_2.py

import module_1

def double_check():
    print('Ahora dos veces:')
    module_1.useful_function()
    module_1.useful_function()

if __name__ == "__main__":
    print("probando función...")
    double_check()

# Si ejecutamos module_2.py como nuestro script principal, entonces el valor __main__ de module_2.py será '__main__' y el valor __name__ de module_1.py será 'module_1':

# $ python module_2.py
# probando función...
# funcionando
# funcionando


## Importar, importar e importar

# Volviendo a la estructura del proyecto, podemos importar tantos módulos como queramos. Muchos de los módulos importados importarán a su vez otros módulos (por ejemplo, la librería Pandas importa de la librería Numpy). Es muy recomendable importar todos los módulos necesarios al principio del script. Primero vienen los paquetes incorporados de la librería estándar, luego los paquetes de terceros y, finalmente, los módulos locales (si los hay):

# myscript5.py

# paquetes incorporados
import math
import os

# paquetes de terceros
import pandas
import numpy

# mi propio módulo
import mymodule

# el resto del programa


## Pregunta 1
# Supongamos que tienes el siguiente módulo:

# my_module.py
import re
def email_check(string: str):
      '''
      Usa expresiones regulares para comprobar el formato de la dirección de correo electrónico:
      el patrón es "algo@algo.algo"
      '''
      if re.match('[.\w]+@\w+[.]\w+', string):
            print('correcto')
      else:
            print('dirección de correo electrónico incorrecta')

def age_check(age: int):
      '''
      Comprueba si la edad está por encima del valor umbral especificado
      '''
      if age >= 50:
            print('acceso permitido')
      else:
            print("eres demasiado joven")

# Respuesta:
import my_module
my_module.email_check('stewie@family.guy')
# ¡Correcto!


# Pregunta 2
# Supongamos que tienes el mismo módulo:

# my_module.py

import re

def email_check(string: str):
      '''
      Usa expresiones regulares para comprobar el formato de la dirección de correo electrónico:
      el patrón es "algo@algo.algo"
      '''
      if re.match('[.\w]+@\w+[.]\w+', string):
            print('correcto')
      else:
            print('dirección de correo electrónico incorrecta')

def age_check(age: int):
      '''
      Comprueba si la edad está por encima del valor umbral especificado
      '''
      if age >= 50:
            print('acceso permitido')
      else:
            print("eres demasiado joven")

# ¿Cuál de las siguientes opciones funcionará correctamente? Se supone que el módulo está ubicado en algún lugar donde el script actual pueda encontrarlo.
# Elige tantas como quieras

# Respuesta 1:
from my_module import email_check
email_check('stewie@family.guy')
# ¡Correcto!

# Respuesta 2:
from my_module import *
email_check('stewie@family.guy')
# Sí. De esta forma importamos todo desde my_module al espacio de nombres actual. Sin embargo, ¡ten mucho cuidado al hacerlo!

# Respuesta 3:
from my_module import email_check, age_check
email_check('stewie@family.guy')
# Sí.

# FIN.