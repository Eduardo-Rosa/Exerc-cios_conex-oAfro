#O bloco finally exceção ter ocorrido ou não:
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro de divisão por zero: {e}")
finally:
    print("Este bloco é sempre executado.")
