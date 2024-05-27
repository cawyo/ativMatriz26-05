def maiorLinha(m,nlinha):
    maior = -1
    while nlinha > len(m)-1:
        nlinha = int(input('Escolha uma linha válida: '))
    for n in m[nlinha]:
        if n > maior:
            maior = n
    return maior


nlinha = int(input('Escolha uma linha: '))

matriz = [
    [1,2],
    [3,4]
]

maior = maiorLinha(matriz,nlinha)

print(maior)