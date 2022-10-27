def crear_tabla(size):
    tabla = [None] * size

    return tabla

def funcion_hash(dato, tamanio_tabla):
    return dato % tamanio_tabla

def insertar(tabla, dato, convert):
    posicion = funcion_hash(ord(dato), len(tabla))

    if (tabla[posicion] is None):
        if convert:
            tabla[posicion] = convertir(dato)
        else:
            tabla[posicion] = dato
    else:
        print('Se ha producido una colision')

def convertir(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


tabla_1 = crear_tabla(255)
tabla_2 = crear_tabla(255)


for i in range(32,126):
    insertar(tabla_1, chr(i), convert = False)

for j in range(32,126):
    insertar(tabla_2, chr(j), convert = True)


print(convertir("hola soy oscar alvarez dodani"))