import random

def Menu():
    while True:
        Escolha = input("1 - EX01\n2 - EX02\n3 - EX03\n0 - Sair\nEscolha: ")
        if Escolha not in "1230":
            print("Por favor escolha um dos exércicios.\n")
        else:
            Escolha = int(Escolha)
        match Escolha:
            case 1:
                EX01()
            case 2:
                Matriz = EX02()
                EX02_Val(Matriz)
            case 3:
                EX03()
            case 0:
                break

def EX01():
    print()
    Auth = 0
    Rec = 0
    for i in range(10):
        Tentativa = input("Digite 'A' caso o utilizador seja autorizado ou 'R' caso seja recusado: ")
        if Tentativa == "A":
            Auth = Auth + 1
        elif Tentativa == "R":
            Rec = Rec + 1
        else:
            print("Digite apenas A ou R! O programa terá de ser reiniciado.\n")
            break
    
    if Auth or Rec > 0:
        print(f"Total de acessos Autorizados {Auth}\nTotal de acessos Recusados {Rec}.")

        if Auth > Rec:
            print("Houve mais acessos AUTORIZADOS do que Recusados ao sistema.\n")
        elif Rec > Auth:
            print("Houve mais acessos RECUSADOS do que Autorizados ao sistema.\n")
        else:
            print("Tanto o número de acessos AUTORIZADOS quanto RECUSADOS é igual.\n")

def EX02():
    print()
    matriz = []

    for l in range(4):
        linha = []
        for c in range(7):
            val = random.randint(0, 1)
            linha.append(val)
        matriz.append(linha)
    for co in range(len(matriz)):
        print(matriz[co])

    return matriz
    
def EX02_Val(Matriz):
    Totais = []
    for i in range(4):
        soma = 0
        for j in range(len(Matriz[i])):
            soma = soma + Matriz[i][j]
        Totais.append(soma)
    print(Totais)

    for checker in range(len(Totais)):
        if Totais[checker] >= 3:
           print(f"Número ELEVADO de alertas no servidor {checker}")
        else:
            print(f"Número de alertas CONTROLADO no servidor {checker}")
    
    print()

def EX03():
    print()
    ips = ["192.168.1.10", "192.168.1.21", "192.168.1.34", "192.168.1.45", "192.168.1.56", "192.168.1.67"]
    falhas = [2, 8, 4, 12, 1, 6]
    ips_block = []
    
    Val = max(falhas)
    CheckValI = falhas.index(Val)

    CheckMaiorNumFalha = ips[CheckValI]

    for x, y in enumerate(ips):
        for cont in falhas:
            z = falhas[x]
        if z > 5:
            ips_block.append(y)
        print(f"O IP: {y} tentou aceder {z} vezes ao servidor!")
    print(f"\nOs seguintes IPs estão BLOQUEADOS: {ips_block}.")
    print(f"O IP com mais acessos foi: {CheckMaiorNumFalha} com {Val} acessos falhos.\n")

Menu()