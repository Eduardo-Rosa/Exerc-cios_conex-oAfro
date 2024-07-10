n_1 = int(input("digite o primeiro numero: "))
numero_2 = int(input("digite o segundo: "))

try:
    div = numero_1 / numero_2
except Execeção as e:
    print(f"Erro de divisão por zero {e}")
else:
    print(f"Resultado: {div}")
