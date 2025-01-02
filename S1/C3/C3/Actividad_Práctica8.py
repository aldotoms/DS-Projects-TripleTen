# EJERCICIO 1
# En la siguiente tarea tenemos como objetivo el implementar algunas operaciones de división 
# que reciben dos variables, numerador y denominador.
# Tu tarea es completar esta implementación, incluyendo una lógica try-except que manejará los diferentes tipos de errores.
#
# Para ello, debes completar los siguientes pasos:
# 1.-Efectúa la operación de división dentro de try utilizando las variables numerador y denominador para ello. 
#    Muestra el siguiente mensaje, combinando el método print() con el F-string:
#    "El resultado de dividir 100 entre 10 es 10.0"
# 
# 2.-Cuando ocurre ZeroDivisionError, despliega el siguiente mensaje utilizando el método print() combinado con el F-string:
#    Error: No se puede dividir 100 entre 0.
#
# 3.-Cuando ocurra TypeError, despliega el siguiente mensaje:
#    Error: Tanto el numerador como el denominador deben ser números.
# 
# La salida esperada es esta:
# Error: No es posible dividir 100 entre 0.
# El resultado de dividir 100 entre 10 es 10.0
# Error: Tanto el numerador como el denominador deben ser números.

a = 100
b = 0
c = 10

# Primera división
try:
    resultado = a / b
    # Uso de un F-string para formatear la salida
    print(f"El resultado de dividir {a} entre {b} es {resultado}")
except ZeroDivisionError:
    # Manejo de la división entre cero
    print(f"Error: No es posible dividir {a} entre {b}.")

# Segunda división
    resultado = a / c
    # Uso de un F-string para formatear la salida
    print(f"El resultado de dividir {a} entre {c} es {resultado}")

# Tercera división
try:
    resultado = a / 'a'
    # Uso de un F-string para formatear la salida
    print(f"El resultado de dividir {a} entre 'a' es {resultado}")
except TypeError:
    # Manejo de los tipos de entradas incorrectas
    print("Error: Tanto el numerador como el denominador deben ser números.")

# Fin.