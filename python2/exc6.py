distancia = float (input("Digite a distancia que sera percorrida: "))

if distancia>200:
    passagem = distancia *0.45
    print(f"""A distancia é de {distancia}km
    O valor da passagem fica {passagem}R$""")
else:
    passagem = distancia * 0.50
    print(f""" A distancia é de {distancia}km
    O valor da passagem fica {passagem}R$""")