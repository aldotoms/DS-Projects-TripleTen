# Capítulo 4/6 · Faltan 3 lecciones
# Trabajar con valores duplicados y ausentes

# Rellenar los valores ausentes cuantitativos

# ¡Todo nuestro trabajo ha dado sus frutos! 
# Al lidiar con los valores ausentes en el conjunto de datos de la fuente de tráfico, hemos determinado que los correos electrónicos tienen la tasa de conversión más alta, 
# mientras que los anuncios contextuales no dan tan buenos resultados. Podríamos terminar nuestro análisis aquí, pero aún no hemos llegado al fondo de la cuestión.
# Además de los datos sobre las fuentes de tráfico, Google Analytics proporciona información resumida sobre los usuarios que visitan el sitio de comercio electrónico (e-commerce). 
# Por suerte, la empresa nos ha enviado otro conjunto de datos que contiene esta información de análisis web.
# En esta lección usarás este conjunto de datos para aprender a tratar los datos cuantitativos ausentes, 
# con el objetivo de comparar el tiempo promedio que pasan en el sitio web los usuarios y las usuarias de dispositivos móviles y de escritorio.
# Hemos guardado el archivo en la carpeta /datasets con el nombre web_analytics_data.csv. Carga los datos en la variable analytics_data e imprime las 10 primeras líneas.

# Código:

# escribe tu código aquí
import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

print(analytics_data.head(10))
print()
analytics_data.info()

# Resultado:

      user_id device_type   age    time
0  7141786820     desktop  33.0  2127.0
1  5644686960      mobile  30.0    35.0
2  1914055396     desktop  25.0     NaN
3  4099355752     desktop  25.0  2123.0
4  6032477554     desktop  27.0    59.0
5  5872473344      mobile  27.0     NaN
6  7977025176      mobile   NaN     NaN
7  3512872755     desktop  40.0    65.0
8  1827368713     desktop  37.0     NaN
9  8688870165     desktop  36.0  2124.0

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100000 entries, 0 to 99999
Data columns (total 4 columns):
 #   Column       Non-Null Count   Dtype  
---  ------       --------------   -----  
 0   user_id      100000 non-null  int64  
 1   device_type  100000 non-null  object 
 2   age          94228 non-null   float64
 3   time         75411 non-null   float64
dtypes: float64(2), int64(1), object(1)
memory usage: 3.1+ MB

# Al igual que el conjunto de datos de la fuente de tráfico con la que trabajaste anteriormente, cada fila de este conjunto de datos corresponde a una visita al sitio web. Para cada visita, tenemos:
#   - 'user_id': identifica de forma única a cada visitante del sitio web (Id de usuario);
#   - 'device_type': tipo de dispositivo utilizado para acceder al sitio web;
#   - 'age': edad (en años) de las personas que visitan el sitio;
#   - 'time': periodo de tiempo, en segundos, que las personas pasan en el sitio web.

# Pregunta
# ¿Qué columnas de este conjunto de datos de análisis web son variables cuantitativas?
# R. 'age'  ¡'age' es sin duda una columna cuantitativa! & 'time' ¡Estamos de acuerdo! Podemos decir que la columna 'time' es una variable cuantitativa.

