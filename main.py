from arvoreAVL import *
from listaEncad import *
from arvoreBin import *
from arvoreRN import *


if __name__ == "__main__": 
	a = RedBlackTree()
	#b = ListaEncad()

	print("----- Inserting -------")
	#inlist = [7, 5, 2]
	inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
	for i in inlist: 
		a.insert(i)

	#a.display()
    
	print("----- Deleting -------")
	a.delete_node(5)
	a.delete_node(3)

	a.pretty_print()
	#a.buscar(4)