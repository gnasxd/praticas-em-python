kwh = int (input("Qual a quantidade de kWh consumida?"))
instalacao = input("""Qual o tipo de instalação?
[R] residencial
[C] comercial
[I] industrial
escolha: """)

match instalacao:
    case "R" | "r": 
        if kwh >500:
            preco = 0.65 * kwh
        else:
            preco = 0.40 * kwh
        print(f"O valor a pagar é {preco}")
    case "C" | "c":
        if kwh > 1000:
            preco1 = 0.60 * kwh
        else:
            preco1 = 0.55 * kwh
            print(f"O valor a pagar é {preco1}")
    case "I"|"i":
        if kwh > 5000:
            preco2 = 0.60 * kwh
        else:
            preco2 = 0.55 * kwh
            print(f"O valor a pagar é {preco2}")
    case _:
        print("""Opção não encontrada.
        Selecione uma das escolhas acima!""")
