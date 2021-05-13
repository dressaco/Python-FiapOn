equipamentos = ['regua','lousa','impressora','lapis','tesoura','caneta','marcador','caderno','impressora']
valores = [5,100,999,2,7,25,12,15,2999]
seriais = [1001,1002,1003,1004,1005,1006,1007,1008,1009]
departamentos = ['PAP','PAP','PAP','IMP','PAP','ESC','ESC','PAP','IMP']

#Situacao 1 => equipamentos 'impressora' sofrem depreciação de 10%
depreciation = input('Digite o nome do equipamento que será depreciado: ')

for indice in range (0,len(equipamentos)):
  if depreciation == equipamentos[indice]:
    print('Valor antigo.:' , valores[indice])
    valores[indice] *= 0.9
    print('Novo valor...:' , valores[indice])

#Situacao 2 => serial danificado, descarte (usar del)
damaged = int(input('Digite o serial do equipamento que será excluido: '))

for indice in range(0,len(equipamentos)):
  if damaged == seriais[indice]:
    del equipamentos[indice]
    del valores[indice]
    del seriais[indice]
    del departamentos[indice]
    break #usamos o break pois já foi encontrado o item desejado. alem disso, deletar um item irá bagunçar o index e consequentemente a ocorrencia do for.

#impressao listas atualizadas
for indice in range(0,len(equipamentos)):
  print('\nEquipamento..:' , (indice+1))
  print('Nome.........:' , equipamentos[indice])
  print('Valor........:' , valores[indice])
  print('Serial.......:' , seriais[indice])
  print('Departamento.:' , departamentos[indice])