from random import randint
from time import sleep
import pyfiglet
from termcolor import colored

texto = "SUPER BLASTER BATALHA NAVAL"
fonte = 'slant'

titulo_estilizado = pyfiglet.figlet_format(text=texto, font= fonte)
titulo_colorido = colored(titulo_estilizado, 'blue')
print(titulo_colorido)
print('-'*50)

#Usuário seleciona a dificuldade desejada
def dificuldade():
  while True:
    try:
      difficulty = int(input("[1] FÁCIL: barcos ocupam uma única posição, cada\n[2] SURVIVOR: barcos possuem tamanhos variados\nSelecione a dificuldade desejada (número da opção): "))
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

  

#Dificuldade mais difícil
def survivor():

  embarcacoes = ['Porta-aviões', 'Navio-tanque', 'Contratorpedeiro', 'Submarino', 'Destroier']
  

  global build_turn
  global porta_avioes1, porta_avioes2, navio_tanque1, navio_tanque2
  global contratorpedo1, contratorpedo2, submarino1, submarino2, destroier1, destroier2
  global total_barcos_jogador, total_barcos_computador
  global matriz_desenhada1, matriz_desenhada2


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
  total_barcos_computador = 1
  matriz_desenhada1 = []
  matriz_desenhada2 = []

  # Cria as matrizes
  def criar_matriz():
    global build_turn

    # Cria a matriz 1
    if build_turn == 1:

      build_turn += 1

      matriz_1 = []

      for i in range(10):
        matriz_1.append([])
        for j in range(10):
          matriz_1[i].append('-')

      print('JOGADOR: ')
      for num, embarcacao in enumerate(embarcacoes):
        print(f'Coordenadas do {embarcacao}, informe apenas as coordenadas do topo da embarcação: ')
        if embarcacao == embarcacoes[0]:
          while True:
            try:
                linha = int(input("Qual linha? "))
                coluna = int(input("Qual coluna? "))
                
                while coluna + 5 > 10:
                    print("Coordenada inválida, fora dos limites...")
                    linha = int(input("Qual linha? "))
                    coluna = int(input("Qual coluna? "))
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')
      
            
          for c in range(5):
            if c == 0:
              linha1 = linha
            if matriz_1[linha1][coluna+c] != '-':
              print("Coordenada já possui navio...")
            else:
              matriz_1[linha1][coluna+c] = 'P'

            
        elif embarcacao == embarcacoes[1]:
          while True:
            try:
                linha = int(input("Qual linha? "))
                coluna = int(input("Qual coluna? "))
                
                while coluna + 4 > 10:
                    print("Coordenada inválida, fora dos limites...")
                    linha = int(input("Qual linha? "))
                    coluna = int(input("Qual coluna? "))
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')

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
          while True:
            try:
                linha = int(input("Qual linha? "))
                coluna = int(input("Qual coluna? "))
                
                while coluna + 3 > 10:
                    print("Coordenada inválida, fora dos limites...")
                    linha = int(input("Qual linha? "))
                    coluna = int(input("Qual coluna? "))
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')

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
          while True:
            try:
                linha = int(input("Qual linha? "))
                coluna = int(input("Qual coluna? "))
                
                while coluna + 2 > 10:
                    print("Coordenada inválida, fora dos limites...")
                    linha = int(input("Qual linha? "))
                    coluna = int(input("Qual coluna? "))
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')

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
          while True:
            try:
                linha = int(input("Qual linha? "))
                coluna = int(input("Qual coluna? "))
                
                while coluna + 1 > 10:
                    print("Coordenada inválida, fora dos limites...")
                    linha = int(input("Qual linha? "))
                    coluna = int(input("Qual coluna? "))
                
                break  # Sai do loop enquanto tudo estiver correto
            except ValueError:
                print('Informe uma coordenada válida...')
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
      # for linha in matriz_1:
      #   print(linha)
      return matriz_1
    
      
    #Cria a matriz 2
    elif build_turn == 2:
      matriz_2 = []

      for i in range(10):
        matriz_2.append([])
        for j in range(10):
          matriz_2[i].append('-')


      for embarcacao in embarcacoes:
        if embarcacao == embarcacoes[0]:
          linha = randint(0,9)
          coluna = randint(0,9)
          #verifica se as coordenadas sorteadas não entram em conflito com as de outro barco. Caso sim, sorteia de novo
          while matriz_2[linha][coluna] != '-' and matriz_2[linha][coluna+1] != '-' and matriz_2[linha][coluna+2] != '-' and matriz_2[linha][coluna+3] != '-' and matriz_2[linha][coluna+4] != '-':
            linha = randint(0,9)
            coluna = randint(0,9)
          for j in range(coluna):
            while matriz_2[linha][j] != '-':
              linha = randint(0,9)
              coluna = randint(0,9)
          while (coluna + 5) > 10:
            coluna = randint(0,9)
          for c in range(5):
            if c == 0:
              linha1 = linha
              coluna1 = coluna
            matriz_2[linha1][coluna1+c] = 'P'
        elif embarcacao == embarcacoes[1]:
          linha = randint(0,9)
          coluna = randint(0,9)
          
          while matriz_2[linha][coluna] != '-' and matriz_2[linha][coluna+1] != '-' and matriz_2[linha][coluna+2] != '-' and matriz_2[linha][coluna+3] != '-':
            linha = randint(0,9)
            coluna = randint(0,9)

          for j in range(coluna):
            while matriz_2[linha][j] != '-':
              linha = randint(0,9)
              coluna = randint(0,9)
          while (coluna + 4) > 10:
            coluna = randint(0,9)
          for c in range(4):
            linha = randint(0,9)
            if c == 0:
              linha1 = linha
              coluna1 = coluna
            matriz_2[linha1][coluna1+c] = 'N'
        elif embarcacao == embarcacoes[2]:
          for c in range(3):
            linha = randint(0,9)
            coluna = randint(0,9)
            while matriz_2[linha][coluna] != '-' and matriz_2[linha][coluna+1] != '-' and matriz_2[linha][coluna+2] != '-':
              linha = randint(0,9)
              coluna = randint(0,9)
            while (coluna + 3) > 10:
              coluna = randint(0,9)
            if c == 0:
              linha1 = linha
              coluna1 = coluna
            matriz_2[linha1][coluna1+c] = 'C'
        elif embarcacao == embarcacoes[3]:
          for c in range(2):
            linha = randint(0,9)
            coluna = randint(0,9)
          
            while matriz_2[linha][coluna] != '-' and matriz_2[linha][coluna+1] != '-':
              linha = randint(0,9)
              coluna = randint(0,9)
            while (coluna + 2) > 10:
              coluna = randint(0,9)
            if c == 0:
              linha1 = linha
              coluna1 = coluna
            matriz_2[linha1][coluna1+c] = 'S'
        elif embarcacao == embarcacoes[4]:
            linha = randint(0,9)
            coluna = randint(0,9)
            while (coluna + 1) > 10:
              coluna = randint(0,9)
            if c == 0:
              linha1 = linha
              coluna1 = coluna
            matriz_2[linha][coluna1+c] = 'D'

      print('\n')
      # for linha in matriz_2:
      #   print(linha)
      return matriz_2


  # Desenha a matriz na tela
  def criar_matriz_tela(matriz):

    for i in range(10):
      matriz.append([])
      for j in range(10):
        matriz[i].append('-')

    return matriz

  def print_matriz(matriz):
    for linha in matriz:
      print(linha)

  # Atirar nos barcos
  def atirar(matriz, matriz_desenhada, turn):
    print("Aguarde um momento...")
    sleep(2)
    if turn == 'player_1':
      while True:
        try: 
          linha = int(input("Informe a linha do adversário: "))
          coluna = int(input("Informe a coluna do adversário: "))
          break
        except ValueError:
          print('Informe uma coordenada válida...')

    else:
      linha = randint(0,9)
      coluna = randint(0,9)
      print(f"Computador escolheu a linha {linha}")
      print(f"Computador escolheu a coluna {coluna}")
    if matriz[linha][coluna] in 'PNCSD':
      print("Você \033[32mACERTOU\033[m a embarcação!")
      print('\n')
      coordenada = matriz[linha][coluna]
      matriz[linha][coluna] = 'X'
      matriz_desenhada[linha][coluna] = 'X'
      pontuation(turn, coordenada)
      return coordenada
    elif matriz[linha][coluna] == 'X':
      print("Embarcação JÁ destruída!")
      print('\n')
    else:
      print("Você \033[31mERROU!\033[m")
      print('\n')
      matriz_desenhada[linha][coluna] = '/'
      
  # Vez do jogador
  def player_turn():
    starts = 'player_1'
    if starts == 'player_1':
      print('JOGADOR: ')
      atirar(matriz_2, matriz_desenhada2, starts)
      if total_barcos_computador == 0:
            return
      starts = 'player_2'
    if starts == 'player_2':
      print('COMPUTADOR: ')
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

  # print("SUPER BLASTER BATALHA NAVAL")
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
      while True:
        try:
          linha = int(input("Qual linha? "))
          coluna = int(input("Qual coluna? "))
          matriz_1[linha][coluna] = 'B'
          break
        except ValueError:
          print("Insira uma coordenada válida...")
        except IndexError:
            print("Insira uma coordenada dentro dos limites da matriz...")

    print('Aguarde um momento...')
    sleep(1)
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
    sleep(2)
    if turn == 'player_1':
      while True:
        try:
          linha = int(input("Informe a linha do adversário: "))
          coluna = int(input("Informe a coluna do adversário: "))
          break
        except ValueError:
          print("Insira uma coordenada válida...") 
        except IndexError:
          print("Insira uma coordenada dentro dos limites da matriz...")
        
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

  sleep(1)
  print('\n')
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
      print("COMPUTADOR Ganhou!!!")
    if barcos_totais_computador == 0:
      print("JOGADOR Ganhou!!!")



dificuldade()

print('-'*50)
print("Jogo desenvolvido por:\n- Riscala Miguel Fadel Neto\n- Pedro Senes\n- Victor Valerio Fadel\n")
print("Esse jogo teve auxílio técnico-criativo de Hideo Kojima, Sam Lake, Hidetaka Miyazaki e Shigeru Miyamoto.")
print('-'*50)