from listaEncad import *

class Hash:
     def __init__(self,tam):
          self.tabela = {}
          self.tam = tam

     def funcaohash(self, chave):
          return (int(chave)%int(self.tam))

     def inserir(self, dado):
          pos = self.funcaohash(dado)          
          if self.tabela.get(pos) == None: # se posicao vazia 
               self.tabela[pos] = ListaEncad()
          else:
               if self.tabela[pos].buscar(dado):
                    return
          self.tabela[pos].inserir(dado)

     def excluir(self, chave):
          pos = self.buscar(chave)
          if pos == -1:
               print(" Item nao encontrado")
          else:
               self.tabela[pos].excluir(chave)

     def printa(self):
          for i in self.tabela:
               print("Hash[%d] -> " %i, end="")
               self.tabela[i].printa()

     def buscar(self, chave):
          pos = self.funcaohash(chave)
          if self.tabela[pos].buscar(chave):
               return pos
          return -1