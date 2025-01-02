# Filtrar DataFrames con NaNs
# Filtrar DataFrame por valores ausentes

# A veces, puede ser necesario examinar las filas del dataset que contienen valores ausentes. Hay varias formas de filtrar un DataFrame para extraer filas con valores ausentes. 
# Una forma es utilizar el método isna(), que genera un Series para cada fila. En esta serie, True indica un valor ausente y False indica un valor no ausente.
# Luego podemos utilizar este Series para filtrar el DataFrame. 
# Por ejemplo, si queremos extraer filas en las que la columna 'source' tiene valores ausentes, podemos hacerlo utilizando el siguiente código:

print(df_logs[df_logs['source'].isna()])

           user_id source       email  purchase
22      1397217221    NaN  79ac569f0b         0
49      5062457902    NaN  9ddce3a861         0
171     6724868284    NaN  c0e48c7cf8         0
258     3221384063    NaN  7fe8da1823         0
379     7515782311    NaN  462462af10         0
...            ...    ...         ...       ...
199342  3439213943    NaN  7edda4e2a4         0
199661  9473123762    NaN  3535509f51         0
199689   722485056    NaN  470ffa3800         0
199709  5950023506    NaN  0fb749d485         0
199758  3747926428    NaN  604850216f         0

[1674 rows x 4 columns]

# Vamos a desglosar esta línea de código:
#   1. Extraemos la columna 'source' utilizando df_logs['source']
#   2. A continuación, le aplicamos el método isna() para obtener una serie de booleanos que indican la ausencia de valores: df_logs['source'].isna()
#   3. Utilizamos esta serie de booleanos para filtrar el DataFrame original, extrayendo solamente las filas en las que 'source' tiene valores ausentes.
#   4. Por último, imprimimos la tabla resultante.

# Otra opción es filtrar el DataFrame y extraer sólo las filas en las que no falte 'source'. El enfoque que utilizamos anteriormente funcionará con una única modificación menor:

print(df_logs[~df_logs['source'].isna()])

           user_id   source       email  purchase
0       7141786820    other         NaN         0
1       5644686960    email  c129aa540a         0
2       1914055396  context         NaN         0
3       4099355752    other         NaN         0
4       6032477554  context         NaN         1
...            ...      ...         ...       ...
199995  8714621942    other         NaN         0
199996  6064948744  context         NaN         1
199997  9210683879  context         NaN         0
199998  1629959686    other         NaN         1
199999  2089329795    other         NaN         0

[198326 rows x 4 columns]

# La única diferencia entre este caso y aquel que nos interesaba por las filas con valores ausentes es la adición del símbolo de tilde (~), que invierte el resultado. 
# Aquí está el desglose de este código:
#   1. Extraemos la columna 'source' utilizando df_logs['source'].
#   2. A continuación, le aplicamos el método isna() para obtener una serie de booleanos que indican la ausencia de valores: df_logs['source'].isna().
#   3, Invertimos la serie utilizando ~. Esto invierte todos los valores True a False y viceversa.
#   4. Utilizamos esta serie de booleanos para filtrar el DataFrame original, extrayendo sólo las filas en las que 'source' no tiene valores ausentes.
#   5. Por último, imprimimos la tabla resultante.


# Múltiples condiciones de filtrado

# Podemos filtrar un DataFrame a partir de múltiples condiciones. 
# Por ejemplo, para crear un DataFrame que no tenga valores ausentes en la columna 'email' y solo el valor 'email' en la columna 'source', podemos emplear el siguiente código:

print(df_logs[(~df_logs['email'].isna()) & (df_logs['source'] == 'email')])

           user_id source       email  purchase
1       5644686960  email  c129aa540a         0
11      8623045648  email  d6d19c571c         0
18      5739438900  email  19379ee49c         0
19      7486955288  email  09c27794fa         0
33      7298923004  email  1fe184ed73         0
...            ...    ...         ...       ...
199922  4075894991  email  2c9a202435         0
199958  9794381984  email  85712b433a         0
199970  3396355438  email  4bba3fde78         0
199979  5008169696  email  e5128e15fd         0
199989  9470921783  email  3977de6aaa         0

[12279 rows x 4 columns]

# El código de filtrado anterior consta de dos partes:
#   1. (~df_logs['email'].isna()) devuelve una serie de booleanos donde True indica que no falta ningún valor en la columna 'email'.
#   2. (df_logs['source'] == 'email') devuelve una serie de booleanos, donde True indica que 'source' tiene 'email' como valor, y False indica lo contrario.
#   3. Comprobamos dos series de booleanos para ver dónde ambas condiciones devuelven True. Utilizamos el símbolo & para representar el operador lógico and. 
#       Las filas que cumplen ambas condiciones (es decir, que cumplen la primera condición y la segunda) se incluyen en el resultado final.

# Ahora, ¡a practicar!


# *Ejercicio 1 de 2:

# 1. Anteriormente determinamos que la columna 'email' tiene 13 953 valores no ausentes. ¡Eso significa que más del 90% de los datos están ausentes! 
# Filtra el DataFrame df_logs para que solo contenga filas donde no haya valores ausentes en la columna 'email'. 
# Asigna el resultado filtrado a una variable llamada df_emails, luego imprime las primeras 10 filas.
# Para comprobar si una condición no es verdadera al filtrar un DataFrame, precede la condición con el carácter ~ (por ejemplo, df[~df.method()]).

