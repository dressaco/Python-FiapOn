inventory = []
answer = 'S'

while answer == 'S':
  equipment = [input('Equipamento: '),float(input('Valor: ')),int(input('Numero Serial: ')),input('Departamento: ')]
  inventory.append(equipment)
  answer = input('Digite \'S\' para continuar: ').upper()

#impressao lista inicial
for i in inventory:
  print('\nEquipamento..:' , (i+1))
  print('Nome.........:' , i[0])
  print('Valor........:' , i[1])
  print('Serial.......:' , i[2])
  print('Departamento.:' , i[3])

#Busca
search = input('Digite o nome do equipamento que deseja buscar: ')
for i in inventory:
  if search == i[0]:
    print('Valor........:' , i[1])
    print('Serial.......:' , i[2])

#Situacao 1 => equipamentos 'impressora' sofrem depreciação de 10%
depreciation = input('Digite o nome do equipamento que será depreciado: ')

for i in inventory:
  if depreciation == i[0]:
    print('Valor antigo.:' , i[1])
    i[1] *= 0.9
    print('Novo valor...:' , i[1])

#Situacao 2 => serial danificado, descarte (usar del)
damaged = int(input('Digite o serial do equipamento que será excluido: '))

for i in inventory:
  if damaged == i[2]:
    inventory.remove(i)
    break #usamos o break pois já foi encontrado o item desejado. alem disso, deletar um item irá bagunçar o index e consequentemente a ocorrencia do for.

#impressao listas atualizadas
for i in inventory:
  print('\nEquipamento..:' , (i+1))
  print('Nome.........:' , i[0])
  print('Valor........:' , i[1])
  print('Serial.......:' , i[2])
  print('Departamento.:' , i[3])

#funções para listas numericas
values = []

for i in inventory:
  values.append(i[1])

if len(values) > 0:
  print('O equipamento mais caro custa: ',max(values))
  print('O equipamento mais barato custa: ',minx(values))
  print('O total de equipamentos é de: ',sum(values))