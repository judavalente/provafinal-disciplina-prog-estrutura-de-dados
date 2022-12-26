class Dominio:
  def __init__(self, hostname, ip):
    self.hostname = hostname
    self.ip = ip

  def __str__(self):
    return str(self.hostname)


class No:
  def __init__(self, carga, ant=None, prox=None):
    self.carga = carga
    self.ant = ant
    self.prox = prox

  def __str__(self):
    return str(self.carga)

class ListaEncadeada:
  def __init__(self, cabeca, cauda):
    self.cabeca = cabeca
    self.cauda = cauda

  def listar(self):
    atual = self.cabeca
    while atual is not None:
      print(atual)
      atual = atual.prox

  def adicionar(self, valor):
    novo = No(valor)
    if self.cabeca is None:
      self.cabeca = self.cauda = novo
    if self.cabeca == self.cauda:
      self.cabeca = novo
    else:
      novo.prox = self.cabeca
      self.cabeca = novo

  def resolver(self, valor):
    atual = self.cabeca
    while atual is not None:
      if atual == valor:
        return atual.ip
      atual = atual.prox
    return -1

  def remover(self, valor):
    if self.cabeca is None:
      print("nao ha lista")
    atual = self.cabeca
    if self.cabeca == valor:
      self.cabeca = self.cabeca.prox
    while atual is not None:
      if atual == valor:
        atual = atual.prox
      atual = atual.prox

  def organizar(self):
    lista_organizados = []
    lista_organizados.sort()
    atual = self.cabeca
    while atual is not None:
      lista_organizados.append(atual.hostname)
      atual = atual.prox
    


site1 = Dominio("localhost", "127.0.0.1")
site2 = Dominio("google.com", "216.58.222.78")
site3 = Dominio("amazon.com", "176.32.103.205")
site4 = Dominio("facebook.com", "31.13.74.35")
lista = ListaEncadeada(site1, site4)
no1 = site1
no2 = site2
no3 = site3
no4 = site4
no1.prox = no2
no2.prox = no3
no3.prox = no4
lista.listar()
print(lista.resolver(site3))
      
