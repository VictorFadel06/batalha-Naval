from random import randint
from time import sleep
#biblioteca de estilização de título
import pyfiglet
#biblioteca para colorir o título
from termcolor import colored

texto = "SUPER BLASTER BATALHA NAVAL"
fonte = 'slant'

barcos = ['N','P','C','S','D']
letras_coordenadas = ['A','B','C','D','E','F','G','H','I','J']
num_coordenadas = [0,1,2,3,4,5,6,7,8,9]

# Variáveis globais
global linha, coluna

#configurações de título
titulo_estilizado = pyfiglet.figlet_format(text=texto, font= fonte)
titulo_colorido = colored(titulo_estilizado, 'blue')
print(titulo_colorido)
print('-'*50)


# Função para definir o tamanho da matriz
def definir_tamanho_matriz():
    global linha, coluna

    while True:
        try:
            tamanho = int(input("[1] Tabuleiro 5 x 10\n[2] Tabuleiro 10 x 10\n\nInforme o tabuleiro desejado (número da opção): "))
            if tamanho == 1:
              linha = 5
              coluna = 10
              return linha, coluna
            elif tamanho == 2:
              linha = 10
              coluna = 10
              return linha, coluna
            else:
                print("\nInsira uma opção valida...\n")
        except ValueError:
            print("\nPor favor, insira uma opção válida...\n")

#Usuário seleciona a dificuldade desejada
def dificuldade():
  while True:
    try:
      difficulty = int(input("[1] FÁCIL: barcos ocupam uma única posição, cada.\n[2] SURVIVOR: barcos possuem tamanhos variados.\n\nSelecione a dificuldade desejada (número da opção): "))
      if difficulty == 1:
        print('-'*50)
        easy()
        break
      elif difficulty == 2:
        print('-'*50)
        survivor()
        break
      else:
          print("\nInsira uma opção válida...\n")
    except ValueError:
      print("\nInsira uma opção válida...\n")

# função converte as coordenadas de letras em números
def converte_coordenadas_letras(coord):
  
  match coord:
      case 'A':
          coord = 0
      case 'B':
          coord = 1
      case 'C':
          coord = 2
      case 'D':
          coord = 3
      case 'E':
          coord = 4
      case 'F':
          coord = 5
      case 'G':
          coord = 6
      case 'H':
          coord = 7
      case 'I':
          coord = 8
      case 'J':
          coord = 9
      case _:
          raise ValueError("Linha inválida")
  
  return coord

def converte_coordenadas_num(coord):
  
  match coord:
      case 0:
          coord = 'A'
      case 1:
          coord = 'B'
      case 2:
          coord = 'C'
      case 3:
          coord = 'D'
      case 4:
          coord = 'E'
      case 5:
          coord = 'F'
      case 6:
          coord = 'G'
      case 7:
          coord = 'H'
      case 8:
          coord = 'I'
      case 9:
          coord = 'J'
      case _:
          raise ValueError("Linha inválida")
  
  return coord

  

