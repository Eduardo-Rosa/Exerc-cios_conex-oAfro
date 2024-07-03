class pessoa: #classe pai
  def __init__(self, nome, idade, genero):
    self.nome = nome
    self.idade = idade
    self.genero = genero

  def PessoaInfo(self):
    print('Nome: {}'.format(self.nome))
    print('Idade: {}'.format(self.idade))
    print('Genero: {}'.format(self.genero))


class estudante(pessoa): #classe filha
  def __init__(self, nome, idade, genero, id, mensalidade):
    pessoa.__init__(self, nome, idade, genero)
    self.id = id
    self.mensalidade = mensalidade

  def EstudanteInfo(self):
    print('ID: {}'.format(self.id))
    print('Mensalidade: {}'.format(self.mensalidade))

class professor(pessoa): #classe filha
  def __init__(self, nome, idade, genero, id, salario):
    pessoa.__init__(self, nome, idade, genero)
    self.id = id
    self.salario = salario

  def Professorinfo(self):
    print('ID: {}'.format(self.id))
    print('Salario:  {}'.format(self.salario))

est1 = estudante("Felipe", 18, "Masculino", 123, 300.00)
print(' Informações do estudante')
print('-------------')
est1.PessoaInfo() #Metodo da classe pai "pessoa"
est1.EstudanteInfo()
print()


prof1 = professor('Eduardo' , 39, 'Masculino', 456, 1000.00)
print('Dados do professor')
print('----------------')
prof1.PessoaInfo()
prof1.Professorinfo()