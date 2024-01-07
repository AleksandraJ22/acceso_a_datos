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
      
    def setProducte(self, nom_categoria: str, p:Producte)->bool:
        if nom_categoria in self.productos:
            self.productos[nom_categoria].append(p)
            return True
        else:
            return False
        
            
       
       
        
    #def updateProducte(self, novaQuantitat: int)->bool:
        
     #   for k,v in self.productos.items():
      #      for i in v
        
     
       
            
        
        

    
        
        
   
        

        

        

        
        
        
