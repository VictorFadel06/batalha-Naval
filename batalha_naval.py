from random import randint


def matriz_jogador_1():
  matriz_1 = []

  for i in range(10):
    matriz_1.append([])
    for j in range(10):
      matriz_1[i].append('-')

  for c in range(5):
    linha = int(input("Qual linha? "))
    coluna = int(input("Qual coluna? "))
    matriz_1[linha][coluna] = 'B'

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

def print_matriz(matriz):
  for linha in matriz:
    print(linha)

def atirar(matriz):
  linha = int(input("Informe a linha do adversário: "))
  coluna = int(input("Informe a coluna do adversário: "))
  if matriz[linha][coluna] == 'B':
    print("Você acertou a embarcação!")
  else:
    print("Você ERROU!")


matriz_1 = matriz_jogador_1()
matriz_2 = matriz_jogador_2()

print_matriz(matriz_1)
print('\n')
print_matriz(matriz_2)
print('\n')
atirar(matriz_2)