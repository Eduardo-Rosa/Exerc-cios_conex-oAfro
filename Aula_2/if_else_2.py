idade_jonas = int(input("digite a idade de Jonas "))
idade_luiza = int(input("digite a idade de Luiza "))

if idade_jonas >= 18 or idade_luiza >= 18:
    if idade_jonas >= 18 and idade_luiza >= 18:
       print("Jonas e Luiza devem  votar")
    else:
        print("Jonas ou Luiza é obrigado a votar")
else:
    print("Jonas e Luiza não são obrigados a votar")