contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue  # Pula a iteração quando == 5
    if contador == 8:
        break  # Encerra o laço quando == 8
    print(f"Contador: {contador}")