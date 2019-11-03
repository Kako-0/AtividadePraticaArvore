import sys

class No(object):
	def __init__(self, dado):
		self.dado = dado
		self.esquerda = None
		self.direita = None
		self.pai = None
		#1 para indicar a cor vermelha e 0 para indicar cor preta
		self.cor = 1


class ArvoreRN(object):
	def __init__(self):
		self.TNULL = No(0)
		self.TNULL.cor = 0
		self.TNULL.esquerda = None
		self.TNULL.direita = None
		self.raiz = self.TNULL



	def inserir(self, chave):
		novoNo = No(chave)
		novoNo.pai = None
		novoNo.cor = 1
		novoNo.dado = chave
		novoNo.esquerda = self.TNULL
		novoNo.direita = self.TNULL

		aux = None
		arvore = self.raiz

		while arvore != self.TNULL:
			aux = arvore
			if novoNo.dado < arvore.dado:
				arvore = arvore.esquerda
			else:
				arvore = arvore.direita

		novoNo.pai = aux

		if aux == None:
			self.raiz = novoNo
		elif novoNo.dado < aux.dado:
			aux.esquerda = novoNo
		else:
			aux.direita = novoNo

		if novoNo.pai == None:
			novoNo.cor = 0
			return

		if novoNo.pai.pai == None:
			return

		self.fixInserir(novoNo)




	def fixInserir(self, no):
		while no.pai.cor == 1:
			if no.pai == no.pai.pai.direita:
				aux = no.pai.pai.esquerda
				if aux.cor == 1:
					#caso 3.1
					aux.cor = 0
					no.pai.cor = 0
					no.pai.pai.cor = 1
					no = no.pai.pai
				else:
					if no == no.pai.esquerda:
						#caso 3.2.2
						no = no.pai
						self.dRotacao(no)
					#caso 3.2.1
					no.pai.cor = 0
					no.pai.pai.cor = 1
					self.eRotacao(no.pai.pai)
			else:
				aux = no.pai.pai.direita
				if aux.cor == 1:
                    # mirror case 3.1
					aux.cor = 0
					no.pai.cor = 0
					no.pai.pai.cor = 1
					no = no.pai.pai 
				else:
					if no == no.pai.direita:
                        # mirror case 3.2.2
						no = no.pai
						self.eRotacao(no)
                    # mirror case 3.2.1
					no.pai.cor = 0
					no.pai.pai.cor = 1
					self.dRotacao(no.pai.pai)
			if no == self.raiz:
				break
		self.raiz.cor = 0




	def eRotacao(self, no):
		aux = no.direita
		no.direita = aux.esquerda
		if aux.esquerda != self.TNULL:
			aux.esquerda.pai = no
		
		aux.pai = no.pai
		if no.pai == None:
			self.raiz = aux
		elif no == no.pai.esquerda:
			no.pai.esquerda = aux
		else:
			no.pai.direita = aux
		aux.esquerda = no
		no.pai = aux



	def dRotacao(self, no):
		aux = no.esquerda
		no.esquerda = aux.direita
		if aux.direita != self.TNULL:
			aux.direita.pai = no
		
		aux.pai = no.pai
		if no.pai == None:
			self.raiz = aux
		elif no == no.pai.direita:
			no.pai.direita = aux
		else:
			no.pai.esquerda = aux
		aux.direita = no
		no.pai = aux



    	
	def exclueAjuda(self, no, chave):
		achou = self.TNULL
		while no != self.TNULL:
			if no.dado == chave:
				achou = no
			if chave < no.dado:
				no = no.esquerda
			else:
				no = no.direita

		aux = achou
		auxCorOrigin = aux.cor

		if achou.esquerda == self.TNULL:
			aux2 = achou.direita
			self.troca(achou, achou.direita)
		elif achou.direita == self.TNULL:
			aux2 = achou.esquerda
			self.troca(achou, achou.esquerda)
		else:
			aux = self.maximo(achou.esquerda)
			auxCorOrigin = aux.cor
			aux2 = aux.esquerda
			if aux.pai == achou:
				aux2.pai = aux
			else:
				self.troca(aux, aux.direita)
				aux.direita = achou.direita
				aux.direita.pai = aux

			self.troca(achou, aux)
			aux.esquerda = achou.esquerda
			aux.esquerda.pai = aux
			aux.cor = achou.cor
		if auxCorOrigin == 0:
			self.fixDelete(aux2)



	def fixDelete(self, no):
		while no != self.raiz and no.cor == 0:
			if no == no.pai.esquerda:
				aux = no.pai.direita
				if aux.cor == 1:
					#caso 3.1
					aux.cor = 0
					no.pai.cor = 1
					self.eRotacao(no.pai)
					aux = no.pai.direita
	
				if aux.esquerda.cor == 0 and aux.direita.cor == 0:
					#caso 3.2
					aux.cor = 1
					no = no.pai
				else:
					if aux.direita.cor == 0:
						#caso 3.3
						aux.esquerda.cor = 0
						aux.cor = 1
						self.dRotacao(aux)
						aux = no.pai.direita
	
					#case 3.4
					aux.cor = no.pai.cor
					no.pai.cor = 0
					aux.direita.cor = 0
					self.eRotacao(no.pai)
					no = self.raiz
			else:
				aux = no.pai.esquerda
				if aux.cor == 1:
					#caso 3.1
					aux.cor = 0
					no.pai.cor = 1
					self.dRotacao(no.pai)
					aux = no.pai.esquerda
	
				if aux.esquerda.cor == 0 and aux.direita.cor == 0:
					#caso 3.2
					aux.cor = 1
					no = no.pai
				else:
					if aux.esquerda.cor == 0:
						#caso 3.3
						aux.direita.cor = 0
						aux.cor = 1
						self.eRotacao(aux)
						aux = no.pai.esquerda
	
					#case 3.4
					aux.cor = no.pai.cor
					no.pai.cor = 0
					aux.esquerda.cor = 0
					self.dRotacao(no.pai)
					no = self.raiz
		no.cor = 0


	def excluir(self, dado):
		self.exclueAjuda(self.raiz, dado)


	def troca(self, papa, filho):
		if papa.pai == None:
			self.raiz = filho
		elif papa == papa.pai.esquerda:
			papa.pai.esquerda = filho
		else:
			papa.pai.direita = filho

		filho.pai = papa.pai
		

	def maximo(self, no):
		if no != self.TNULL:
			while no.direita != self.TNULL:
				no = no.direita

			return no


	def buscando(self, node, key):
		if node == self.TNULL or key == node.dado:
			return int(node.dado)

		if key < node.dado:
			return self.buscando(node.esquerda, key)
		return self.buscando(node.direita, key)

	def buscar(self, k):
		return self.buscando(self.raiz, k)


	def printando(self, node, indent, last):
        # print the tree structure on the screen
		if node != self.TNULL:
			sys.stdout.write(indent)
			if last:
				sys.stdout.write("R----")
				indent += "     "
			else:
				sys.stdout.write("L----")
				indent += "|    "

			s_color = "RED" if node.cor == 1 else "BLACK"
			print(str(node.dado) + "(" + s_color + ")")
			self.printando(node.esquerda, indent, False)
			self.printando(node.direita, indent, True)


  # print the tree structure on the screen
	def printa(self):
		self.printando(self.raiz, "", True)
