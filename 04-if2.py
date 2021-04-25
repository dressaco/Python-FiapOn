name = input('Digite o nome: ')
age = int(input('Digite a idade: '))
contagious_susp = input('Suspeita de doença infecto-contagiosa?').upper()

if age >= 65:
  print('O paciente ' + name + ' possui atendimento prioritário!')
elif contagious_susp == 'SIM':
  print('O paciente ' + name + ' deve ser direcionado para sala de espera reservada.')
else:
  print('O paciente ' + name + ' NÃO possui atendimento prioritário e pode aguardar na sala comum!')
print('FIM')