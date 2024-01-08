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
        
    def afegir_Producte_a_categoria(self, c: Categoria, p:List[Producte])->bool:
        if c in self.categorias:
            self.categorias[c].append(p)
            return True
        else:
            return False
       
        
    def afegir_categoria(self, c: Categoria)->bool:
        if c in self.categorias:
            
            
            return False
        else:
            
            self.categorias[c.nombre] = c
            return True
        

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
        
    


#print(f'Ahora borramos la categoria animal')

#if miApp.eliminar_categoria('Animal'):
 #   print('Se ha borrado correctamente')
   
  #  miApp.imprimirCategorias()
#else:
#    print('Esa categoria no existe')
    
    
#El usuario  puede ver todo la lista 
#miApp.verTodaLaLista()


#El usuario puede filtrar por categoria



#miApp.filtrar_por_categoria('Lactis')
