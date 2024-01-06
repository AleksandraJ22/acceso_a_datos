from clase_categoria import Categoria
from clase_producto import Producte
from typing import Dict,List

class ListaItem:

    def __init__(self):
        self.categorias = {
            'Frescos': Categoria('Frescos', [Producte('Carne', 2), Producte('Pescado', 3)]),
            'Begudes': Categoria('Begudes', [Producte('Coca-Cola', 5), Producte('Agua', 10)]),
            'Làctis': Categoria('Lactis', [Producte('Leche', 1), Producte('Iogurts', 4)]),
            'Neteja': Categoria('Neteja', [Producte('Detergent', 3), Producte('Esponjas', 2)]),
            'Fruita i verdures': Categoria('Fruita i verdures', [Producte('Fruita', 6), Producte('Verduras', 8)]),
        }
        #self.categorias: List[Categoria] = []
        
        
 #usuario quiere añadir categoria 
 

  #  def afegir_categoria(self, nombre: str, productos: Dict[str, List[str]] = None):
   #     nueva_categoria = Categoria(nombre, productos)
    #    self.categorias[nombre] = nueva_categoria
        
        
        
    def afegir_categoria(self, c: Categoria)->None:
        self.categorias[c.nombre] = c
        

#si usuario quiere filtrar por categoria
    def filtrar_por_categoria(self, c: Categoria) -> List[Categoria]:
        return c.mirarLosProductos(c.nombre)
     
    
    def eliminar_categoria(self, nom_categoria: str) -> bool:
        
        if nom_categoria in self.categorias:
            del(self.categorias[nom_categoria])
           
            return True
        else:
            return False
            
    
    
    def imprimirCategorias(self)->None:
        
        print(f'----------------------Estas son las categorias existentes: ------------------')
        for categora in self.categorias:
            print(categora)
       
       
  

    
miApp=ListaItem()


miApp.imprimirCategorias()
         
categoria_animal = Categoria('Animal', {})

miApp.afegir_categoria(categoria_animal)    

print(f'Ahora se ha añadido la categoria comida para animales (Animal)')
 

miApp.imprimirCategorias()


print(f'Ahora borramos la categoria animal')

if miApp.eliminar_categoria('Animal'):
    print('Se ha borrado correctamente')
   
    miApp.imprimirCategorias()
else:
    print('Esa categoria no existe')
    
    
    


         

     