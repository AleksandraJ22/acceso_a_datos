from clase_producto import Producte

from typing import Dict, List

class Categoria:
    
    def __init__(self, nombre: str, diccionario_productos: Dict[str, List[Producte]]):
        self.nombre = nombre
        self.diccionario_productos = diccionario_productos
        
        
        
#le paso categoria por parametro y que me devuelva los productos que tiene y su cantidad 
        
    def mirarLosProductos(self, nom_categoria)->List[Producte]:
        
        if nom_categoria in self.diccionario_productos:
            return self.diccionario_productos[nom_categoria]
        else:
            return []
            
            
            
            
        
        

    
        
        
   
        

        

        

        
        
        
