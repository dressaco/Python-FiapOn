name = input('Digite o nome: ')
age = int(input('Digite a idade: '))
contagious_susp = input('Suspeita de doença infecto-contagiosa (S/N)?').upper()

if age >= 65 and contagious_susp == 'S':
  print('O paciente ' + name + ' será direcionado para a sala AMARELA - COM prioridade')
elif age < 65 and contagious_susp == 'S':
  print('O paciente ' + name + ' será direcionado para a sala AMARELA - SEM prioridade')
elif age >= 65 and contagious_susp == 'N':
  print('O paciente ' + name + ' será direcionado para a sala BRANCA - COM prioridade')
elif age < 65 and contagious_susp == 'N':
  print('O paciente ' + name + ' será direcionado para a sala BRANCA - SEM prioridade')
else:
  print('Responda a suspeita de doença infectocontagiosa com \'S\' ou \'N\'')
print('FIM')