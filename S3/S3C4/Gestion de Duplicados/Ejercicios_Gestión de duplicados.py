# Capítulo 4/6 · Faltan 2 lecciones
# Trabajar con valores duplicados y ausentes

# *Gestión de duplicados
# *Ejercicios

# Ejercicio 1
# Cambia los nombres de los modelos de teléfonos a minúsculas usando el método str.lower() y guárdalos en una nueva columna llamada 'item_lowercase', pero conserva también la columna original 'item'.
# Imprime las primeras filas de la tabla actualizada y mira el resultado.

# Código:

import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')

df_stock['item_lowercase'] = df_stock['item'].str.lower() # escribe tu código aquí

print(df_stock.head()) # escribe tu código aquí)

# Resultado:

          id                     item  count           item_lowercase
0  100480924     Apple iPhone Xr 64gb     10     apple iphone xr 64gb
1  100480924     Apple iPhone Xr 64GB     19     apple iphone xr 64gb
2  100480959     Xiaomi Redmi 6A 16GB     44     xiaomi redmi 6a 16gb
3  100480975          HUAWEI P30 lite     38          huawei p30 lite
4  100480988  Samsung Galaxy A30 32GB     49  samsung galaxy a30 32gb


# Ejercicio 2
# Utilizando tu recién creada columna 'item_lowercase' y el método sum(), calcula el número total de dos modelos de teléfono:
#   1) 'apple iphone xr 64gb'
#   2) 'samsung galaxy a30 32gb'
# Para contar el número de teléfonos Apple, filtra el DataFrame a partir de la columna 'item_lowercase' para incluir solo las filas con 'apple iphone xr 64gb' como valor. 
# A continuación, extrae la columna 'count' del DataFrame filtrado y aplícale el método sum(). Almacena la cantidad total de teléfonos Apple en la variable apple.
# Para los teléfonos Samsung, sigue el mismo procedimiento con la única diferencia de que guardes el número total de teléfonos Samsung en la variable samsung.
# El precódigo ya contiene el código para imprimir tus resultados, no lo modifiques.

# Código:

import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum() # completa esta línea de código
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum() # completa esta línea de código

print("Número total de teléfonos Apple:", apple)
print("Número total de teléfonos Samsung:", samsung)


# Ejercicio 3
# Ahora elimina las filas con teléfonos duplicados llamando a drop_duplicates() en df_stock. 
# Necesitamos eliminar filas únicamente en función de la columna item_lowercase', así que asegúrate de utilizarla como valor para el parámetro subset=.
# Recuerda que después de eliminar los duplicados, tenemos que llamar al método reset_index() con el parámetro drop=True. Esto nos permite arreglar la indexación y eliminar el índice antiguo.
# Por cierto, ¡puedes hacer todo esto con una sola línea de código! Puede ser un poco difícil, pero intenta encontrar la manera de hacerlo.
# El resultado final debería asignarse de nuevo a df_stock. Imprime las primeras filas del df_stock cuando hayas terminado.

# Código:

import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop=True) # escribe tu código aquí
print(df_stock) # escribe tu código aquí)

# Resultado

          id                     item  count           item_lowercase
0  100480924     Apple iPhone Xr 64gb     10     apple iphone xr 64gb
1  100480959     Xiaomi Redmi 6A 16GB     44     xiaomi redmi 6a 16gb
2  100480975          HUAWEI P30 lite     38          huawei p30 lite
3  100480988  Samsung Galaxy A30 32GB     49  samsung galaxy a30 32gb
4  100481020            Honor 8X 64GB     64            honor 8x 64gb


# Ejercicio 4
# ¡Vamos a hacer algo realmente interesante! No te preocupes, estás preparado al 100% y nosotros te ayudaremos.
# El precódigo incluye una línea que escribiste anteriormente para eliminar duplicados, por lo que ahora tenemos el DataFrame df_stock sin duplicados. 
# Tu objetivo es establecer los valores correctos en la columna 'count' para las filas donde 'item' es 'Apple iPhone XR 64GB' y 'Samsung Galaxy A30 32GB'.
# Los valores que vas a establecer ya fueron calculados por ti previamente y están almacenados en las variables apple y samsung en el precódigo.
# La mejor forma de actualizar los valores de la columna 'count' es utilizar el atributo loc[] que puede reemplazar los valores en un lugar especificado.
# Revisemos el df_stock después de eliminar los duplicados para ilustrar cómo loc[] puede ayudarnos a actualizar los valores:

          id                     item  count           item_lowercase
0  100480924     Apple iPhone Xr 64gb     10     apple iphone xr 64gb
1  100480959     Xiaomi Redmi 6A 16GB     44     xiaomi redmi 6a 16gb
2  100480975          HUAWEI P30 lite     38          huawei p30 lite
3  100480988  Samsung Galaxy A30 32GB     49  samsung galaxy a30 32gb
4  100481020            Honor 8X 64GB     64            honor 8x 64gb

# Podemos utilizar loc[] para actualizar el valor de la primera fila (índice 0) y la columna 'count' del modelo Apple iPhone. 
# Pasamos dos valores a loc[] para especificar el índice de la fila y el nombre de la columna, y luego utilizamos el signo = para establecer el valor deseado:

df_stock.loc[0,'count'] = 33

# En el ejemplo anterior, utilizamos el valor 33, pero en realidad queremos establecer el valor de la variable apple que previamente hemos calculado y guardado.
# Fue un ejemplo para el iPhone de Apple. El procedimiento para Samsung será el mismo, salvo que le pasaremos valores diferentes al atributo loc[].

# Código:

import pandas as pd

df_stock = pd.read_csv('/datasets/phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum()
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum()

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop=True)

# escribe tu código aquí
df_stock.loc[0, 'count'] = apple
df_stock.loc[3, 'count'] = samsung

print(df_stock)

# Fin.