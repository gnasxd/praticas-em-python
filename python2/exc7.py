produto = input("Digite um produto: ")
categoria = int (input("""Qual a sua categoria?
categoria [1]
categoria [2]
categoria [3]
categoria [4]
categoria [5]: """ ))

if categoria == 1:
    print(f"O {produto} fica no valor de 10R$")
elif categoria == 2:
    print (f"O {produto} fica no valor de 15R$")
elif categoria ==3:
    print(f"O {produto} fica no valor de 19R$")
elif categoria == 4:
    print(f"O {produto} fica no valor de 23R$")
elif categoria == 5:
    print (f"O {produto} fica no valor de 27R$")
else:
    print("Categoria não existente, digite uma das categorias acima!")