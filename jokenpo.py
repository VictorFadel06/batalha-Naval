import random

jogador1 = 0
jogador2 = 0
pontosHumano1 = 0
pontosHumano2 = 0
escolhaPC = ''
pontosPC = 0
pontosPC2 = 0
continuar=''
opcoesPC = ''
escolhaHumano1=''
escolhaHumano2=''
from getpass import getpass 
print(f"\n\033[33m{'=-'*3}JOGO DO JOKENPÔ ULTIMATE EDITION{'-='*3}\033[m")

while True:
  modalidade = int(input("\nEscolha a sua modalidade:\n\n [1] Humano x Humano\n [2] Humano x Computador\n [3] Computador x Computador\n\nSua escolha: "))
  if modalidade == 1 or modalidade ==2 or modalidade == 3:
    break


if modalidade == 1:
  while True:
    while (escolhaHumano1 != "A" and escolhaHumano1 != "B" and escolhaHumano1 != "C"):
      escolhaHumano1 = getpass("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha:Está escondida!").upper()
    while (escolhaHumano2 != "A" and escolhaHumano2 != "B" and escolhaHumano2 != "C"):
      escolhaHumano2 = input("\n ==JOGADOR 2==\n[A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha:Tome cuidado a sua escolha estará exposta! ").upper()

    if escolhaHumano1 == escolhaHumano2:
      print("\nEMPATE!")
      pontosHumano1+=1
      pontosHumano2+=1
    elif escolhaHumano1 == 'A' and escolhaHumano2 == 'B':
      print("\nJogador 1 perdeu")
      pontosHumano2 +=1
    elif escolhaHumano1 == 'A' and escolhaHumano2 == 'C':
      print("\nJogador 1 venceu")
      pontosHumano1 +=1
    elif escolhaHumano1 == 'B' and escolhaHumano2 == 'A':
      print("\nJogador 1 venceu")
      pontosHumano1 +=1
    elif escolhaHumano1 == 'B' and escolhaHumano2 =='C':
      print("\nJogador 1 perdeu")
      pontosHumano2 +=1
    elif escolhaHumano1 == 'C' and escolhaHumano2 == 'A':
      print("\nJogador 1 perdeu")
      pontosHumano2 +=1
    elif escolhaHumano1 == 'C' and escolhaHumano2 == 'B':
      print("\nJogador 1 venceu")
      pontosHumano1 +=1
    continuar = input("\nDeseja jogar novamente?[S/N] ").upper()
    if continuar == "N":
        break


if modalidade == 2:
  while True:
    escolhaHumano1 = input("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha: ").upper()
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      escolhaPC = "A"
    elif numeroAleatorio == 2:
      escolhaPC = "B"
    elif numeroAleatorio == 3:
      escolhaPC = "C"
    if escolhaHumano1 == escolhaPC:
      print(f"\nO computador jogou {escolhaPC}")
      print("\nEMPATE!")
      pontosHumano1+=1
      pontosPC+=1
    elif escolhaHumano1 == 'A' and escolhaPC == 'B':
      print(f"\nO computador jogou {escolhaPC}")
      print("\nJogador 1 perdeu")
      pontosPC +=1
    elif escolhaHumano1 == 'A' and escolhaPC == 'C':
      print(f"\nO computador jogou {escolhaPC}")
      print("\nJogador 1 venceu")
      pontosHumano1 +=1
    elif escolhaHumano1 == 'B' and escolhaPC == 'A':
      print(f"\nO computador jogou {escolhaPC}")
      print("\nJogador 1 venceu")
      pontosHumano1 +=1
    elif escolhaHumano1 == 'B' and escolhaPC =='C':
      print(f"\nO computador jogou {escolhaPC}")
      print("\nJogador 1 perdeu")
      pontosPC +=1
    elif escolhaHumano1 == 'C' and escolhaPC == 'A':
      print(f"\nO computador jogou {escolhaPC}")
      print("\nJogador 1 perdeu")
      pontosPC +=1
    elif escolhaHumano1 == 'C' and escolhaPC == 'B':
      print(f"\nO computador jogou {escolhaPC}")
      print("\nJogador 1 venceu")
      pontosHumano1 +=1
    continuar = input("\nDeseja jogar novamente?[S/N] ").upper()
    if continuar == "N":
      break
if modalidade == 3:
  while True:
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      escolhaPC = "A"
    elif numeroAleatorio == 2:
      escolhaPC = "B"
    else:
      escolhaPC = "C"
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
      escolhaPC2 = "A"
    elif numeroAleatorio == 2:
      escolhaPC2 = "B"
    else:
      escolhaPC2 = "C"
    if escolhaPC == escolhaPC2:
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print(f"\nOcorreu um empate entre máquinas")
    elif escolhaPC == 'A' and escolhaPC2 == 'B':
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print(f"\nO computador 1 perdeu e computador 2 ganhou")
      pontosPC2 +=1
    elif escolhaPC == 'A' and escolhaPC2 == 'C':
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print(F"\nO computador 1 ganhou e computador 2 perdeu")
      pontosPC +=1
    elif escolhaPC == 'B' and escolhaPC2 == 'A':
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print(f"\nO computador 1 ganhou e o computador 2 perdeu")
      pontosPC +=1
    elif escolhaPC == 'B' and escolhaPC2 =='C':
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print(f"\nO computador 1 perdeu e computador 2 ganhou")
      pontosPC2 +=1
    elif escolhaPC == 'C' and escolhaPC2 == 'A':
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print("\nO computador 1 perdeu e computador 2 ganhou")
      pontosPC2 +=1
    elif escolhaPC == 'C' and escolhaPC2 == 'B':
      print(f"\nO computador 1 jogou {escolhaPC}")
      print(f"\nO computador 2 jogou {escolhaPC2}")
      print(f"\nO computador 1 ganhou e computador 2 perdeu")
      pontosPC +=1
    continuar = input("\nDeseja jogar novamente?[S/N] ").upper()
    if continuar == "N":
      break


print("\n=-=-= RESULTADOS =-=-=")
print(f"Jogador 1 : [{pontosHumano1}]")
print(f"Jogador 2 : [{pontosPC}]")
print(f"Este jogo foi um desenvolvimento de Hideo Kojima e Sam Lake")

      
      


  
  


