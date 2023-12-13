#Desafio 4

a = input('Digite algo: ') #como eu posso mudar o tipo, quando o código estiver rodando? Ou sempre será string?
print('O tipo primitivo deste valor é:', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É um alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em letras maiusculas? ', a.isupper())
print('Está em letras minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

#Desafio 4 com método

a = input('Digite algo:')
print('O tipo primitivo deste valor é {}. Só há espaços ? {} É numérico? {} É alfabético? {} É alfanumérico? {} Está em letras maiusculas? {} Está em letras minusculas? {} Está capitalizada? {}' .format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle()))
