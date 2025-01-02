#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Tom! 😊
# 
# Mi nombre es **Alejandro Castellanos** y hoy tengo el placer de ser el revisor de tu proyecto.
# 
# Voy a revisar todo tu código con detalle, buscando tanto los puntos fuertes como aquellos en los que podrías mejorar. Te dejaré comentarios a lo largo del notebook, destacando lo que has hecho bien y sugiriendo ajustes donde sea necesario. Si encuentro algún error, no te preocupes, te lo haré saber de forma clara y te daré información útil para que puedas corregirlo en la próxima. Si en algún punto tienes comentarios, siéntete libre de dejarlos también.
# 
# 
# Encontrarás mis comentarios específicos dentro de cajas verdes, amarillas o rojas, es muy importante que no muevas, modifiques o borres mis comentarios, con el fin de tener un seguimiento adecuado de tu proceso.:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si todo está perfecto.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# </div>
# 
# A continuación te dejaré un comentario general con mi valoración del proyecto. **¡Mi objetivo es que sigas aprendiendo y mejorando con cada paso!**

# -----

# <div class="alert alert-block alert-danger">
# <b>Comentario General del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Tom has tenido un excelente inicio, especialmente en el análisis exploratorio de datos (EDA), donde lograste manejar de manera efectiva los datos duplicados y faltantes. También evidenciaste una buena comprensión del contexto del proyecto al responder correctamente algunas de las preguntas planteadas. Aunque aún hay algunas preguntas por resolver, tu trabajo hasta ahora sugiere que tienes las habilidades necesarias para completar el proyecto de manera satisfactoria. Un aspecto clave para potenciar tu trabajo es incorporar análisis en cada sección, lo que le dará más profundidad y valor a la información obtenida y evitará que el proyecto se quede solo en código. Quedo atento a tu próxima iteración 👀
# 
# </div>

# <div class="alert alert-block alert-warning">
# <b>Comentario General del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Tom has tenido un avance signigficativo respecto a la primera iteración, has ajustado correctamente gran parte del notebook y has dado respuesta a la mayoría de preguntas. He dejao comentarios específicos en las preguntas en las que veo que requieres ayuda, confío que con esto podrás completar este proyecto de manera satisfactoria. 💯
# 
# </div>

# ----

# # ¡Llena ese carrito!

