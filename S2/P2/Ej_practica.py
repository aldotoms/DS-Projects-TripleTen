# Ejercicio de Practica

# En caso de que sientas que necesitas más práctica antes de abordar el proyecto, he preparado algunas tareas adicionales para ti. 
# Este Jupyter notebook contiene ejercicios similares a los del proyecto. Intenta resolverlos y revisa la clave de respuestas que se proporciona al final.
# La solución para estos ejercicios se encuentra al final del Jupyter notebook, así que puedes comprobarlos tras resolverlos. 
# Esto es completamente opcional, puedes ir directamente al proyecto si te sientes preparado.
# ¡Buena suerte y disfruta trabajando en tu proyecto!

# Mejoremos nuestra práctica del capítulo anterior y resolvamos algunas tareas más del Banco ABC.
# El banco analizó la lista de sus clientes y encontró más clientes de interés para prestar servicios bancarios privilegiados. 
# Se agregaron a nuestra lista anterior.

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
]

### Ejercicio 1

# Los departamentos de seguridad del banco no quedaron satisfechos con la forma en la que presentamos la lista de clientes la última vez. 
# Esta vez nos pidieron que proporcionáramos los nombres de los clientes imprimiendo cada nombre en una línea separada.
# Haz un bucle en la lista de clientes y muestra sus nombres.

# escribe tu código aquí
for client in clients:
    name = client[1]
    print(name)


### Ejercicio 2

# El departamento de marketing del Banco ABC está interesado en conocer la edad promedio de su clientela. 
# La edad promedio es simplemente la suma de las edades de todos los clientes dividida entre la cantidad de clientes. 
# Utiliza el bucle for para iterar sobre la lista `clients` y actualiza las variables `total_age` y `num_clients` en cada iteración del bucle.
# La variable `total_age` debe almacenar la suma de edades, mientras que la variable `num_clients` se usa para almacenar el número total de clientes.
# Las variables `total_age` y `num_clients` ya están declaradas para que hagas tus cálculos con ellas. 
# Tras recorrer la lista y actualizar estas dos variables, calcula la edad promedio de todos los clientes, almacénala en la variable `average_age` y muéstrala.

total_age = 0
num_clients = 0

# escribe tu código aquí
for client in clients:
    total_age += client[2]
    num_clients = len(clients)

average_age = total_age / num_clients
print('La edad promedio de los clientes es de', int(average_age),'anos.')


### Ejercicio 3

# La gerencia está interesada en saber cuándo un cliente alcanza un millón en ingresos totales y te pidieron que escribieras un código 
# que calcule la cantidad de años que necesita un cliente para alcanzar este número. 
# Para empezar, te pidieron que probaras tu código para 'Jack Wilson', que gana 150000 al año. 
# Escribe un bucle while que sume los ingresos anuales totales de Jack hasta que llegue a un millón. 
# Una vez que lo alcance, muestra el número de años que tardó en alcanzar este ingreso total.

annual_income = 150_000 # ingreso anual de Jack
target_income = 1_000_000 # ingreso objetivo

total_income_sum = 0 # ingresos totales que se actualizarán para cada año
years_to_million = 0 # cantidad de años que también se actualizará

while total_income_sum < target_income:
    total_income_sum += annual_income
    years_to_million += 1

print('El numero de anos que tardo', clients[0][1], 'en alcanzar el ingreso total de', target_income, 'fue de', years_to_million, 'anos.')


### Ejercicio 4

# El Banco ABC ha presentado una nueva cuenta Elite diseñada para clientes y clientas de alto poder adquisitivo que ganan más de $200 000 al año. 
# Escribe código para iterar sobre los clientes, comprueba que sus ingresos anuales superen los $200 000 y agrega la sublista sobre un cliente elegible 
# a la variable elite_clients, que es una lista de clientes ricos. 
# Muestra la variable elite_clients al final.

elite_clients = [] # añade la variable elite_clients aquí
anual_income_elite_clients = 200_000

# escribe tu código aquí
for client in clients:
    income = client[3]
    if income >= anual_income_elite_clients:
        elite_clients.append(client)

print(elite_clients)


### Ejercicio 5

