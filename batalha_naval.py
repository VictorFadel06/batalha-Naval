from random import randint
from time import sleep
import os

total_barcos_jogador = 5
total_barcos_computador = 5

embarcacoes = ['Porta-aviões', 'Navio-tanque', 'Contratorpedeiro', 'Submarino', 'Destroier']

print("SUPER BLASTER BATALHA NAVAL")
print('-'*50)

def matriz_jogador_1():
  matriz_1 = []

  for i in range(10):
    matriz_1.append([])
    for j in range(10):
      matriz_1[i].append('-')

  print('JOGADOR: ')
  for num, embarcacao in enumerate(embarcacoes):
    print(f'Coordenadas do {embarcacao}, informe apenas as coordenadas do topo da embarcação: ')
    if embarcacao == embarcacoes[0]:
      linha = int(input("Qual linha? "))
      coluna = int(input("Qual coluna? "))
      while (coluna + 5 > 10):
        print("Coordenada inválida, fora dos limites...")
        linha = int(input("Qual linha? "))
        coluna = int(input("Qual coluna? "))
      
      for c in range(5):
        if c == 0:
          linha1 = linha
        if matriz_1[linha1][coluna+c] != '-':
          print("Coordenada já possui navio...")
        else:
          matriz_1[linha1][coluna+c] = 'P'

        
    elif embarcacao == embarcacoes[1]:
      linha = int(input("Qual linha? "))
      coluna = int(input("Qual coluna? "))
      while (coluna + 5 > 10):
        print("Coordenada inválida, fora dos limites...")
        linha = int(input("Qual linha? "))
        coluna = int(input("Qual coluna? "))

      for c in range(4):
        if c == 0:
          linha1 = linha
        while matriz_1[linha1][coluna+c] != '-':
          print("Coordenada já possui navio...")
          linha = int(input("Qual linha? "))
          coluna = int(input("Qual coluna? "))
          linha1 = linha
        else:
          matriz_1[linha1][coluna+c] = 'N'

    elif embarcacao == embarcacoes[2]:
      linha = int(input("Qual linha? "))
      coluna = int(input("Qual coluna? "))
      while (coluna + 5 > 10):
        print("Coordenada inválida, fora dos limites...")
        linha = int(input("Qual linha? "))
        coluna = int(input("Qual coluna? "))

      for c in range(3):
        if c == 0:
          linha1 = linha
        while matriz_1[linha1][coluna+c] != '-':
          print("Coordenada já possui navio...")
          linha = int(input("Qual linha? "))
          coluna = int(input("Qual coluna? "))
          linha1 = linha
        else:
          matriz_1[linha1][coluna+c] = 'C'
    elif embarcacao == embarcacoes[3]:
      linha = int(input("Qual linha? "))
      coluna = int(input("Qual coluna? "))
      while (coluna + 5 > 10):
        print("Coordenada inválida, fora dos limites...")
        linha = int(input("Qual linha? "))
        coluna = int(input("Qual coluna? "))
      for c in range(2):
        if c == 0:
          linha1 = linha
        while matriz_1[linha1][coluna+c] != '-':
          print("Coordenada já possui navio...")
          linha = int(input("Qual linha? "))
          coluna = int(input("Qual coluna? "))
          linha1 = linha
        else:
          matriz_1[linha1][coluna+c] = 'S'
    if embarcacao == embarcacoes[4]:
      linha = int(input("Qual linha? "))
      coluna = int(input("Qual coluna? "))
      while (coluna + 5 > 10):
        print("Coordenada inválida, fora dos limites...")
        linha = int(input("Qual linha? "))
        coluna = int(input("Qual coluna? "))
      for c in range(1):
        if c == 0:
          linha1 = linha
        while matriz_1[linha1][coluna+c] != '-':
          print("Coordenada já possui navio...")
          linha = int(input("Qual linha? "))
          coluna = int(input("Qual coluna? "))
          linha1 = linha
        else:
          matriz_1[linha1][coluna+c] = 'D'

  print('Aguarde um momento...')
  sleep(1)
  for linha in matriz_1:
    print(linha)
  return matriz_1




