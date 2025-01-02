# Capítulo 2/6
# Tipos de datos

## Un primer vistazo al conjunto de datos

# Para empezar, vamos a trabajar con una versión reducida del conjunto de datos de ventas minoristas online (materiales en inglés) del repositorio de machine learning de UCI:
https://archive.ics.uci.edu/dataset/352/online+retail

# NOTAS: Este es un conjunto de datos transnacional que contiene todas las transacciones que tuvieron lugar entre el 12/01/2010 y el 12/09/2011 en una tienda de ventas minoristas online con sede y registro en el Reino Unido. 
# La compañía vende principalmente regalos únicos para cualquier ocasión. Gran parte de la clientela se dedica a las ventas mayoristas.

# Información de atributos
#   InvoiceNo:  	Número de factura. Categórico/nominal, un número entero de 6 dígitos único asignado a cada transacción. Si este código comienza con la letra 'c', significa que hubo una cancelación.
#   StockCode:      Código de producto (artículo). Categórico/nominal, un número de 5 dígitos único asignado a cada producto.
#   Description:    Nombre del producto (artículo). Categórico/nominal.
#   Quantity:       La cantidad de cada producto (artículo) por transacción. Numérico.
#   InvoiceDate:    Fecha y hora de la factura. Numérico, el día y la hora en la que se generó cada transacción.
#   UnitPrice:      Precio unitario. Numérico, precio por unidad de cada producto en libras esterlinas.
#   CustomerID:     Número de cliente. Categórico/nominal, un número de 5 dígitos único asignado a cada cliente.
#   Country:       	Nombre del país. Categórico/nominal, el nombre del país donde reside cada cliente.

# Intentemos entender los datos que contiene este conjunto de datos.
# Primero, vamos a cargar el conjunto de datos y mostrar las primeras líneas:

import pandas as pd
df = pd.read_excel('Sprint 4_Data Wrangling (cont)\Online Retail.xlsx')
print(df.head())

# Pregunta
# Con base en la salida anterior, ¿qué tipo de datos esperarías de las columnas 'StockCode' 'Description' y 'UnitPrice'?
'StockCode'     # entero
'Description'   # strin
'UnitPrice'     # flotante

# Parece bastante claro que 'StockCode', 'Description' y 'UnitPrice' deberían contener valores de entero, string y flotante, respectivamente. Sin embargo, como dice el dicho, las apariencias engañan.
# Vamos a explorar los datos un poco más. Empezaremos por mostrar los valores mínimo y máximo de la columna 'StockCode':

print(df['StockCode'].min(), df['StockCode'].max())
# Devuelve: 10002 m     "según"

# Al mostrar las primeras filas, parece que 'StockCode' tiene un tipo de datos entero. Sin embargo, ahora vemos que su valor máximo es 'm', el cual, definitivamente, no es un entero.
# De hecho, la columna representa valores de ID, algunos de los cuales parecen enteros. Si miras otros valores en la columna, encontrarás algunos como '82494L', '84029G', '35004G' y otros.
# Después, quizá te hagas la siguiente pregunta: si 'StockCode' contiene valores de string, ¿cómo es posible que al llamar min() y max() se devuelvan valores en lugar de arrojar un error?
# Python es perfectamente capaz de comparar valores de string utilizando los operadores > y <. Sin embargo, las reglas para comparar strings son distintas de aquellas para comparar números. 
# El comportamiento de un operador depende de los tipos de datos y sus operandos.
# Dado los valores inesperados en la columna 'StockCode', probablemente será mejor que retrocedamos un poco y obtengamos más información sobre el conjunto de datos. 
# Vamos a utilizar el método info() para hacerlo.

df.info()

# Esto, en definitiva, confirma que 'StockCode' no es un entero.
# Aún más, nos gustaría señalar dos cosas más sobre los tipos de datos de nuestras columnas:
#   1. La columna 'Quantity' tiene un tipo de datos float64 en lugar de int64, incluso si se espera que los productos se vendan en cantidades parciales. 
#      Esto puede suceder si hay valores ausentes tal como NaN, que es un tipo de datos float, lo cual obliga a los enteros a convertirse también en flotantes. 
#      No es el caso de 'Quantity', ya que no tiene ningún valor ausente. 
#      Sin embargo, es importante destacar que convertir enteros en flotantes es una herramienta bastante común de los sistemas de exportación de datos, tal como convertir archivos de Excel a formato CSV.
#   2. La columna 'UnitPrice' tiene el tipo de datos object en vez de float64.
#      En la próxima lección, aprenderemos a lidiar con estas dos cosas (por ejemplo, convertir la columna 'Quantity' de float64 a int64 e identificar por qué pandas no logró detectar el tipo de datos correcto para la columna 'UnitPrice').

# Las claves de esta lección son:
#   - Al leer datos, no debemos asumir que Python asigna los tipos de datos que esperamos.
#   - Siempre es buena idea llamar a info() en tu DataFrame antes de lanzarte a hacer cálculos y modificaciones. Haz de esto una rutina.

# Fin.