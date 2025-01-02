# Capítulo 3/6 · Faltan 2 lecciones
# Introducción al preprocesamiento de datos y al análisis inicial

# Ordenar datos
# El primer paso en tu búsqueda de habilidades de manipulación de datos fue el agrupamiento de datos. 
# Lograste hacerlo usando la técnica combinada dividir-aplicar, junto con el uso de los métodos groupby(), asociados con count() y sum().
# Pero para dominar la manipulación de datos, necesitas otra valiosa habilidad: ordenamiento. 
# El ordenamiento puede ser útil de muchas maneras. Al final de esta lección, serás capaz de ordenar tus datos en orden ascendente o descendente utilizando el método sort_values().

# Teoria

# El método sort_values() en pandas es una poderosa herramienta para ordenar valores. Puede ordenar la tabla completa o grupos de filas dentro de ella.
# Este método se aplica a un DataFrame y tiene dos parámetros:
#   1. by=: el nombre o nombres de la columna cuyos valores se usan para ordenar las filas del DataFrame.
#   2. ascending= indica el orden al realizar el ordenamiento. Su valor predeterminado es True. Para ordenar los datos en orden descendente, establece este parámetro en False.
# Si aplicas el método sort_values() a una sola columna no habrá ningún parámetro by=, ya que solo tenemos una columna.

# Ordenar los datos de nuestros exoplanetas
# Digamos que tenemos un gran interés en los exoplanetas que son similares en tamaño a la Tierra. Ordenemos los datos por radio en orden ascendente. Primero vendrán los planetas más pequeños:

print(exoplanet.sort_values(by='radius').head(10))

             name     mass    radius  discovered
253   Kepler-37 b  0.01000  0.291431        2013
137  Kepler-102 b  0.01353  0.470774        2014
175  Kepler-138 b  0.00021  0.526818        2014
327   Kepler-62 c  0.01300  0.538027        2013
281   Kepler-42 d  0.00300  0.571654        2011
138  Kepler-102 c  0.00944  0.582863        2014
280   Kepler-42 c  0.00600  0.728579        2011
254   Kepler-37 c  0.03776  0.750996        2013
128      KOI-55 b  0.00140  0.762205        2011
279   Kepler-42 b  0.00900  0.784623        2011

# Este es el código que ordena únicamente la columna radius y muestra los primeros 10 resultados:

print(exoplanet['radius'].sort_values().head(10))

253    0.291431
137    0.470774
175    0.526818
327    0.538027
281    0.571654
138    0.582863
280    0.728579
254    0.750996
128    0.762205
279    0.784623
Name: radius, dtype: float64

# Recuerda que un valor de 1 significa que el radio es igual al de la Tierra. Parece que tenemos muchos exoplanetas que son más pequeños.
# Podemos extraer todos los exoplanetas con un radio menor al de la Tierra utilizando la indexación lógica:

print(exoplanet[exoplanet['radius'] < 1])

             name     mass    radius  discovered
128      KOI-55 b  0.00140  0.762205        2011
129      KOI-55 c  0.00210  0.863085        2011
137  Kepler-102 b  0.01353  0.470774        2014
138  Kepler-102 c  0.00944  0.582863        2014
141  Kepler-102 f  0.01636  0.885503        2014
146  Kepler-106 b  0.01668  0.818250        2014
148  Kepler-106 d  0.02549  0.952757        2014
152  Kepler-107 d  0.01196  0.863085        2014
174  Kepler-131 c  0.02600  0.840668        2014
175  Kepler-138 b  0.00021  0.526818        2014
194   Kepler-20 e  0.00970  0.863085        2011
195   Kepler-20 f  0.04500  0.997592        2011
253   Kepler-37 b  0.01000  0.291431        2013
254   Kepler-37 c  0.03776  0.750996        2013
264  Kepler-406 c  0.00900  0.851876        2014
266  Kepler-408 b  0.01573  0.818250        2014
279   Kepler-42 b  0.00900  0.784623        2011
280   Kepler-42 c  0.00600  0.728579        2011
281   Kepler-42 d  0.00300  0.571654        2011
327   Kepler-62 c  0.01300  0.538027        2013
336   Kepler-68 c  0.00642  0.926976        2013

# Ahora, digamos que solo nos interesan los valores para el 2014, podemos nuevamente usar la indexación lógica para extraerlos:

print(exoplanet[exoplanet['discovered'] == 2014])

            name    mass     radius  discovered
