from Cap03Pt02_Funcoes.Ex01_IdentificacaoDeFuncoes import *

minhaLista = []

print('Preenchendo')
fillInventory(minhaLista)

print('Exibindo')
showInventory(minhaLista)

print('Pesquisando')
searchByName(minhaLista)

print('Alterando')
depreciateByName(minhaLista,20)

print('Excluindo')
print(removeBySerial(minhaLista))
showInventory(minhaLista)

print('Resumindo')
totalValues(minhaLista)