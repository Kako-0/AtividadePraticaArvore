class No(object):
	def __init__(self, dado):
		self.dado = dado
		self.esquerda = None
		self.direita = None


class AVL(object):
	def __init__(self):
		self.no = None
		self.altura = -1
		self.balanco = 0


	def altura(self):
		if self.no:
			return self.no.altura
		else:
			return 0


	def folha(self):
		return (self.altura == 0)


	def inserir(self, dado):
		arvore = self.no
		novoNo = No(dado)
		if arvore == None:
			self.no = novoNo
			self.no.esquerda = AVL()
			self.no.direita = AVL()
		elif dado < arvore.dado:
			self.no.esquerda.inserir(dado)
		elif dado > arvore.dado:
			self.no.direita.inserir(dado)
		
		self.rebalanco()


	def rebalanco(self):
		self.updateAltura(False)
		self.updateBalanco(False)
		while self.balanco < -1 or self.balanco > 1:
			if self.balanco > 1:
				if self.no.esquerda.balanco < 0:
					self.no.esquerda.eRotacao()
					self.updateAltura()
					self.updateBalanco()
				self.dRotacao()
				self.updateAltura()
				self.updateBalanco()

			if self.balanco < -1:
				if self.no.direita.balanco > 0:
					self.no.direita.dRotacao()
					self.updateAltura()
					self.updateBalanco()
				self.eRotacao()
				self.updateAltura()
				self.updateBalanco()


	def dRotacao(self):
		pai = self.no
		filhoEsquerdo = self.no.esquerda.no
		filhoDireito = filhoEsquerdo.direita.no

		self.no = filhoEsquerdo
		filhoEsquerdo.direita.no = pai
		pai.esquerda.no = filhoDireito


	def eRotacao(self):
		pai = self.no
		filhoDireito = self.no.direita.no
		filhoEsquerdo = filhoDireito.esquerda.no

		self.no = filhoDireito
		filhoDireito.esquerda.no = pai
		pai.direita.no = filhoEsquerdo


	def updateAltura(self, status = True):
		if not self.no == None:
			if status:
				if self.no.esquerda != None:
					self.no.esquerda.updateAltura()
				if self.no.direita != None:
					self.no.direita.updateAltura()

			self.altura = max(self.no.esquerda.altura, self.no.direita.altura) + 1
		else:
			self.altura = -1


	def updateBalanco(self, status = True):
		if not self.no == None:
			if status:
				if self.no.esquerda != None:
					self.no.esquerda.updateBalanco()
				if self.no.direita != None:
					self.no.direita.updateBalanco()

			self.balanco = self.no.esquerda.altura - self.no.direita.altura
		else:
			self.balanco = 0

	
	def excluir(self, chave):
		if self.no != None:
			if self.no.dado == chave:
				if self.no.esquerda.no == None and self.no.direita.no == None:
					self.no = None
				elif self.no.esquerda.no == None:
					self.no = self.no.direita.no
				elif self.no.direita.no == None:
					self.no = self.no.esquerda.no
				else:
					troca = self.maior(self.no)
					if troca != None:
						self.no.dado = troca.dado
						self.no.esquerda.excluir(troca.dado)

			elif chave < self.no.dado:
				self.no.esquerda.excluir(chave)
			elif chave > self.no.dado:
				self.no.direita.excluir(chave)

			self.rebalanco()
			return
		else:
			return


	def buscar(self, chave):
		if self.no != None:
			if self.no.dado == chave:
				print(str(self.no.dado))
			elif chave < self.no.dado:
				self.no.esquerda.buscar(chave)
			elif chave > self.no.dado:
				self.no.direita.buscar(chave)
		else:
			return

	#maior nó no filho a esquerda
	def maior(self, no):
		no = no.esquerda.no
		if no != None:
			while no.direita != None:
				if no.direita.no == None:
					return no
				else:
					no = no.direita.no

		return no

	#Menor nó no filho a direita
	def menor(self, no):
		no = no.direita.no
		if no != None:
			while no.esquerda != None:
				if no.esquerda.no == None:
					return no
				else:
					no = no.esquerda.no
		return no


	def printa(self, level=0):        
		self.updateAltura()  # Must update heights before balances 
		self.updateBalanco()
		if(self.no != None): 
			print(self.no.dado, "[" + str(self.altura + 1) + ":" + str(self.balanco) + "]", 'L' if self.folha() else ' ')    
			if self.no.esquerda != None: 
				self.no.esquerda.display(level + 1)
			if self.no.esquerda != None:
				self.no.direita.display(level + 1)