def fillInventory(list):
  answer = 'S'
  while answer == 'S':
    equipment = [input('\nEquipamento: '),float(input('Valor: ')),int(input('Numero Serial: ')),input('Departamento: ')]
    list.append(equipment)
    answer = input('\nDigite \'S\' para continuar: ').upper()

def showInventory(list):
  for i in list:
    print('Nome.........:' , i[0])
    print('Valor........:' , i[1])
    print('Serial.......:' , i[2])
    print('Departamento.:' , i[3])
    print('-'*20)

def searchByName(list,name):
  for i in list:
    if name == i[0]:
      print('Valor........:' , i[1])
      print('Serial.......:' , i[2])

def depreciateByName(list,name,porcent):
  for i in list:
    if name == i[0]:
      print('Valor antigo.:' , i[1])
      i[1] *= 1 - (porcent/100)
      print('Novo valor...:' , i[1])

def removeBySerial(list,serial):
  for i in list:
    if serial == i[2]:
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
