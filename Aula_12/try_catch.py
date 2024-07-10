n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

try:
    if n2 == 0:
        raise ValueError("error")

    div = n1 / n2
    print(f"a divisão erro: {div}")

except ZeroDivisionError:
    print("error2")
except ValueError:
    print(f"erro de {ValueError}")
except Exception as e:
    print(f"error: {e}")