#Dificuldade mais difícil
def survivor():

  embarcacoes = ['Porta-aviões', 'Navio-tanque', 'Contratorpedeiro', 'Submarino', 'Destroier']
  
  global build_turn
  global porta_avioes1, porta_avioes2, navio_tanque1, navio_tanque2
  global contratorpedo1, contratorpedo2, submarino1, submarino2, destroier1, destroier2
  global total_barcos_jogador, total_barcos_computador
  global matriz_desenhada1, matriz_desenhada2
  global linha, coluna

  linha, coluna = definir_tamanho_matriz()

  #define qual "matriz desenhada na tela" vai ser criada primeiro pela função
  build_turn = 1

  porta_avioes1  = 5
  porta_avioes2  = 5
  navio_tanque1 = 4
  navio_tanque2 = 4
  contratorpedo1 = 3
  contratorpedo2 = 3
  submarino1 = 2
  submarino2 = 2
  destroier1 = 1
  destroier2 = 1
  total_barcos_jogador = 5
  total_barcos_computador = 5
  matriz_desenhada1 = []
  matriz_desenhada2 = []
    

  # Cria as matrizes
  def criar_matriz():
    global linha, coluna
    global build_turn

    # Cria a matriz 1
    if build_turn == 1:

      build_turn += 1

      matriz_1 = []

      for i in range(linha):
        matriz_1.append([])
        for j in range(coluna):
          matriz_1[i].append('-')

      print('\033[33mJOGADOR: \033[m')
      for embarcacao in embarcacoes:
        print(f'Coordenadas do {embarcacao}, informe apenas as coordenadas do topo da embarcação: ')
        if embarcacao == embarcacoes[0]:

          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))

                linhas_para_num = int(converte_coordenadas_letras(linhas))

                
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue
                
                if colunas + 5 > coluna:
                    print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                    continue
                
                # Verifica se todas as posições estão livres
                if any(matriz_1[linhas_para_num][colunas + c] != '-' for c in range(5)):
                    print("Coordenada já possui navio em uma das posições...")
                    continue

                # Coloca o navio na matriz
                for c in range(5):
                    matriz_1[linhas_para_num][colunas + c] = 'P'
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')

            
        elif embarcacao == embarcacoes[1]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))

                linhas_para_num = int(converte_coordenadas_letras(linhas))

                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue
                
                if colunas + 4 > coluna:
                    print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                    continue
                
                # Verifica se todas as posições estão livres
                if any(matriz_1[linhas_para_num][colunas + c] != '-' for c in range(4)):
                    print("Coordenada já possui navio em uma das posições...")
                    continue

                # Coloca o navio na matriz
                for c in range(4):
                    matriz_1[linhas_para_num][colunas + c] = 'N'
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')

        elif embarcacao == embarcacoes[2]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))

                linhas_para_num = int(converte_coordenadas_letras(linhas))
                
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue
                
                if colunas + 3 > coluna:
                    print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                    continue
                
                # Verifica se todas as posições estão livres
                if any(matriz_1[linhas_para_num][colunas + c] != '-' for c in range(3)):
                    print("Coordenada já possui navio em uma das posições...")
                    continue

                # Coloca o navio na matriz
                for c in range(3):
                    matriz_1[linhas_para_num][colunas + c] = 'C'
                
                break  # Sai do loop enquanto tudo estiver correto
            
            except ValueError:
                print('Informe uma coordenada válida...')

        elif embarcacao == embarcacoes[3]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))

                linhas_para_num = int(converte_coordenadas_letras(linhas))
                
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue
                
                if colunas + 2 > coluna:
                    print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                    continue
                
                # Verifica se todas as posições estão livres
                if any(matriz_1[linhas_para_num][colunas + c] != '-' for c in range(2)):
                    print("Coordenada já possui navio em uma das posições...")
                    continue

                # Coloca o navio na matriz
                for c in range(2):
                    matriz_1[linhas_para_num][colunas + c] = 'S'
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')
        if embarcacao == embarcacoes[4]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))

                linhas_para_num = int(converte_coordenadas_letras(linhas))
                
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue
                
                if colunas + 1 > coluna:
                    print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                    continue
                
                # Verifica se todas as posições estão livres
                if any(matriz_1[linhas_para_num][colunas + c] != '-' for c in range(1)):
                    print("Coordenada já possui navio em uma das posições...")
                    continue

                # Coloca o navio na matriz
                for c in range(1):
                    matriz_1[linhas_para_num][colunas + c] = 'D'
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')

      print('Aguarde um momento...')
      sleep(1)
      for line in matriz_1:
        print(line)
      return matriz_1
    
      
    #Cria a matriz 2
    elif build_turn == 2:
      matriz_2 = []

      for i in range(linha):
        matriz_2.append([])
        for j in range(coluna):
          matriz_2[i].append('-')


      for embarcacao in embarcacoes:
        if embarcacao == embarcacoes[0]:
          # Gera coordenadas aleatórias
          linhas = randint(0, linha - 1)
          colunas = randint(0, coluna - 1)

          # Verifica se as coordenadas sorteadas não entram em conflito com as de outro barco. Caso sim, sorteia de novo
          while (colunas + 4) >= coluna or any(matriz_2[linhas][c] != '-' for c in range(colunas, colunas + 5)):
              linhas = randint(0, linha - 1)
              colunas = randint(0, coluna - 1)

          # Posiciona o barco
          for c in range(5):
              matriz_2[linhas][colunas + c] = 'P'

        elif embarcacao == embarcacoes[1]:
          # Gera coordenadas aleatórias
          linhas = randint(0, linha - 1)
          colunas = randint(0, coluna - 1)

          # Verifica se as coordenadas sorteadas não entram em conflito com as de outro barco. Caso sim, sorteia de novo
          while (colunas + 3) >= coluna or any(matriz_2[linhas][c] != '-' for c in range(colunas, colunas + 4)):
              linhas = randint(0, linha - 1)
              colunas = randint(0, coluna - 1)

          # Posiciona o barco
          for c in range(4):
              matriz_2[linhas][colunas + c] = 'N'
            
        elif embarcacao == embarcacoes[2]:
          # Gera coordenadas aleatórias
          linhas = randint(0, linha - 1)
          colunas = randint(0, coluna - 1)

          # Verifica se as coordenadas sorteadas não entram em conflito com as de outro barco. Caso sim, sorteia de novo
          while (colunas + 2) >= coluna or any(matriz_2[linhas][c] != '-' for c in range(colunas, colunas + 3)):
              linhas = randint(0, linha - 1)
              colunas = randint(0, coluna - 1)

          # Posiciona o barco
          for c in range(3):
              matriz_2[linhas][colunas + c] = 'C'

        elif embarcacao == embarcacoes[3]:
           # Gera coordenadas aleatórias
          linhas = randint(0, linha - 1)
          colunas = randint(0, coluna - 1)

          # Verifica se as coordenadas sorteadas não entram em conflito com as de outro barco. Caso sim, sorteia de novo
          while (colunas + 1) >= coluna or any(matriz_2[linhas][c] != '-' for c in range(colunas, colunas + 2)):
              linhas = randint(0, linha - 1)
              colunas = randint(0, coluna - 1)

          # Posiciona o barco
          for c in range(2):
              matriz_2[linhas][colunas + c] = 'S'

        elif embarcacao == embarcacoes[4]:
             # Gera coordenadas aleatórias
          linhas = randint(0, linha - 1)
          colunas = randint(0, coluna - 1)

          # Verifica se as coordenadas sorteadas não entram em conflito com as de outro barco. Caso sim, sorteia de novo
          while (colunas + 0) >= coluna or any(matriz_2[linhas][c] != '-' for c in range(colunas, colunas + 1)):
              linhas = randint(0, linha - 1)
              colunas = randint(0, coluna - 1)

          # Posiciona o barco
          for c in range(1):
              matriz_2[linhas][colunas + c] = 'D'

      print('\n')
      for line in matriz_2:
        print(line)
      return matriz_2


  # Cria a matriz com barcos "escondidos" na tela
  def criar_matriz_tela(matriz):
    global linha, coluna
    
    
    for i in range(linha):
      matriz.append([])
      for j in range(coluna):
        matriz[i].append('-')

    return matriz

  # Desenha a matriz com barcos "escondidos" na tela
  def print_matriz(matriz):
    global letras_coordenadas
    global num_coordenadas
    count = 0
    print(' ', end = ' ')
    for num in num_coordenadas:
       print(f'  \033[34m{num}\033[m  ', end='')
    print()
    for line in matriz:
      print(f'\033[34m{letras_coordenadas[count]}\033[m', end=' ')
      # print(f'\033[36m{line}\033[m')
      print(end= '  ')
      #Imprime os elementos coloridos no tabuleiro
      for elemento in line:
        if elemento == 'X':
            print(f'\033[31m{elemento}\033[m', end='    ')
        elif elemento == '/':
           print(f'\033[33m{elemento}\033[m', end='    ')
        else:
          print(f'\033[36m{elemento}\033[m', end='    ')
      print()
      count+=1


  # Atirar nos barcos
  def atirar(matriz, matriz_desenhada, turn):
    global linha, coluna
    print("Aguarde um momento...")
    sleep(1)
    if turn == 'player_1':
      while True:
        try: 
          linhas = input("Informe a linha do adversário: ").strip().upper()
          colunas = int(input("Informe a coluna do adversário: "))

          linhas = int(converte_coordenadas_letras(linhas))

          while linhas >= linha or colunas >= coluna:
            print("Coordenada fora dos limites")
            linhas = int(input("Informe a linha do adversário: "))
            colunas = int(input("Informe a coluna do adversário: "))
          break
        except ValueError:
          print('Informe uma coordenada válida...')

    elif turn == 'player_2':
      linhas = randint(0,linha-1)
      colunas = randint(0,coluna-1)

      linhas_letra = converte_coordenadas_num(linhas)

      print(f"Computador escolheu a linha {linhas_letra}")
      print(f"Computador escolheu a coluna {colunas}")

    if matriz[linhas][colunas] in 'PNCSD':
      print("Você \033[32mACERTOU\033[m a embarcação!")
      print('\n')
      coordenada = matriz[linhas][colunas]
      matriz[linhas][colunas] = 'X'
      matriz_desenhada[linhas][colunas] = 'X'
      pontuation(turn, coordenada)
      return coordenada
    elif matriz[linhas][colunas] == 'X':
      print("Embarcação JÁ destruída!")
      print('\n')
    else:
      print("Você \033[31mERROU!\033[m")
      print('\n')
      matriz_desenhada[linhas][colunas] = '/'
      
  # Vez do jogador
  def player_turn():
    starts = 'player_1'
    if starts == 'player_1':
      print('\033[33mJOGADOR: \033[m')
      atirar(matriz_2, matriz_desenhada2, starts)
      if total_barcos_computador == 0:
            return
      starts = 'player_2'
    if starts == 'player_2':
      print('\033[33mCOMPUTADOR: \033[m')
      atirar(matriz_1, matriz_desenhada1, starts)
      if total_barcos_jogador == 0:
        return

  # Pontuação
  def pontuation(turn, coordenada):
    global total_barcos_computador
    global total_barcos_jogador
    global porta_avioes1  
    global porta_avioes2  
    global navio_tanque1 
    global navio_tanque2 
    global contratorpedo1 
    global contratorpedo2 
    global submarino1 
    global submarino2 
    global destroier1 
    global destroier2 
    
    if turn == 'player_1':
      if coordenada == 'P':
        porta_avioes1  -= 1
        if porta_avioes1 == 0:
          print("\033[32mVocê destruiu o Porta-Aviões!\033[m")
          total_barcos_computador -= 1
      if coordenada == 'N':
        navio_tanque1 -= 1
        if navio_tanque1 == 0:
          print("\033[32mVocê destruiu o Navio-Tanque!\033[m")
          total_barcos_computador -= 1
      if coordenada == 'C':
        contratorpedo1 -= 1
        if contratorpedo1 == 0:
          print("\033[32mVocê destruiu o Contra-Torpedo!\033[m")
          total_barcos_computador -= 1
      if coordenada == 'S':
        submarino1 -= 1
        if submarino1 == 0:
          print("\033[32mVocê destruiu o Submarino!\033[m")
          total_barcos_computador -= 1
      if coordenada == 'D':
        destroier1 -= 1
        if destroier1 == 0:
          print("\033[32mVocê destruiu o Destroier!\033[m")
          total_barcos_computador -= 1
      if total_barcos_computador == 0:
        return
      
    elif turn == 'player_2':
      if coordenada == 'P':
        porta_avioes2  -= 1
        if porta_avioes2 == 0:
          print("Você destruiu o Porta-Aviões!")
          total_barcos_jogador -= 1
      if coordenada == 'N':
        navio_tanque2 -= 1
        if navio_tanque2 == 0:
          print("Você destruiu o Navio-Tanque!")
          total_barcos_jogador -= 1
      if coordenada == 'C':
        contratorpedo2 -= 1
        if contratorpedo2 == 0:
          print("Você destruiu o Contra-Torpedo!")
          total_barcos_jogador -= 1
      if coordenada == 'S':
        submarino2 -= 1
        if submarino2 == 0:
          print("Você destruiu o Submarino!")
          total_barcos_jogador -= 1
      if coordenada == 'D':
        destroier2 -= 1
        if destroier2 == 0:
          print("Você destruiu o Destroier!")
          total_barcos_jogador -= 1
      if total_barcos_jogador == 0:
        return
      

  matriz_1 = criar_matriz()
  matriz_2 = criar_matriz()
  matriz_d1 = criar_matriz_tela(matriz_desenhada1)
  matriz_d2 = criar_matriz_tela(matriz_desenhada2)

  sleep(0.5)
  print('\n')
  print('-'*50)
  print('Tabuleiro do Jogador')
  print_matriz(matriz_d1)
  print('-'*50)
  print(f'Embarcações restantes: {total_barcos_jogador}')
  print('\n')
  sleep(0.5)
  print('-'*50)
  print('Tabuleiro do Computador')
  print_matriz(matriz_d2)
  print('-'*50)
  print(f'Embarcações restantes: {total_barcos_computador}')
  print('\n')

  while total_barcos_computador != 0 and total_barcos_jogador != 0:
      player_turn()
      sleep(0.5) 
      print('-'*50)
      print('Tabuleiro do Jogador')
      print_matriz(matriz_d1)
      print('-'*50)
      print(f'Embarcações restantes: {total_barcos_jogador}')
      print('\n')
      sleep(0.5)
      print('-'*50)
      print('Tabuleiro do Computador')
      print_matriz(matriz_d2)
      print('-'*50)
      print(f'Embarcações restantes: {total_barcos_computador}')
      print('\n')
      if total_barcos_jogador == 0:
          print("\033[31mCOMPUTADOR afundou todas as embarcações do inimigo!!!\033[m")
          break  # Encerra o loop quando o jogador perde
      if total_barcos_computador == 0:
          print("\033[32mJOGADOR afundou todas as embarcações do inimigo. Parabéns!!!\033[m")
          break  # Encerra o loop quando o jogador ganha



