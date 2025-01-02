# Capítulo 2/6 · Faltan 3 lecciones
# Tipos de datos

## *Trabajar con fechas y horas

# La librería pandas es útil para mucho más que solo convertir strings y números. También puede manejar datos de fecha y horas.
# En esta lección, te mostraremos cómo sacarle el mayor provecho. Echa un vistazo al siguiente video y después vuelve aquí para aprender todo sobre esto.

# En el mundo se usan muchos formatos diferentes de fecha. Por ejemplo, se prefiere el orden día/mes/año en muchos países, de modo que el 8 de marzo de 2010 se escribe 08/03/2010. 
# Sin embargo, en Estados Unidos se usa principalmente el formato mes/día/año, así que 08/03/2010 sería el 3 de agosto.

# Excel puede comprender ambos formatos, pero tiene límites. Cuando cargas datos desde una base de datos, 
# puede que tengas valores como 2019-08-03Z17:25:00 y 03, Aug 19, 5:25 PM en el mismo archivo, y definitivamente Excel no podrá desenredar la madeja.
# Así que, cuando quieras asegurarte de que tus fechas y horas se hayan almacenado correctamente, o quieras hacer cálculos con ellas, deberás usar el formato datetime de Python.


## *Convertir a datetime

# Imagina que en nuestro conjunto de datos OnlineRetail.csv, el sitio web de la compañía no puede procesar algunas solicitudes de compra en horas pico.
# El equipo de infraestructura de la compañía puede configurar un proceso automatizado para agregar más servidores web virtualizados justo a tiempo para procesar más solicitudes. 
# Solo necesitan a alguien que les diga cuáles son las horas pico.
# Veamos si podemos ayudar.
# Cargaremos de nuevo el conjunto de datos y mostraremos algunas filas aleatorias.

import pandas as pd
df = pd.read_excel('Sprint 4_Data Wrangling (cont)\Online Retail.xlsx')
print(df.head())

# La columna 'InvoiceDate' contiene la fecha y hora de cuando se emitió la factura del pedido.
# De las lecciones anteriores, sabemos que la columna 'InvoiceDate' tiene el tipo de datos object.
# Vamos a corroborar esto mirando el atributo dtype:

print(df['InvoiceDate'].dtype)

# Por ahora, 'InvoiceDate' almacena sus valores como un tipo string. 
# Sin embargo, si queremos hacer cualquier tipo de operación de fecha u hora con esos valores, necesitamos convertirlos al tipo datetime. 
# Esto lo podemos lograr con el método to_datetime() de pandas.


# *Formatear valores datetime
# El método to_datetime() se usa para convertir fechas de un tipo de datos string al tipo de datos datetime. 
# Al llamar al método, debemos usar el parámetro format=, el cual toma un string especificando cómo se formatean las fechas. 
# Los códigos de formato señalados por el símbolo % se utilizan para especificar el formato.
# Por ejemplo, podemos convertir el string 2010-12-17T12:38:00Z (un formato ISO 8601) a objeto datetime pasando el string de formato correcto al parámetro format=: %Y-%m-%dT%H:%M:%SZ.

string_date = '2010-12-17T12:38:00Z'
datetime_date = pd.to_datetime(string_date, format='%Y-%m-%dT%H:%M:%SZ')

print(type(string_date))
print(type(datetime_date))
print(datetime_date)

# Después de llamar to_datetime() con nuestra fecha basada en strings y el string de formato, podemos tener ahora un objeto con el tipo de datos Timestamps. 
# El tipo Timestamp de pandas es equivalente al tipo datetime de Python, así que usaremos el término "datetime" para referirnos a ambas.
# Observa que el formato del objeto datetime es distinto al del string original: 2010-12-17T12:38:00Z. En el objeto datetime, tenemos YYYY-MM-DD HH:MM:SS: 2010-12-17 12:38:00. 
# Sin importar cómo se formateó el string original, el tipo datetime tendrá este formato uniforme.


## *Cómo funcionan los códigos de formato

# ¿Cómo sabíamos que el patrón de código para '2010-12-17T12:38:00Z' debía ser '%Y-%m-%dT%H:%M:%SZ'? Porque el código representa una generalización del string. 
# Cada elemento de fecha y hora se convierte en un símbolo que le dice a pandas cómo interpretarlo.
# Por ejemplo, %Y al inicio del patrón especifica que el valor de año ocurre en la ubicación de los strings en 'InvoiceDate'. 
# Los guiones, dos puntos y letras T y Z  en el string datetime se reproducen en el patrón de formato: "primero el año, luego un guion, el mes, luego otro guion, etc.".
# Hay muchos símbolos de formato, pero solamente unos cuantos los usarás con regularidad. Por ejemplo:

#   %d: día del mes (01 a 31).
#   %m: mes (01 a 12).
#   %Y: año en cuatro dígitos (2019).
#   %y: año en dos dígitos (19).
#   %H: hora en formato de 24 horas.
#   %I: hora en formato de 12 horas.
#   %M: minutos (00 a 59).
#   %S: segundos (00 a 59).

# Aquí (materiales en inglés) podrás encontrar una lista completa de todos los símbolos de formato datetime.
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior


## *Práctica
# ¡Vamos a hacer la prueba! Te daremos datetimes como strings y tú escribirás el string de formato correspondiente que debes usar para el argumento format= en to_datetime().
# Supón que estamos usando un horario de 24 horas.

# Pregunta
'20-12-2002Z04:31:00'
'%d-%m-%YZ%H:%M:%S'


## *Buscar objetos datetime
# Veamos ahora si nuestros datos cambian en cuanto a la apariencia y el tipo de datos tras usar to_datetime():

import pandas as pd
df = pd.read_excel('Sprint 4_Data Wrangling (cont)\Online Retail.xlsx')
df.info()
print(df.head())
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y/&m/&dT%H:%M:%SZ')

#¿Puedes ver que los valores mostrados se ven diferente que antes? Eso es porque ahora la columna 'InvoiceDate' es datetime. 
# Aunque los valores se vean diferentes, la información de los strings originales aún sigue ahí.
# Ahora, el tipo de datos de la columna datetime es un objeto datetime64[ns]. 
# Las letras [ns] se refieren al formato de tiempo basado en nanosegundos que especifica la precisión del objeto DateTime.

# Fin.