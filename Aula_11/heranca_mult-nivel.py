class pessoa: #classe pai
  def __init__(self, nome, idade, genero):
    self.nome = nome
    self.idade = idade
    self.genero = genero

  def PessoaInfo(self):
    print('Nome: {}'.format(self.nome))
    print('Idade: {}'.format(self.idade))
    print('Genero: {}'.format(self.genero))

class funcionario(pessoa): #classe filho
  def __init__(self, nome, idade, genero, funcionarioid, cargo, salario):
    pessoa.__init__(self, nome, idade, genero)
    self.funcionarioid = funcionarioid
    self.cargo = cargo
    self.salario = salario

  def funcionarioInfo(self):
    print('Funcionario ID: {}'.format(self.funcionarioid))
    print('Cargo: {}'.format(self.cargo))
    print('Salario: {}'.format(self.salario))


class tempo_integral(funcionario): #classe neta
  def __init__(self, nome, idade, genero, funcionarioid, cargo, salario, experiencia):
    funcionario.__init__(self, nome, idade, genero, funcionarioid, cargo, salario)
    self.experiencia = experiencia

  def TempoIntegralInfo(self):
    print('Experiencia Anterior: {}'.format(self.TempoIntegralInfo))


class contrato(funcionario): #classe neta
  def __init__(self, nome, idade, genero, funcionarioid, cargo, salario, vencimento_contratual):
    funcionario.__init__(self, nome, idade, genero, funcionarioid, cargo, salario )
    self.vencimento_contratual = vencimento_contratual

  def ContratoInfo(self):
    print('Vencimento do Conterato: {}'.format(self.vencimento_contratual))



print("Dados funcionarios Tempo Integral")
print('----------------------------------')
func_tempo_int1 = tempo_integral("Luiz", 32, "Masculino", 345,"gerente", 12000.00,12)
func_tempo_int1.PessoaInfo()
func_tempo_int1.funcionarioInfo()
func_tempo_int1.TempoIntegralInfo()

print('********************************')
print("\n \n")

print("Detalhes do contrato de funcionários")
print("--------------------------------------")
funcionario1 = contrato("Eduardo", 39, 'Masculino', 456, "suporte", 1500.00, '01/10/2019')
funcionario1.PessoaInfo()
funcionario1.funcionarioInfo()
funcionario1.ContratoInfo()









