tabuada = int(input('Digite um número para exibir a tabuada: '))
print('Tabuada do número',tabuada)
for valor in range (1,11,1):
#for 'var' in range (start,end,addition)
  print (str(tabuada) + ' x ' + str(valor) + ' = ' + str((tabuada*valor)))