def matriz_jogador_2():
  matriz_2 = []

  for i in range(10):
    matriz_2.append([])
    for j in range(10):
      matriz_2[i].append('-')

  # for c in range(5):
    # matriz_2[randint(0,5)][randint(0,5)] = 'B'

  for embarcacao in embarcacoes:
    if embarcacao == embarcacoes[0]:
      linha = randint(0,5)
      coluna = randint(0,5)
      for c in range(5):
        if c == 0:
          linha1 = linha
          coluna1 = coluna
        matriz_2[linha1][coluna1+c] = 'P'
    elif embarcacao == embarcacoes[1]:
      for c in range(4):
        linha = randint(0,5)
        if c == 0:
          linha1 = linha
        coluna = randint(0,5)
        matriz_2[linha1][coluna] = 'N'
    elif embarcacao == embarcacoes[2]:
      for c in range(3):
        linha = randint(0,5)
        if c == 0:
          linha1 = linha
        linha = randint(0,5)
        coluna = randint(0,5)
        matriz_2[linha1][coluna] = 'C'
    elif embarcacao == embarcacoes[3]:
      for c in range(2):
        linha = randint(0,5)
        if c == 0:
          linha1 = linha
        linha = randint(0,5)
        coluna = randint(0,5)
        matriz_2[linha1][coluna] = 'S'
    if embarcacao == embarcacoes[4]:
        linha = randint(0,5)
        if c == 0:
          linha1 = linha
        linha = randint(0,5)
        coluna = randint(0,5)
        matriz_2[linha1][coluna] = 'D'

  print('\n')
  for linha in matriz_2:
    print(linha)
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
  sleep(2)
  if turn == 'player_1':
    linha = int(input("Informe a linha do adversário: "))
    coluna = int(input("Informe a coluna do adversário: "))
  else:
    linha = randint(0,9)
    coluna = randint(0,9)
    print(f"Computador escolheu a linha {linha}")
    print(f"Computador escolheu a coluna {coluna}")
  if matriz[linha][coluna] == 'B':
    print("Você acertou a embarcação!")
    print('\n')
    matriz[linha][coluna] = 'X'
    matriz_desenhada[linha][coluna] = 'X'
    pontuation(turn)
  elif matriz[linha][coluna] == 'X':
    print("Embarcação JÁ destruída!")
    print('\n')
  else:
    print("Você ERROU!")
    print('\n')
    matriz_desenhada[linha][coluna] = '/'
    

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

sleep(1)
print('\n')
print('-'*50)
print('Tabuleiro do Jogador')
print_matriz(matriz_desenhada1)
print('-'*50)
print(f'Embarcações restantes: {total_barcos_jogador}')
print('\n')
sleep(1)
print('-'*50)
print('Tabuleiro do Computador')
print_matriz(matriz_desenhada2)
print('-'*50)
print(f'Embarcações restantes: {total_barcos_computador}')
print('\n')

while total_barcos_computador != 0 and total_barcos_jogador != 0:
  player_turn()
  sleep(2) 
  print('-'*50)
  print('Tabuleiro do Jogador')
  print_matriz(matriz_desenhada1)
  print('-'*50)
  print(f'Embarcações restantes: {total_barcos_jogador}')
  print('\n')
  sleep(1)
  print('-'*50)
  print('Tabuleiro do Computador')
  print_matriz(matriz_desenhada2)
  print('-'*50)
  print(f'Embarcações restantes: {total_barcos_computador}')
  print('\n')
  if total_barcos_jogador == 0:
    print("COMPUTADOR Ganhou!!!")
  if total_barcos_computador == 0:
    print("JOGADOR Ganhou!!!")