# Puedes responderme de esta forma:
# <div class="alert alert-block alert-info">
# <b></b> <a class=“tocSkip”></a>
#     Está pendiente actualizar la lista de contenido; así como también, arreglar los vínculos que no funciona, pero lo realizaré con más calma otro día.
# </div>
# 

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Paso 1. Descripción de los datos](#data_review)
#     * [1.1 Diccionario de datos](#dictionary)
#     * [1.2 Plan de solucion](#plan)
#     * [1.3 Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# ¡Gran Idea! El uso de una tabla de contenido es una excelente estrategia para mejorar la estructura del notebook y facilitar su revisión. 
# 
# </div>

# # Introducción <a id='intro'></a>
# 
# Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.
# El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.
# 
# Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones al tiempo que avanzas en tu solución.  También escribe una conclusión que resuma tus hallazgos y elecciones.
# 

# [Volver a Contenidos](#back)

# # Paso 1. Descripción de los datos <a id='data_review'></a>
# 
# Para este trabajo se tienen los siguientes 5 archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) los cuales se leeran con la librería Pandas de Python, utilizando el método de lectura de archivos separados por comas `pd.read_csv()` usando el parámetro sep=';' para leer los datos correctamente. 
# De primer instancia, se verificará la información para cada uno de los DataFrames.
# 

# ## Diccionario de datos <a id='dictionary'></a>
# 
# Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.
# 
# - `instacart_orders.csv`: cada fila corresponde a un pedido en la aplicación Instacart.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'user_id'`: número de ID que identifica de manera única la cuenta de cada cliente.
#     - `'order_number'`: el número de veces que este cliente ha hecho un pedido.
#     - `'order_dow'`: día de la semana en que se hizo el pedido (0 si es domingo).
#     - `'order_hour_of_day'`: hora del día en que se hizo el pedido.
#     - `'days_since_prior_order'`: número de días transcurridos desde que este cliente hizo su pedido anterior.
# - `products.csv`: cada fila corresponde a un producto único que pueden comprar los clientes.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'product_name'`: nombre del producto.
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
# - `order_products.csv`: cada fila corresponde a un artículo pedido en un pedido.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'add_to_cart_order'`: el orden secuencial en el que se añadió cada artículo en el carrito.
#     - `'reordered'`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.
# - `aisles.csv`
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'aisle'`: nombre del pasillo.
# - `departments.csv`
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
#     - `'department'`: nombre del departamento.

# [Volver a Contenidos](#back)

# ## Plan de solución <a id='plan'></a>
# 
# Escribe aquí tu plan de solución para el Paso 1. Descripción de los datos.
# 
# Para iniciar con la revisión de todos los datos, vamos a importa las librerias de Pandas y matplotlib que nos serviran para crear un Data Frame por cada uno de los archivos.
# 
# De esta manera será posible revisar la información contenida en cada archivo, realizando el preprocesamiento de los datos, que incluye corregir los nombres de las columnas, rellenar valores ausentes y eliminar datos duplicados principalmente.
# 
# Finalmente, realizar el análisis de los datos, creando gráficos que nos ayuden a comprender de mejor forma la información.

# In[1]:


# importar librerías
import pandas as pd   # importamos pandas
from matplotlib import pyplot as plt   # importamos pyplot desde matplotlib


# In[2]:


# leer conjuntos de datos en los DataFrames
df_instacart_orders = pd.read_csv('/datasets/instacart_orders.csv', sep=';')
df_products = pd.read_csv('/datasets/products.csv', sep=';')
df_order_products = pd.read_csv('/datasets/order_products.csv', sep=';')
df_aisles = pd.read_csv('/datasets/aisles.csv', sep=';')
df_departments = pd.read_csv('/datasets/departments.csv', sep=';')


# In[3]:


# mostrar información del DataFrame instacart_orders:
df_instacart_orders.info()
df_instacart_orders.head()


# In[4]:


# mostrar información del DataFrame products:
df_products.info()
df_products.head()


# In[5]:


# mostrar información del DataFrame aisles:
df_aisles.info()
df_aisles.head()


# In[6]:


# mostrar información del DataFrame departments:
df_departments.info()
df_departments.head()


# <div class="alert alert-block alert-info">
# <b>Hola Alejandro, muchas gracias por tus comentarios.</b> <a class=“tocSkip”></a>
# Voy a empezar a afinar algunos detalles que no me había percatado, el primero es que agregue un parámetro: df_order_products.info(show_counts=True) para poder visualizar los valores nulos, ya que al ser muy extenso ese DataFrame, no se visualizaban por defecto.
# </div>

# In[7]:


# mostrar información del DataFrame products:
df_order_products.info(show_counts=True)   # agregamos el parámetro show_counts para visualizar los datos nulos.
df_order_products.head()


# [Volver a Contenidos](#back)

# ## Conclusiones <a id='data_review_conclusions'></a>
# 
# Descripción de los datos.
# Estas son las observaciones rápidas sobre cada uno de los DataFrames. 
# 
# df_instacart_orders
# 
#     - `Contiene información general sobre los pedidos: número de cliente 'user_id', número de pedido 'order_id', número de orden 'order_number', día del pedido 'order_dow', hora del pedido 'order_hour_of_day', y días desde el primer pedido 'days_since_prior_order'.
#     - `Contiene 6 columnas en total. Almacena 2 tipos de datos: int64(5) y float64(1).
#     - `Tiene un total de 478,967 líneas. La 5ta columna llamada 'days_since_prior_order' tiene datos faltantes, un total de 450,148 líneas.
# 
# df_products
# 
#     - `Contiene información sobre los productos: número de producto 'product_id', nombre del producto 'product_name', número del pasillo 'aisle_id', y número del departamento 'department_id'.
#     - `Contiene 4 columnas en total. Almacena 2 tipos de datos: int64(3) y object(1)
#     - `Tiene un total de 49,694 líneas. La 2da columna llamada 'product_name' tiene datos faltantes, un total de 48,436 líneas.
# 
# df_order_products
# 
#     - `Contiene información sobre las órdenes de los productos: número de orden 'order_id', código del producto 'product_id', número de orden para agregar al carrito 'add_to_cart_order', reordenamiento 'reordered'.
#     - `Contiene 4 columnas en total. Almacena 2 tipos de datos: int64(3) y float64(1).
#     - `Tiene un total de 4,545,007 líneas. 
# 
# df_aisles
# 
#     - `Contiene información sobre los pasillos: número del pasillo 'asile_id', nombre del pasillo 'asile'.
#     - `Contiene 2 columnas en total. Almacena 2 tipos de datos: int64(1) y object(1).
#     - `Tiene un total de 134 líneas. Ninguna de las 2 columnas tiene datos faltantes.
# 
# df_departments
# 
#     - `Contiene información sobre los departamentos: número del departamento 'department_id' y nombre del departamento 'department'.
#     - `Contiene 2 columnas en total. Almacena 2 tipos de datos: int64(1) y object(1).
#     - `Tiene un total de 21 líneas. Nínguna de las 2 columnas tiene datos faltantes.

# [Volver a Contenidos](#back)

# # Paso 2. Preprocesamiento de los datos
# 
# Preprocesa los datos de la siguiente manera:
# 
# - Verifica y corrige los tipos de datos (por ejemplo, asegúrate de que las columnas de ID sean números enteros).
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.
# 
# Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

# [Volver a Contenidos](#back)

# ## Plan de solución
# 
# 2. Preprocesamiento de los datos.
# 
# Antes de realizar un analisis de los datos, vamos a preprocesar cada uno de los cinco archivos para homologar la información y corregir cualquier inconsistencia que pueda existir; por ejemplo, la información correspondiente a los ID debe de ser de tipo int64 (números enteros), la descripción de los productos deberá ser de tipo objetc (string) ya que es de tipo cualitativo.
# 
# Por otra parte, también vamos a buscar por valores ausentes y/o duplicados, a los cuales vamos a revisarlos para ver si los rellenamos de alguna manera que no afecten al análisis, y en el caso de los valores duplicados, revisar si es posible eliminarlos para evitar incongruencias.

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Tom realizaste un excelente análisis exploratorio de datos. Esto te permitió establecer una hoja de ruta clara para el manejo del dataset con el fin de preparar los datos para los análisis posteriores.
# 
# </div>

# ## Encuentra y elimina los valores duplicados (y describe cómo tomaste tus decisiones).

# ### `instacart_orders` data frame

# In[8]:


# Revisa si hay pedidos duplicados
print(f"Las líneas duplicadas en el Data Frame instacart_orders son", df_instacart_orders.duplicated().sum(), "de un total de", len(df_instacart_orders), "líneas.")


# ¿Tienes líneas duplicadas? Si sí, ¿qué tienen en común?
# Encontramos que hay 15 líneas duplicadas, vamos a ver cuáles son esas 15 líneas imprimiendolas.

# In[9]:


# Basándote en tus hallazgos,
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.
df_instacart_orders[df_instacart_orders.duplicated()]   # imprimimos las 15 lineas duplicadas


# ¿Qué sugiere este resultado?
# 
# A pesar de que las líneas duplicadas que detecta el método duplicated() tienen el mismo día miércoles (día 3) y la misma hora 02:00 am (2 hra), la información de las columnas 'order_id' y 'user_id' es diferente, lo que nos da a entender que los pedidos fueron realizados por usuarios diferentes y números de orden diferentes.

# In[10]:


# De las 15 líneas duplicadas, revisamos si existen duplicados en la columna 'order_ir'
df_instacart_orders[df_instacart_orders.duplicated(subset='order_id')].value_counts()


# In[11]:


# De las 15 líneas duplicadas, revisamos si exiten valores duplicados en la columna 'user_id'
df_instacart_orders[df_instacart_orders.duplicated(subset='user_id')].value_counts()


# In[12]:


# Vuelve a verificar si hay IDs duplicados de pedidos
df_instacart_orders_duplicates = df_instacart_orders[df_instacart_orders.duplicated()]   # creamos un nuevo DataDrame con l
df_instacart_orders_duplicates.count()   # realizamos un conteo de las líneas duplicadas.


# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, en esta sección de búsqueda de duplicados, he mejorado el análisis, ya que no estaba completamente convencido de dejar las 15 líneas duplicadas, ahora he analizado esas 15 líneas en todas las demás columnas y he llegado a la misma conclusión de dejarlas pero con mayor determinación.
# </div>

# Describe brevemente tus hallazgos y lo que hiciste con ellos
# 
# En conclusión se encontraron 15 lineas que comparten la misma información en las colunmas 'order_dow' y 'order_hour_of_day', se trata de los días miércoles (3) y el horario de las 02:00am (2).
# 
# Pero revisando esas 15 líneas en específico para las demás columnas 'order_id', 'user_id' y 'days_since_prior_order', los valores son diferentes.
# En la columnas 'order_id' no hay duplicados, en la columna 'user_id' si hay 5 usuarios repetidos, pero existen valores diferentes para las columnas 'order_number' y 'days_since_prior_order', lo que nos indica que no son verdaderos duplicados.
# En la columna 'days_since_prior_order' se tienen dos valores ausentes.
# 
# Por las razones anteriores, las 15 líneas encontradas como "duplicadas", no deben considerarse como duplicadas verdaderas, finalmente se decide NO eliminarlas del Data Frame df_instacart_orders.

# [Volver a Contenidos](#back)

# ### `products` data frame

# In[13]:


# Verifica si hay filas totalmente duplicadas
print(f"Las líneas duplicadas en el Data Frame products son", df_products.duplicated().sum(), "de un total de", len(df_products), "líneas.")


# In[14]:


# Verifica si hay IDs duplicadas de productos
print(df_products[df_products.duplicated(subset='product_id')])   # filtramos el DataFrame por duplicados en números de producto


# In[15]:


# Revisa si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
df_products['product_name'] = df_products['product_name'].str.upper()   # convertimos a mayúsculas los nombres de los productos
df_products[df_products.duplicated(subset='product_name')]   # filtramos el DataFrame por duplicados el nombre del producto


# In[16]:


# Revisa si hay nombres duplicados de productos no faltantes
df_products[df_products.duplicated(subset='product_name')].value_counts()   # realizamos el conteo de los nombres de productos


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# products data frame está definico como 'df_products'
# 
# Primeramente analizamos si habían líneas duplicadas en el Data Frame de los productos, son 0 duplicados de un total de 49694 líneas.
# 
# Segundo verificamos si hay id de productos duplicados, encontrando un Empty DataFrame lo que significa que no hay.
# 
# Tercero pasamos todos los nombres de los productos a mayúsculas, para revisar si existian duplicados pero no los hay; lo que se alcanza a notar es que hay varias líneas con valores ausentes en esta columna de los nombres de los productos.
# 
# Finalmente revisamos si había nombres duplicados de productos con nombres faltantes, pero no encontramos duplicados para estos.

# [Volver a Contenidos](#back)

# ### `departments` data frame

# In[17]:


# Revisa si hay filas totalmente duplicadas
print(f"Las líneas duplicadas en el Data Frame departments son", df_departments.duplicated().sum(), "de un total de", len(df_departments), "líneas.")


# In[18]:


# Revisa si hay IDs duplicadas de productos
df_departments[df_departments.duplicated()].sum()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# En el Data Frame correspondiente a los departamentos, no se encontraron ningún valor duplicado, por lo que no se realizaron acciones.

# [Volver a Contenidos](#back)

# ### `aisles` data frame

# In[19]:


# Revisa si hay filas totalmente duplicadas
print(f"Las líneas duplicadas en el Data Frame departments son", df_aisles.duplicated().sum(), "de un total de", len(df_aisles), "líneas.")


# In[20]:


# Revisa si hay IDs duplicadas de productos
df_aisles[df_aisles.duplicated()].sum()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# En el Data Frame correspondiente a los pasillos (aisles), no se encontraron ningún valor duplicado, por lo que no se realizaron acciones.

# [Volver a Contenidos](#back)

# ### `order_products` data frame

# In[21]:


# Revisa si hay filas totalmente duplicadas
print(f"Las líneas duplicadas en el Data Frame departments son", df_order_products.duplicated().sum(), "de un total de", len(df_order_products), "líneas.")


# In[22]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
df_order_products[df_order_products.duplicated()].sum()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# En el último Data Frame de las órdenes de los productos, no se encontraron ningún valor duplicado, por lo que no se realizaron acciones algunas.

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Muy buen trabajos con los datos duplicados. Hacer una revisión de este tipo de valores es fundamental para evitar afectaciones en el comportamiento del conjunto de los datos que nos lleven a conclusiones erroneas.
# 
# </div>

# ## Encuentra y elimina los valores ausentes
# 
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
# 
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[23]:


# Encuentra los valores ausentes en la columna 'product_name'
print(df_products.isna().sum())   # realizamos el conteo de los valores ausentes en cada columna
df_products['product_name'].value_counts(dropna=False)   # filtramos los valores ausentes en la columna de los nombres de productos y los contamos


# Describe brevemente cuáles son tus hallazgos.
# 
# En el Data Frame de los productos se encuentra un total de 1,258 valores ausentes en la columna llamada 'product_name', estos se representan con las siglas NaN que significa Not a Number.

# In[24]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
df_products_missing = df_products[df_products['product_name'].isna()]   # creamos un DataFrame con los valores ausentes
df_products_missing.head(10)   # imprimimos el DataFrame filtrado con valores ausentes para revisarlo


# Describe brevemente cuáles son tus hallazgos.
# 
# En el Data Frame de productos tenemos valores ausentes en la coliumna 'product_name', revisando las primeras 10 líneas que tienen valores ausentes, notamos que todas están relacionadas con el ID del pasillo número 100.

# In[25]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
df_products_missing = df_products[df_products['product_name'].isna()]   # creamos un DataFrame con los valores ausentes
df_products_missing.sample(10)   # imprimimos una muestra aleatoria con valores ausentes para revisarlas


# Describe brevemente cuáles son tus hallazgos.
# 
# Con el nuevo Data Frame filtrado por los productos faltantes, hemos notado que el número de pasillo 100 se relaciona con el ID del departamento 21, inclusive mirando una muestra aleatoria de 10 líneas del data frame.

# In[26]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.
df_products_missing.sample(20)    # imprimimos una muestra aleatoria de 20 líneas para revisal los pasillos y departametos


# Describe brevemente cuáles son tus hallazgos.
# 
# Ya tenemos agrupado un nuevo Data Frame con valores ausentes en la columna 'product_name', la columna 'aisle_id' es igual a 100 y la columna 'department_id' es igual a 21.
# 
# Podemos notar que tanto los 'product_id' como los 'product_name' son completamente diferentes.

# In[27]:


# Completa los nombres de productos ausentes con 'Unknown'
df_products['product_name'] = df_products['product_name'].fillna('Unknown')   # rellenamos los valores ausentes con la palabra 'unknown' o desconocido en español.
df_products.isna().sum()   # realizamos la suma de los valores ausentes


# In[28]:


# Verificamos los valores marcados como 'unknown' (desconocidos)
df_products['product_name'].value_counts(dropna=False)   # Realizamos un conteo de los nombres de los productos.


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Una vez que los valores ausentes en la columna 'product_name' ya han sido sustituidos por la palabra 'Unknown' o desconocido en español.
# Volvemos a comprobar con el conteo de los valores ausentes obteniendo 0 y finalmente contando el número de veces que se repite cada nombre, obteniendo que Unknow se repite 1,258 veces, muchas más que los demás nombres con 3, 2 y 1 vez repetido cada nombre de los productos.

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, en esta sección de búsqueda y eliminación de duplicados, regresé ya que no estaba completada del todo.
# En el Data Frame de instacart_orders se tienen valores ausentes, los cuales se analizaron, se sustituyeron y cambiaron de tipo de la siguiente manera:
# </div>

# ### `instacart_orders` data frame

# In[29]:


# Encuentra los valores ausentes
print(df_instacart_orders.isna().sum())   # imprimimos la suma de los valores ausentes por columna
df_instacart_orders[df_instacart_orders.isna()]   # filtramos los valores ausentes para revisarlos


# In[30]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
df_instacart_orders_missing = df_instacart_orders[df_instacart_orders.isna()]   # creamos un DataFrame con los valores ausentes
df_instacart_orders_missing['days_since_prior_order'].value_counts(dropna=False)   # contamos los valores en la columna 'days_since_prior_order'


# In[31]:


# Rellenamos los valores ausentes en el DataFrame de ordenes de Instacart
df_instacart_orders['days_since_prior_order'] = df_instacart_orders['days_since_prior_order'].fillna(0)
print(df_instacart_orders.isna().sum())   # imprimimos la suma de los valores ausentes por columna


# In[32]:


# Se convierten los valores de la columna 'days_since_prior_order' de tipo 'float64' a tipo 'int64'
df_instacart_orders['days_since_prior_order'] = df_instacart_orders['days_since_prior_order'].astype('int64')
df_instacart_orders.info()   # imprimimos la información general para verificar el tipo de datos


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Al buscar valores ausentes en el DataFrame instacart_orders se encontraron 28,819 en 'days_since_prior_order'.
# 
# Se resguardaron todas las líneas con valores ausentes en un nuevo DataFrame llamado 'df_instacart_orders_missing'.
# 
# Finalmente se decidió reemplazar todos los valores ausentes con "0" (cero), y también se covirtieron los datos del tipo float a int64, para homologar la información de los días transcurridos desde el primer pedido.

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, en esta sección de búsqueda y eliminación de duplicados, regresé ya que no estaba completada del todo.
# En el Data Frame de order_product se tienen valores ausentes, los cuales se analizaron, se sustituyeron y cambiaron de tipo de la siguiente manera:
# </div>

# ### `order_products` data frame

# In[33]:


print(df_order_products.isna().sum())   # realizamos el conteo de los valores ausentes en cada columna
df_order_products['add_to_cart_order'].value_counts(dropna=False)   # filtramos los valores ausentes en la columna 'add_to_cart_order' y los contamos


# In[34]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?
print(df_order_products['add_to_cart_order'].min())   # valor mínimo
print(df_order_products['add_to_cart_order'].max())   # valor máximo


# Describe brevemente cuáles son tus hallazgos.
# 
# Se buscan los valores ausentes en el Data Frame de 'order_products' entonctrando 836 en la tercer columna llamada 'add_to_cart_order'.
# 
# Se revisan el mínimo (1.0) y el máximo (64.00) en la columna 'add_to_cart_order'.

# In[35]:


df_orders_products_missing = df_order_products[df_order_products['add_to_cart_order'].isna()] # Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
df_orders_products_missing   # imprimimos el data frame filtrado por valores ausentes


# In[36]:


order_id_missing = df_orders_products_missing['order_id'] # En tu nueva tabla filtrada extrae una lista con los ID de las órdenes donde hay valores ausentes.
order_id_missing   # imprimimos la lista para revisarla


# In[37]:


df_orders_missing = df_order_products[df_order_products['order_id'].isin(order_id_missing)] # Finalmente, debes comprobar si los valores de esta lista que creaste, están presentes en el resto de ID de órdenes por medio de un filtro que te devuelva una nueva tabla que puedes agrupar y contabilizar.
df_orders_missing   # imprimimos el nuevo Data Frame para revisarlo


# In[38]:


# Agrupa todos los pedidos con datos ausentes por su ID de pedido. 
df_orders_missing.groupby(by='order_id')['product_id'].count().min() # Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.


# Describe brevemente cuáles son tus hallazgos.
# 
# En general se tienen 4,544,171 de líneas en el df_product_orders con 836 valores non-null  de tipo float64.
# Se extrajo la lista de los 'order_id' para los 836 valores y se comparó contra el resto de las líneas.
# Se agruparon todos los pedidos con datos ausentes por su ID de pedido (70 líneas).
# Finalmente, se contó el número de 'product_id' en cada pedido y se revisó el valor mínimo del conteo (65)
# 
# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
# Sí, todos los pedidos tienen más de 64 productos.

# In[39]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.
df_order_products.info(show_counts=True)   # revisamos la información del Data Frame original
print()
print(df_order_products.isna().sum())   # realizamos el conteo de los valores ausentes en cada columna
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].fillna(999).astype('int64')   # reemplazamos los valores asuentes y convertimos todos en números enteros
print(df_order_products)   # imprimimos el DataFrame como quedó
print()
df_order_products.info(show_counts=True)   # revisamos la información del nuevo Data Frame


# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, ya he concluído el análisis de los valores ausentes en cada uno de los 5 Data Frames, mejorando mis resultados y abarcando cada una de las preguntas o ejercicios a realizar.
# Favor de revisarlos para ver si están bien, gracias!
# </div>

# [Volver a Contenidos](#back)

# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 2. Preprocesamiento de los datos
# 
# En el Data Frame llamado 'df_order_products' se contaba con 836 valores ausentes específicamente en la columna 'add_to_cart_order'.
# 
# Después de examinarla a detalle, juntándola con otro Data Frame llamado 'df_orders_products y el Data Frame 'df_products', obtenemos el nombre de los productos, al contarlos obtenemos un total de 285 nombres de productos, los cuales se han solicitado en al menos 1 vez cada uno de ellos.
# 
# Finalmente, después del análisis de los valores ausentes, se decide reemplazarlos por el número '999' y se convierte a tipo entero ('int64') para fines de análisis.
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Excelente trabajo con los datos faltantes, es importante saber interpretar su naturaleza y lo que singinifican en el contexto del proyecto. Más adelante aprenderás técnicas avanzadas de manejo de este tipo de datos.
# 
# </div>

# [Volver a Contenidos](#back)

# # Paso 3. Análisis de los datos
# 
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
# 
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# ### [A1] Verifica que los valores sean sensibles

