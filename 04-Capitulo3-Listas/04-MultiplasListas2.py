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