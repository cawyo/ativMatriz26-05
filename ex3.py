def somarMatriz(matriz):
    soma = 0
    for linha in matriz:
        somaL=0
        for num in linha:
            if num%2==0:
                somaL=somaL+num
        soma = soma+somaL
    return soma

matriz = [
    [2,4,5],
    [4,6,5],
    [6,8,5]
]

soma = somarMatriz(matriz)


print(soma)

