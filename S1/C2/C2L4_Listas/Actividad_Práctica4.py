# Tarea 1
# En el siguiente código hay algunos errores. 
# Implementa una solución try-except que detecte el error ZeroDivisionError y muestre el mensaje No es posible dividir entre cero.
# La salida esperada es esta: No es posible dividir entre cero

numerator = 10
denominator = 0
# escribe tu código aquí
try:
    result = numerator / denominator
    print(result)
except:
    print('No es posible dividir entre cero')