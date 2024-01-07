from clase_categoria import Categoria
from clase_producto import Producte
from typing import Dict,List

class ListaItem:

    def __init__(self):
        self.categorias = {
            #'Frescos': Categoria('Frescos', [Producte('Carne', 2), Producte('Pescado', 3)]),
            #'Begudes': Categoria('Begudes', [Producte('Coca-Cola', 5), Producte('Agua', 10)]),
           # 'Làctis': Categoria('Lactis', [Producte('Leche', 1), Producte('Iogurts', 4)]),
            #'Neteja': Categoria('Neteja', [Producte('Detergent', 3), Producte('Esponjas', 2)]),
            #'Fruita i verdures': Categoria('Fruita i verdures', [Producte('Fruita', 6), Producte('Verduras', 8)]),
        }
        #self.categorias: List[Categoria] = []
        
        
 #usuario quiere añadir categoria 
 

  #  def afegir_categoria(self, nombre: str, productos: Dict[str, List[str]] = None):
   #     nueva_categoria = Categoria(nombre, productos)
    #    self.categorias[nombre] = nueva_categoria
        
        
        
    def afegir_categoria(self, c: Categoria)->None:
        self.categorias[c.nombre] = c
        

#si usuario quiere filtrar por categoria
    def filtrar_por_categoria(self, nom_categoria: str) -> None:
        if nom_categoria in self.categorias:
            print(f'---------------------- Estas son los productos de la categoria {nom_categoria}: ------------------')
            for categoria, productos in self.categorias.items():
                for producto in productos.mirarLosProductos(nom_categoria):
                    print(f'{producto.getNom()},{producto.getQuantitat()}')
            print()
        else:
            print('Categoria no existe')
     
    
    def eliminar_categoria(self, nom_categoria: str) -> bool:
        
        if nom_categoria in self.categorias:
            del(self.categorias[nom_categoria])
           
            return True
        else:
            return False
            
    
    def imprimirCategorias(self) -> None:
        print("---------------------- Estas son las categorias existentes: ------------------")
        for categoria, productos in self.categorias.items():
            print(f'{categoria}:')
            for producto in productos.mirarLosProductos(productos.getNom()):
                print(f'  Producto: {producto.getNom()}, Cantidad: {producto.getQuantitat()}')
        print()
            
    def agregarProducto(self, nom_categoria: str, p: Producte)->bool:
        if nom_categoria not in self.productos:
           
            return False
        else: 
            self.productos[nom_categoria].append(p)
            return True
        
    def verTodaLaLista(self)->None:
        print(f'----------------------LISTA DE LA COMPRA: ------------------')
        for categoria, productos in self.categorias.items():
           
            for producto in productos.mirarLosProductos(productos.getNom()):
                print(f'{producto.getNom()}, {producto.getQuantitat()}')
       
            
            
            
            
            
            
            
            
        
        
        
        
        
    
        
   # def updateCategoria(self, nom_categoria: str, p:Producte, novaQuantitat: int)->bool:
        
    #    if nom_categoria in self.categorias:#compruebo que la categoria existe
            
                
                
            
     #       if p in self.categorias[nom_categoria]: #compruebo que el producto existe
      #          p.setQuantitat(novaQuantitat+p.getQuantitat())
       #         return True
        
                
                
                
                
                
                
                
                
                
            
            
            
        
  

    
miApp=ListaItem()



 
            

categoria_frescos=Categoria('Frescos', {'Frescos':[Producte('Carne', 2), Producte('Pescado', 3)]})
categoria_begudes=Categoria('Begudes',{'Begudes':[Producte('Coca-Cola', 5), Producte('Agua', 10)]})
categoria_lactis=Categoria('Lactis', {'Lactis':[Producte('Leche', 1), Producte('Iogurts', 4)]})
categoria_neteja=Categoria('Neteja', {'Neteja': [Producte('Detergent', 3), Producte('Esponjas', 2)]})
categoria_fiv= Categoria('Fruita i verdures',{'Fruita i verdures': [Producte('Fruita', 6), Producte('Verduras', 8)]})
categoria_animal = Categoria('Animal', {'Animal': [Producte('Pienso', 3), Producte('Snacks', 5)]})

miApp.afegir_categoria(categoria_frescos)   
miApp.afegir_categoria(categoria_begudes) 
miApp.afegir_categoria(categoria_lactis) 
miApp.afegir_categoria(categoria_neteja) 
miApp.afegir_categoria(categoria_fiv) 
miApp.afegir_categoria(categoria_animal)    



miApp.imprimirCategorias()
atun_gatos=Producte('atun_gatos',3)




print(f'Ahora se ha añadido la categoria comida para animales (Animal)')
 

miApp.imprimirCategorias()


print(f'Ahora borramos la categoria animal')

if miApp.eliminar_categoria('Animal'):
    print('Se ha borrado correctamente')
   
    miApp.imprimirCategorias()
else:
    print('Esa categoria no existe')
    
    
#El usuario  puede ver todo la lista 
#miApp.verTodaLaLista()


#El usuario puede filtrar por categoria



miApp.filtrar_por_categoria('Lactis')





         

     
