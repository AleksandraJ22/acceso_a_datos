from clase_lista_item import ListaItem
from clase_categoria import Categoria
from clase_producto import Producte




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

miApp.imprimirCategorias()
#atun_gatos=Producte('atun_gatos',3)


def testAñadirCategoria():
    miApp.afegir_categoria(categoria_animal)
    
    assert( miApp.afegir_categoria(categoria_animal) == True)
    print(f'Ahora se ha añadido la categoria comida para animales (Animal)')
    miApp.imprimirCategorias()

    
testAñadirCategoria()
 



