class father:
  def __init__(self):
    self.fathername = str()


class mother:
  def __init__(self):
    self.mothername = str()


class Son(father, mother):
  name = str()
  def show(self):
    print('My name: ', self.name)
    print('Father: ', self.fathername)
    print('Mother: ', self.mothername)

s1 = Son()
s1.name = 'Bill'
s1.fathername = 'John'
s1.mothername = 'Kristen'
s1.show()