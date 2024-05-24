from random import randint

total_barcos_jogador = 5

total_barcos_computador = 5

def matriz_jogador_1():
  matriz_1 = []

  for i in range(10):
    matriz_1.append([])
    for j in range(10):
      matriz_1[i].append('-')

  print('JOGADOR: ')
  for c in range(5):
    print(f'Coordenadas da {c+1}º embarcação: ')
    linha = int(input("Qual linha? "))
    coluna = int(input("Qual coluna? "))
    matriz_1[linha][coluna] = 'B'

  return matriz_1



def matriz_jogador_2():
  matriz_2 = []

  for i in range(10):
    matriz_2.append([])
    for j in range(10):
      matriz_2[i].append('-')

  for c in range(5):
    matriz_2[randint(0,5)][randint(0,5)] = 'B'

  return matriz_2

def print_matriz(matriz):
  for linha in matriz:
    print(linha)

def atirar(matriz, turn):
  linha = int(input("Informe a linha do adversário: "))
  coluna = int(input("Informe a coluna do adversário: "))
  if matriz[linha][coluna] == 'B':
    print("Você acertou a embarcação!")
    pontuation(turn)

  else:
    print("Você ERROU!")

def player_turn():
  starts = 'player_1'
  if starts == 'player_1':
      print('JOGADOR: ')
      atirar(matriz_2, starts)
      starts = 'player_2'
  if starts == 'player_2':
    print('COMPUTADOR: ')
    atirar(matriz_1, starts)

def pontuation(turn):
  global total_barcos_computador
  global total_barcos_jogador
  if turn == 'player_1':
    total_barcos_computador -= 1
  elif turn == 'player_2':
    total_barcos_jogador -= 1
  print(f'barcos do jogador: {total_barcos_jogador}')
  print(f'barcos do computador: {total_barcos_computador}')
    


matriz_1 = matriz_jogador_1()
matriz_2 = matriz_jogador_2()

print_matriz(matriz_1)
print('\n')
print_matriz(matriz_2)
print('\n')
while True:
  player_turn()