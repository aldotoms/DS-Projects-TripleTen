# Ejercicio 1
# Vamos a mostrar los tipos de las variables avg_height_men_cm y avg_height_women_cm.
# La salida esperada es esta: 
# <class 'float'>
# <class 'str'>

avg_height_men_cm = 183.70
avg_height_women_cm = ' 170.36 '

print(type(avg_height_men_cm))
print(type(avg_height_women_cm))

# Ejercicio 2
# Ahora calcula la altura promedio average de los hombres y mujeres y almacénalas en la variable average_height.
# Ten en cuenta que podrías necesitar cambiar primero el tipo de datos de una de las variables. 
# Muestra el resultado en la pantalla.
# La salida esperada es esta: 177.07

avg_height_women_cm = float(avg_height_women_cm)

average_height = (avg_height_men_cm + avg_height_women_cm) / 2
average_height = float(average_height)

print(average_height)
print(type(average_height))

# Ejercicio 3
# Convierte la variable share_english en flotante y ejecuta de nuevo el código antes de enviar tu respuesta.
# La salida esperada es esta: 
# <class 'float'>
# 0.639

share_english = '0.539'

share_english = float(share_english)

print(type(share_english))
print(share_english + 0.1)