# El departamento de marketing quiere una lista de todos los clientes del banco, dividida en cuatro segmentos de cuenta. 
# Te han pedido que les presentes la lista. Divide a todos los clientes del Banco ABC en cuatro segmentos: 
# - la cuenta Standard para los clientes con ingresos inferiores a $100 000 (exclusive), 
# - la cuenta Plus para ingresos de $100 000 (inclusive) a $200 000 (exclusive), 
# - la cuenta Elite para ingresos de $200 000 (inclusive) a $300 000 (exclusive), 
# - y la cuenta Executive para ingresos de $300 000 (inclusive) o más.
# En el precódigo a continuación, verás cuatro variables con las listas: standard, plus, elite y executive. 
# Escribe código para iterar sobre los clientes, comprueba a qué categoría pertenecen sus ingresos y agrégalos a la lista correspondiente. 
# Muestra la lista de clientes executive al final.

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vacías para agregar clientes y clientas
standard = []
plus = []
elite = []
executive = []

# escribe tu código aquí
for client in clients:
    if client[3] < 100_000:
        standard.append(client)
        
    elif client[3] >= 100_000 and client[3] < 200_000:
        plus.append(client)
        
    elif client[3] >= 200_000 and client[3] < 300_000:
        elite.append(client)
        
    elif client[3] >= 300_000:
        executive.append(client)

print(executive)


### Ejercicio 6

# Es el Día de la Juventud y el equipo de marketing desea enviar un correo electrónico para atraer a nuestros clientes jóvenes.
# Para mejorar la solución anterior, debemos actualizar los criterios de edad para identificar a los clientes jóvenes.
# Hemos actualizado el código anterior con las nuevas categorías juveniles, pero necesitas añadir filtros de edad a tus filtros de ingresos previos para que funcionen como se espera. 
# Las reglas son las siguientes:

standard_young: # Ingreso anual inferior a $100 000 (exclusive) Y la edad es menor a 40 años (exclusive).
plus_young: # Ingreso anual de $100 000 (inclusive) a $200 000 (exclusive) Y la edad es menor a 35 años (exclusive).
elite_young: # Ingreso anual de $200 000 (inclusive) a $300 000 (exclusive) Y la edad es menor a 35 años (exclusive).
executive_young: # Ingreso anual superior a $300 000 (inclusive) Y la edad es menor a 35 años (exclusive).

# Por favor, proporciona listas actualizadas con base en estas reglas y luego mostrar de nuevo solo la lista incluyendo los clientes "executive young".
# Los comentarios que aparecen en el precódigo te ayudarán a realizar los cambios necesarios. 
# Por favor, préstales atención. Si tienes dificultades, no dudes en consultar la pista que te hemos dejado.

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

standard_young = []
plus_young = []
elite_young = []
executive_young = []

for client in clients:
    if client[3] < 100_000 and client[2] < 40:
        standard_young.append(client)
    
    elif client[3] >= 100_000 and client[3] < 200_000 and client[2] < 35:
        plus_young.append(client)
    
    elif client[3] >= 200_000 and client[3] < 300_000 and client[2] < 35:
        elite_young.append(client)
    
    elif client[3] >= 300_000 and client[2] < 35:
        executive_young.append(client)

# no modifiques nada por debajo de esta línea
print(executive_young)


### Ejercicio 7

# El equipo de gestión del Banco ABC te ha pedido que reorganices nuestra lista de clientes para que puedan acceder a los datos con mayor facilidad.
# En el siguiente precódigo, hemos inicializado una lista llamada clients_dict. 
# Tu objetivo es llenar esta lista con diccionarios, donde cada diccionario contiene información sobre un cliente de la lista clients. 
# En otras palabras, queremos que transformes cada lista de la lista clients en un diccionario y adjuntes este diccionario a la lista clients_dict.
# Utiliza las siguientes claves para cada diccionario que crees y adjuntes:

# "id"
# "client_name"
# "age"
# "yearly_income"
# "work_field"

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# primero, crea un diccionario utilizando llaves
# client_dict = {}

# escribe tu código aquí
for client in clients:
    client_info = {"id": client[0],
                   "client_name": client[1],
                   "age": client[2],
                   "yearly_income": client[3],
                   "work_field": client[4]}
    print(client_info)
    # luego agrega este diccionario a clients_dict
    # client_dict[client_info] = client

# print(client_dict)


### Ejercicio 8

