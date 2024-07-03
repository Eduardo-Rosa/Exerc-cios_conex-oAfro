#bloco else se o try não gerrar exceção
try:
    x = 10 / 2
except ZeroDivisionError as e:
    print(f"Erro de divisão por zero: {e}")
else:
    print(f"Resultado: {x}")
