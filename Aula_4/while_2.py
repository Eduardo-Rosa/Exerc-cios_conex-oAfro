numero_secreto = 7
adivinhado = False

while not adivinhado:
    chute = int(input("Adivinhe o número (entre 1 e 10): "))
    if chute == numero_secreto:
        print("Parabéns! Você acertou!")
        adivinhado = True
    else:
        print("Tente novamente!")