# A continuación, el departamento de marketing de ABC se interesa por el nivel de ingresos de cada área en el que trabajan sus clientes. 
# Te pidieron que recopilaras los ingresos de la clientela para cada área.
# En el precódigo, de forma similar al ejercicio anterior, verás de nuevo la lista clients. 
# Aquí la tienes por si quieres mirarla de nuevo:

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# Además de eso, en el precódigo, inicializamos un diccionario llamado incomes_per_field. Tu objetivo es llenarlo. 
# Las claves serán las áreas en las que trabajan los clientes de ABC 
# y los valores serán listas con los ingresos de todos los clientes de ABC que trabajan en cada área correspondiente. 
# A continuación se muestra un ejemplo de un par clave-valor:

"Healthcare": [150000, 193000]

# La clave es el área ("Healthcare") y los valores son dos ingresos de dos clientes de la lista clients que trabajan en "Healthcare" (Salud).
# Para llenar el diccionario incomes_per_field, itera sobre la lista clients y extrae el nombre del área y los ingresos de cada cliente. 
# A continuación, comprueba si el área extraído existe en el diccionario incomes_per_filed:
# - Si no es así, agrégalo como clave y establece una lista con un único ingreso como valor.
# - Si existe, añade el ingreso a la lista de ingresos.

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

incomes_per_field = {} # aquí colocarás los ingresos para cada área

# primero, extrae el nombre del área
# segundo, extrae los ingresos

for client in clients:
	field = client[4]
	income = client[3]
	if incomes_per_field.get(field) == None:    # comprueba si el área extraído NO está en el diccionario incomes_per_field
		incomes_per_field[field] = [income]     # añade un nuevo área como clave y establece una lista como valor
	else:
		incomes_per_field[field].append(income) # si el área extraído está en el diccionario incomes_per_field
        # añade el nuevo ingreso a la lista de ingresos para un área en particular

# no modifiques el código de abajo, ya que imprime el resultado
print(incomes_per_field)


### Ejercicio 9

# Empecemos por escribir una función llamada filter_clients para filtrar la lista de clientes por el área de trabajo del cliente. 
# Esta función recibirá dos parámetros: clients_list (la lista de clientes) y field (el área a buscar). 
# La función recorrerá cada cliente de la lista y, si encuentra un cliente con el área especificado, añadirá la información sobre este cliente a una nueva lista. 
# Esta lista se devolverá como resultado de la ejecución de la función cuando concluya.
# Para probar, llama a la función para el área "Transportation". A continuación, imprime la lista filtrada (ya en el precódigo).

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# crea aquí tu función filter_clients
def filter_clients(clients_list, field):
    new_list = []
    for client in clients_list:
        if field in client[4]:
            new_list.append(client)
    return new_list

filtered_list = filter_clients(clients, "Transportation")  # llama a la función aquí

# muestra el resultado aquí
print(filtered_list)


### Ejercicio 10
# ¡Vamos a hacerlo aún más flexible! Escribe otras dos funciones similares a la anterior y llámalas así:
# filter_age() y filter_income()
# En la primera, utilizaremos como filtro la edad con el valor por defecto de 0 mientras que en la segunda función, 
# utilizaremos como filtro los ingresos con un valor por defecto también fijado en 0.
# Establece clients como valor por defecto en el parámetro clients_list para ambas funciones de la misma forma que hiciste en la tarea anterior.
# Ambas funciones deben filtrar los clientes que tienen valores mayores que el valor pasado como argumento en la llamada a la función.
# Llama a la función filter_age() y filtra la lista clients, extrayendo los datos de clientes que son mayores de 40 años. Guarda los resultados en la variable filtered_age.
# De la misma manera, llama a la función filter_income() y filtra la lista clients, extrayendo solo los clientes que tengan ingresos superiores a 250 000. 
# Guarda los resultados en la variable filtered_income.
# Imprime las variables filered_age y filtered_income (ya en el precódigo).

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# escribe aquí dos funciones de filtrado: filter_age y filter_income
def filter_age(client_list, age):
    new_list = []
    for client in client_list:
        if age < client[2]:
            new_list.append(client)
    return new_list

def filter_income(client_list, income):
    new_list = []
    for client in client_list:
        if income < client[3]:
            new_list.append(client)
    return new_list

filtered_age = filter_age(clients, 40) # llama a la función filter_age aquí
filtered_income = filter_income(clients, 250000) # llama a la función filter_income aquí

# muestra el resultado
print(filtered_age)
print(filtered_income)


### Fin.

