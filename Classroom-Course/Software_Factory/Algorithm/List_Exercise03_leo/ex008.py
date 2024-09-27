# 8 - Faça um algoritmo que calcule o custo 
# estimado de uma viagem de carro.
# Posteriormente imprima o resultado.

local = str(input("Qual é o destino: "))
combustivel  = str(input("Qual é o combustivel:  "))

if (combustivel == "Aditivada") or (combustivel == "aditivada"):

    litros = float(input("Quantos kilometros seu veiculo faz com 1 litro de gasolina: "))
    distancia = float(input("Qual a distancia em kilometros ate o destino: "))

    gasolinaAdtivada = 6.28

    destino = litros * distancia
    valor = destino * gasolinaAdtivada

    print("o valor para ir até {} vai ser {}".format(destino, valor))

elif (combustivel == "comum") or (combustivel == "Comum"):

    litros = float(input("Quantos kilometros seu veiculo faz com 1 litro de gasolina: "))
    distancia = float(input("Qual a distancia em kilometros ate o destino: "))

    gasolinaComum = 6.09   

    destino = litros * distancia
    valor = destino * gasolinaComum

    print("o valor para ir até {} vai ser {}".format(destino, valor))


elif (combustivel == "Etanol") or (combustivel == "etanol"):

    litros = float(input("Quantos kilometros seu veiculo faz com 1 litro de gasolina: "))
    distancia = float(input("Qual a distancia em kilometros ate o destino: "))

    gasolinaEtanol = 4.04 

    destino = litros * distancia
    valor = destino * gasolinaEtanol

    print("o valor para ir até {} vai ser {}".format(destino, valor))

else:
    print("esse tipo de combustivel nao exite!!!")
