import random

jogador1 = 0
jogador2 = 0
pontosHumano1 = 0
pontosHumano2 = 0
pontosPC = 0
continuar=''

print(f"\033[33m{'=-'*3}JOGO DO JOKENPÔ ULTIMATE EDITION{'-='*3}\033[m")

while True:
  modalidade = int(input("Escolha a sua modalidade:\n [1] Humano x Humano\n [2] Humano x Computador\n [3] Computador x Computador\nSua escolha: "))
  if modalidade == 1 or modalidade ==2 or modalidade == 3:
    break


if modalidade == 1:
  while True:
    escolhaHumano1 = input(" ==JOGADOR 1==\n [A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha: ")
    escolhaHumano2 = input(" ==JOGADOR 2==\n[A] PEDRA\n [B] PAPEL\n [C] TESOURA\nSua escolha: ")
    if escolhaHumano1 == escolhaHumano2:
      print("EMPATE!")
      pontosHumano1+=1
      pontosHumano2+=1
    continuar = input("Deseja jogar novamente?[S/N] ")
    if continuar == "N" or continuar =="n":
      break

      
      


  
  


