# 5 - Faça um algortmo que leia o nome do aluno, o nome da disciplina,
# notas de 3 provas e calcule a media desse numero.
# Posteriormente imprima o resultado de cada variavel linha a baixo de linha!

print("=" * 60)
print("*** Escola Enilda Melhor Professora!! ***")
print("* Seja Bem-Vindo(a) Professor(a)! *")
print("=" * 60)

print("* Relatorio De Notas Bimestrais *")
print("=" * 60)

nome = str(input("- Digite o Nome Do Aluno: "))
disciplina = str(input("- Digite o Nome Da Disciplina: "))

print("=" * 60)
print("Disciplina selecionada!")
print("* Nome Do Aluno Selecionado: {}*".format(nome))
print("* Nome Da Disciplina Selecionada: {}*".format(disciplina))
print("=" * 60)

primeiraNota = float(input("- Digite a Primeira Nota Do Aluno: "))
segundaNota = float(input("- Digite a Segunda Nota Do Aluno: "))
terceiraNota = float(input("- Digite a Terceira Nota Do Aluno: "))

print("=" * 60)

media = primeiraNota + segundaNota + terceiraNota / 3

print("* O aluno: {} *".format(nome))
print("* Na Primeira Nota Tirou: {}*".format(primeiraNota))
print("* Na Segunda Nota Tirou: {}*".format(segundaNota))
print("* Na Terceira Nota Tirou: {}*".format(terceiraNota))

print("=" * 60)
print("*** A Media De Nota Do Aluno: {}, é de: {} ***".format(nome, media))
print("*** Relatorio Concluido Professor! ***")
print("*** Até a Proxima ***")
print("=" * 60)