# module2.py

import re

def check_email(string: str):
    '''
    usa expresiones regulares para comprobar el formato de la dirección de correo electrónico
    el patrón es "algo@algo.algo"
    '''
    if re.match('[.\w]+@\w+[.]\w+', string):
        print('correcto')
    else:
        print('comprobar dirección de correo electrónico')

def check_age(age: int):
    if age >= 50:
        print('acceso permitido')
    else:
        print("eres demasiado joven")