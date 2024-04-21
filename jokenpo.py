#Biblioteca random será usada para randomizar a escolha da jogada do "computador"
import random
#Biblioteca getpass será usada para esconder o input do jogador no momento da jogada
from getpass import getpass
#Biblioteca time será usada para criar uma "pausa" entre os inputs e respostas, através de uma contagem regressiva. Também será usada para criar um efeito mais dinâmico ao jogo, para torná-lo mais atrativo aos olhos do jogador, no momento do JO-KEN-PÔ.
from time import sleep

#Contador de pontos dos jogadores 1 e 2. Será usado tanto pelos jogadores humanos quantos pelos computadores.
player1Points = 0
player2Points = 0
#Variáveis usadas para armazenar as escolhas dos jogadores: PEDRA, PAPEL ou TESOURA.
player1Choice=''
player2Choice=''
#Variável usada ao final de uma partida, para definir se o jogador quer ou não reiniciar a partida.
restart = ''

#Título do jogo
print(f"\n\033[33m{'=-'*3}JOGO DO JOKENPÔ ULTIMATE EDITION{'-='*3}\033[m")

#Serve como 'divisória' entre os textos exibidos. Torna mais organizado e legível o jogo.
print('-'*30)
#variável para armazenar a escolha do tipo de modalidade do jogo. Só pode ser escolhida uma vez.
modalidade = input("\nEscolha a sua modalidade:\n\n [1] Humano x Humano\n [2] Humano x Computador\n [3] Computador x Computador\n\nSua escolha: ").strip().upper()
print('-'*30)

#serve como pausa de 1 segundo até o próximo input
sleep(1)

#Loop que só será encerrado quando o jogador digitar '1', '2' ou '3' como input ao escolher a modalidade.
while modalidade != '1' and modalidade !='2' and modalidade !='3':
  sleep(1)
  modalidade = input("\nPor favor, escolha uma opção VÁLIDA!\n [1] Humano x Humano\n [2] Humano x Computador\n [3] Computador x Computador\n\nSua escolha: ").strip().upper()
  print('-'*30)