# In[40]:


reasonable_orders = df_instacart_orders[df_instacart_orders['order_hour_of_day'] <= 23]   # filtramos por horario de 0 a 23 horas en la columna 'order_hour_of_day'
reasonable_orders = reasonable_orders[reasonable_orders['order_dow'] <= 6]   # filtramos por días del domingo (0) al viernes (6) en la columna 'order_dow'
print('Días de la semana (Dom-Lun-Mar-Mie-Jue-Vie-Sab)')
print(reasonable_orders['order_dow'].sort_values().unique())   # revisamos los días de la semana
print()
print('Horario de los pedidos (0-23 horas)')
print(reasonable_orders['order_hour_of_day'].sort_values().unique())   # revisamos los horarios de los pedidos
reasonable_orders


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Acá no estás comprobando que *order_hour_of_day* y *order_dow* estén en un rango razonable. Podías usar la función `unique` 
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, de acuerdo a tu recomendación utilizando el método unique ya he podido verificar el horario y días razonables en el nuevo Data Frame creado, gracias!
# </div>

# Escribe aquí tus conclusiones
# 
# Se ha creado un nuevo DataFrame para instacart orders que contiene dos límites importantes para ser razonable.
# El primero es que contenga los días de la semana, comenzando por el 0-Dom, 1-Lun, 2-Mar, 3-Mie, 4-Jue, 5-Vie y 6-Sab.
# El segundo es el horario que va de las 00 horas a las 23 horas del día.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Ahora si has comprobado que los datos estén un rango correcto.
# 
# </div>

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Tom debes responder todas las preguntas del proyecto, para que éste sea aprobado.
# 
# </div>

# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[41]:


# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
hour_orders = reasonable_orders.groupby(by='order_hour_of_day')['user_id'].count()
hour_orders.plot(kind='bar',
                 title='Pedidos por Hora',
                 xlabel='Hora del día',
                 ylabel='Usuarios'
                )
plt.show()


# Escribe aquí tus conclusiones
# 
# De acuerdo a la grráfica anterior, podemos deducir que el mayor número de pedidos se encuentra entre las 09:00 hrs y las 16:00 hrs del día.
# 
# En el resto de las horas del día, si se reciben pedidos pero con mucho menos frecuencia, en la madrugada es cuando hay menos actividad por parte de los clientes.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Tom has encontrado la distribución correcta de compras por hora.
# 
# </div>

# [Volver a Contenidos](#back)

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[42]:


# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras
days_orders = reasonable_orders.groupby(by='order_dow')['order_number'].sum()   # agrupamos por día y sumamos los pedidos
days_orders.plot(kind='bar',
                 title='Pedidos por día', 
                 xlabel='Día de la semana', 
                 ylabel='No. de Pedidos'
                )
plt.show()


# Escribe aquí tus conclusiones
# 
# Al agrupar la información por día de la semana y sumar el número de ordenes, podemos notar que los días "Domingos" (0) y "Lunes" (1) es cuando se realiza el mayor número de pedidos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Perfecto, la mayoría de compras se hacen entre domingo y lunes.
# 
# </div>