42      GU Psc b  11.000  15.132015        2014
84    HAT-P-49 b   1.730  15.838176        2014
86    HAT-P-54 b   0.760  10.581202        2014
92     HATS-15 b   2.170  12.385834        2014
95      HATS-4 b   1.323  11.433078        2014
..           ...     ...        ...         ...
478    WASP-74 b   0.826  13.988707        2014
487    WASP-83 b   0.300  11.657256        2014
489  WASP-87 A b   2.210  15.524326        2014
491    WASP-89 b   5.900  11.657256        2014
493  WASP-94 A b   0.452  19.279308        2014

[105 rows x 4 columns]

# Combinemos ahora nuestras dos condiciones para encontrar estos planetas:
#   - Planetas descubiertos en 2014.
#   - Planetas más pequeños que la Tierra.

# exoplanetas más pequeños que la Tierra y descubiertos en 2014
exo_small_14 = exoplanet[exoplanet['radius'] < 1]
exo_small_14 = exo_small_14[exo_small_14['discovered'] == 2014]
print(exo_small_14)

             name     mass    radius  discovered
137  Kepler-102 b  0.01353  0.470774        2014
138  Kepler-102 c  0.00944  0.582863        2014
141  Kepler-102 f  0.01636  0.885503        2014
146  Kepler-106 b  0.01668  0.818250        2014
148  Kepler-106 d  0.02549  0.952757        2014
152  Kepler-107 d  0.01196  0.863085        2014
174  Kepler-131 c  0.02600  0.840668        2014
175  Kepler-138 b  0.00021  0.526818        2014
264  Kepler-406 c  0.00900  0.851876        2014
266  Kepler-408 b  0.01573  0.818250        2014

# Ordenemos el resultado por radio en orden descendente.

print(exo_small_14.sort_values(by='radius', ascending=False))

             name     mass    radius  discovered
148  Kepler-106 d  0.02549  0.952757        2014
141  Kepler-102 f  0.01636  0.885503        2014
152  Kepler-107 d  0.01196  0.863085        2014
264  Kepler-406 c  0.00900  0.851876        2014
174  Kepler-131 c  0.02600  0.840668        2014
146  Kepler-106 b  0.01668  0.818250        2014
266  Kepler-408 b  0.01573  0.818250        2014
138  Kepler-102 c  0.00944  0.582863        2014
175  Kepler-138 b  0.00021  0.526818        2014
137  Kepler-102 b  0.01353  0.470774        2014

# El método sort_values() devuelve un nuevo objeto en vez de modificarlo localmente. 
# Por lo tanto, si deseas seguir trabajando con el DataFrame ordenado, deberás almacenar el resultado en una variable. 
# Puedes guardarla nuevamente en la misma:

exo_small_14 = exo_small_14.sort_values(by='radius', ascending=False)

# El más grande de estos planetas, Kepler-106 d, es casi del tamaño de la Tierra. 
# Orbita alrededor de la estrella Kepler-106, que forma parte de la constelación Cygnus. 
# Sin embargo, tendrías que hacer un largo viaje para visitarlo, ya que se encuentra a más de 1000 años luz de distancia.
# Curiosamente, el ordenamiento se puede hacer no solo para números, sino también para strings. 
# Echemos un vistazo rápido a un ejemplo paralelo para ilustrarlo. Vamos a crear un simple DataFrame que tenga una sola columna llamada alphabet:

df = pd.DataFrame(['b', 'a', 'c'], columns=['alphabet'])
print(df)   # Así es como se ve este DataFrame si lo imprimimos:

 alphabet
0       b
1       a
2       c

# Como podemos ver, aquí están las tres primeras letras del alfabeto, pero el orden es incorrecto. 
# ¿Qué pasará si ordenamos este DataFrame por la columna alphabet? Vamos a probarlo:

df = df.sort_values(by= 'alphabet', ascending=True)
print(df)   # Así es como se ve este DataFrame si lo imprimimos:

  alphabet
1        a
0        b
2        c

df = df.sort_values(by= 'alphabet', ascending=False)
print(df)   # Así es como se ve este DataFrame si lo imprimimos:

  alphabet
2        c
0        b
1        a

# ¡Ahora tenemos nuestro alfabeto en el orden correcto gracias al ordenamiento! 
# La conclusión es que el ordenamiento también se puede aplicar a las columnas que contienen no solo valores numéricos, sino también strings. 
# Al ordenar strings, podemos ordenarlas en orden alfabético o de manera opuesta si establecemos ascending= en False. ¡Ahora practiquemos el ordenamiento!

# Fin.