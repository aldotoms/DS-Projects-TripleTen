# Operadores y tipos de datos
# Veamos ahora cómo funciona la suma para distintos tipos de datos. Echa un vistazo al siguiente código para ver cómo funciona:

#1
# strings
ch_language = 'Chino'
en_language = 'Inglés'

#2
# flotantes
ch_website_share = 0.017
en_website_share = 0.539

#3
# enteros
ch_total_speakers = 1107
en_total_speakers = 1121

#4
# booleanos
ch_majority_native = True
en_majority_native = False

print(ch_language + en_language) # Al sumar strings, estos se concatenan, lo que básicamente significa que se unen en un solo string.
print(ch_website_share + en_website_share)  # Al sumar un entero con un flotante, el resultado será un flotante. De hecho, cualquier operación aritmética con un flotante dará como resultado un flotante.
print(ch_total_speakers + en_total_speakers)    # Al sumar números enteros, siempre resultará un número entero. Al sumar números de punto flotante, obtendremos un número de punto flotante.
print(ch_majority_native + en_majority_native)  # Al sumar booleanos, el resultado será un entero: True es igual a 1 y False es igual a 0. Así pues, cuando se suman booleanos, simplemente se cuentan todos los valores True.

# Los tipos de datos de nuestros objetos de Python determinan qué operadores están permitidos y cómo se comportan:
# Los strings se pueden concatenar usando +
print('a' + 'b')
print('Negrito'+'Bekka')

# Los strings se pueden multiplicar (*) por un número.
print('a' * 3)  # Esto es tres veces 'a'
print(' Beetlejuice ' * 3)

# Los números (que en Python se representan mediante números de punto flotante y enteros) 
# se pueden sumar, restar, multiplicar y dividir.

# 1: El resultado de dos más dos
print(2 + 2)
# 2: El resultado de dos menos dos
print(2 - 2)
# 3: El resultado de dos multiplicado por dos
print(2 * 2)
# 4: El resultado de dos dividido entre dos (un flotante)
print(2 / 2)
