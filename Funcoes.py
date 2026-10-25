import random

def gerador():
    matliz = []

    lin = random.randint(2, 15)
    col = random.randint(2, 15) 

    for l in range(lin):
        linha = []
        for c in range(col):
            val = random.randint(0, 15)
            linha.append(val)
        matliz.append(linha)
    for co in range(len(matliz)):
        print(matliz[co])
    return matliz

def matriz():
    som = 0
    logs = [[0, 5, 1, 0], [2, 0, 0, 1], [1, 1, 4, 6]]
    for i in range(len(logs)):
        for j in range(len(logs[i])):
            som = som + logs[i][j]
            if logs[i][j] > 3:
                print(f"Alerta: User: {i} no Dia: {j} falhou {logs[i][j]} vezes!")

        if som >= 7:
            print(f"User {i} suspeito! Teve {som} nesta semana")

def somaLinha(matriz):
    soma = 0
    for i in range(1):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
    print(soma)    
    return soma

def somaColuna(matriz):
    soma = 0
    print(len(matriz))
    for i in range(len(matriz)):
            soma += matriz[i][1]
    print(soma)    
    return soma