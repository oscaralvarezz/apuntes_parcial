"""
Módulo que agrupa todas las funcionalidades
que permiten solicitar introducir un dato numérico
"""


import sys
#tiene una libreria que tiene funciones que si las llamas puedes "corregir erroes" e
#interactuar con el programa muchas veces sin que se cuelgue, te permite hacer código
#con "errores", solo puedes escribir los caracteres de arriba.

MIN=0
MAX=100      #estos números quizás habría que cambiarlos


def solicitar_introducir_numero(invite):       #debido al invite, todo lo que metamos será si o si una cadena
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres [0-9].", file=sys.stderr) #esos valores de 0-9 podrían variar y habría que cambiarlos.
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

def solicitar_introducir_numero_extremo(invite, minimum=MIN, maximum=MAX):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    invite = "{} entre {} y {} incluídos".format(invite, minimum, maximum)
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = solicitar_introducir_numero(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido