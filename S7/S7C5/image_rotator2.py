# image_rotator.py

from PIL import Image # importa el módulo Image de la librería PIL

# carga una imagen llamada 'tripleten_logo.jpeg'.
im = Image.open('S7\S7C5\tripleten_logo.png')

# obtén el tamaño de la imagen mediante el atributo .size y muéstralo
print(im.size)

# gira la imagen 90 grados en sentido contrario a las agujas del reloj
rotated = im.rotate(90)

# guarda la imagen girada
rotated.save('rotated.png')