km = int (input("Digite a velocidade do carro: "))
multa = 0
if km>80:
    multa= (km - 80 )*5
    print(f"""A velocidade do carro é de {km}km!
Você foi multado!
O valor da multa a pagar é de {multa}.""")
else:
    print(f"A velocidade do carro foi de {km}km!")