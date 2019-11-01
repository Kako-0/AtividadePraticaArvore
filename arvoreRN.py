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
		self.no = None
		self.cor = 0



	def altura(self):
		if self.no:
			return self.no.altura
		else:
			return 0


	def folha(self):
		return (self.altura == 0)


	def inserir(self, dado):
        aux = None
		arvore = self.no
		novoNo = No(dado)
		if arvore == None:
			self.no = novoNo
            self.cor = 1
            self.pai = None
			self.no.esquerda = None
			self.no.direita = None
		elif dado < arvore.dado:
            aux = arvore
			self.no.esquerda.inserir(dado)
		elif dado > arvore.dado:
            aux = arvore
			self.no.direita.inserir(dado)

        arvore.pai = aux

        if self.no.pai == None:
            no.cor = 0
            return

        if self.no.pai.pai == None
            return

        self.fixInserir()



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
						self.no.dado = troca.chave
						self.no.direita.excluir(troca.chave)

			elif chave < self.no.chave:
				self.no.esquerda.excluir(chave)
			elif chave > self.no.chave:
				self.no.direita.excluir(chave)
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
		if(self.no != None): 
			print(self.no.dado, "[" + str(self.altura) + "]", 'L' if self.folha() else ' ')    
			if self.no.esquerda != None: 
				self.no.esquerda.display(level + 1)
			if self.no.esquerda != None:
				self.no.direita.display(level + 1)
