from clase_categoria import Categoria
from typing import Dict,List

class ListaItem:

    def __init__(self):
         self.categorias = {
            'Frescos': Categoria('Frescos', {'Carne': ['Pollo', 'Res'], 'Pescado': ['Salmón', 'Atún']}),
            'Begudes': Categoria('Begudes', {'Refrescos': ['Coca-Cola', 'Pepsi'], 'Aigua': ['Mineral', 'Amb gas']}),
            'Làctis': Categoria('Làctis', {'Llet': ['Sencera', 'Descremada'], 'Iogurts': ['Naturales', 'De frutas']}),
            'Neteja': Categoria('Neteja', {'Detergent': ['Líquido', 'En polvo'], 'Esponjas': ['Normales', 'Metálicas']}),
            'Fruita i verdures': Categoria('Fruita i verdures', {'Fruita': ['Manzanas', 'Plátanos'], 'Verduras': ['Lechuga', 'Tomate']})
        }
        #self.categorias: List[Categoria] = []
        
        
 #usuario quiere añadir categoria 
 

    def afegir_categoria(self, nombre: str, productos: Dict[str, List[str]] = None):
        nueva_categoria = Categoria(nombre, productos)
        self.categorias[nombre] = nueva_categoria

#si usuario quiere filtrar por categoria
    def filtrar_por_categoria(self, c: Categoria) -> List[Categoria]:
        return c.mirarLosProductos(c.nombre)
     
    
    def eliminar_categoria(self, nom_categoria: str) -> bool:
        
        if nom_categoria in self.categorias:
            del(self.categorias[nom_categoria])
           
            return True
        else:
            return False
            
    
    def getCategorias(self)->List[str]:
        nombres_categorias = list(self.categorias.keys())
        print("Categorías disponibles:", nombres_categorias)
        return nombres_categorias
    
    
miApp=ListaItem()
miApp.getCategorias()
         
         
         

     