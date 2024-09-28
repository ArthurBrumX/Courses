# 2 -  Faça um algoritmo que leia o nome as notas dos 4 bimestres de um aluno.
# Posteriormente Imprima o resultado de cada variavel linha abaixo de linha.

print("=" * 60)
print("***Escola Tarda mais não falha***")
print("*** Relatorio de notas bimestrais!! ***")
print("=" *60)

nomeAluno = str(input("- Digite o Nome Completo do aluno: "))
print("=" * 60)

print("*** Aluno: ({}) ***".format(nomeAluno))
print("=" * 60)

notaPrimeiroBi = float(input("Digite a Nota do Primeiro bimestre: "))
notaSegundoBi = float(input("Digite a Nota Do Segundo Bimestre: "))
notaTerceiroBi = float(input("Digite a Nota Do Terceiro Bimestre: "))
notaQuartoBi = float(input("Digite a Nota do Quarto Bimestre: "))

print("=" * 60)

print("* Aluno: ({})*".format(nomeAluno))
print("* Nota Primeiro Bimestre: {}*".format(notaPrimeiroBi))
print("* Nota Segundo Bimestre: {}".format(notaSegundoBi))
print("* Nota Terceiro Bimestre: {}".format(notaTerceiroBi))
print("* Nota Quarto Bimestre: {}".format(notaQuartoBi))

print("=" * 60)
print("Relatorio Concluido com Sucesso!")
print("=" * 60)