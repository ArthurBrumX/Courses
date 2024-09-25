# Faça um algoritmo que leia o nome e as notas dos 4 bimestres de um aluno.
# Posteriormente imprima o resultado de cada variavel linha a baixo de linha.

print("=" * 60)

print("*** Escola Tarda mais na falha ***")
print("*** Relatorio de notas Bimetrais! ***")
    # Apresentacao pro usario

print("=" * 60)

nomeAluno = input("- Digite o nome completo do Aluno: ")
    # Nome da variavel = nomeAluno
    # Tipo da variavel = Str(string)
    # Funcao = Entrada de dados

print("=" * 60)

print("*** Aluno: ({})***".format(nomeAluno))
    # Funcao = saida de dados.
    # Apresentado mensagem na tela.
    # .format = formata o texto, alocando o valor de uma variavel no espaço: {}
        # Ex: .format(nome_da_Variavel)

print("-" * 60)

notaPrimeiroBi = float(input("- Digite a Nota Do 1º Bimestre: "))
    # nome da varariavel = NotaPrimeiroBi
    # Tipo da variavel = Float(Real)
    # Fucao = Entrada de dados

notaSegundoBi = float(input("- Digite a Nota Do 2º Bimestre: "))
    # nome da varariavel = NotaSegundoBi
    # Tipo da variavel = Float(Real)
    # Fucao = Entrada de dados

notaTerceiroBi = float(input("- Digite a Nota Do 3º Bimestre: "))
    # nome da varariavel = NotaTerceiroBi
    # Tipo da variavel = Float(Real)
    # Fucao = Entrada de dados

notaQuartoBi = float(input("- Digite a Nota Do 4º Bimestre: "))
    # nome da varariavel = NotaQuartoBi
    # Tipo da variavel = Float(Real)
    # Fucao = Entrada de dados

print("=" * 60)

print("* Aluno ({})".format(nomeAluno))
    # Funcao = Saida de dados.
    # Apresentado mensagem na tela.
    # .format = formata o texto, alocando o valor de uma variavel no espaço: {}
        # Ex: .format(Nome_Da_Variavel)

print("* Nota 1º Bimestre: {}".format(notaPrimeiroBi))
print("* Nota 2º Bimestre: {}".format(notaSegundoBi))
print("* Nota 3º Bimestre: {}".format(notaTerceiroBi))
print("* Nota 4º Bimestre: {}".format(notaQuartoBi))
    # Funcao = Saida de dados.
    # Apresentado mensagem na tela.
    # .format = formata o texto, alocando o valor de uma variavel no espaço: {}
        # Ex: .format(Nome_Da_Variavel)

print("-" * 60)
print("*** Relatorio Finalizado Com Sucesso!!! ***")
    # Funcao = Saida de dados.
    # Apresentado mensagem na tela.


print("=" * 60)
