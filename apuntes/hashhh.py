def crear_tabla(tamanio):
    """Crear una tabla hash vacia"""
    tabla = [None]*tamanio
    return tabla

def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla"""
    return len(tabla) - tabla.count(None)

def funcion_hash(dato, tamanio_tabla):
    """Determina la posicion del dato en la tabla"""
    return len(str(dato).strip()) % tamanio_tabla

def agregar (tabla, dato):
    """Agrega un elemento a la tabla encadenada"""
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is None):
        tabla[posicion] = dato
    
    else:
        print("Se produjo una colision")

        """ Si se produce dicha colision ejectuar funcion de sondeo para reubicar el elemento """

def buscar(tabla, buscado):
    """ Determina si un elemento existe en la tabla y determina su posicion. """
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if (tabla[posicion] is not None):
        
        if (buscado == tabla[posicion]):
            pos = posicion

        else:
            print("Aplicar funcion de sondeo")

    return pos

def quitar(tabla, dato):
    """Quita un elemento de la tabla cerrada si existe"""

    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is not None):

        if (dato == tabla[posicion]):
            dato = tabla[posicion]
            tabla[posicion] = None

        else:
            print("Aplicar funcion de sondeo")
            """Para determinar si esta en otra posicion y quitarlo"""

    return dato

tabla = crear_tabla(6)
agregar(tabla, "pelo")
agregar(tabla, "Hola")
agregar(tabla,"saludos")
print(buscar(tabla,"saludos"))
print(buscar(tabla,"Hola"))
