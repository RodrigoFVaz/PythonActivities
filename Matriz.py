def matriz1():
    som = 0
    logs = [[0, 5, 1, 0], [2, 0, 0, 1], [1, 1, 4, 6]]
    for i in range(len(logs)):
        for j in range(len(logs[i])):
            som = som + logs[i][j]
            if logs[i][j] > 3:
                print(f"Alerta: User: {i} no Dia: {j} falhou {logs[i][j]} vezes!")

        if som >= 7:
            print(f"User {i} suspeito! Teve {som} nesta semana")
         

matriz1()