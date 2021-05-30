def fillInventory(list):
  answer = 'S'
  while answer == 'S':
    equipment = [input('Equipamento: '),float(input('Valor: ')),int(input('Numero Serial: ')),input('Departamento: ')]
    list.append(equipment)
    answer = input('Digite \'S\' para continuar: ').upper()

def showInventory(list):
  for i in list:
    print('\nEquipamento..:' , (i+1))
    print('Nome.........:' , i[0])
    print('Valor........:' , i[1])
    print('Serial.......:' , i[2])
    print('Departamento.:' , i[3])

def searchByName(list):
  search = input('Digite o nome do equipamento que deseja buscar: ')
  for i in list:
    if search == i[0]:
      print('Valor........:' , i[1])
      print('Serial.......:' , i[2])

def depreciateByName(list,porcent):
  depreciation = input('Digite o nome do equipamento que será depreciado: ')

  for i in list:
    if depreciation == i[0]:
      print('Valor antigo.:' , i[1])
      i[1] *= 1 - (porcent/100)
      print('Novo valor...:' , i[1])

def removeBySerial(list):
  damaged = int(input('Digite o serial do equipamento que será excluido: '))

  for i in list:
    if damaged == i[2]:
      list.remove(i)
    return 'Itens excluídos.'

def totalValues(list):
  values = []
  for i in list:
    values.append(i[1])

  if len(values) > 0:
    print('O equipamento mais caro custa: ',max(values))
    print('O equipamento mais barato custa: ',min(values))
    print('O total de equipamentos é de: ',sum(values))
