# EJERCICIO 1
#
# Reemplaza el substring 'corto' por el substring 'breve' en la cadena quote. Muestra quote cuando realices este cambio.
# La salida esperada es esta: 
# La vida es demasiado corta para no divertirse; estamos aquí por un breve tiempo en comparación con el Sol y la Luna y todo eso

quote = 'La vida es demasiado corta para no divertirse; estamos aquí por un corto tiempo en comparación con el Sol y la Luna y todo eso'
# escribe tu código aquí
new_quote = quote.replace('corto', 'breve')
print(new_quote)


# EJERCICIO 2
#
# Supongamos que estás creando un programa que recibe la entrada del usuario y la guarda en una base de datos. 
# Quieres asegurarte de que todas las letras en su entrada estén en mayúsculas y sin espacios en blanco adicionales.
# La salida esperada es esta: MARADONA
# Completa el siguiente precódigo para obtener el string de entrada de usuario limpio:

user_input = " MaRaDoNa "
clean_input = user_input.upper() # escribe tu código aquí
clean_input = clean_input.strip()
print(clean_input)

# Código corto:
user_input = " MaRaDoNa "
clean_input = user_input.strip().upper()
print(clean_input)

# Fin.