# EJERCICIO 1
#
# Se ha añadido información sobre una nueva clienta, Nina Brown, a la lista de clients.
# El banco está interesado en su ingreso neto anual, que se sitúa en la 4ª posición de la lista. 
# Nuestro objetivo es extraer esta información, asignarla a la variable client_income y mostrarla en pantalla.
#
# La salida esperada es esta: 250000

clients = [
    [32456, 'Jack Wilson', 32, 150000, 'Personal sanitario'],
    [34591, 'Nina Brown', 45, 250000, 'Telecomunicaciones']
]

client_income = clients[1][3] # escribe tu código aquí
print(client_income)


# EJERCICIO 2
#
# El número de clientes crece rápidamente. 
# Dos clientes más se han unido recientemente al servicio y ya figuran en la lista de clients. 
# Tu trabajo es calcular la edad promedio de nuestros clientes.
# La salida esperada es esta: 36.25

clients = [
    [32456, 'Jack Wilson', 32, 150000, "Personal sanitario"],
    [34591, 'Nina Brown', 45, 250000, "Telecomunicaciones"],
    [37512, 'Alex Smith', 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transporte"],
]

avg_age = (clients[0][2] + clients[1][2] + clients[2][2] + clients[3][2]) / len(clients) # escribe tu código aquí
print(avg_age)

# Fin.