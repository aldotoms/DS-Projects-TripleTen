# MODIFICACION DE LISTAS
#
# Si comparamos las listas y los strings con lo que hemos aprendido hasta ahora, podemos concluir que estas estructuras de datos son bastante similares. 
# Sin embargo, hay una diferencia significativa que las distingue: las listas de Python son mutables, mientras que los strings son inmutables.
# Esto significa que puedes agregar, cambiar o eliminar elementos de una lista, mientras que cualquier modificación de un string crea un nuevo string en lugar de alterar el original.
# En esta lección, aprenderás y harás uso de la capacidad mutable de las listas.
# Lo que aprenderas: 
#  - Cómo agregar elementos a una lista.
# - Cómo eliminar elementos de una lista.

# Existen dos modos principales de añadir elementos a una lista:
# 1.- al final de esta;
# 2.- en una posición de índice específica.
# Vamos a examinarlos con más detalle.

# Agregar elementos al final de la lista
# En función de lo que quieras hacer, puedes añadir uno o varios elementos a tu lista. 
# Utiliza el método append() si quieres añadir un elemento a tu lista.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Si necesitas agregar varios elementos, utiliza el método extend().

my_list = [1, 2, 3]
my_list.extend([4, 5, 6]) # similar al operador aritmético +
print(my_list)

# Agregar elementos en una posición específica
# El método insert() permite añadir un elemento en una posición específica dentro de la lista. 
# Toma dos argumentos:
# 1) El índice, el lugar donde quieres insertar el elemento.
# 2) El propio elemento a insertar.

my_list = [1, 2, 3]
my_list.insert(1, 1.5)  # Inserta 1.5 en el índice 1
print(my_list)

# Ten en cuenta que el método insert() agrega un elemento por vez. 
# Si intentas agregar varios elementos, se creará una lista anidada en el índice 1.

my_list = [1, 2, 3]
my_list.insert(1, [1.2, 1.5])  # Inserta 1.2 y 1.5 en el índice 1
print(my_list)

# Lo mismo ocurrirá si pasas otra lista al método append().
# Recuerda que append(), extend() e insert() modifican la lista original en lugar de devolver una nueva. 
# Así es la propiedad mutable de las listas.


# Eliminar elementos
# Ahora que sabemos cómo agregar elementos a nuestra lista, veamos cómo podemos eliminarlos.
# Puedes utilizar el método remove() para eliminar la primera aparición de un valor específico de la lista. 
# Si no se encuentra el valor, se produce un ValueError.

my_list = [1, 2, 3, 3, 4]
my_list.remove(3) # elimina la primera aparición de un valor específico
print(my_list)

# Fíjate que el elemento 3 ha sido eliminado de la lista.
# Por otro lado, puedes utilizar el método pop() para eliminar un elemento por su índice específico.
# Este método también devuelve el elemento eliminado. Si el índice está fuera de rango, se produce un IndexError.

my_list = [1, 2, 3, 4]
removed_element = my_list.pop(2)  # Elimina el elemento en el índice 2
print(my_list)          
print(removed_element)

# Si no se especifica ningún argumento, este método eliminará el último elemento de la lista. 

my_list = [1, 2, 3, 4]
my_list.pop()  # Elimina el último elemento
print(my_list)

# ¡Ahora puedes modificar las listas todo lo que quieras!
# Fin.