class No(object):
	def __init__(self, dado):
		self.dado = dado
		self.esquerda = None
		self.direita = None


class ArvoreBin(object):
	def __init__(self):
		self.no = None
		self.altura = -1


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
			self.no.esquerda = ArvoreBin()
			self.no.direita = ArvoreBin()
		elif dado < arvore.dado:
			self.no.esquerda.inserir(dado)
		elif dado > arvore.dado:
			self.no.direita.inserir(dado)


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


	def excluir(self, chave):
		if self.no != None:
			if self.no.dado == chave:
				#É uma folha
				if self.no.esquerda.no == None and self.no.direita.no == None:
					self.no = None
				#É uma subarvore só com um filho a direita
				elif self.no.esquerda.no == None:
					self.no = self.no.direita.no
				#É uma subarvore só com um filho a esquerda
				elif self.no.direita.no == None:
					self.no = self.no.esquerda.no
				else:
					#É uma subarvore com dois filhos
					troca = self.maior(self.no)
					if troca != None:
						self.no.dado = troca.dado
						self.no.esquerda.excluir(troca.dado)

			elif chave < self.no.dado:
				self.no.esquerda.excluir(chave)
			elif chave > self.no.dado:
				self.no.direita.excluir(chave)
		else:
			return


	def buscar(self, chave):
		if self.no != None:
			if self.no.dado == chave:
				return int(self.no.dado)
			elif chave < self.no.dado:
				self.no.esquerda.buscar(chave)
			elif chave > self.no.dado:
				self.no.direita.buscar(chave)
		else:
			return


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

	def maior(self, no):
		no = no.esquerda.no
		if no != None:
			while no.direita != None:
				if no.direita.no == None:
					return no
				else:
					no = no.direita.no

		return no


	def printa(self, level=0):        
		self.updateAltura()  # Must update heights before balances 
		if(self.no != None): 
			print(self.no.dado, "[" + str(self.altura) + "]", 'L' if self.folha() else ' ')    
			if self.no.esquerda != None: 
				self.no.esquerda.printa(level + 1)
			if self.no.esquerda != None:
				self.no.direita.printa(level + 1)
		
		