equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S':
  equipamentos.append(input('Equipamento: '))
  valores.append(float(input('Valor: ')))
  seriais.append(int(input('Número Serial: ')))
  departamentos.append(input('Departamento: '))
  
  resposta = input('Digite \"S\" para continuar: ').upper()
  #.upper -> força o input a ficar com letras maiusculas

'''
  for indice in range(0,len(equipamentos)):
    print('\nEquipamento..:' , (indice+1))
    print('Nome.........:' , equipamentos[indice])
    print('Valor........:' , valores[indice])
    print('Serial.......:' , seriais[indice])
    print('Departamento.:' , departamentos[indice])
'''
#um pouco mais sobre listas
search = input('Digite o nome do equipamento que deseja buscar: ')

for indice in range (0,len(equipamentos)):
  if search == equipamentos[indice]:
    print('Valor........:' , valores[indice])
    print('Serial.......:' , seriais[indice])