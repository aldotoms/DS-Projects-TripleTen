# Capítulo 3/6
# Introducción al preprocesamiento de datos y al análisis inicial

## Ejercicios


## Ejercicio 1


# En el fragmento de código a continuación, encontrarás la variable pop que almacena un DataFrame filtrado que contiene solo canciones pop. 
# Tu objetivo es determinar la cantidad de duplicados en este DataFrame y almacenar este valor en la variable duplicates. Por último, muestra esta variable.

import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

duplicates = pop.duplicated().sum()

print(duplicates)

# Eliminación de duplicados
# Para eliminar filas completamente duplicadas, llamaremos al método drop_duplicates():

df = df.drop_duplicates()

print(df.duplicated().sum())

0

# Alternativamente, podemos volver a especificar inplace=True para que no haya necesidad de reasignación:

df.drop_duplicates(inplace=True)

print(df.duplicated().sum())

0

# Como podemos ver, el resultado es idéntico.
# Sin embargo, cuando utilizamos este método, debemos tener en cuenta nuestros índices. Echa un vistazo a las primeras cinco filas después de eliminar los duplicados:

print(df.head())

    user_id          total play                                  Artist      genre              track_name
0  BF6EA5AF           92.851388                              Marina Rei        pop                  Musica
1  FB1E568E          282.981000                            Stive Morgan    ambient             Love Planet
3  EF15C7BA            8.966000                                     NaN      dance     Loving Every Minute
4  82F52E69          193.776327                                  Rixton        pop  Me And My Broken Heart
5  4166D680            3.007000  Henry Hall & His Gleneagles Hotel Band       jazz                    Home

# El índice 1 es seguido por el 3 porque el índice 2 ha desaparecido, junto con su fila duplicada. Conviene señalar que en DataFrames, 
# a diferencia de las listas de Python, los índices siguen siendo los mismos cuando se eliminan las filas.
# Cuando eliminas filas, a menudo también es importante actualizar el índice. Para hacerlo, llama al método reset_index(). 
# Esto creará un nuevo DataFrame en el que:
#   - Los índices del DataFrame original se ubicarán en una nueva columna llamada 'index'.
#   - Los nuevos índices se establecerán en orden para todas las filas en el DataFrame.
# Así es como restablecemos los índices:

df = df.drop_duplicates().reset_index()

print(df.head())

   index   user_id  total play                                  Artist   
0      0  BF6EA5AF   92.851388                              Marina Rei  \
1      1  FB1E568E  282.981000                            Stive Morgan   
2      3  EF15C7BA    8.966000                                 no_info   
3      4  82F52E69  193.776327                                  Rixton   
4      5  4166D680    3.007000  Henry Hall & His Gleneagles Hotel Band   

     genre                   track  
0      pop                  Musica  
1  ambient             Love Planet  
2    dance     Loving Every Minute  
3      pop  Me And My Broken Heart  
4     jazz                    Home

# Como resultado, obtuvimos la enumeración correcta para nuestras filas y también para la columna 'index', que básicamente almacena los índices anteriores. 
# Por lo general, queremos eliminar esta columna 'index'. Para ello, necesitamos establecer el parámetro drop= en True:

df = df.drop_duplicates().reset_index(drop=True)

    user_id   total play                                  Artist    genre   
0  BF6EA5AF   92.851388                              Marina Rei      pop  \
1  FB1E568E  282.981000                            Stive Morgan  ambient   
2  EF15C7BA    8.966000                                     NaN    dance   
3  82F52E69  193.776327                                  Rixton      pop   
4  4166D680    3.007000  Henry Hall & His Gleneagles Hotel Band     jazz   

                    track  
0                  Musica  
1             Love Planet  
2     Loving Every Minute  
3  Me And My Broken Heart  
4                    Home

# Como resultado, ahora tenemos índices correctos para nuestro DataFrame, que ya no contiene datos duplicados. Para resumir:
#   - Llamamos al método drop_duplicates() y obtenemos un DataFrame sin duplicados, pero con índices rotos.
#   - Luego usamos el método reset_index() para restablecer los índices de las filas y eliminar la columna 'index'.
# Aquí tienes algunas ilustraciones que muestran todos los pasos. La de en medio muestra el resultado de restablecer el índice sin eliminar los índices originales.


## Ejercicio 2


# Partiendo de nuestro ejercicio anterior, debemos eliminar las filas duplicadas del DataFrame pop con el que estamos trabajando. 
# El DataFrame resultante debe almacenarse en la misma variable pop como antes. Después de la eliminación, vuelve a comprobar el número de duplicados e imprime este número.

# Codigo
import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

