from datetime import date

class UrnaEletronica:
  def __init__(self, candidatos, secao, zona):
    self.candidatos = candidatos
    self.voto = list
    self.secao = secao
    self.zona = zona

  def inicializar(self):
    pass

  def adicionar_voto(self, voto):
    pass


  def listar_todos_os_votos(self):
    pass

  def listar_voto(self):
    pass
    

class Partido:
  def __init__(self, numero, nome):
    self.numero = numero
    self.nome = nome


class Candidato(Partido):
  def __init__(self, nome):
    self.nome = nome


class Eleitor:
  def __init__(self, titulo, nome):
    self.nome = nome
    self.titulo = titulo


class Voto(Candidato, Eleitor):
  def __init__(self, data):
    self.data = date.today()
