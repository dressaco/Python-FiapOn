name = input('Digite o nome: ')
age = int(input('Digite a idade: '))

if age >= 65:
  print('O paciente ' + name + ' possui atendimento prioritário!')
else:
  print('O paciente ' + name + ' NÃO possui atendimento prioritário!')
print('FIM')