import random
from getpass import getpass
from time import sleep

player1Points = 0
player2Points = 0
player1Choice=''
player2Choice=''
restart = ''
 
print(f"\n\033[33m{'=-'*3}JOGO DO JOKENPÔ ULTIMATE EDITION{'-='*3}\033[m")

while True:
  modalidade = int(input("\nEscolha a sua modalidade:\n\n [1] Humano x Humano\n [2] Humano x Computador\n [3] Computador x Computador\n\nSua escolha: "))
  if modalidade == 1 or modalidade ==2 or modalidade == 3:
    break


if modalidade == 1:
  while True:
    player1Choice = getpass("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
    
    player2Choice = getpass("\n ==JOGADOR 2==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()

    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)

    print(f"\nO computador 1 jogou {player1Choice}")
    print(f"\nO computador 2 jogou {player2Choice}")

    if player1Choice == player2Choice:
      print("\nEMPATE!")
      player1Points+=1
      player2Points+=1
    elif player1Choice == 'A' and player2Choice == 'B':
      print("\nPapel ganha de pedra!")
      print("\nJogador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print("\nPedra ganha de tesoura!")
      print("\nJogador 1 VENCEU")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print("\nPapel ganha de pedra!")
      print("\nJogador 1 VENCEU")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print("\nTesoura ganha de papel!")
      print("\nJogador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print("\nPedra ganha de tesoura!")
      print("\nJogador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print("\nTesoura ganha de papel!")
      print("\nJogador 1 VENCEU")
      player1Points +=1
    
    sleep(1)

    restart = input("\nDeseja jogar novamente?[S/N] ").strip().upper()

    if restart == "N":
      break


if modalidade == 2:
  while True:
    player1Choice = getpass("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha(está escondida!): ").strip().upper()
    
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

    print("O jogador 2 já fez a sua escolha! ")

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

    print(f"\nO jogador 1 jogou {player1Choice}")
    print(f"\nO jogador 2 jogou {player2Choice}")

    if player1Choice == player2Choice:
      print("\nEMPATE!")
      player1Points+=1
      player2Points+=1
    elif player1Choice == 'A' and player2Choice == 'B':
      print("\nPapel ganha pedra!")
      print("\nJogador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print("\nPedra ganha de tesoura!")
      print("\nJogador 1 VENCEU")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print("\nPapel ganha pedra!")
      print("\nJogador 1 VENCEU")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print("\nTesoura ganha de papel!")
      print("\nJogador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print("\nPedra ganha de tesoura!")
      print("\nJogador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print("\nTesoura ganha de papel!")
      print("\nJogador 1 VENCEU")
      player1Points +=1
    
    sleep(1)

    restart = input("\nDeseja jogar novamente?[S/N] ").strip().upper()
    
    if restart == "N":
          break
    
if modalidade == 3:
  while True:
    sleep(1)
    print("O computador 1 já fez a sua escolha!")
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

    print("O computador 2 já fez a sua escolha!")
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

    print(f"\nO computador 1 jogou {player1Choice}")
    print(f"\nO computador 2 jogou {player2Choice}")

    if player1Choice == player2Choice:
      print(f"\nOcorreu um EMPATE entre máquinas")
    elif player1Choice == 'A' and player2Choice == 'B':
      print("\nPapel ganha pedra!")
      print(f"\nO computador 1 PERDEU e computador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print("\nPedra ganha de tesoura!")
      print(F"\nO computador 1 VENCEU e computador 2 PERDEU")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print("\nPapel ganha pedra!")
      print(f"\nO computador 1 VENCEU e o computador 2 PERDEU")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print("\nTesoura ganha de papel!")
      print(f"\nO computador 1 PERDEU e computador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print("\nPedra ganha de tesoura!")
      print("\nO computador 1 PERDEU e computador 2 VENCEU")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print("\nTesoura ganha de papel!")
      print(f"\nO computador 1 VENCEU e computador 2 PERDEU")
      player1Points +=1
    
    sleep(1)

    restart = input("\nDeseja jogar novamente?[S/N] ").strip().upper()

    if restart == "N":
      break


print("\n=-=-= RESULTADOS =-=-=")
print(f"Jogador 1 : [{player1Points}]")
print(f"Jogador 2 : [{player2Points}]")
print(f"\nEste jogo foi concebido pelas mentes brilhantes de Hideo Kojima e Sam Lake")

      
      


  
  


