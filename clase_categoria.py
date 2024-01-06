from clase_producto import Producte

from typing import Dict, List

class Categoria:
    
    def __init__(self, nombre: str, productos: Dict[str, List[Producte]]):
        self.nombre = nombre
        self.productos = productos
        
    
    def getNom(self):
        return self.nombre
        
    def mirarLosProductos(self, nom_categoria: str) ->  List[Producte]:
        if nom_categoria in self.productos:
            return self.productos[nom_categoria]
        else:
            return []
      
       
            
        
        

    
        
        
   
        

        

        

        
        
        
