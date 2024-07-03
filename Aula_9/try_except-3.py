#exceção especifica
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Erro de divisão por zero: {e}")