# Codigo:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

# escribe tu código aquí
df_emails = df_logs[~df_logs['email'].isna()]
print(df_emails.head(10))

# Resultado:

       user_id source       email  purchase
1   5644686960  email  c129aa540a         0
11  8623045648  email  d6d19c571c         0
18  5739438900  email  19379ee49c         0
19  7486955288  email  09c27794fa         0
22  1397217221    NaN  79ac569f0b         0
33  7298923004  email  1fe184ed73         0
43  6034222291  email  fb58a27f03         0
49  5062457902    NaN  9ddce3a861         0
56  5690036640  email  a088a48182         0
66  9963049355  email  9cc43ebd15         0


# *Ejercicio 2 de 2:

# 2. La columna 'source' muestra que muchas de estas visitas procedían de enlaces de correo electrónico de marketing. Pero también hay algunos valores NaN. 
# Es posible que las visitas con una dirección de correo electrónico, pero sin un valor 'source', también provengan de enlaces de marketing por correo electrónico, pero que la fuente no se haya registrado.
# Comprueba si hay filas con valores ausentes en las columnas 'source' y 'email'. 
# Si no hay ninguna fila en la que ambas condiciones sean verdaderas, entonces es una buena señal de que los valores ausentes en la columna 'source' deberían ser 'email'.
# Filtra df_logs en la condición donde las columnas 'email' y 'source' tienen valores ausentes. Asigna el resultado a una variable llamada df_emails y luego imprímelo.

# Codigo:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

# escribe tu código aquí
df_emails = (df_logs[(~df_logs['email'].isna()) & (~df_logs['source'].isna())])
print(df_emails)

# Resultado:

           user_id source       email  purchase
1       5644686960  email  c129aa540a         0
11      8623045648  email  d6d19c571c         0
18      5739438900  email  19379ee49c         0
19      7486955288  email  09c27794fa         0
33      7298923004  email  1fe184ed73         0
43      6034222291  email  fb58a27f03         0
56      5690036640  email  a088a48182         0
66      9963049355  email  9cc43ebd15         0
76      7686901492  email  539df283fd         0
100     7557066181  email  4687297254         0
104     2278608366  email  b3e557cc4d         0
110     4264247631  email  83c774439b         0
174     7292910564  email  aefe3f67c8         0
202     5986650152  email  9176da1ad3         0
204     2577252296  email  f750604b79         0
211     3490271629  email  affcb18009         0
229     4295654539  email  c853962df8         1
232     3289595905  email  0393fcc30f         0
255     6040457264  email  ffe64c4d89         0
259     1420635064  email  2f5b5f32c6         0
261     7449896313  email  80e947e249         0
272     9449527180  email  78c6a96183         0
273     1737991566  email  8d8b0dd9ed         0
275     7640923349  email  af32787fa8         0
278     6585199517  email  2fc967e782         0
296     1571241836  email  c5323fe4a2         1
357     7578186763  email  5bec1ae959         0
364     5314423714  email  1259adc1c1         0
368     1680892461  email  28b3fbbf1b         0
375     2323162683  email  d002655b3d         0
...            ...    ...         ...       ...
199624  5381619476  email  cf4802a5b6         0
199632  6466383158  email  d3f3a120d8         0
199642  1342596208  email  6170c41938         1
199653  4271406556  email  2a98c6d01d         0
199659   171005052  email  0751e539a5         0
199664  3754680846  email  5b3dd8363c         1
199665  6143544739  email  f63a2a4186         0
199667  4830288620  email  1b60bca8ca         0
199727  3476227269  email  fb674ac628         0
199729  9997359171  email  faa41c1720         0
199760  3318200743  email  1bb7421ed4         0
199766  4065772480  email  ef6fc46b6a         0
199772  8048408811  email  1de053cf5f         0
199779  6066862133  email  5a7bd36b15         1
199787  6601152857  email  f4a7c703c8         0
199788  6217071028  email  bba7630703         0
199800  1461199744  email  a4bc977e1f         0
199820   521291457  email  8fa9368d69         0
199830  1344147236  email  6d81a28c77         0
199832  7619283692  email  0f1101265a         0
199852  1573330294  email  0ac53876b4         0
199858  1624485290  email  9b013aaa2e         0
199865  8221297507  email  33e9588911         0
199897  2910313620  email  94cc3996f4         0
199910  5962452277  email  91c7410fb8         0
199922  4075894991  email  2c9a202435         0
199958  9794381984  email  85712b433a         0
199970  3396355438  email  4bba3fde78         0
199979  5008169696  email  e5128e15fd         0
199989  9470921783  email  3977de6aaa         0

[12279 rows x 4 columns]

# Codigo 2:

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

# escribe tu código aquí
df_emails = (df_logs[(df_logs['email'].isna()) & (df_logs['source'].isna())])
print(df_emails)

# Resultado:

Empty DataFrame
Columns: [user_id, source, email, purchase]
Index: []

# Fin.