from Cap03Pt02_Funcoes.Ex01_IdentificacaoDeFuncoes import *

minhaLista = []

print('Preenchendo')
fillInventory(minhaLista)

print('\nExibindo')
showInventory(minhaLista)

print('\nPesquisando')
searchByName(minhaLista,input('Equipamento: '))

print('\nAlterando')
depreciateByName(minhaLista,input('Equipamento: '),int(input('% Depreciação: ')))

print('\nExcluindo')
print(removeBySerial(minhaLista,int(input('Serial: '))))
showInventory(minhaLista)

print('\nResumindo')
totalValues(minhaLista)