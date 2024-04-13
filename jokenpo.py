import random
from getpass import getpass

player1 = 0
player2 = 0
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
    player1Choice = getpass("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha:Está escondida!").upper()
    player2Choice = input("\n ==JOGADOR 2==\n[A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha:Tome cuidado a sua escolha estará exposta! ").upper()

    if player1Choice == player2Choice:
      print("\nEMPATE!")
      player1Points+=1
      player2Points+=1
    elif player1Choice == 'A' and player2Choice == 'B':
      print("\nJogador 1 perdeu")
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print("\nJogador 1 venceu")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print("\nJogador 1 venceu")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print("\nJogador 1 perdeu")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print("\nJogador 1 perdeu")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print("\nJogador 1 venceu")
      player1Points +=1
    
    restart = input("\nDeseja jogar novamente?[S/N] ").upper()

    if restart == "N":
      break


if modalidade == 2:
  while True:
    player1Choice = getpass("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha:Está escondida!").upper()
    print("O computador já fez a escolha! ")
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      player2Choice = "A"
    elif numeroAleatorio == 2:
      player2Choice = "B"
    elif numeroAleatorio == 3:
      player2Choice = "C"
    if player1Choice == player2Choice:
      print(f"\nO computador jogou {player2Choice}")
      print("\nEMPATE!")
      player1Points+=1
      player2Points+=1
    elif player1Choice == 'A' and player2Choice == 'B':
      print(f"\nO computador jogou {player2Choice}")
      print("\nJogador 1 perdeu")
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print(f"\nO computador jogou {player2Choice}")
      print("\nJogador 1 venceu")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print(f"\nO computador jogou {player2Choice}")
      print("\nJogador 1 venceu")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print(f"\nO computador jogou {player2Choice}")
      print("\nJogador 1 perdeu")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print(f"\nO computador jogou {player2Choice}")
      print("\nJogador 1 perdeu")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print(f"\nO computador jogou {player2Choice}")
      print("\nJogador 1 venceu")
      player1Points +=1
    
    restart = input("\nDeseja jogar novamente?[S/N] ").upper()
    
    if restart == "N":
          break
    
if modalidade == 3:
  while True:
    print("O computador 1 já fez a sua escolha!")
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      player1Choice = "A"
    elif numeroAleatorio == 2:
      player1Choice = "B"
    else:
      player1Choice = "C"
    
    print("O computador 2 já fez a sua escolha!")
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      player2Choice = "A"
    elif numeroAleatorio == 2:
      player2Choice = "B"
    else:
      player2Choice = "C"

    if player1Choice == player2Choice:
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print(f"\nOcorreu um empate entre máquinas")
    elif player1Choice == 'A' and player2Choice == 'B':
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print(f"\nO computador 1 perdeu e computador 2 ganhou")
      player2Points +=1
    elif player1Choice == 'A' and player2Choice == 'C':
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print(F"\nO computador 1 ganhou e computador 2 perdeu")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice == 'A':
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print(f"\nO computador 1 ganhou e o computador 2 perdeu")
      player1Points +=1
    elif player1Choice == 'B' and player2Choice =='C':
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print(f"\nO computador 1 perdeu e computador 2 ganhou")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'A':
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print("\nO computador 1 perdeu e computador 2 ganhou")
      player2Points +=1
    elif player1Choice == 'C' and player2Choice == 'B':
      print(f"\nO computador 1 jogou {player1Choice}")
      print(f"\nO computador 2 jogou {player2Choice}")
      print(f"\nO computador 1 ganhou e computador 2 perdeu")
      player1Points +=1
    
      restart = input("\nDeseja jogar novamente?[S/N] ").upper()

      if restart == "N":
          break


print("\n=-=-= RESULTADOS =-=-=")
print(f"Jogador 1 : [{player1Points}]")
print(f"Jogador 2 : [{player2Points}]")
print(f"Este jogo foi um desenvolvimento de Hideo Kojima e Sam Lake")

      
      


  
  


