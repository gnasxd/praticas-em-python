n1 = float (input("Digite o primeiro valor: "))
n2 = float (input("Digite o segundo valor: "))
operação = input("""Escolha a operação que deseja: 
[+] adição
[-] subtração
[*] multiplicação
[/] divisão
escolha:""")

match operação:
    case "+":
        soma = n1 + n2
        print(f"A soma dos valores {n1} e {n2} é: {soma} ")
    case "-": 
        sub = n1 - n2
        print(f"A subtração dos valores {n1} e {n2} é: {sub}")
    case "*":
        mult = n1 * n2
        print(f"A multiplicação dos valores {n1} e {n2} é: {mult}")
    case "/":
        div = n1 / n2
        print(f"A divisão dos valores {n1} e {n2} é: {div}")