pop = pop.drop_duplicates() # escribe tu código aquí

print(pop.duplicated().sum())# escribe tu código aquí)]

# Detección de duplicados implícitos
# La búsqueda de duplicados en columnas que contienen strings puede ser más difícil, pero no es imposible. 
# Para ver todos los valores únicos en una columna, utiliza el método unique(). Este método devuelve todos los valores únicos en una columna especificada. 
# Así es como lo usamos:

print(df['column'].unique())

# Para descubrir duplicados menos evidentes, los analistas buscan valores únicos, que pueden incluir:
#   - ortografías alternativas de la misma palabra (por ejemplo, ortografía estadounidense o británica);
#   - faltas de ortografía (por ejemplo, 'jazzz' en lugar de 'jazz');
#   = mayúsculas inconsistentes.
# Probemos este método en un pequeño dataset.
# El ranking ATP de tenis para 2018 se actualizó 17 veces. Guardaremos todas las versiones en una tabla:

import pandas as pd

rating = ['date', 'name', 'points']
players = [
        ['2018.01.01',  'Rafael Nadal', 10645],
                ['2018.01.08',  'Rafael Nadal', 10600],
                ['2018.01.29',  'Rafael Nadal', 9760],
                ['2018.02.19',  'Roger Federer', 10105], 
                ['2018.03.05',  'Roger Federer', 10060],
                ['2018.03.19',  'Roger Federerr', 9660],
                ['2018.04.02',  'Rafael Nadal Parera', 8770],
                ['2018.06.18',  'Roger Fedrer', 8920],
                ['2018.06.25',  'Rafael Nadal Parera', 8770],
                ['2018.07.16',  'Rafael Nadal Parera', 9310],
                ['2018.08.13',  'Rafael Nadal Parera', 10220],
                ['2018.08.20',  'Rafael Nadal Parera', 10040],
                ['2018.09.10',  'Rafael Nadal Parera', 8760],
                ['2018.10.08',  'Rafael Nadal Parera', 8260],
                ['2018.10.15',  'Rafael Nadal Parera', 7660],
                ['2018.11.05',  'Novak Djokovic', 8045],
                ['2018.11.19',  'Novak Djokovic', 9045]
]
tennis = pd.DataFrame(data=players, columns=rating)
print(tennis)

          date                 name  points
0   2018.01.01         Rafael Nadal   10645
1   2018.01.08         Rafael Nadal   10600
2   2018.01.29         Rafael Nadal    9760
3   2018.02.19        Roger Federer   10105
4   2018.03.05        Roger Federer   10060
5   2018.03.19       Roger Federerr    9660
6   2018.04.02  Rafael Nadal Parera    8770
7   2018.06.18         Roger Fedrer    8920
8   2018.06.25  Rafael Nadal Parera    8770
9   2018.07.16  Rafael Nadal Parera    9310
10  2018.08.13  Rafael Nadal Parera   10220
11  2018.08.20  Rafael Nadal Parera   10040
12  2018.09.10  Rafael Nadal Parera    8760
13  2018.10.08  Rafael Nadal Parera    8260
14  2018.10.15  Rafael Nadal Parera    7660
15  2018.11.05       Novak Djokovic    8045
16  2018.11.19       Novak Djokovic    9045

# Llamaremos al método unique() en la columna que almacena los nombres de los jugadores de tenis:

print(tennis['name'].unique())

['Rafael Nadal' 'Roger Federer' 'Roger Federerr' 'Rafael Nadal Parera'
 'Roger Fedrer' 'Novak Djokovic']

# Así que tenemos seis nombres. Espera un momento… El nombre de Roger Federer se escribió mal dos veces. Y Rafael Nadal aparece con y sin Parera. 
# ¡Estos son duplicados implícitos!
# A veces, solo queremos saber el número de valores únicos en una columna en lugar de los valores en sí. En ese caso, podemos usar el método nunique():

print(tennis['name'].nunique())

6

# En nunique(), n representa un número. Como acabamos de ver, esta función devuelve el número de valores únicos. En el ejemplo anterior, vimos que hay seis nombres únicos.

## Eliminación de duplicados implícitos
# Utiliza el método replace() para corregir la ortografía incorrecta o alternativa. Pasa el valor no deseado de la tabla como primer argumento y el valor correcto como segundo:

tennis['name'] = tennis['name'].replace('Roger Federerr', 'Roger Federer')
tennis['name'] = tennis['name'].replace('Roger Fedrer', 'Roger Federer')
tennis['name'] = tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera')

print(tennis)

          date                 name  points
