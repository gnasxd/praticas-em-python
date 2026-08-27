sal = float (input("Digite o salario do funcionario: "))

if sal>1250:
    aumento = (10/100)*sal
    novoSal1 = aumento + sal
    print(f"""O aumento do salario foi de {aumento}R$
o novo salario do funcionario é: {novoSal1}R$""")
else:
    aum= (15/100)*sal
    novoSal2 = aum + sal
    print(f"""O aumento do salario foi de {aum}R$
o novo salario do funcionario é: {novoSal2}R$""")