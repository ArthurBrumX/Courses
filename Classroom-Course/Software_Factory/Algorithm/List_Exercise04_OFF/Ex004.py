# 4 - Faça um algoritmo que leia o nome, a placa do carro, o modelo do carro e a cor do carro.
# Posteriomente imprima o resultado de cada variavel linha abaixo de linha.

print("=" * 60)
print("*** Sistema De Fiscalização De Transito! ***")
print("* Preencha os Dados Do seu Veiculo: *")
print("=" * 60)

nome = str(input("- Digite Seu Nome Completo: "))
placa = str(input("- Digite a Placa Do seu Viculo: "))
modelo = str(input("- Digite O Modelo Do Veiculo: "))
cor = str(input("- Digite a Cor Do Veiculo: "))

print("=" * 60)

print("*Nome Completo: {}*".format(nome))
print("*Placa do Veiculo é: {}*".format(placa))
print("*O Modelo Do Veiculo é: {}*".format(modelo))
print("*A Cor do Veiculo é: {}*".format(cor))

print("=" * 60)
print("*** Fiscalizacao Concluida Com Sucesso!!! ***")
print("=" * 60)
