#Desafio15

diasA = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
total = ((diasA * 60) + (km * 0.15))
print('O valor total a pagar é de R$ {:.2f}' .format(total))

#Use sempre ponto para separar os números, caso contrário estará criando uma tupla.