# Capítulo 3/5
# Aprender Python más a fondo

## Funciones: valores de retorno

# Ahora conocemos los parámetros obligatorios y opcionales (o predeterminados) de una función. Recuerda que el parámetro es lo que pasamos entre los paréntesis de una función cuando la creamos. 
# Los parámetros obligatorios deben pasarse para ejecutar una función, mientras que los opcionales, si no se pasan, serán sustituidos por valores por defecto.

# Devolución de resultados
# Habiendo terminado con los argumentos posicionales y clave, echemos un vistazo a cómo podemos mejorar nuestro uso de la palabra clave return. 
# Al final de esta lección, serás capaz de utilizar la palabra clave return para asignar la salida de una función con uno o más valores a una o más variables.
# Mira el video a continuación, ¡pero no olvides continuar leyendo para obtener una comprensión sólida de este tema!
# https://www.youtube.com/watch?time_continue=1&v=wq3ihqDHjRw&embeds_referring_euri=https%3A%2F%2Ftripleten.com%2F&embeds_referring_origin=https%3A%2F%2Ftripleten.com&source_ve_path=Mjg2NjY

# Finalización de la función
# La palabra clave return puede aparecer más de una vez dentro del cuerpo de una función, pero solo se ejecutará la primera llamada. 
# Tan pronto como Python ve esta palabra clave, termina la ejecución de la función y devuelve el resultado.
# Aquí estamos cascando huevos otra vez. Imagina que intentaras hacer un omelet sin huevos, ¿no sería una locura? Entonces necesitamos probarlo y devolver un mensaje diferente.
# Para ello, puedes tener distintas palabras clave return. Vamos a echar un vistazo:

# Código
def omelet(eggs_number=2):
    if eggs_number > 0:
        return '¡El omelet está listo! Huevos utilizados: ' + str(eggs_number)
    else:
        return '¿Cómo puedo hacer un omelet sin huevos?'
    print('Nunca podré mostrar el resultado :(')


print(omelet(3))
print(omelet(0))

# Si la función print va después de la sentencia if, nunca se ejecutará porque el código finalizará dentro del bloque if o dentro del bloque else. 
# El uso de return en diferentes partes de una función es una práctica común con la que te encontrarás a lo largo de tu vida laboral. 
# Por lo tanto, es importante asegurarse de que cualquier código escrito después de un bloque que tenga una sentencia return sea ejecutado.


## Múltiples resultados
# ¿Qué hacemos si queremos que una función devuelva más de un valor? Escribamos una función que tome dos lados de un rectángulo y calcule tanto el área como el perímetro:

def area_and_perim(side_1, side_2):
    area = side_1 * side_2
    perimeter = 2 * (side_1 + side_2)
    return area, perimeter

print(area_and_perim(2, 3))

# Aquí la palabra clave return va seguida por dos variables, por lo que la función devolverá ambos valores. En realidad, si quieres puedes devolver cualquier número de valores. 
# Lo único que hay que recordar es que las distintas variables que siguen a la palabra clave return deben ir separadas por comas.
# Técnicamente, una función siempre devuelve un valor. Cuando enumeramos varias variables después de return, la función las agrupa en una única estructura llamada tupla. 
# A partir de ahí podemos descomprimirlas asignando múltiples variables al resultado de la función (en este caso, dos variables):

# Código
def find_area_and_perim(side1, side2):
    area = side1 * side2
    perimeter = 2 * (side1 + side2)
    return area, perimeter

# descomprime el resultado de la función
rec_area, rec_perimeter = (find_area_and_perim(7, 3))

print(f'El área del rectángulo es {rec_area}, el perímetro es {rec_perimeter}')  

# Aquí asignamos la salida de la función a las variables globales rec_area y rec_perimeter. Ten en cuenta que el orden es importante. 
# La variable global rec_area va primera, así que toma el primer valor que viene después de return, que es el valor de la variable local area.
# Fíjate en que hemos evitado nombrar de la misma manera las variables locales y globales del área y del perímetro. 
# No se producirá ningún error si les das el mismo nombre (pruébalo por tu cuenta en el cuadro de código), pero esta práctica no es recomendable, ya que dificulta tanto la lectura del código como su depuración en caso de error.
# ¡Ha llegado la hora de la práctica!

# Pregunta
# Las funciones de Python pueden devolver:
# R. Cualquier número de valores.   ¡Correcto!

# ¡Y uno más, por favor!
# Pregunta
# Si quieres que una función devuelva varios resultados, tienes que enumerarlos después de la palabra clave return y separarlos con:
# R. Comas.     ¡Exactamente! Por ejemplo: return 'the', 'final', 'lesson'.  

# FIN.