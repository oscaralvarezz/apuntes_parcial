class hash_table:
    def __init__(self):
        self.table = [None] * 127
    
    # Función hash
    def Hash_funcion(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insertar(self, value): # Metodo para ingresar elementos
        hash = self.Hash_funcion(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Buscar(self,value): # Metodo para buscar elementos
        hash = self.Hash_funcion(value)
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
    def Eliminar(self,value): # Metodo para eleminar elementos
        hash = self.Hash_funcion(value)
        if self.table[hash] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[hash] is None
        
        
H = hash_table()
H.Insertar("Hola")
H.Insertar("Soy")
H.Insertar("Oscar")


print(H.Buscar("Hola"))
print(H.Buscar("Soy"))
print(H.Buscar("Oscar"))
