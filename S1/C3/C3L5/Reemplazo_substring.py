# Reemplazo de un substring
# 
# Otra parte común del procesamiento de datos de texto es eliminar o reemplazar partes de strings. 
# Por ejemplo, podríamos necesitar corregir errores ortográficos. Como sabes, los objetos de strings son inmutables,
# por lo que si quisiéramos hacer algunos cambios, tendríamos que reasignar todo el string. 
# Afortunadamente, podemos usar el método replace() para eliminar o reemplazar substrings (partes de strings).
#
# El método replace() toma dos argumentos:
# 1. El substring que queremos reemplazar.
# 2. El string por el que queremos reemplazarlo.
#
# Usemos replace() para corregir algunos errores tipográficos en una lista de compras diferente 
# donde accidentalmente escribimos mal la palabra “oil” (aceite) un par de veces:

# Creemos una lista de compras
shopping_list = '''canola oli   
sunflower oil
avocado oil
peanut oli'''

# Ahora verifiquemos la lista de compras
print(shopping_list.replace('oli', 'oil'))

# Cada instancia de oli en el string shopping_list se ha reemplazado por oil.
#
# También podemos usar replace() para eliminar substrings sin reemplazarlos. 
# Para ello, simplemente pasamos el string vacío '' como segundo argumento. 
# Vamos a utilizar replace() para eliminar los guiones bajos de un string:

user_ids = "_151234_, _792051_, _955247_"

# Reemplazamos el "_" con espacios. En otras palabras, eliminamos el "_"
user_ids = user_ids.replace('_', '') 
print(user_ids)

# El método replace() es sumamente poderoso. Te ahorrará mucho tiempo. Pero debe utilizarse con cuidado. 
# Volvamos al ejemplo de oil - oli: 

careful_example = "TODAY OLIVIA HAS BOUGHT SOME OLIVE OLI"
print(careful_example)
# La salida esperada es: TODAY OLIVIA HAS BOUGHT SOME OLIVE OLI

# Otra vez tenemos un error ortográfico; en lugar de OLIVE OIL tenemos OLIVE OLI. Corrijámoslo. 
careful_example = careful_example.replace('OLI', 'OIL')
print(careful_example)
# La salida esperada es: TODAY OILVIA HAS BOUGHT SOME OILVE OIL

# ¡Un momento! ¿Qué pasó? Arreglamos un error ortográfico, pero generamos otro. 
# Ahora tenemos OLIVE OIL, pero también tenemos OILVIA y OILVE.
# Como ves, debes tener cuidado al utilizar replace().
# Al utilizar replace() siempre es buena idea verificar dos veces que lo que estás reemplazando solo modifica lo que se necesita y nada más.

# Fin.