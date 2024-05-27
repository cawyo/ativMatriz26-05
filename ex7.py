def gerarPessoa():
    pessoa = []
    nome = input("Digite o nome: ")
    pessoa.append(nome)
    cpf = input("Digite o CPF: ")
    pessoa.append(cpf)
    idade = int(input('Digite a idade: '))
    pessoa.append(idade)
    renda = float(input("Digite a renda mensal: "))
    pessoa.append(renda)
    return pessoa
def calcRendaMedia(matriz):
    soma = 0
    for l in matriz:
        soma = soma+l[3]
        qtd =+ 1
    med = soma/qtd
    return med
def calcIdadeMedia(matriz):
    soma = 0
    for l in matriz:
        soma = soma+l[2]
        qtd =+ 1
    med = soma/qtd
    return med


pessoas = []

while True:
    pessoa = gerarPessoa()
    pessoas.append(pessoa)
    
    continuar = input("Deseja adicionar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break


print("\nPessoas cadastradas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, CPF: {pessoa[1]}, Idade: {pessoa[2]}, Renda Mensal: {pessoa[3]:.2f}")

print("\nEstatísticas:")
print(f"Renda média: R$ {calcRendaMedia(pessoas):.2f}")
print(f"Idade média: {calcIdadeMedia(pessoas):.2f} anos")