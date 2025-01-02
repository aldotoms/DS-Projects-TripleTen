# Tipos de Datos y Cómo convertirlos

# Objetos y sus tipos
# Llamamos objeto a los datos almacenados en una variable. Cada objeto tiene un tipo de dato determinado.
# No tienes que identificar el tipo de dato cuando creas un objeto, Python lo hará por ti.
# Por ejemplo, supongamos que tenemos dos variables:

a = 2020
b = '1'
print(a + b)

# Tenemos un número entero y un string y no podemos sumarlos.
# Los tipos de datos más comunes incluyen strings, números enteros ("integers"), números de punto flotante ("float") 
# y valores booleanos (verdadero/falso)
# Los enteros y los flotantes son tipos de datos numericos, mientras que los strings son tipos de datos de texto.

# Aplicación: datos de idiomas
# Utilicemos la tabla de datos de idiomas para explorar las operaciones permitidas para los cuatro tipos de datos principales. 
# La tabla es la siguiente:

# La columna "Mayoría de hablantes nativos" indica si la proporción de hablantes nativos supera a la de hablantes no nativos de este idioma. 
# Python tiene la función type() que se utiliza para determinar el tipo de dato.

language = 'Chino'
website_share = 0.017
native_speakers = 908.7
total_Speakers = 1107
majority_native = True

print(type(language))           # language: string (str).
print(type(website_share))      # website_share y native_speakers: números de punto flotante (float).
print(type(native_speakers))
print(type(total_Speakers))     # total_speakers: número entero (int).
print(type(majority_native))    # majority_native: booleano (bool).