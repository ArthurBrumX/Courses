# 1 - Faça um algoritmo que leia o nome, a idade, o sexo, o endereço e o telefone.
# Posteriormente imprima o resultado de cada variavel linha a baixo.

print("=" * 40)
print("* Seja bem-vindo Usuário!")
print("* Porfavor, complete as informações a baixo!")
    # Boas vindas ao usuario!

print("=" * 40)

nome = input("Qual é o seu nome: ")
    # nome da variavel = nome
    # Tipo da variavel = str(string)
    # funcao = Entrada de dados

idade = int(input("Qual é a sua idade: "))
    # nome da variavel = idade
    # Tipo da variavel = int(inteiro)
    # Funcao = Entrada de dados

sexo = input("Qual é o seu sexo [M/F]: ")
    # nome da variavel = sexo
    # Tipo da variavel = str(string)
    # Funcao = Entrada de dados

rua = input("Qual é o nome da rua da sua Residencia: ")
    # nome da variavel = rua
    # Tipo da variavel = str(string)
    # Funcao = Entrada de dados

nRua = int(input("Qual é o numero da sua residencia: "))
    # nome da variavel = nRua
    # Tipo da variavel = int(inteiro)
    # Funcao = Entrada de dados

telefone = int(input("Qual é o seu telefone para contato: "))
    # noem da variavel = telefone
    # Tipo da variavel = int(inteiro)
    # Funcao = Entrada de dados

print("=" * 40)
print("Voce se chama {}, é do sexo {}, mora na rua {} {}°, e o seu telefone pra contato é o {}".format(nome,sexo,rua,nRua,telefone))
print("=" * 40)

print("Informaçoes armazenadas no sistema!")
print("Obrigado Pelas Informações {}! Até a proxima!".format(nome))

print("=" * 40)