# [Volver a Contenidos](#back)

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[43]:


# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, 
# y comenta sobre los valores mínimos y máximos.
days_since_prior_order = reasonable_orders['days_since_prior_order']
days_since_prior_order.plot(kind='hist',
                            title='Días entre Pedidos',
                            bins=50,
                            xlabel='Días'
                           )
plt.show()   # imprimimos la gráfica

days_since_prior_order.min()   # valor mínimo de días
days_since_prior_order.max()   # valor máximo de días


# Escribe aquí tus conclusiones
# 
# La gráfica de distribución nos muestra que en los primeros 10 días, los clientes vuelven a realizar un pedido.
# 
# Si no lo realizan en este periodo de tiempo, se van a los 30 días para volver a pedir un nuevo producto.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Aunque estás trabajando con los datos requeridos, te estás complicando un poco. Realmente solo necesitamos ver la distribución que presentan los datos de *days_since_prior_order*, para esto no es necesario contarlos, solo debes usar una gráfica para mostrar la distrbución podrias usar un histograma, aunque dado que la información de esta columna son días (que se pueden estudiar como categorías) también puedes usar un diagrama de barras.
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, tenías razón me estaba complicando la vida yo mismo; ahora he graficado la distribución con un histograma y es más sencillo de lo que creía. ¡Gracias!
# </div>

# [Volver a Contenidos](#back)

# # [B] Intermedio (deben completarse todos para aprobar)
# 
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[44]:


wednesday = df_instacart_orders[df_instacart_orders['order_dow'] == 3]   # filtramos por miércoles
saturday = df_instacart_orders[df_instacart_orders['order_dow'] == 6]   # filtramos por sábado


# In[45]:


wed_sat = pd.concat([wednesday, saturday])   # concatenamos los DF's de miércoles y sábado
wed_sat


# In[46]:


wed_sat_mean = wed_sat.groupby(by='order_dow')['order_hour_of_day'].plot(kind='hist', bins=40, alpha=0.7, xlabel='Hora', title='Miércoles vs Sábado')
plt.legend(['Miércoles', 'Sábado'])   # leyenda
plt.show()


# Escribe aquí tus conclusiones
# 
# Primeramente se separaron los dataframes, filtrando por día uno para miércoles y otro para sábado.
# 
# Seguido se concatenaron por filas para dejarlos en un mismo data frame.
# 
# Se grafica con un histograma para comparar la frecuencia de pedidos conforme al horario de cada uno de los días,
# viendo que son muy similares ya que a partir de las 6:00 am hasta las 23:00 hrs, el número de frecuencia es muy similar.
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Muy buen trabajo comparando los datos de los días miércoles y sábado. Al parecer hay un descenso de uso en horas de medio día para el miércoles, posiblemente porque sea el momento de almorzar.
# 
# </div>

