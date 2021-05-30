from Cap03Pt02_Funcoes.Ex01_IdentificacaoDeFuncoes import *

minhaLista = []

print('Preenchendo')
fillInventory(minhaLista)

print('\nExibindo')
showInventory(minhaLista)

print('\nPesquisando')
searchByName(minhaLista)

print('\nAlterando')
depreciateByName(minhaLista,20)

print('\nExcluindo')
print(removeBySerial(minhaLista))
showInventory(minhaLista)

print('\nResumindo')
totalValues(minhaLista)