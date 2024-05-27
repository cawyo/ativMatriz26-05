def somarColuna(m,ncoluna):
    soma = 0
    while ncoluna > len(m[0])-1:
        ncoluna = int(input('Escolha uma coluna válida: '))
    for l in m:
        soma = soma+l[ncoluna]
    return soma


ncoluna = int(input('Escolha uma coluna: '))

matriz = [
    [2,4,5],
    [4,6,5],
    [6,8,5]
]

soma = somarColuna(matriz,ncoluna)

print(soma)