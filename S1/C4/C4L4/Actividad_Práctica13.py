# EJERCICIO 1
# La información sobre Brian Pérez ha sido actualizada. Además, otros dos clientes se han unido recientemente al servicio.
# hora el banco quiere analizar a los clientes para determinar la distribución de edades de mayor a menor.
#
# En el precódigo, encontrarás la variable ages que contiene las edades de todos los clientes actuales.
# Nuestro objetivo es ordenar esta lista en orden descendente y mostrarla. Para ordenar, utiliza el método sort().
# La salida esperada es esta: [45, 39, 32, 32, 29, 25]

ages = [32, 45, 39, 29, 25, 32]
ages.sort(reverse=True)# escribe tu código aquí
print(ages)

# Resumen
# Saber ordenar listas es importante para organizar los datos y facilitar su búsqueda, análisis y presentación.
#
# El método sort():
# - Modifica la lista original.
# - Ordena los elementos en orden ascendente por defecto.
# - Puedes ordenar en orden descendente utilizando reverse=True.
#
# La función sorted():
# - Devuelve una nueva lista ordenada.
# - Útil cuando necesitas mantener intacta la lista original.
# - También puedes ordenarla en orden descendente con reverse=True.
#
# Fin.