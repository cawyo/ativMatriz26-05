import random

def criarMatriz():
    linhas = int(input('Digite o número de linhas: '))
    while linhas < 0 :
        linhas = int(input('Digite um valor de linhas positivo: '))
    colunas = int(input('Digite o número de colunas: '))
    while colunas < 0:
        colunas = int(input('Digite o número de colunas: '))
    
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randrange(1,20))
        matriz.append(linha)

    return matriz

matriz = criarMatriz()

print(matriz)

