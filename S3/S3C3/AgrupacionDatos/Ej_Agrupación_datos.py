# Capítulo 3/6 · Faltan 3 lecciones
# Introducción al preprocesamiento de datos y al análisis inicial

## Ejercicios


# Ejercicio 1


# Revisemos nuestro conjunto de datos de música y agrupémoslo de manera similar a como lo hicimos con los exoplanetas. 
# Es importante tener en cuenta que la agrupación generalmente se realiza en un dataset procesado que no contiene valores NaN, duplicados o nombres de columna sin formato. 
# Por lo tanto, no usaremos el conjunto de datos music_log_raw.csv original, sino que usaremos el dataset preprocesado con todos los problemas eliminados.
# Nuestro primer paso es agrupar el conjunto de datos por 'genre'. Cuando se aplique el agrupamiento, guárdalo en la variable genre_groups y muestra su tipo.

import pandas as pd
df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre') # escribe tu código aquí
print(type(genre_groups)) # escribe tu código aquí)

# Resultado
<class 'pandas.core.groupby.generic.DataFrameGroupBy'>


## Ejercicio 2


# Ahora pasemos a la etapa de aplicación y apliquemos métodos de cálculo a cada grupo. 
# Recuerda que eventualmente, queremos calcular el tiempo total. 
# Cuando hablamos del tiempo total, el método que necesitamos aplicar, debe darnos una suma como resultado. 
# Aplica en el precódigo a continuación el método adecuado (cuando se agrega, la variable genre_groups almacenará un DataFrame con un resultado). 
# Imprime la variable genre_groups al final.

# Codigo
import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre').sum() # aplica el método apropiado aquí

print(genre_groups)

Resultado
                    total_play
genre                         
acapella            355.000000
acid                484.922000
acoustic            240.348163
action              511.903586
adult              2301.923250
african            1896.137258
afrika              474.883936
afrikaans           273.889731
afro                 29.217000
alternative      170130.211929
alternativepunk      86.385000
ambient           51639.539645
americana           471.466438
animated           4021.608357
anime               751.202113
arabesk            1018.146036
argentinetango     2551.019394
art                 417.851020
asiapop             338.050583
audiobook           236.554283
avantgarde        12183.085784
axé                 222.718705
bacheta              24.841131
baile                 0.100000
balkan              552.986123
bass                265.427000
bassline            273.789375
beats              1382.324388
bigroom            1507.803070
black              1953.294523
...                        ...
synthrock             3.360341
tango               619.389444
tatar              5619.555254
tech               6406.143602
techno            21657.562258
thrash              473.815469
top                   9.445213
traditional         702.177000
tradjazz            231.906500
trance            18725.541647
trip               1416.563099
tropical           1416.466472
trumpet             315.454667
turbo               109.956875
türk                754.892671
türkçe             1659.734988
ukr                 227.800000
ukrrock            2040.479284
urban             33481.157831
uzbek              1222.375799
variété            2612.730347
videogame          4769.137427
vocal              8120.499994
western           13521.969634
world            256630.643956
worldmusic           20.000000
wort                117.139871
yoga                307.177143
şiir                  2.043000
электроника           1.009000

[305 rows x 1 columns]


## Ejercicio 3


# Nuestro paso final es combinar los resultados. Por si acaso, te recordamos que queremos calcular el tiempo total que nuestros oyentes pasaron escuchando cada género. 
# Tenemos una columna 'total_play' en nuestro dataset que contiene exactamente lo que necesitamos. 
# Necesitamos pasar esto a nuestro flujo de agrupación: primero, selecciona la columna y luego aplica un método que calcule el tiempo total.
# Hazlo e imprime el resultado final.

# Codigo
import pandas as pd

df = pd.read_csv('/datasets/music_log_processed.csv')

genre_groups = df.groupby('genre')['total_play'].sum() # escribe tu código aquí

print(genre_groups)

# Resultado
genre
acapella              355.000000
acid                  484.922000
acoustic              240.348163
action                511.903586
adult                2301.923250
african              1896.137258
afrika                474.883936
afrikaans             273.889731
afro                   29.217000
alternative        170130.211929
alternativepunk        86.385000
ambient             51639.539645
americana             471.466438
animated             4021.608357
anime                 751.202113
arabesk              1018.146036
argentinetango       2551.019394
art                   417.851020
asiapop               338.050583
audiobook             236.554283
avantgarde          12183.085784
axé                   222.718705
bacheta                24.841131
baile                   0.100000
balkan                552.986123
bass                  265.427000
bassline              273.789375
beats                1382.324388
bigroom              1507.803070
black                1953.294523
                       ...      
synthrock               3.360341
tango                 619.389444
tatar                5619.555254
tech                 6406.143602
techno              21657.562258
thrash                473.815469
top                     9.445213
traditional           702.177000
tradjazz              231.906500
trance              18725.541647
trip                 1416.563099
tropical             1416.466472
trumpet               315.454667
turbo                 109.956875
türk                  754.892671
türkçe               1659.734988
ukr                   227.800000
ukrrock              2040.479284
urban               33481.157831
uzbek                1222.375799
variété              2612.730347
videogame            4769.137427
vocal                8120.499994
western             13521.969634
world              256630.643956
worldmusic             20.000000
wort                  117.139871
yoga                  307.177143
şiir                    2.043000
электроника             1.009000
Name: total_play, Length: 305, dtype: float64

# Ahora puedes agrupar los datos de una manera que los comprendas mejor. 
# Este es un comienzo sólido en el viaje de obtener conocimiento de los conjuntos de datos. Y no finaliza aquí. 
# En la siguiente lección, veremos otra poderosa herramienta que nos ayudará en este camino, ordenar nuestros datos. ¡Apúntate!

# Fin.