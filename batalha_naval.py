from random import randint
import os

total_barcos_jogador = 5
total_barcos_computador = 5

print("SUPER BLASTER BATALHA NAVAL")
print('-'*50)

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

def desenhar_matriz_1():
  matriz_desenhada1 = []

  for i in range(10):
    matriz_desenhada1.append([])
    for j in range(10):
      matriz_desenhada1[i].append('-')

  return matriz_desenhada1

def desenhar_matriz_2():
  matriz_desenhada2 = []

  for i in range(10):
    matriz_desenhada2.append([])
    for j in range(10):
      matriz_desenhada2[i].append('-')

  return matriz_desenhada2

def print_matriz(matriz):
  for linha in matriz:
    print(linha)

def atirar(matriz, matriz_desenhada, turn):
  if turn == 'player_1':
    linha = int(input("Informe a linha do adversário: "))
    coluna = int(input("Informe a coluna do adversário: "))
  else:
    linha = randint(0,9)
    coluna = randint(0,9)
  if matriz[linha][coluna] == 'B':
    print("Você acertou a embarcação!")
    matriz[linha][coluna] = 'X'
    matriz_desenhada[linha][coluna] = 'X'
    pontuation(turn)
  elif matriz[linha][coluna] == 'X':
    print("Embarcação JÁ destruída!")
  else:
    print("Você ERROU!")
    matriz_desenhada[linha][coluna] = 'N'
    

def player_turn():
  starts = 'player_1'
  if starts == 'player_1':
    # os.system('cls')
    print('JOGADOR: ')
    atirar(matriz_2, matriz_desenhada2, starts)
    starts = 'player_2'
  if starts == 'player_2':
    # os.system('cls')
    print('COMPUTADOR: ')
    atirar(matriz_1, matriz_desenhada1, starts)

def pontuation(turn):
  global total_barcos_computador
  global total_barcos_jogador
  if turn == 'player_1':
    total_barcos_computador -= 1
  elif turn == 'player_2':
    total_barcos_jogador -= 1
  

matriz_1 = matriz_jogador_1()
matriz_2 = matriz_jogador_2()
matriz_desenhada1 = desenhar_matriz_1()
matriz_desenhada2 = desenhar_matriz_2()


print('\n')
print('Tabuleiro do Jogador')
print_matriz(matriz_desenhada1)
print('-'*50)
print(f'Embarcações restantes: {total_barcos_jogador}')
print('\n')
print('Tabuleiro do Computador')
print_matriz(matriz_desenhada2)
print('-'*50)
print(f'Embarcações restantes: {total_barcos_computador}')
print('\n')

while total_barcos_computador != 0 and total_barcos_jogador != 0:
  player_turn()
  print('Tabuleiro do Jogador')
  print_matriz(matriz_desenhada1)
  print('-'*50)
  print(f'Embarcações restantes: {total_barcos_jogador}')
  print('\n')
  print('Tabuleiro do Computador')
  print_matriz(matriz_desenhada2)
  print('-'*50)
  print(f'Embarcações restantes: {total_barcos_computador}')
  print('\n')
  if total_barcos_jogador == 0:
    print("COMPUTADOR Ganhou!!!")
  if total_barcos_computador == 0:
    print("JOGADOR Ganhou!!!")