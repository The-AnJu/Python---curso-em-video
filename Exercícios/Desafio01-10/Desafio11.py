#Desafio11

l = float(input('Largura: '))
a = float(input('Altura: '))
ar = l*a
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².' .format(l, a, ar))
li = ar/2
print('Para pintar sua parede, você precisará de {:.4f}l de tinta.' .format(li))
