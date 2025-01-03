# module_2.py

import module_1

def double_check():
    print('Ahora dos veces:')
    module_1.useful_function()
    module_1.useful_function()

if __name__ == "__main__":
    print("probando función...")
    double_check()