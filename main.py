from arvoreAVL import *
from listaEncad import *
from arvoreBin import *
from arvoreRN import *
from hash import *

#Escolhe o tamanho do arquivo
def tamanho(tam):
	if int(tam) == 1:
		t = '1000'
	elif int(tam) == 2:
		t = '5000'
	elif int(tam) == 3:
		t = '10000'
	elif int(tam) == 4:
		t = '50000'
	elif int(tam) == 5:
		t = '100000'
	elif int(tam) == 6:
		t = '500000'

	return t

#Escolhe o metodo a ser utilizado
def arvore(tam):
	if int(tam) == 1:
		tabela = AVL()
	elif int(tam) == 2:
		tabela = ArvoreRN()
	elif int(tam) == 3:
		tabela = ArvoreBin()
	elif int(tam) == 4:
		tabela = ListaEncad()
	elif int(tam) == 5:
		tabela = hash()

	return tabela



if __name__ == "__main__": 

	tam = input("Qual tamanho de arquivo voce deseja?\n[1] 1000\t[2] 5000\t[3] 10000\t[4] 50000\t[5] 100000\t[6] 500000\n")
	
	x = tamanho(tam)
	with  open("/home/kayro/Documentos/AtividadePraticaArvore/arquivos_teste/file" + x + ".txt", "r") as arq:
		for i in arq:
			i = i.strip().split(', ')
			tabAux = i

	tabA = arvore(4)
	for i in tabAux:
		tabA.inserir(i)
	
	tam1 = input("Qual tamanho de arquivo voce deseja?\n[1] 1000\t[2] 5000\t[3] 10000\t[4] 50000\t[5] 100000\t[6] 500000\n")
	#se tam1 > tam:
	y = tamanho(tam1)
	with  open("/home/kayro/Documentos/AtividadePraticaArvore/arquivos_teste/file" + y + ".txt", "r") as arq:
		for i in arq:
			i = i.strip().split(', ')
			tabAux = i

	y = input("Escolha:\n[1]arvore AVL\t[2]arvore rubro-negra\t[3]arvore binaria\t[4]lista encadeada\t[5]hash\n")

	arv = arvore(y)

	arv.printa()
	
		