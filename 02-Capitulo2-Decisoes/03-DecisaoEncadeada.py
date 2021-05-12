name = input('Digite o nome: ')
age = int(input('Digite a idade: '))
contagious_susp = input('Suspeita de doença infecto-contagiosa (S/N)?').upper()

if age >= 65:
  print('Paciente COM prioridade')
  if contagious_susp == 'S':
  print('Encaminhe o paciente para a sala AMARELA')
  elif contagious_susp == 'N':
  print('Encaminhe o paciente para a sala BRANCA')
  else:
  print('Responda a suspeita de doença infectocontagiosa com \'S\' ou \'N\'')

else:
  print('Paciente SEM prioridade')
  if contagious_susp == 'S':
  print('Encaminhe o paciente para a sala AMARELA')
  elif contagious_susp == 'N':
  print('Encaminhe o paciente para a sala BRANCA')
  else:
  print('Responda a suspeita de doença infectocontagiosa com \'S\' ou \'N\'')

print('FIM')