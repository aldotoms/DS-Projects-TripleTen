# Procesamiento de strings
#
# Cómo dividir un string en unidades de texto más pequeñas?
# Cómo convertir una lista de strings en un solo string?

# División de strings en una lista
#
# i quieres convertir un string en una lista, puedes utilizar el método split(), 
# que divide un string con base en un carácter especificado. 
# Por defecto, el método split() separa el string dondequiera que encuentre espacios en blanco, como en el siguiente caso:

phrase = 'dividir o no dividir'
words = phrase.split()  # Configuración por defecto
print(words)

# Sin embargo, puedes cambiar esta funcionalidad especificando un carácter diferente. Observa el siguiente ejemplo.

text = 'Esta es una oración. Esta es otra oración.'
sentences = text.split('.')     # Delimitador específico para dividir
print(sentences)


# Combinación de elementos de una lista en un string
#
# A menudo dividimos un string para hacer modificaciones, 
# como corregir la ortografía o llevar a cabo un análisis de frecuencia de palabras.
# Supongamos que ya hicimos esos cambios y necesitamos devolver el texto a su forma original.
# Para ello, podemos utilizar el método join() para convertir nuestra lista en un solo string otra vez. 
# Es importante especificar el carácter que se colocará entre cada elemento de la lista, siendo un espacio en blanco ' ' la elección más común.
# Este es un ejemplo en el que todos los elementos de la lista words están unidos con un espacio entre ellos:

words = ['Mi', 'pelicula', 'favorita', 'es', 'The', 'Graduate']
phrase = ' '.join(words)   # Este es un ejemplo en el que todos los elementos de la lista words están unidos con un espacio entre ellos:
print(phrase)

# Fin.
