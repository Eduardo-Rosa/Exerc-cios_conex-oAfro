# Passo 1: Solicitar um número ao usuário e validar a entrada
while True:
    entrada = input("Insira um número inteiro positivo para iniciar a contagem regressiva: ")
    if entrada.isdigit() and int(entrada) > 0:
        numero = int(entrada)
        break
    else:
        print("Entrada inválida!! ")
        print("Certifique-se de inserir um número inteiro positivo.")

# Passo 2: Utilizar um laço while para realizar a contagem regressiva
while numero >= 0:
    print(numero)
    numero -= 1  # Decrementa o valor de numero a cada iteração

print("Contagem regressiva concluída!")
