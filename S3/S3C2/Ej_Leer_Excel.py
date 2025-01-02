# Capítulo 2/6
# Leer y visualizar datos

# Cómo leer archivos Excel

# Ejercicios
# Ejercicio 1 - Calcula la puntuación promedio de las opiniones siguiendo estos pasos:

# Lee la primera hoja del fichero Excel ubicado en /datasets/product_reviews.xlsx y guárdala en una variable llamada df_reviews.
# 1. Selecciona la columna 'review' de df_reviews.
# 2. Aplica el método adecuado para calcular el valor medio.
# 3. Muestra el resultado en la pantalla.

# Código
import pandas as pd
df_reviews = pd.read_excel('/datasets/product_reviews.xlsx') # escribe tu código aquí
print(df_reviews['review'].mean())

# Resultado: 3.01


# Ejercicio 2
# Para obtener más información sobre los productos de este conjunto de datos, lee la hoja products del archivo Excel en una variable llamada df_products. 
# A continuación, ordena el DataFrame por la columna 'id' en orden ascendente utilizando el método apropiado y guárdalo en la variable sorted_df_products. 
# Si no recuerdas el nombre del método, no te preocupes, tenemos una pista que te ayudará.
# Por último, no olvides imprimir el dataframe ordenado.

# Código
import pandas as pd
df_products = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name='products') # escribe tu código aquí
sorted_df_products = df_products.sort_values('id')
print(sorted_df_products) # escribe tu código aquí

# Resultado
            id  category_id                         name
3   1862691474            1                iPhone 6 Plus
15  2203505344            2                  Amazon Echo
14  3108772165            4          Microsoft Office XP
19  3201109340            4              Adobe Photoshop
10  3679575768            3           Dell Latitude D600
18  3785879508            5             The Oregon Trail
12  4004717767            3             IBM ThinkPad T22
16  4023404310            4                 Ableton Live
8   4920540660            3         Power Macintosh 4400
1   5003186430            1                    iPhone 3G
17  5947803319            5                  Ms. Pac-Man
9   6419177218            2               Casiotone 7000
5   6852963736            1               Asus ZenFone 5
4   6962058955            2           Philips DVD player
11  7130698135            3           Toshiba Tecra 8100
13  7326194383            1           Samsung Galaxy Neo
7   8594363698            4  Mavis Beacon Teaches Typing
6   8847800628            4                   Windows Me
0   9315269501            5                       Tetris
2   9741979309            1                    iPhone 4S

# Ejercicio 3
# Además de los nombres de los productos, el dataset también contiene información sobre cómo se clasifican los productos. 
# Por eso había una columna 'category_id' en la tabla del último ejercicio.
# Lee la hoja final de product_categories en una variable llamada df_categories. Luego simplemente muestra df_categories en la pantalla.

# Código
import pandas as pd
df_categories = pd.read_excel('/datasets/product_reviews.xlsx', sheet_name='product_categories')# escribe tu código aquí
print(df_categories)

# Resultado
   id                   category
0   1  Cell Phones & Accessories
1   2       Consumer Electronics
2   3         Personal Computers
3   4                   Software
4   5                Video Games

# Fin.