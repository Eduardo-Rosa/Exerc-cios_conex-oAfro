class pessoa: #classe pai
  def __init__(self, nome, idade, genero):
    self.nome = nome
    self.idade = idade
    self.genero = genero

  def saudacao(self):
    print('Olá pessoa {}'.format(self.nome))


class estudante(pessoa): #classe filho

  def __init__(self, nome, idade, genero, estudanteid, mensalidade):
    pessoa. __init__(self, nome, idade, genero)
    self.estudanteid = estudanteid
    self.mesalidade = mensalidade


  def saudacao(self):
    print('Olá Estudante {}'.format(self.nome))

estud = estudante('Felipe', 19, 'Masculino', 123, 300.000)
estud.saudacao()

pessoa1 = pessoa('Vera', 34, 'Feminino' )
pessoa1.saudacao()