#Condição para caso o jogador escolha a modalidade '1'
if modalidade == '1':
  #Loop que só será encerrado quando o jogador digitar 'N' como input ao escolher encerrar a partida.
  while True:
    player1Choice = getpass(" ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
    print('-'*30)
    #Loop que só será encerrado quando o jogador 1 digitar 'A', 'B' ou 'C' como input ao escolher PEDRA, PAPEL ou TESOURA, respectivamente.
    while player1Choice != 'A' and player1Choice !='B' and player1Choice !='C':
      #input da jogada do jogador 1
      player1Choice = getpass("Por favor, escolha uma opção VÁLIDA!\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
      print('-'*30)
    
    sleep(1)

    #Loop que só será encerrado quando o jogador 2 digitar 'A', 'B' ou 'C' como input ao escolher PEDRA, PAPEL ou TESOURA, respectivamente.
    player2Choice = getpass(" ==JOGADOR 2==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
    print('-'*30)
    while player2Choice != 'A' and player2Choice !='B' and player2Choice !='C':
      #input da jogada do jogador 2
      player2Choice = getpass("Por favor, escolha uma opção VÁLIDA!\n ==JOGADOR 2==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
      print('-'*30)

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')

    sleep(1)

    #condição para caso ambos os jogadores tenham escolhido a mesma opção. Não haverá vencedor.
    if player1Choice == player2Choice:
      print("\033[34mEMPATE!\033[m")
      print('-'*30)
    #condição para caso o jogador1 tenha escolhida PEDRA e o jogador 2 tenha escolhido PAPEL
    elif player1Choice == 'A' and player2Choice == 'B':
      print('-'*30)
      print(f"\nO Jogador 1 jogou PEDRA")
      print(f"\nO Jogador 2 jogou PAPEL")
      print('-'*30)
      print("PAPEL ganha de PEDRA!")
      print(f"\nO \033[33mJogador 1\033[m \033[31m\033[31mPERDEU\033[m\033[m e \033[33mJogador 2\033[m \033[32mVENCEU\033[m")
      print('-'*30)
      #soma 1 ponto ao vencedor (jogador2)
      player2Points +=1
    #condição para caso o jogador1 tenha escolhida PEDRA e o jogador 2 tenha escolhido TESOURA
    elif player1Choice == 'A' and player2Choice == 'C':
      print('-'*30)
      print(f"O Jogador 1 jogou PEDRA")
      print(f"\nO Jogador 2 jogou TESOURA")
      print('-'*30)
      print("PEDRA ganha de TESOURA!")
      print(F"\nO \033[33mJogador 1\033[m \033[32mVENCEU\033[m e \033[33mJogador 2\033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    #condição para caso o jogador1 tenha escolhida PAPEL e o jogador 2 tenha escolhido PEDRA
    elif player1Choice == 'B' and player2Choice == 'A':
      print('-'*30)
      print(f"O Jogador 1 jogou PAPEL")
      print(f"\nO Jogador 2 jogou PEDRA")
      print('-'*30)
      print("PAPEL ganha de PEDRA!")
      print(f"\nO \033[33mJogador 1\033[m \033[32mVENCEU\033[m e o \033[33mJogador 2\033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    #condição para caso o jogador1 tenha escolhida PAPEL e o jogador 2 tenha escolhido TESOURA
    elif player1Choice == 'B' and player2Choice =='C':
      print('-'*30)
      print(f"O Jogador 1 jogou PAPEL")
      print(f"\nO Jogador 2 jogou TESOURA")
      print('-'*30)
      print("TESOURA ganha de PAPEL!")
      print(f"\nO \033[33mJogador 1\033[m \033[31mPERDEU\033[m e \033[33mJogador 2\033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    #condição para caso o jogador1 tenha escolhida TESOURA e o jogador 2 tenha escolhido PEDRA
    elif player1Choice == 'C' and player2Choice == 'A':
      print('-'*30)
      print(f"O Jogador 1 jogou TESOURA")
      print(f"\nO Jogador 2 jogou PEDRA")
      print('-'*30)
      print("PEDRA ganha de TESOURA!")
      print("\nO \033[33mJogador 1\033[m \033[31mPERDEU\033[m e \033[33mJogador 2\033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    #condição para caso o jogador1 tenha escolhida TESOURA e o jogador 2 tenha escolhido PAPEL
    elif player1Choice == 'C' and player2Choice == 'B':
      print('-'*30)
      print(f"O Jogador 1 jogou TESOURA")
      print(f"\nO Jogador 2 jogou PAPEL")
      print('-'*30)
      print("TESOURA ganha de PAPEL!")
      print(f"\nO \033[33mJogador 1\033[m \033[32mVENCEU\033[m e \033[33mJogador 2\033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    
    sleep(1)

    #Opção para reiniciar a partida. 'S' ou 's' para reiniciar. 'N' ou 'n' para encerrar e ver resultados finais.
    restart = input("Deseja jogar novamente?[S/N] ").strip().upper()
    #Loop que será encerrado apenas quando o jogador inserir um input correto. No caso, 's', 'S', 'n' ou 'N'.
    while restart != 'N' and restart != 'S':
      restart = input("Por favor, digite uma resposta VÁLIDA! Deseja jogar novamente?[S/N] ").strip().upper()
    #Encerra o loop da partida.
    if restart == 'N':
      break



if modalidade == '2':
  #Loop que só será encerrado quando o jogador digitar 'N' como input ao escolher encerrar a partida.
  while True:
    player1Choice = getpass(" ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
    print('-'*30)
    #Loop que só será encerrado quando o jogador 1 digitar 'A', 'B' ou 'C' como input ao escolher PEDRA, PAPEL ou TESOURA, respectivamente.
    while player1Choice != 'A' and player1Choice !='B' and player1Choice !='C':
      #input da jogada do jogador 1
      player1Choice = getpass("Por favor, escolha uma opção VÁLIDA!\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
      print('-'*30)
    
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

    print('-'*30)
    print("O jogador 2 (Computador) já fez a sua escolha! ")
    print('-'*30)

    #Biblioteca random sendo usada para randomizar a escolha do Computador. Se 1, então escolha tribuída ao computador é 'A'. Se 2, então escolha é 'B'. Se 3, então escolha é 'C'.
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      player2Choice = "A"
    elif numeroAleatorio == 2:
      player2Choice = "B"
    elif numeroAleatorio == 3:
      player2Choice = "C"

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')

    sleep(1)

    #condição para caso ambos os jogadores tenham escolhido a mesma opção. Não haverá vencedor.
    if player1Choice == player2Choice:
      print("\033[34mEMPATE!\033[m")
      print('-'*30)
    #condição para caso o jogador1 tenha escolhida PEDRA e o jogador 2 tenha escolhido PAPEL
    elif player1Choice == 'A' and player2Choice == 'B':
      print('-'*30)
      print(f"O Jogador 1 jogou PEDRA")
      print(f"\nO Jogador 2 (Computador) jogou PAPEL")
      print('-'*30)
      print("Papel ganha pedra!")
      print(f"\nO \033[33mJogador 1\033[m \033[31m\033[31mPERDEU\033[m\033[m e \033[33mJogador 2 (Computador) \033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    #condição para caso o jogador1 tenha escolhida PEDRA e o jogador 2 tenha escolhido TESOURA
    elif player1Choice == 'A' and player2Choice == 'C':
      print('-'*30)
      print(f"O Jogador 1 jogou PEDRA")
      print(f"\nO Jogador 2 (Computador) jogou TESOURA")
      print('-'*30)
      print("Pedra ganha de tesoura!")
      print(F"\nO \033[33mJogador 1\033[m \033[32mVENCEU\033[m e \033[33mJogador 2 (Computador) \033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    #condição para caso o jogador1 tenha escolhida PAPEL e o jogador 2 tenha escolhido PEDRA
    elif player1Choice == 'B' and player2Choice == 'A':
      print('-'*30)
      print(f"O Jogador 1 jogou PAPEL")
      print(f"\nO Jogador 2 (Computador) jogou PEDRA")
      print('-'*30)
      print("Papel ganha pedra!")
      print(f"\nO \033[33mJogador 1\033[m \033[32mVENCEU\033[m e o \033[33mJogador 2 (Computador) \033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    #condição para caso o jogador1 tenha escolhida PAPEL e o jogador 2 tenha escolhido TESOURA
    elif player1Choice == 'B' and player2Choice =='C':
      print('-'*30)
      print(f"O Jogador 1 jogou PAPEL")
      print(f"\nO Jogador 2 (Computador) jogou TESOURA")
      print('-'*30)
      print("Tesoura ganha de papel!")
      print(f"\nO \033[33mJogador 1\033[m \033[31mPERDEU\033[m e \033[33mJogador 2 (Computador) \033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    #condição para caso o jogador1 tenha escolhida TESOURA e o jogador 2 tenha escolhido PEDRA
    elif player1Choice == 'C' and player2Choice == 'A':
      print('-'*30)
      print(f"O Jogador 1 jogou TESOURA")
      print(f"\nO Jogador 2 (Computador) jogou PEDRA")
      print('-'*30)
      print("Pedra ganha de tesoura!")
      print("\nO \033[33mJogador 1\033[m \033[31mPERDEU\033[m e \033[33mJogador 2 (Computador) \033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    #condição para caso o jogador1 tenha escolhida TESOURA e o jogador 2 tenha escolhido PAPEL
    elif player1Choice == 'C' and player2Choice == 'B':
      print('-'*30)
      print(f"O Jogador 1 jogou TESOURA")
      print(f"\nO Jogador 2 (Computador) jogou PAPEL")
      print('-'*30)
      print("Tesoura ganha de papel!")
      print(f"\nO \033[33mJogador 1\033[m \033[32mVENCEU\033[m e \033[33mJogador 2 (Computador) \033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    
    sleep(1)

    #Opção para reiniciar a partida. 'S' ou 's' para reiniciar. 'N' ou 'n' para encerrar e ver resultados finais.
    restart = input("Deseja jogar novamente?[S/N] ").strip().upper()
    #Loop que será encerrado apenas quando o jogador inserir um input correto. No caso, 's', 'S', 'n' ou 'N'.
    while restart != 'N' and restart != 'S':
      restart = input("Por favor, digite uma resposta VÁLIDA! Deseja jogar novamente?[S/N] ").strip().upper()
    #Encerra o loop da partida.
    if restart == 'N':
      break
    
if modalidade == '3':
  while True:
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('-'*30)
    print("O Computador 1 já fez a sua escolha!")
    print('-'*30)
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      player1Choice = "A"
    elif numeroAleatorio == 2:
      player1Choice = "B"
    else:
      player1Choice = "C"
    
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

    print('-'*30)
    print("O Computador 2 já fez a sua escolha!")
    print('-'*30)
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      player2Choice = "A"
    elif numeroAleatorio == 2:
      player2Choice = "B"
    else:
      player2Choice = "C"

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')

    sleep(1)

    if player1Choice == player2Choice:
      print(f"Ocorreu um \033[34mEMPATE\033[m entre máquinas")
      print('-'*30)
    elif player1Choice == 'A' and player2Choice == 'B':
      print('-'*30)
      print(f"O computador 1 jogou PEDRA")
      print(f"\nO computador 2 jogou PAPEL")
      print('-'*30)
      print("Papel ganha pedra!")
      print(f"\nO \033[33mComputador 1\033[m \033[31m\033[31mPERDEU\033[m\033[m e \033[33mComputador 2\033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print('-'*30)
      print(f"O computador 1 jogou PEDRA")
      print(f"\nO computador 2 jogou TESOURA")
      print('-'*30)
      print("Pedra ganha de tesoura!")
      print(F"\nO \033[33mComputador 1\033[m \033[32mVENCEU\033[m e \033[33mComputador 2\033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print('-'*30)
      print(f"O computador 1 jogou PAPEL")
      print(f"\nO computador 2 jogou PEDRA")
      print('-'*30)
      print("Papel ganha pedra!")
      print(f"\nO \033[33mComputador 1\033[m \033[32mVENCEU\033[m e o \033[33mComputador 2\033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print('-'*30)
      print(f"O computador 1 jogou PAPEL")
      print(f"\nO computador 2 jogou TESOURA")
      print('-'*30)
      print("Tesoura ganha de papel!")
      print(f"\nO \033[33mComputador 1\033[m \033[31mPERDEU\033[m e \033[33mComputador 2\033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print('-'*30)
      print(f"O computador 1 jogou TESOURA")
      print(f"\nO computador 2 jogou PEDRA")
      print('-'*30)
      print("Pedra ganha de tesoura!")
      print("\nO \033[33mComputador 1\033[m \033[31mPERDEU\033[m e \033[33mComputador 2\033[m \033[32mVENCEU\033[m")
      print('-'*30)
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print('-'*30)
      print(f"O computador 1 jogou TESOURA")
      print(f"\nO computador 2 jogou PAPEL")
      print('-'*30)
      print("Tesoura ganha de papel!")
      print(f"\nO \033[33mComputador 1\033[m \033[32mVENCEU\033[m e \033[33mComputador 2\033[m \033[31mPERDEU\033[m")
      print('-'*30)
      player1Points +=1
    
    sleep(1)

    restart = input("Deseja jogar novamente?[S/N] ").strip().upper()
    while restart != 'N' and restart != 'S':
      restart = input("Por favor, digite uma resposta VÁLIDA! Deseja jogar novamente?[S/N] ").strip().upper()
    if restart == 'N':
      break

sleep(1)

#Apresenta os resultados finais da partida, após o jogador escolher sair do jogo
print("\n=-=-= RESULTADOS =-=-=")
print(f"Jogador 1 : [{player1Points}]")
print(f"Jogador 2 : [{player2Points}]")
print("=-"*11)
print(f"\nEste jogo foi concebido pelas mentes brilhantes de Hideo Kojima e Sam Lake")

      
      


  
  


