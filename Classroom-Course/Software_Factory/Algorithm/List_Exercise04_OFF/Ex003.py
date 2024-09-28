# 3 - Faça um algoritmo que leia o nome, o titulo eleitoral e o numero do candidato.
# Posteriormente imprima o resultado de cada variavel linha abaixo de linha.

print("=" * 60)
print("*** Cabine Eleitoral ***")
print("=" * 60)

print("*** Seja Bem-Vindo! Cidadão! ***")
print("* Insira Seus Dados Para Prosseguirmos!!! *")

print("=" * 60)

nome = str(input("- Digite Seu Nome Completo: "))
titulo = int(input("- Digite Seu Titulo De eleitor Completo: "))
numero_Candidato = int(input("- Digite O numero do seu candidato: "))

print("=" * 60)


print("* Nome Completo: {}*".format(nome))
print("* Numero Do Titulo De Eleitor: {}*".format(titulo))
print("* O numero do seu candidato que voce votou é: {}*".format(numero_Candidato))
print("=" * 60)

print("*** Dados Confirmados Com Sucesso! ***")

print("=" * 60)