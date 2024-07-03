pessoas = [
    {"nome": "Clara", "idade": 30, "profissao": "Advogada"},
    {"nome": "Bruno", "idade": 42, "profissao": "Médico"},
    {"nome": "João", "idade": 28, "profissao": "Pintor"}
]

# Usando um laço for para chamar cada pessoa
for p in pessoas:
    print(f"Nome: {p['nome']}, Idade: {p['idade']}, Profissão: {p['profissao']}")
