import random
import math
# recebendo inputs
menor = int(input("Digite o menor numero:- "))

# recebendo inputs
maior = int(input("Digite o maior numero:- "))

# gerando um numero aleatório
# entre o menor e o maior numero
x = random.randint(menor, maior)
print("\n\tVocê tem chances ",
       round(math.log(maior - menor + 1, 2)),
      "use somente numeros inteiro!\n")

# começando o contador numero sorteado.
count = 0

# cálcula do número mínimo de
# suposições dependem do intervalo
while count < math.log(maior - menor + 1, 2):
    count += 1

    # recebendo o número de adivinhação como entrada
    guess = int(input("Digite um numero:- "))

    # testa a condição
    if x == guess:
        print("Parabén você acertou em ",
              count, " tentativas!")
        # Uma vez adivinhado, o loop será interrompido
        break
    elif x > guess:
        print("o numero digitado é baixo!")
    elif x < guess:
        print("o numero digitado é muito alto!")

# Se precisar de mais do que as suposições necessárias para acertar,
# mostra esta saída.
if count >= math.log(maior - menor + 1, 2):
    print("\nO numero é: %d" % x)
    print("\tBoa sorte na próxima tentativa!")