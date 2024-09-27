#  5- Faça um algoritmo que leia o nome do aluno, o nome da disciplina, notas de 3 provas e calcule 
# a média desse aluno.Posteriormente imprima o resultado de cada variável linha abaixo de linha.

nome = str(input("Digite o nome do aluno: "))
nomediciplina = str(input("Digite o nome da diciplina: "))

primeiranota = float(input("Primeir nota: "))
segundanota = float(input("Segunda nota: "))
terceiranota = float(input("terceira nota: "))

media = primeiranota + segundanota + terceiranota / 3

print("seu nome é: {}".format(nome))
print("Sua diciplina é: {}".format(nomediciplina))

print("A primeira nota é: {}".format(primeiranota))
print("A segunda nota é: {}".format(segundanota))
print("A terceira é: {}".format(terceiranota))

print("E a media desseas notas é: {}".format(media))



