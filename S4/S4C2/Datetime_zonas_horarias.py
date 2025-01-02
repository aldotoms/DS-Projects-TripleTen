# # Teoría
## *Trabajar con atributos datetime y zonas horarias

# Acceder a los atributos de columna datetime usando .dt

# Ya que pandas se basa en tipos de datos que son nativos de Python (así como algunos de distintas librerías), los tipos de datos pueden volverse un poco complicados a veces.
# Recuerda que en pandas, los objetos datetime están representados por el tipo de datos TimeStamp. 
# Para obtener, por ejemplo, el atributo year del primer valor Timestamp de la columna 'InvoiceDate', utiliza el siguiente código:

import pandas as pd
df = pd.read_csv('/datasets/OnlineRetail.csv')

# convierte 'InvoiceDate' a datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%Y-%m-%dT%H:%M:%SZ')

print(df['InvoiceDate'][0].year)    
# devuelve el año del primer InvoiceDate: 2010

# Si bien podemos acceder a todos los atributos de los valores individuales de Timestamp de esta manera, no podemos hacerlo para valores de Series Timestamp. 
# Mira lo que ocurre cuando intentamos obtener el atributo day para la columna 'InvoiceDate' entera:

df['day'] = df['InvoiceDate'].day

# Obtenemos un error porque df['InvoiceDate'] es un objeto Series, el cual no tiene un atributo day, a pesar de que sí lo tienen los valores individuales Timestamp dentro de Series.
# Para obtener atributos para todas las columnas de datos datetime, usa en su lugar el objeto accesor .dt.
# Por ejemplo, podemos crear un DataFrame 'df_days' que contenga el atributo day para cada valor en la columna 'InvoiceDate':

df_days = df['InvoiceDate'].dt.day
print(df_days.sample(5, random_state=42))

# ¡Ningún error esta vez! Recuerda que si quieres accesar los atributos de toda una columna de datos datetime, debes usar el accesor .dt de la columna datetime y no la propia columna.
# Existen muchos más atributos datetime (materiales en inglés) disponibles en pandas, así que utiliza los que necesites para el problema en cuestión.

https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components

# Hay algunos escenarios comunes que tienen que ver con las zonas horarias que te encontrarás al trabajar con datos datetime.
# Tus datos pueden venir de diferentes zonas geográficas en donde cada ubicación registra estos datos usando su hora local. 
# O puede que estés trabajando con valores datetime registrados en una zona horaria, pero necesites presentar los resultados de tu análisis a un público que esté en otra.
# En cualquier caso, debes saber cómo convertir entre distintas zonas horarias sin confundirte. Es ahí donde nos son útiles .dt.tz_localize() y .dt.tz_convert(). 
# El primero te permite asignar una zona horaria a una columna datetime para que tus datos "tengan conocimiento" de su zona horaria. 
# El segundo te permite convertir una columna "con conocimiento de su zona horaria" en una zona horaria distinta.
# Veamos cómo funciona en la práctica. Vamos a asignar el huso horario UTC a la columna 'InvoiceDate':

df['InvoiceDate'] = df['InvoiceDate'].dt.tz_localize('UTC')
print(df['InvoiceDate'].sample(5, random_state=42))

# ¿Notaste que ahora el dtype de la columna contiene información sobre el huso horario UTC?
# ¿Qué pasaría si necesitáramos mostrar datos a alguien en Nueva York que prefiere ver los valores datetime en su hora local?
# En este caso, pasaremos 'America/New_York' al método .dt.tz_convert():

df['InvoiceDate_NYC'] = df['InvoiceDate'].dt.tz_convert('America/New_York')
print(df['InvoiceDate_NYC'].sample(5, random_state=42))

# Ahora vemos dos cosas:
#   1. El dtype de la nueva columna 'InvoiceDate_NYC' ahora contiene la información America/New_York en vez de UTC.
#   2. Los valores datetime son diferentes. Difieren por 5 horas exactamente porque Nueva York, como en la mayor parte de Norteamérica, 
#      tiene el horario estándar del este (UTC-5) durante el invierno y el horario de verano del este (UTC-4) el resto del año.

# Este artículo de Wikipedia (materiales en inglés) contiene una lista con los nombres de cada zona horaria estándar que puedes usar con .dt.tz_convert().
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List

# Fin.