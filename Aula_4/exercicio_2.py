<<<<<<< HEAD
# Passo 1: Inicializar a soma
soma = 0

# Passo 2: Solicitar números ao usuário continuamente
while True:
    entrada = input("Insira um número (ou um número negativo para sair): ")
    
#   Tentar converter a entrada para um número
    try:
        numero = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue
    
#   Passo 3: Verificar se o número é negativo
    if numero < 0:
        break  # Encerra o loop se o número for negativo
    
#   Adicionar o número à soma
    soma += numero

# Passo 4: Exibir a soma total
print(f"A soma total é: {soma}")
=======
# Passo 1: Inicializar a soma
soma = 0

# Passo 2: Solicitar números ao usuário continuamente
while True:
    entrada = input("Insira um número (ou um número negativo para sair): ")
    
#   Tentar converter a entrada para um número
    try:
        numero = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue
    
#   Passo 3: Verificar se o número é negativo
    if numero < 0:
        break  # Encerra o loop se o número for negativo
    
#   Adicionar o número à soma
    soma += numero

# Passo 4: Exibir a soma total
print(f"A soma total é: {soma}")
>>>>>>> 08b2136512fad3bd18765b823f223fa35b93a67d
