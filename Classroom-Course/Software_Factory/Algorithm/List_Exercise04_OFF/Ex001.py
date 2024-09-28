# 1 - faça um algoritmo que leia o nome, idade, sexo, endeço e o telefone.
# Posteriormente imprima o resultado de cada variavel linha abaixo de linha

print("=" * 40)
print("* Seja bem-vindo Usuario!*")
print("* Porfavor, compelte as informacoes a baixo: *")

print("=" * 40)

nome = input("Qual é o seu nome: ")
sexo = str(input("Digite o seu sexo: "))
endereco = str(input("Digite o seu endereço: "))
telefone = int(input("Digite O seu tlefone pra contato: "))

print("=" * 40)

print("Voce se chama: {}".format(nome))
print("Voce é do sexo: {}".format(sexo))
print("Atualmente esta morando no endereço: {}".format(endereco))
print("Atualmente o seu telefone pra contato é o: {}".format(telefone))

print("=" * 40)

print("Informacoes armazenadas com Sucesso!")
print("Obrigado pelas informacoes {}! Até a proxima".format(nome))

print("=" * 40)