#tratando uma exceção generica
try:
    x = 1 / 0
except Exception as e:
    print(f"Ocorreu um erro: {e}")