# [Volver a Contenidos](#back)

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[47]:


df = df_instacart_orders.groupby('user_id')['order_id'].count() # agrupamos el DataFrame de órdenes por id de usuario y contamos el número de pedidos
df.plot(kind='hist', 
        title='Pedidos por cliente', 
        bins=60
       )
plt.show()   # imprimimos el histograma


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Para dar respuesta a esta pregunta, puedes agrupar la información de **df_instacart_orders** por *user_id* y luego contar las ordenes (*order_id*). Con esta información tienes los datos para mostrarlos como una distribución. Recuerda que siempre que te hablen o pidan una distribución es necesario usar gráficas acorde a esto, puede ser un histograma.
# 
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, te agradezco la explicación de las distribuciones, en realidad no me habían quedado totalmente claras del todo. ¡Gracias!
# </div>

# Escribe aquí tus conclusiones
# 
# Para realizar este ejercicio agrupamos el DataFrame 'df_instacart_orders' por id de usuario 'user_id' y contamos el número de pedidos 'order_id', lo que nos da una distribución que relaciona el número de pedidos por cliente.
# 
# Lo que nos da a entender es que baja la frecuencia de los pedidos con relación a la mayor cantidad de clientes.

# [Volver a Contenidos](#back)

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[80]:


df_merged = df_order_products.merge(df_products, on='product_id')   # juntamos los Data Frames de 'ordenes' con el de 'productos'
df_merged   # visualizamos el nuevo Data Frame


# In[81]:


count_products = df_merged['product_name'].value_counts().sort_values(ascending=False)   # realizamos el conteo de los nombres de los productos y ordenamos de manera descendiente
top_20 = count_products.head(20)  # filtramos los primeros 20 productos
top_20 = top_20.reset_index()   # reseteamos los índices
top_20.columns = ['product_name', 'frequency']   # renombramos las columnas
top_20   # visualizamos la lista


# In[82]:


top_20.plot(kind='bar', x='product_name', y='frequency', title='Top 20', xlabel='Productos', ylabel='Frecuencia')   # seteamos los valores para la gráfica
plt.show()   # imprimimos la gráfica


# Escribe aquí tus conclusiones
# 
# Primeramente se realizó un merge con los Data Frames de 'order_products' y el 'df_products'.
# 
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Genial, has encontrado el top 20 de productos más populares.
# 
# </div>

# [Volver a Contenidos](#back)

# # [C] Difícil (deben completarse todos para aprobar)
# 
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[83]:


data_order = df_order_products.groupby('order_id')['product_id'].count() # 
data_order


# In[84]:


data_ordered_products = data_order.value_counts().sort_index()
data_ordered_products
data_ordered_products.columns = ['product_order', 'frecuency']


# In[85]:


data_ordered_products.plot(x='product_order',
                           y='frecuency',
                           title='Productos Solicitados', 
                           kind='bar',
                           log=True
                          )
plt.show()


# Escribe aquí tus conclusiones

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Aunque la información es correcta, el histograma no nos da mucha información, podrías optar por definir `kind = 'bar'`, para tener una mejor visualización de los datos.
# 
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, aun no me queda claro del todo cómo debe verse la gráfica de barras para esta distribución.
# </div>

# [Volver a Contenidos](#back)

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[54]:


products_reordered = df_order_products[df_order_products['reordered'] == 1] 
products_reordered


# In[55]:


popular_products = products_reordered['product_id'].value_counts().sort_values(ascending=False)
top_20 = popular_products.head(20)
top_20 = top_20.reset_index()
top_20.columns = ['product_id', 'frequency']
top_20


# In[56]:


top_20_names = top_20.merge(df_products, on='product_id')
top_20_names.drop(['aisle_id', 'department_id'], axis='columns', inplace=True)
top_20_names


# In[57]:


top_20_names.plot(x='product_name',
                  y='frequency',
                  kind='bar',
                  title='Artículos Top 20',
                  xlabel='Nombre del Artículo',
                  ylabel='Frecuencia de pedido',
                  legend=False
                  )
plt.show()


# Escribe aquí tus conclusiones

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Perfecto Tom, has encontrado el top 20 de productos que son más "re-ordenados" por los usuarios. 
# 
# </div>

# [Volver a Contenidos](#back)

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Acá debes usar la información de la columna *reordered* del dataset **df_order_products**. Si combinamos la información de este dataset con el de **df_products** y agrupamamos por *product_id* y *product_name*, podemos determinar la proporción sacando el promedio de *reordered*, teniendo en cuenta que esta columna solo maneja valores de 1 y 0
# </div>

# In[58]:


df_products_merged = df_order_products.merge(df_products, on='product_id') # combinamos los DataFrames por el número de ID de producto
df_products_merged   # echamos un vistazo al dataframe


# In[64]:


# Proporción de las veces que se pide una sola vez cada producto
once_ordered = df_products_merged[df_products_merged['reordered'] == 0] # agrupamos por id de producto y sacamos el promedio de la comuna reordenamiento
once_ordered.groupby('product_name')['order_id'].mean()


# In[65]:


# Proporción de las veces que se vuelve a pedir un porducto
reordered = df_products_merged[df_products_merged['reordered'] == 1] # agrupamos por nombre de producto y sacamos el promedio de la comuna reordenamiento
reordered.groupby('product_name')['order_id'].mean()


# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, aun no estoy seguro si estas distribuciones son correctas.
# </div>

# Escribe aquí tus conclusiones

# [Volver a Contenidos](#back)

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[67]:


client_behaviour = df_order_products.merge(df_instacart_orders, on='order_id') # combinamos los DataFrames por el número de ID de pedido
client_behaviour.drop(['order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order'], axis='columns', inplace=True) # eliminamos las columnas inecesarias
client_behaviour # echamos un vistazo


# In[62]:


client_order = client_behaviour.groupby('user_id')['reordered'].sum() # agrupamos el DataFrame por Usuario y sumamos si se ha reordenado
client_reordered = client_behaviour.groupby('user_id')['product_id'].count() # agrupamos el DataFRame por Usuario y contamos los ID de producto


# In[69]:


client_rate = client_order / client_reordered
client_rate


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# La proporción que has encontrado de "re-ordenenes" por usuario es correcta. Buen trabajo.
# 
# </div>

# Escribe aquí tus conclusiones

# [Volver a Contenidos](#back)

# ### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (2da Iteración)</b> <a class=“tocSkip”></a>
# 
# Acá debes hacer un conteo similar al los que has hecho en las preguntas relacionadas con ***top 20***, pero para esta pregunta debes considerar la información de la columna *add_to_cart_order*, ya que aquellos productos que tengan esa columna con valor de 1, quieren decir que son los primeros en se añadidos al carrito de compras. Ya con eso puedes hacer el conteo y luego definir el top 20.
# 
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# Alejandro, muchas gracias por los tips, ya me ha quedado bien claro como hacer estos útimos ejercicios. ¡Saludos!
# </div>

# In[86]:


df_merged = df_order_products.merge(df_products, on='product_id')   # juntamos los Data Frames de 'ordenes' con el de 'productos'
top_products = df_merged[df_merged['add_to_cart_order'] == 1] # filtramos los productos que se han agregado primero al carrito
top_products # echamos un vistazo al Data Frame


# In[87]:


count_products = top_products['product_name'].value_counts().sort_values(ascending=False)   # realizamos el conteo de los nombres de los productos y ordenamos de manera descendiente
top_20_first = count_products.head(20)  # filtramos los primeros 20 productos
top_20_first = top_20_first.reset_index()   # reseteamos los índices
top_20_first.columns = ['product_name', 'frequency']   # renombramos las columnas
top_20_first   # visualizamos la lista


# In[88]:


top_20_first.plot(x='product_name',
                  y='frequency',
                  kind='bar',
                  title='Artículos Top 20',
                  xlabel='Nombre del Artículo',
                  ylabel='Frecuencia de pedido',
                  legend=False
                 )
plt.show()


# Escribe aquí tus conclusiones
# 
# El método para obtener este top_20_first fue:
# 
# 1. Juntamos los Data Frames de 'ordenes' con el de 'productos'
# 2. Filtramos los productos que se han agregado primero al carrito
# 3. Realizamos el conteo de los nombres de los productos y ordenamos de manera descendiente
# 4. Filtramos los primeros 20 productos
# 5. Reseteamos los índices y renombramos las columnas
# 6. Visualizamos la lista y la graficamos
# 
# En conclusión, este Top 20 de productos que son agregados al carrito al principio, es diferente de los otros 2 Top 20 de artículos, lo que nos puede dar una idea de los artículos más escenciales en la canasta de cada usuario.

# [Volver a Contenidos](#back)

# ### Conclusion general del proyecto:

# Este Proyecto ha sido un proyecto bastante extenso y me ha costado muchas horas de estudio y repaso.
# En general me ha costado algo la comprensión de los ejercicios; sin embargo, una vez captada la idea, se vuelven fáciles.
# 
# EL primer Paso de Descripción de los datos, me ha servido bastante el describir lo mejor posible cada uno de los Data Frames, sus columnas, qué tipo de datos contiene y enlistarlos ha sido de gran ayuda para los siguientes 2 pasos. Así como también el imprimirlos, me ha dado una primera visión de cómo lucen y que se debe considerar para revisión, si es necesario corregir, etc.
# 
# El segundo Paso de Preprocesamiento de los datos, ha sido bastante retador, ya que no sólo hay que corregir los tipos de datos para homologarlos, también ha sido necesario analizar a fondo los datos duplicados para saber si se elimnana o no; sino que también se han tenido que completar los valores ausentes en algunos DataFRames. Todo lo anterior para cada uno de los cinco Data Frames, lo cual ha sido bastante tiempo invertido en sólo limpiar los datos.
# 
# El tercer y último paso de Análisis de los datos, ha tenido su grado de dificultad pero me agradó mucho ya que una vez coprendido como realizar una distribución, el hacer gráficos de diferentes tipos me ha servido de mucha ayuda para prácticar.
# Se han encontrado datos muy interesantes en esta última sección, lo cual sin duda será información muy valiosa para nuestros clientes o las personas que lean el reporte.
# 
# Para terminar, me ha agradado mucho el ver que lo que se ha aprendido hasta el momento en el Bootcamp, es muy util para resolver problemas comunes de una empresa muy común hoy en día.
# 

# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# No olvides incluir tus interpretaciones y conclusiones sobre el caso de estudio.
# 
# </div>
