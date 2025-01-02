# PRÁCTICA GUIADA
# Accede a la lista movies_info y muestra en pantalla:
#
# El país de producción de Good Will Hunting.
# El año de estreno de Pulp Fiction.
# La valoración de The Godfather (8.730).
#
# Recupera los elementos por sus índices y muestra cada uno de ellos en una nueva línea.
# La salida esperada es esta:
# USA
# 1994
# 8.73

movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# muestra aquí el país de producción de *Good Will Hunting*
# muestra aquí el año de estreno de Pulp Fiction
# muestra aquí la valoración de The Godfather

print(movies_info[9][1])
print(movies_info[5][2])
print(movies_info[1][5])

# Fin.