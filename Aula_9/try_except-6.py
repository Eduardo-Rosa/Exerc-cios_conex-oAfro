<<<<<<< HEAD
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
    else:
        print(f"Resultado: {result}")
    finally:
        print("Operação de divisão concluída.")

divide(10, 2)
divide(10, 0)
=======
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
    else:
        print(f"Resultado: {result}")
    finally:
        print("Operação de divisão concluída.")

divide(10, 2)
divide(10, 0)
>>>>>>> 08b2136512fad3bd18765b823f223fa35b93a67d
