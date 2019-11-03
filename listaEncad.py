class No(object):
	def __init__(self, dado):
		self.dado = dado
		self.proximo = None


class ListaEncad(object):
	def __init__(self):
		self.primeiro = None
	

	def inserir(self, dado):
		novoNo = No(dado)

		if self.primeiro == None:
			self.primeiro = novoNo
		else:
			aux = self.primeiro
			while aux.proximo != None:
				aux = aux.proximo

			aux.proximo = novoNo


	def excluir(self, chave):
		if self.primeiro == None:
			return
		else:
			aux = self.primeiro
			anterior = None
			while aux.proximo != None and aux.dado != chave:
				anterior = aux
				aux = aux.proximo
		
			if aux.dado == chave:
				if aux == self.primeiro:
					self.primeiro = aux.proximo
				else:
					anterior.proximo = aux.proximo
			else:
				return


	def buscar(self, chave):
		if self.primeiro == None:
			return
		else:
			aux = self.primeiro
			while aux.proximo != None and aux.dado != chave:
				aux = aux.proximo
		
			if aux.dado == chave:
				return True
			else:
				return False

	def printa(self):
		temp = self.primeiro
		while temp != None:
			#print(str(temp.dado))
			print("%s -> " %temp.dado, end="")
			temp = temp.proximo
		print("NULL")




