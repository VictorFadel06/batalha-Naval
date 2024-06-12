from random import randint, choice
from time import sleep
#biblioteca de estilização de título
import pyfiglet
#biblioteca para colorir o título
from termcolor import colored

texto = "METAL BATTLESHIP SOLID"
fonte = 'slant'

#iniciais de cada embarcação colocadas no tabuleiro "survivor"
barcos = ['N','P','C','S','D']
#coordenadas de linhas do tabuleiro
letras_coordenadas = ['A','B','C','D','E','F','G','H','I','J']
#coordenadas de colunas no tabuleiro
num_coordenadas = [0,1,2,3,4,5,6,7,8,9]

# Variáveis globais para definir tamanho do tabuleiro
global linha, coluna

#configurações de título
titulo_estilizado = pyfiglet.figlet_format(text=texto, font= fonte)
titulo_colorido = colored(titulo_estilizado, 'blue')
print(titulo_colorido)
print('-'*50)


# Função para definir o tamanho da matriz
def definir_tamanho_matriz():
    global linha, coluna
    #loop para escolher tamanho do tabuleiro
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
  #loop para escolher nivel de dificuldade
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

#Oposto da função converte_coordenadas_letras(coord)
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
  #linha e coluna recebem os valores definidos ao escolher o tamanho da matriz
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
      #build_turn fica com valor 2, fazendo com que a proxima matriz a ser montada seja a do computador
      build_turn += 1

      matriz_1 = []
      #loop para criar uma matriz vazia
      for i in range(linha):
        matriz_1.append([])
        for j in range(coluna):
          matriz_1[i].append('-')
      #loop que passará por cada embarcação da lista "embarcacoes, para definir a possição de cada embarcação"
      print('\033[33mJOGADOR: \033[m')
      for embarcacao in embarcacoes:
        if embarcacao == embarcacoes[0]:  # Porta-aviões
          tamanho_embarcacao = 5
        elif embarcacao == embarcacoes[1]:  # Navio-tanque
          tamanho_embarcacao = 4
        elif embarcacao == embarcacoes[2]:  # Contratorpedeiro
          tamanho_embarcacao = 3
        elif embarcacao == embarcacoes[3]:  # Submarino
          tamanho_embarcacao = 2
        else: # Destroier
          tamanho_embarcacao = 1
        print(f'Coordenadas do {embarcacao}, informe apenas as coordenadas do topo da embarcação: ')
        if embarcacao == embarcacoes[0]: #Porta-aviões
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper().strip()
                #chama a função converte_coordenadas_letras(linhas) para converter a coordenada "letra" informada pela usuário em um número
                linhas_para_num = int(converte_coordenadas_letras(linhas))

                #checar se as coordenadas informadas estão dentros dos limites do tabuleiro
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue

                if orientacao == 'H':
                  #checar se a embarcação, ao ser posicionada, não ultrapassa os limites do tabuleiro. Soma-se 5 a colunas, pois nesse caso o Porta-aviões ocupa 5 casas. Para as embarcações seguintes, soma-se 4,3,2...
                  if colunas + tamanho_embarcacao > coluna:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue
                  
                  if any(colunas + c >= coluna or matriz_1[linhas_para_num][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  # Coloca o navio na matriz
                  for c in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num][colunas + c] = 'P'
                
                elif orientacao == 'V':
                  if linhas_para_num + tamanho_embarcacao > linha:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue

                  if any(linhas_para_num + r >= linha or matriz_1[linhas_para_num + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  for r in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num + r][colunas] = 'P'
                else:
                    print("Orientação inválida, escolha 'H' para horizontal ou 'V' para vertical.")
                    continue

                break  # Sai do loop enquanto tudo estiver correto

            except ValueError:
                print('Informe uma coordenada válida...')

            
        elif embarcacao == embarcacoes[1]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper().strip()
                #chama a função converte_coordenadas_letras(linhas) para converter a coordenada "letra" informada pela usuário em um número
                linhas_para_num = int(converte_coordenadas_letras(linhas))

                #checar se as coordenadas informadas estão dentros dos limites do tabuleiro
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue

                if orientacao == 'H':
               
                  #checar se a embarcação, ao ser posicionada, não ultrapassa os limites do tabuleiro. Soma-se 5 a colunas, pois nesse caso o Porta-aviões ocupa 5 casas. Para as embarcações seguintes, soma-se 4,3,2...
                  if colunas + tamanho_embarcacao > coluna:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue
                  
                  if any(colunas + c >= coluna or matriz_1[linhas_para_num][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  # Coloca o navio na matriz
                  for c in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num][colunas + c] = 'N'
                
                elif orientacao == 'V':
                  if linhas_para_num + tamanho_embarcacao > linha:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue

                  if any(linhas_para_num + r >= linha or matriz_1[linhas_para_num + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  for r in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num + r][colunas] = 'N'
                else:
                    print("Orientação inválida, escolha 'H' para horizontal ou 'V' para vertical.")
                    continue

                break  # Sai do loop enquanto tudo estiver correto

            except ValueError:
                print('Informe uma coordenada válida...')

        elif embarcacao == embarcacoes[2]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper().strip()
                #chama a função converte_coordenadas_letras(linhas) para converter a coordenada "letra" informada pela usuário em um número
                linhas_para_num = int(converte_coordenadas_letras(linhas))

                #checar se as coordenadas informadas estão dentros dos limites do tabuleiro
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue

                if orientacao == 'H':
               
                  #checar se a embarcação, ao ser posicionada, não ultrapassa os limites do tabuleiro. Soma-se 5 a colunas, pois nesse caso o Porta-aviões ocupa 5 casas. Para as embarcações seguintes, soma-se 4,3,2...
                  if colunas + tamanho_embarcacao > coluna:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue
                  
                  if any(colunas + c >= coluna or matriz_1[linhas_para_num][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  # Coloca o navio na matriz
                  for c in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num][colunas + c] = 'C'
                
                elif orientacao == 'V':
                  if linhas_para_num + tamanho_embarcacao > linha:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue

                  if any(linhas_para_num + r >= linha or matriz_1[linhas_para_num + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  for r in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num + r][colunas] = 'C'
                else:
                    print("Orientação inválida, escolha 'H' para horizontal ou 'V' para vertical.")
                    continue

                break  # Sai do loop enquanto tudo estiver correto

            except ValueError:
                print('Informe uma coordenada válida...')

        elif embarcacao == embarcacoes[3]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper().strip()
                #chama a função converte_coordenadas_letras(linhas) para converter a coordenada "letra" informada pela usuário em um número
                linhas_para_num = int(converte_coordenadas_letras(linhas))

                #checar se as coordenadas informadas estão dentros dos limites do tabuleiro
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue

                if orientacao == 'H':
               
                  #checar se a embarcação, ao ser posicionada, não ultrapassa os limites do tabuleiro. Soma-se 5 a colunas, pois nesse caso o Porta-aviões ocupa 5 casas. Para as embarcações seguintes, soma-se 4,3,2...
                  if colunas + tamanho_embarcacao > coluna:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue
                  
                  if any(colunas + c >= coluna or matriz_1[linhas_para_num][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  # Coloca o navio na matriz
                  for c in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num][colunas + c] = 'S'
                
                elif orientacao == 'V':
                  if linhas_para_num + tamanho_embarcacao > linha:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue

                  if any(linhas_para_num + r >= linha or matriz_1[linhas_para_num + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  for r in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num + r][colunas] = 'S'
                else:
                    print("Orientação inválida, escolha 'H' para horizontal ou 'V' para vertical.")
                    continue

                break  # Sai do loop enquanto tudo estiver correto

            except ValueError:
                print('Informe uma coordenada válida...')

        if embarcacao == embarcacoes[4]:
          while True:
            try:
                linhas = input("Qual linha? ").upper().strip()
                colunas = int(input("Qual coluna? "))
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper().strip()
                #chama a função converte_coordenadas_letras(linhas) para converter a coordenada "letra" informada pela usuário em um número
                linhas_para_num = int(converte_coordenadas_letras(linhas))

                #checar se as coordenadas informadas estão dentros dos limites do tabuleiro
                if linhas_para_num >= linha or colunas >= coluna:
                    print("Coordenada inválida, fora dos limites...")
                    continue

                if orientacao == 'H':
               
                  #checar se a embarcação, ao ser posicionada, não ultrapassa os limites do tabuleiro. Soma-se 5 a colunas, pois nesse caso o Porta-aviões ocupa 5 casas. Para as embarcações seguintes, soma-se 4,3,2...
                  if colunas + tamanho_embarcacao > coluna:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue
                  
                  if any(colunas + c >= coluna or matriz_1[linhas_para_num][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  # Coloca o navio na matriz
                  for c in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num][colunas + c] = 'D'
                
                elif orientacao == 'V':
                  if linhas_para_num + tamanho_embarcacao > linha:
                      print("Coordenada inválida, o navio ultrapassa os limites da matriz...")
                      continue

                  if any(linhas_para_num + r >= linha or matriz_1[linhas_para_num + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    print("Coordenada já possui navio em uma das posições ou ultrapassa os limites...")
                    continue

                  for r in range(tamanho_embarcacao):
                      matriz_1[linhas_para_num + r][colunas] = 'D'
                else:
                    print("Orientação inválida, escolha 'H' para horizontal ou 'V' para vertical.")
                    continue

                break  # Sai do loop enquanto tudo estiver correto

            except ValueError:
                print('Informe uma coordenada válida...')

      print('Aguarde um momento...')
      sleep(1)
      for line in matriz_1:
        print(line)
      return matriz_1
    
      
    #Cria a matriz 2(computador)
    elif build_turn == 2:
      matriz_2 = []

      for i in range(linha):
        matriz_2.append([])
        for j in range(coluna):
          matriz_2[i].append('-')

      letras = ['H', 'V']
      for embarcacao in embarcacoes:
        if embarcacao == embarcacoes[0]:  # Porta-aviões
          tamanho_embarcacao = 5
        elif embarcacao == embarcacoes[1]:  # Navio-tanque
          tamanho_embarcacao = 4
        elif embarcacao == embarcacoes[2]:  # Contratorpedeiro
          tamanho_embarcacao = 3
        elif embarcacao == embarcacoes[3]:  # Submarino
          tamanho_embarcacao = 2
        else: # Destroier
          tamanho_embarcacao = 1
        if embarcacao == embarcacoes[0]:
          while True:
            # Gera coordenadas aleatórias
            linhas = randint(0, linha - 1)
            colunas = randint(0, coluna - 1)
            orientacao = choice(letras) #Escolhe randomicamente entre H e V

            if orientacao == 'H':
              if colunas + tamanho_embarcacao > coluna:
                  continue  # Ultrapassa os limites, tente novamente
              
              # Verifica se as posições estão livres
              if any(matriz_2[linhas][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                  continue  # Posição ocupada, tente novamente

              # Posiciona o barco
              for c in range(tamanho_embarcacao):
                  matriz_2[linhas][colunas + c] = 'P'
              break

            elif orientacao == 'V':
                if linhas + tamanho_embarcacao > linha:
                    continue  # Ultrapassa os limites, tente novamente
                
                # Verifica se as posições estão livres
                if any(matriz_2[linhas + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    continue  # Posição ocupada, tente novamente

                # Posiciona o barco
                for r in range(tamanho_embarcacao):
                    matriz_2[linhas + r][colunas] = 'P'
                break

        elif embarcacao == embarcacoes[1]:
          while True:
            # Gera coordenadas aleatórias
            linhas = randint(0, linha - 1)
            colunas = randint(0, coluna - 1)
            orientacao = choice(letras) #Escolhe randomicamente entre H e V

            if orientacao == 'H':
              if colunas + tamanho_embarcacao > coluna:
                  continue  # Ultrapassa os limites, tente novamente
              
              # Verifica se as posições estão livres
              if any(matriz_2[linhas][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                  continue  # Posição ocupada, tente novamente

              # Posiciona o barco
              for c in range(tamanho_embarcacao):
                  matriz_2[linhas][colunas + c] = 'N'
              break

            elif orientacao == 'V':
                if linhas + tamanho_embarcacao > linha:
                    continue  # Ultrapassa os limites, tente novamente
                
                # Verifica se as posições estão livres
                if any(matriz_2[linhas + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    continue  # Posição ocupada, tente novamente

                # Posiciona o barco
                for r in range(tamanho_embarcacao):
                    matriz_2[linhas + r][colunas] = 'N'
                break
            
        elif embarcacao == embarcacoes[2]:
          while True:
            # Gera coordenadas aleatórias
            linhas = randint(0, linha - 1)
            colunas = randint(0, coluna - 1)
            orientacao = choice(letras) #Escolhe randomicamente entre H e V

            if orientacao == 'H':
              if colunas + tamanho_embarcacao > coluna:
                  continue  # Ultrapassa os limites, tente novamente
              
              # Verifica se as posições estão livres
              if any(matriz_2[linhas][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                  continue  # Posição ocupada, tente novamente

              # Posiciona o barco
              for c in range(tamanho_embarcacao):
                  matriz_2[linhas][colunas + c] = 'C'
              break

            elif orientacao == 'V':
                if linhas + tamanho_embarcacao > linha:
                    continue  # Ultrapassa os limites, tente novamente
                
                # Verifica se as posições estão livres
                if any(matriz_2[linhas + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    continue  # Posição ocupada, tente novamente

                # Posiciona o barco
                for r in range(tamanho_embarcacao):
                    matriz_2[linhas + r][colunas] = 'C'
                break

        elif embarcacao == embarcacoes[3]:
          while True:
            # Gera coordenadas aleatórias
            linhas = randint(0, linha - 1)
            colunas = randint(0, coluna - 1)
            orientacao = choice(letras) #Escolhe randomicamente entre H e V

            if orientacao == 'H':
              if colunas + tamanho_embarcacao > coluna:
                  continue  # Ultrapassa os limites, tente novamente
              
              # Verifica se as posições estão livres
              if any(matriz_2[linhas][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                  continue  # Posição ocupada, tente novamente

              # Posiciona o barco
              for c in range(tamanho_embarcacao):
                  matriz_2[linhas][colunas + c] = 'S'
              break

            elif orientacao == 'V':
                if linhas + tamanho_embarcacao > linha:
                    continue  # Ultrapassa os limites, tente novamente
                
                # Verifica se as posições estão livres
                if any(matriz_2[linhas + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    continue  # Posição ocupada, tente novamente

                # Posiciona o barco
                for r in range(tamanho_embarcacao):
                    matriz_2[linhas + r][colunas] = 'S'
                break

        elif embarcacao == embarcacoes[4]:
          while True:
            # Gera coordenadas aleatórias
            linhas = randint(0, linha - 1)
            colunas = randint(0, coluna - 1)
            orientacao = choice(letras) #Escolhe randomicamente entre H e V

            if orientacao == 'H':
              if colunas + tamanho_embarcacao > coluna:
                  continue  # Ultrapassa os limites, tente novamente
              
              # Verifica se as posições estão livres
              if any(matriz_2[linhas][colunas + c] != '-' for c in range(tamanho_embarcacao)):
                  continue  # Posição ocupada, tente novamente

              # Posiciona o barco
              for c in range(tamanho_embarcacao):
                  matriz_2[linhas][colunas + c] = 'D'
              break

            elif orientacao == 'V':
                if linhas + tamanho_embarcacao > linha:
                    continue  # Ultrapassa os limites, tente novamente
                
                # Verifica se as posições estão livres
                if any(matriz_2[linhas + r][colunas] != '-' for r in range(tamanho_embarcacao)):
                    continue  # Posição ocupada, tente novamente

                # Posiciona o barco
                for r in range(tamanho_embarcacao):
                    matriz_2[linhas + r][colunas] = 'D'
                break

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
    count = 0 #contador
    print(' ', end = ' ')
    for num in num_coordenadas:
       print(f'  \033[34m{num}\033[m  ', end='') #imprime os numeros das coordenadas de colunas no tabuleiro
    print()
    for line in matriz:
      print(f'\033[34m{letras_coordenadas[count]}\033[m', end=' ') #imprime os numeros das coordenadas de colunas no tabuleiro
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
    if turn == 'player_1': #turno do jogador, para informar coordenadas para atacar o adversário
      while True:
        try: 
          linhas = input("Informe a linha do adversário: ").strip().upper()
          colunas = int(input("Informe a coluna do adversário: "))

          linhas = int(converte_coordenadas_letras(linhas)) #converte a coordenada letra informada em "linhas", para um número inteiro

          while linhas >= linha or colunas >= coluna: #verifica se as coordenadas informadas estão dentro dos limites
            print("Coordenada fora dos limites")
            linhas = int(input("Informe a linha do adversário: "))
            colunas = int(input("Informe a coluna do adversário: "))
          break
        except ValueError:
          print('Informe uma coordenada válida...')

    elif turn == 'player_2': #turno do computador
      linhas = randint(0,linha-1)
      colunas = randint(0,coluna-1)

      linhas_letra = converte_coordenadas_num(linhas) #converte a coordenada letra informada em "linhas", para um número inteiro

      print(f"Computador escolheu a linha {linhas_letra}")
      print(f"Computador escolheu a coluna {colunas}")

    if matriz[linhas][colunas] in 'PNCSD': #verifica se as coordenadas correspondem a uma das letras representativas das embarcações. Caso sim, a embarcação foi atingida
      print("Você \033[32mACERTOU\033[m a embarcação!")
      print('\n')
      coordenada = matriz[linhas][colunas]
      matriz[linhas][colunas] = 'X' #indica que a embarcação foi atingida em tal posição
      matriz_desenhada[linhas][colunas] = 'X'
      pontuation(turn, coordenada)
      return coordenada
    elif matriz[linhas][colunas] == 'X': # posição já foi atingida
      print("Embarcação JÁ destruída!")
      print('\n')
    else:
      print("Você \033[31mERROU!\033[m")
      print('\n')
      matriz_desenhada[linhas][colunas] = '/' #coordenada possuia apenas água
      
  # Vez do jogador
  def player_turn():
    starts = 'player_1' # define turno inicial para o JOGADOR
    if starts == 'player_1':
      print('\033[33mJOGADOR: \033[m')
      atirar(matriz_2, matriz_desenhada2, starts) #Chama função atirar na matriz do computador
      if total_barcos_computador == 0: #encerra
            return
      starts = 'player_2' # define turno para o COMPUTADOR
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
    #diminui em 1 a variavel para o tamanho de determinada embarcação. Se chegar a 0, a embarcação é destruída e diminui em 1 o total de embarcações
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
      
  #atribui a variaveis a criação de desenhar tabuleiro na tela
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
  #loop principal do jogo
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

          linhas_para_num = int(converte_coordenadas_letras(linhas)) #converte valor alfabética da coordenada da linha em numérico

          matriz_1[linhas_para_num][colunas] = 'B' # atribui posição da embarcação a coordenada da matriz
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

    for i in range(linha): # cria a matriz 2 vazia
      matriz_2.append([])
      for j in range(coluna):
        matriz_2[i].append('-')

    for c in range(5): # randomiza a colocação dos barcos em cada uma das 5 linhas
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
    count = 0 #contador
    print(' ', end = ' ')

    for num in num_coordenadas:
       print(f'  \033[34m{num}\033[m  ', end='') #imprime os numeros das colunas no tabuleiro
    print()
    for line in matriz:
      print(f'\033[34m{letras_coordenadas[count]}\033[m', end=' ') #imprime as letras das linhas no tabuleiro
      print(end= '  ')
      for elemento in line: # passa por cada elemento da linha, e verifica para colorir
        if elemento == 'X':
            print(f'\033[31m{elemento}\033[m', end='    ')
        elif elemento == 'N':
           print(f'\033[33m{elemento}\033[m', end='    ')
        else:
          print(f'\033[36m{elemento}\033[m', end='    ')
      print()
      count+=1 #atualiza contador

  #função para atirar no inimigo
  def atirar(matriz, matriz_desenhada, turn):
    global linha, coluna
    sleep(1)
    if turn == 'player_1':
      while True:
        try:
          linhas = input("Informe a linha do adversário: ").upper().strip()
          colunas = int(input("Informe a coluna do adversário: "))

          linhas = int(converte_coordenadas_letras(linhas))  #converte valor alfabética da coordenada da linha em numérico

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
      linhas_letra = converte_coordenadas_num(linhas)  #converte valor numérico da coordenada da linha em alfabetico
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
    starts = 'player_1' #turno inicia com JOGADOR
    if starts == 'player_1':
      print('\033[34mJOGADOR\033[m: ')
      atirar(matriz_2, matriz_desenhada2, starts)
      starts = 'player_2' #Muda turno para COMPUTADOR
    if starts == 'player_2':
      print('\033[33mCOMPUTADOR\033[m: ')
      atirar(matriz_1, matriz_desenhada1, starts)

  #calcula a pontuação do total de barcos destruídos
  def pontuation(turn):
    global linha, coluna
    global barcos_totais_computador
    global barcos_totais_jogador
    if turn == 'player_1': #Se foi o jogador que acertou, diminui em 1 o total de barcos do computador
      barcos_totais_computador -= 1
    elif turn == 'player_2': #Se foi o computador que acertou, diminui em 1 o total de barcos do jogador
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
  #loop principal do jogo easy, confere se a quantidade de barcos não está zerada para continuar dentro do loop
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

dificuldade() # chama a função para definir dificuldade
#créditos dos desenvolvedores
print('-'*50)
print("Jogo desenvolvido por:\n- Riscala Miguel Fadel Neto\n- Pedro Senes\n- Victor Valerio Fadel\n")
print("Esse jogo teve auxílio técnico-criativo de Hideo Kojima, Sam Lake, Hidetaka Miyazaki e Shigeru Miyamoto.")
print('-'*50)

