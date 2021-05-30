continua = 'SIM'

while continua == 'SIM':
  role = input('Digite o nível de acesso: ').upper()

  if role == 'ADM' or role == 'USR':
    gender = input('Digite o seu gênero: ').upper()
    if role == 'ADM' and gender == 'F':
      print('Olá administradora')
    elif role == 'ADM' and gender == 'M':
      print('Olá administrador')
    elif role == 'USR' and gender == 'F':
      print('Olá usuária')
    elif role == 'USR' and gender == 'M':
      print('Olá usuário')
  elif role == 'GUEST':
    print('Olá visitante')
  else:
    print('Olá desconhecido(a)')
  
  continua = input('Digite SIM para continuar: ').upper()