# Así es, 'age' y 'time' son cuantitativas, mientras que 'user_id' y 'device_type' son categóricas.
# Puedes estar pensando, "¡pero la columna 'user_id' contiene números!". 
# Es verdad, y si llamaste a info() en el DataFrame, hallarías que 'user_id' es un tipo de datos enteros (te recomendamos que hagas esto en el sandbox, 
# incluso cuando llamar a info() no sea parte de la tarea). Pero recuerda que los ID son categóricos, no cuantitativos. Es importante tener en mente estas propiedades de los datos al realizar el análisis.
# Además, observa que especificamos unidades para las variables cuantitativas (años y segundos). Es importante que siempre tengas en cuenta las unidades cuando trabajes con datos cuantitativos. 
# Claro, probablemente sea obvio que la columna 'age' está en años, pero es posible que no sea tan obvio que la columna 'time' está en segundos. Cualquiera que sea el caso, es mejor no asumir.
# Ahora volvamos a los valores ausentes. En las primeras 10 filas podemos ver que tanto 'age' como 'time' tienen valores NaN. 
# Debido a que queremos hacer cálculos numéricos con estas columnas, no podemos rellenar esos valores con cadenas como 'Unknown' o ''. 
# En su lugar, debemos rellenarlos con valores representativos apropiados. Para estos valores se suele utilizar la media o la mediana del conjunto de datos.
# Recuerda que la media es la suma de todos los valores dividida entre el número total de valores y la mediana es el valor que se encuentra en el centro cuando los valores se ordenan.


# *Cuándo usar la media o la mediana

# Si conocemos tanto la media como la mediana, ¿cómo vamos a elegir cuál de ellas utilizar como valor representativo? 
# Bueno, depende de cuál sea más representativo de un valor "típico" para nuestro conjunto de datos.
# La media no es un buen valor típico cuando los datos con los que se trabaja tienen valores atípicos importantes. 
# Por ejemplo, supongamos que cinco empleados de una empresa tienen sueldos de 30 000 dólares. Tanto la media como la mediana son iguales a 30 000 dólares.
# Entonces se contrata a un director de marketing con un sueldo de 90 000 dólares. La media ha subido a 40 000 dólares, mientras que la mediana sigue siendo de 30 000 dólares.
# Este valor atípico hace que la mediana sea un mejor indicador del salario típico que la media.

# Resumiendo
# Para decidir si la media o la mediana es un valor más representativo, podemos seguir estos pasos:
#   1. Determina si los datos tienen valores atípicos significativos.
#   2. Si no hay valores atípicos significativos, calcula la media utilizando el método mean().
#   3. Si tus datos tienen valores atípicos significativos, calcula la mediana utilizando el método median().
#   4. Reemplaza los valores ausentes con la media o la mediana utilizando el método fillna().

# También vale la pena señalar que a veces no necesitamos rellenar los valores ausentes en absoluto.  
# Por ejemplo, si solo falta una pequeña parte de tus datos, y los datos ausentes son aleatorios, podría ser buena idea dejar los valores como NaN, 
# en cuyo caso simplemente no se incluirían en ningún cálculo numérico.
# Podremos analizar los datos de los usuarios web para encontrar factores distintos de las fuentes de tráfico que influyen en las decisiones de compra. 
# Pero para ello, primero tendremos que rellenar los valores ausentes en las columnas 'age' y 'time'.


# *Comprobar los valores atípicos

# Antes de que comiences a rellenar los valores cuantitativos ausentes, siempre debes comprobar si hay valores atípicos. 
# Pero por ahora, te ahorraremos los pasos adicionales, ya que no hay valores atípicos importantes en nuestro conjunto de datos de marketing.

# Pregunta: Teniendo en cuenta la información anterior, ¿cuál puede ser el valor representativo de los datos?
# R. La media. Solo se recomienda utilizar la media cuando no hay valores atípicos.

# Como no hay valores atípicos importantes en los datos, podemos utilizar la media como valor representativo tanto para 'age' como para 'time'. 
# En el siguiente código, calculamos la edad promedio y la guardamos en una variable llamada age_avg, luego la usamos para completar los valores ausentes de 'age':

import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
print("Mean age:", age_avg)

analytics_data['age'] = analytics_data['age'].fillna(age_avg)

# Respuesta: Mean age: 32.48966336969903

# Observa que, de forma predeterminada, las filas con valores ausentes de 'age' no se incluyen en el cálculo mediante el método mean().
# Y así, nos hemos ocupado de nuestros valores ausentes de 'age'. Ahora es momento de que rellenes los valores de 'time' que están ausentes en las tareas.

# Fin.