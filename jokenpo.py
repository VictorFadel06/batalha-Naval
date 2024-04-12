import random

jogador1 = 0
jogador2 = 0
pontosHumano1 = 0
pontosHumano2 = 0
escolhaPC = ''
pontosPC = 0
continuar=''
opcoesPC = ''

print(f"\n\033[33m{'=-'*3}JOGO DO JOKENPÔ ULTIMATE EDITION{'-='*3}\033[m")

while True:
  modalidade = int(input("\nEscolha a sua modalidade:\n\n [1] Humano x Humano\n [2] Humano x Computador\n [3] Computador x Computador\n\nSua escolha: "))
  if modalidade == 1 or modalidade ==2 or modalidade == 3:
    break


if modalidade == 1:
  while True:
    escolhaHumano1 = input("\n ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha: ").upper()
    escolhaHumano2 = input("\n ==JOGADOR 2==\n[A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha: ").upper()
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

print("\n=-=-= RESULTADOS =-=-=")
print(f"Jogador 1 : [{pontosHumano1}]")
print(f"Jogador 2 : [{pontosPC}]")

      
      


  
  


