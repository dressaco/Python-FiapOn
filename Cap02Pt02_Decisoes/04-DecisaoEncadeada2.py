name = input('Digite o nome: ')
age = int(input('Digite a idade: '))
contagious_susp = input('Suspeita de doença infecto-contagiosa (S/N)?').upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if contagious_susp == 'S':
  print('Encaminhe o paciente para a sala AMARELA')
elif contagious_susp == 'N':
  print('Encaminhe o paciente para a sala BRANCA')
else:
  print('Responda a suspeita de doença infectocontagiosa com \'S\' ou \'N\'')

# SEGUNDO PROBLEMA A SER RESOLVIDO
if age >= 65:
  print('Paciente COM prioridade')
else:
  gender = input('Digite o gênero do paciente (F/M): ').upper()
  if gender == 'F' and age > 10:
    pregnant = input('A paciente está grávida (S/N)?')
    if pregnant == 'S':
      print('Paciente COM prioridade')
    else:
      print('Paciente SEM prioridade')
  else:
    print('Paciente SEM prioridade')

print('FIM')