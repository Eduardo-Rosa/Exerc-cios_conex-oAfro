#String(str)
print("Bom dia_queridos alunos"[7])
#concatenar
print("123"+"456")

#Inteiros(int)
print(123 + 456)

#Flutuantes(float)
3.14159

#Boolean
num1 = 10 == 10
print(num1)#imprime True

num2 = 10 == 20
print(num2) #imprime False


# Lista
paises = ["Brasil", "EUA", "Inglaterra"]
print(type(paises))  # <class 'list'>
print(paises[1])  # EUA

# Tuplas
pontos = (1, 2, 3, 4, 5)
print(type(pontos))  # <class 'tuple'>
print(pontos[3])  # 3

# Set
animais = {"elefante", "leão", "cachorro"}
print(type(animais))  # <class 'set'>


# Dict
pessoa = {"nome": "Ricardo", "idade": 30}
print(type(pessoa))  # <class 'dict'>
print(pessoa["nome"])  # Ricardo


# NoneType
vazio = None
print(type(vazio))  # <class 'NoneType'>