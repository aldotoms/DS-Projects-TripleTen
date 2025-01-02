# Capítulo 4/6 · Faltan 3 lecciones
# Trabajar con valores duplicados y ausentes

# *Ejercicios

# Ejercicio 1
# Recuerda que queremos comparar el tiempo promedio que pasan en el sitio web las personas que utilizan dispositivos móviles y de escritorio, 
# luego usaremos esos tiempos promedio para rellenar los valores ausentes.
# Comienza dividiendo los datos en dos DataFrames: uno para visitas desde dispositivos de escritorio y otro para visitas desde dispositivos móviles. 
# Asigna las visitas de escritorio a una variable llamada desktop_data y las visitas móviles a otra variable llamada mobile_data.
# El precódigo ya lee los datos y rellena los valores ausentes de 'age'. 
# Este también llama a info() por ti después de crear tus DataFrames filtrados para que puedas ver cuántos valores ausentes hay para cada dispositivo.

# Código:
import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop'] # completa esta línea
mobile_data =  analytics_data[analytics_data['device_type'] == 'mobile'] # completa esta línea

desktop_data.info()
print()
mobile_data.info()

# Resultado:

<class 'pandas.core.frame.DataFrame'>
Int64Index: 73764 entries, 0 to 99999
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   user_id      73764 non-null  int64  
 1   device_type  73764 non-null  object 
 2   age          73764 non-null  float64
 3   time         61588 non-null  float64
dtypes: float64(2), int64(1), object(1)
memory usage: 2.8+ MB

<class 'pandas.core.frame.DataFrame'>
Int64Index: 26236 entries, 1 to 99997
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   user_id      26236 non-null  int64  
 1   device_type  26236 non-null  object 
 2   age          26236 non-null  float64
 3   time         13823 non-null  float64
dtypes: float64(2), int64(1), object(1)
memory usage: 1.0+ MB


# Ejercicio 2
# Ahora que los datos de escritorio y móviles están separados, calcula el tiempo medio de visita para cada dispositivo.
# Asigna la media del tiempo de visita de los usuarios de escritorio a una variable llamada desktop_avg y la media de los usuarios móviles a mobile_avg. 
# El precódigo ya contiene el código para imprimir tus resultados.

# Código:

import pandas as pd

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
mobile_data =  analytics_data[analytics_data['device_type'] == 'mobile']

desktop_avg = desktop_data['time'].mean() # completa esta línea
mobile_avg =  mobile_data['time'].mean() # completa esta línea

print(f"Tiempo de escritorio promedio: {desktop_avg:.2f} segundos")
print(f"Tiempo móvil promedio: {mobile_avg:.2f} segundos")

# Resultado: 
# Tiempo de escritorio promedio: 1741.87 segundos
# Tiempo móvil promedio: 41.16 segundos


# Ejercicio 3
# Utiliza el tiempo promedio de visita de escritorio para rellenar los valores ausentes en la columna 'time' de desktop_data y el tiempo promedio de visita móvil para rellenarlos en mobile_data.
# El precódigo contiene tu trabajo de las tareas anteriores y llama a info() para que compruebes que los valores ausentes se hayan rellenado.
# Es posible que también hayas visto un SettingWithCopyWarning cuando ejecutaste tu código. 
# No hay nada de que preocuparse en este caso, pero si deseas obtener más información al respecto consulta la documentación (materiales en inglés).

# Código:

import pandas as pd
pd.options.mode.chained_assignment = None
import warnings
warnings.filterwarnings('ignore')

analytics_data = pd.read_csv('/datasets/web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
mobile_data =  analytics_data[analytics_data['device_type'] == 'mobile']

desktop_avg = desktop_data['time'].mean()
mobile_avg = mobile_data['time'].mean()

# escribe tu código aquí para rellenar los valores ausentes
desktop_data['time'] = desktop_data['time'].fillna(desktop_avg)
mobile_data['time'] = mobile_data['time'].fillna(mobile_avg)

# esto comprobará si tienes algún valor ausente
desktop_data.info()
print()
mobile_data.info()

# Resultado:

<class 'pandas.core.frame.DataFrame'>
Int64Index: 73764 entries, 0 to 99999
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   user_id      73764 non-null  int64  
 1   device_type  73764 non-null  object 
 2   age          73764 non-null  float64
 3   time         73764 non-null  float64
dtypes: float64(2), int64(1), object(1)
memory usage: 2.8+ MB

<class 'pandas.core.frame.DataFrame'>
Int64Index: 26236 entries, 1 to 99997
Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   user_id      26236 non-null  int64  
 1   device_type  26236 non-null  object 
 2   age          26236 non-null  float64
 3   time         26236 non-null  float64
dtypes: float64(2), int64(1), object(1)
memory usage: 1.0+ MB

# Fin.