0   2018.01.01  Rafael Nadal Parera   10645
1   2018.01.08  Rafael Nadal Parera   10600
2   2018.01.29  Rafael Nadal Parera    9760
3   2018.02.19        Roger Federer   10105
4   2018.03.05        Roger Federer   10060
5   2018.03.19        Roger Federer    9660
6   2018.04.02  Rafael Nadal Parera    8770
7   2018.06.18        Roger Federer    8920
8   2018.06.25  Rafael Nadal Parera    8770
9   2018.07.16  Rafael Nadal Parera    9310
10  2018.08.13  Rafael Nadal Parera   10220
11  2018.08.20  Rafael Nadal Parera   10040
12  2018.09.10  Rafael Nadal Parera    8760
13  2018.10.08  Rafael Nadal Parera    8260
14  2018.10.15  Rafael Nadal Parera    7660
15  2018.11.05       Novak Djokovic    8045
16  2018.11.19       Novak Djokovic    9045

# Tuvimos que llamar al método replace() dos veces. Si hubiéramos tenido más faltas de ortografía, habríamos tenido que volver a llamarlo.
# Como siempre, pasar inplace=True produce el mismo resultado sin necesidad de reasignación.

tennis['name'].replace('Roger Federerr', 'Roger Federer', inplace = True)
tennis['name'].replace('Roger Fedrer', 'Roger Federer', inplace = True)
tennis['name'].replace('Rafael Nadal', 'Rafael Nadal Parera', inplace = True)

print(tennis)

          date                 name  points
0   2018.01.01  Rafael Nadal Parera   10645
1   2018.01.08  Rafael Nadal Parera   10600
2   2018.01.29  Rafael Nadal Parera    9760
3   2018.02.19        Roger Federer   10105
4   2018.03.05        Roger Federer   10060
5   2018.03.19        Roger Federer    9660
6   2018.04.02  Rafael Nadal Parera    8770
7   2018.06.18        Roger Federer    8920
8   2018.06.25  Rafael Nadal Parera    8770
9   2018.07.16  Rafael Nadal Parera    9310
10  2018.08.13  Rafael Nadal Parera   10220
11  2018.08.20  Rafael Nadal Parera   10040
12  2018.09.10  Rafael Nadal Parera    8760
13  2018.10.08  Rafael Nadal Parera    8260
14  2018.10.15  Rafael Nadal Parera    7660
15  2018.11.05       Novak Djokovic    8045
16  2018.11.19       Novak Djokovic    9045

# Automatización con funciones personalizadas
# Para evitar repetir el mismo código varias veces, los profesionales de los datos suelen escribir sus propias funciones. 
# Vamos a crear una función que tome cuatro argumentos:
#   - el DataFrame;
#   - el nombre de la columna donde queremos realizar el reemplazo;
#   - una lista de valores incorrectos;
#   - el valor correcto.
# La función reemplazará todos los valores incorrectos por el correcto en la columna seleccionada.

def replace_wrong_values(df, column, wrong_values, correct_value): # pasar una lista de valores incorrectos y un string con el valor correcto en la entrada de la función
        for wrong_value in wrong_values: # un bucle sobre nombres mal escritos
                df[column] = df[column].replace(wrong_value, correct_value) # llamar a replace() para cada nombre incorrecto
        return df   # devolver el DataFrame modificado

duplicates = ['Roger Federerr', 'Roger Fedrer'] # una lista de nombres mal escritos
name = 'Roger Federer'  # El nombre correcto
tennis = replace_wrong_values(tennis, 'name', duplicates, name) # llamar a la función, replace() se llamará dos veces
print(tennis)   # el nuevo DataFrame sin duplicados

# Veamos si puedes detectar algunos datos únicos en el siguiente ejercicio:


## Ejercicio 3


# Y finalmente, verifica el número de valores únicos en la columna 'Artist'. Guarda los valores únicos en la variable pop_artists. 
# El número de artistas únicos debe almacenarse en la variable n_artists. Muestra ambas variables.

# Codigo
import pandas as pd

df = pd.read_csv('/datasets/music_log_raw.csv')

pop = df[df['genre'] == 'pop']

pop_artists = pop['Artist'].unique() # escribe tu código aquí
n_artists = pop['Artist'].nunique() # escribe tu código aquí

print(pop_artists) # escribe tu código aquí)
print(n_artists) # escribe tu código aquí)

# ¿Increíble, no? Ahora ya puedes encontrar y procesar duplicados explícitos e implícitos. Y también tienes tus datos listos para rocanrrolear. 
# En la siguiente lección, comenzarás tu proceso de análisis de datos aprendiendo cómo agrupar datos. ¡No te distraigas!

# Fin.