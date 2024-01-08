#Desafio08

m = int(input('Distância em metros: '))
print('Uma distância de {} metros, corresponde a:'.format(m))
km = m / 1000
print('{:.3f}km'.format(km))
hm = m / 100
print('{:.3f}hm'.format(hm))
dam = m / 10
print('{:.3f}dam'.format(dam))
dm = m * 10
cm = m * 100
mm = m *1000
print('{}dm \n{}cm \n{}mm'.format(dm, cm, mm))