#Dificuldade 'fácil'

def easy():
  global barcos_totais_computador
  global barcos_totais_jogador
  barcos_totais_jogador = 5
  barcos_totais_computador = 1
  global linha, coluna

  linha, coluna = definir_tamanho_matriz()

  print('-'*50)

  #criar matriz 1 e posiciona embarcações
  def matriz_jogador_1():
    global linha, coluna
    matriz_1 = []

    for i in range(linha):
      matriz_1.append([])
      for j in range(coluna):
        matriz_1[i].append('-')

    print('\033[34mJOGADOR\033[m: ')
    for c in range(5):
      print(f'Coordenadas da {c+1}º embarcação: ')
      while True:
        try:
          linhas = input("Qual linha? ").strip().upper()
          colunas = int(input("Qual coluna? "))

          linhas_para_num = int(converte_coordenadas_letras(linhas))

          matriz_1[linhas_para_num][colunas] = 'B'
          break
        except ValueError:
          print("Insira uma coordenada válida...")
        except IndexError:
            print("Insira uma coordenada dentro dos limites da matriz...")

    print('Aguarde um momento...')
    sleep(0.5)
    return matriz_1

  def matriz_jogador_2():
    global linha, coluna
    matriz_2 = []

    for i in range(linha):
      matriz_2.append([])
      for j in range(coluna):
        matriz_2[i].append('-')

    for c in range(5):
      matriz_2[randint(0,linha-1)][randint(0,coluna-1)] = 'B'

    return matriz_2

  def desenhar_matriz_1():
    global linha, coluna
    matriz_desenhada1 = []

    for i in range(linha):
      matriz_desenhada1.append([])
      for j in range(coluna):
        matriz_desenhada1[i].append('-')

    return matriz_desenhada1

  def desenhar_matriz_2():
    global linha, coluna
    matriz_desenhada2 = []

    for i in range(linha):
      matriz_desenhada2.append([])
      for j in range(coluna):
        matriz_desenhada2[i].append('-')

    return matriz_desenhada2

  #função para imprimir a matriz na tela
  def print_matriz(matriz):
    global letras_coordenadas
    global num_coordenadas
    global linha, coluna
    count = 0
    print(' ', end = ' ')

    for num in num_coordenadas:
       print(f'  \033[34m{num}\033[m  ', end='')
    print()
    for line in matriz:
      print(f'\033[34m{letras_coordenadas[count]}\033[m', end=' ')
      # print(f'\033[36m{line}\033[m')
      print(end= '  ')
      for elemento in line:
        if elemento == 'X':
            print(f'\033[31m{elemento}\033[m', end='    ')
        elif elemento == 'N':
           print(f'\033[33m{elemento}\033[m', end='    ')
        else:
          print(f'\033[36m{elemento}\033[m', end='    ')
      print()
      count+=1

  #função para atirar no inimigo
  def atirar(matriz, matriz_desenhada, turn):
    global linha, coluna
    sleep(1)
    if turn == 'player_1':
      while True:
        try:
          linhas = input("Informe a linha do adversário: ").upper().strip()
          colunas = int(input("Informe a coluna do adversário: "))

          linhas = int(converte_coordenadas_letras(linhas))

          if linhas < 0 or linhas >= linha or colunas < 0 or colunas >= coluna:
            raise IndexError
          break

        except ValueError:
          print("Insira uma coordenada válida...") 
        except IndexError:
          print("Insira uma coordenada dentro dos limites da matriz...")
        
    else:
      linhas = randint(0,linha-1)
      colunas = randint(0,coluna-1)
      linhas_letra = converte_coordenadas_num(linhas)
      print(f"Computador escolheu a linha {linhas_letra}")
      print(f"Computador escolheu a coluna {colunas}")
    if matriz[linhas][colunas] == 'B':
      print("\033[32mVocê acertou a embarcação!\033[m")
      print('\n')
      matriz[linhas][colunas] = 'X'
      matriz_desenhada[linhas][colunas] = 'X'
      pontuation(turn)
    elif matriz[linhas][colunas] == 'X':
      print("Embarcação JÁ destruída!")
      print('\n')
    else:
      print("Você \033[31mERROU!\033[m")
      print('\n')
      matriz_desenhada[linhas][colunas] = 'N'
      
  #define o turno do jogador
  def player_turn():
    global linha, coluna
    starts = 'player_1'
    if starts == 'player_1':
      print('\033[34mJOGADOR\033[m: ')
      atirar(matriz_2, matriz_desenhada2, starts)
      starts = 'player_2'
    if starts == 'player_2':
      print('\033[33mCOMPUTADOR\033[m: ')
      atirar(matriz_1, matriz_desenhada1, starts)

  #calcula a pontuação do total de barcos destruídos
  def pontuation(turn):
    global linha, coluna
    global barcos_totais_computador
    global barcos_totais_jogador
    if turn == 'player_1':
      barcos_totais_computador -= 1
    elif turn == 'player_2':
      barcos_totais_jogador -= 1

  matriz_1 = matriz_jogador_1()
  matriz_2 = matriz_jogador_2()
  matriz_desenhada1 = desenhar_matriz_1()
  matriz_desenhada2 = desenhar_matriz_2()

  sleep(0.5)
  print('\n')
  print('-'*50)
  print('Tabuleiro do Jogador')
  print_matriz(matriz_desenhada1)
  print('-'*50)
  print(f'Embarcações restantes: {barcos_totais_jogador}')
  print('\n')
  sleep(0.5)
  print('-'*50)
  print('Tabuleiro do Computador')
  print_matriz(matriz_desenhada2)
  print('-'*50)
  print(f'Embarcações restantes: {barcos_totais_computador}')
  print('\n')

  while barcos_totais_computador != 0 and barcos_totais_jogador != 0:
    player_turn()
    sleep(1) 
    print('-'*50)
    print('Tabuleiro do Jogador')
    print_matriz(matriz_desenhada1)
    print('-'*50)
    print(f'Embarcações restantes: {barcos_totais_jogador}')
    print('\n')
    sleep(1)
    print('-'*50)
    print('Tabuleiro do Computador')
    print_matriz(matriz_desenhada2)
    print('-'*50)
    print(f'Embarcações restantes: {barcos_totais_computador}')
    print('\n')
    if barcos_totais_jogador == 0:
      print("\033[31mCOMPUTADOR afundou todas as embarcações do jogador!!!\033[m")
    if barcos_totais_computador == 0:
      print("\033[32mJOGADOR afundou todas as embarcações do inimigo, parabéns!!!\033[m")

dificuldade()

print('-'*50)
print("Jogo desenvolvido por:\n- Riscala Miguel Fadel Neto\n- Pedro Senes\n- Victor Valerio Fadel\n")
print("Esse jogo teve auxílio técnico-criativo de Hideo Kojima, Sam Lake, Hidetaka Miyazaki e Shigeru Miyamoto.")
print('-'*50)

