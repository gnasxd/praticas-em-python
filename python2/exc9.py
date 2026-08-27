sal = float (input("Qual o salario do comprador: "))
casa = int (input("Qual o valor da casa desejada; "))
ano = int (input("Em quantos anos deseja pagar"))

meses = ano *12
novoSal= (30/100)*sal
prestacao = casa // meses

if prestacao > novoSal:
    print(f"""O valor da prestação ficou {prestacao}, sendo maior que 30% do seu salario
    logo o seu emprestimo não foi aprovado!""")
else:
    print(f"""O valor da prestação ficou {prestacao}, sendo menor que 30% do seu salario
    logo o seu emprestimo foi aprovado!""")
 