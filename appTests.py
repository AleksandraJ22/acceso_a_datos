import unittest
from clase_lista_item import ListaItem
from clase_categoria import Categoria
from clase_producto import Producte


class Tests(unittest.TestCase):
    
   
     
     
     def testAñadirCategoria(self):
         miApp=ListaItem()
         categoria_animal = Categoria('Animal', {'Animal': []})
         miApp.afegir_categoria(categoria_animal)
         
         self.assertEqual(True, miApp.afegir_categoria(categoria_animal))
         
     
       
        
     def testBorrarCategoria(self):
          miApp=ListaItem()
          categoria_animal = Categoria('Animal', {'Animal': []})
          miApp.afegir_categoria(categoria_animal)         
        
          self.assertNotEqual(False,miApp.eliminar_categoria('Animal'))
        
          
     def testAñadirProducteACategoria(self):
         miApp=ListaItem()
         categoria_animal = Categoria('Animal', {'Animal': []})
         miApp.afegir_categoria(categoria_animal)        
         atun_gato=Producte('atun_gatos',3)
         self.assertEqual(True, miApp.agregarProducto(categoria_animal,atun_gato))
         
     
       
     def testFiltrarPorCategoria(self):
         miApp=ListaItem()
        # categoria_frescos=Categoria('Frescos', {'Frescos':[Producte('Carne', 2), Producte('Pescado', 3)]})
         categoria_animal = Categoria('Animal', {'Animal': [Producte('atun_gatos',3)]})
         miApp.afegir_categoria(categoria_animal)
         #miApp.afegir_categoria(categoria_frescos)        
         self.assertNotEqual('Categoria no existe',miApp.filtrar_por_categoria(categoria_animal.getNom()))
         
         
     def testImprimirTodasLasCategorias(self):
         miApp=ListaItem()
         
         self.assertEqual(miApp.imprimirCategorias(),miApp.imprimirCategorias())
         
         
         
         
         
        
    
        
    
if __name__ == '__main__':
    unittest.main()
