import random

while True:
    try:
        esc = int(input("1- Validação de password\n" + 
                        "2- PPS\n" +
                        "3- Validar email\n" +
                        "4- Lançamentos & Adivinhar\n" +
                        "5- Break\n" +
                        "Escolha: "))
        match esc:
            case 1:
                def pedir_utilizador():
                    return input("Digite o user: ")
                
                def pedir_senha():
                    return input("Digite a senha: ")
                
                def validar_login(utilizador, senha):
                    if login == user and senha_login == password:
                        return True
                    else:
                        return False
                
                def mostrar_resuldado(valido, tester):
                    if val == True:
                        print("Acesso concedido")
                    else:
                       print("Credenciais Inválidas; Tentativas restantes:", tester) 

                password = "1234"
                user = "admin"

                tester = 3

                while True:
                    login = pedir_utilizador()
                    senha_login = pedir_senha()

                    if tester == 1:
                        print("Conta bloqueada por excesso de tentaivas. Contacte o ADM")
                        break

                    tester = tester - 1
                    val = validar_login(login, senha_login)
                    mostrar_resuldado(val, tester)

                    if validar_login == True:
                        break
            case 2:
                while True:
                    pps = input("Digite o valor PPS ou SAIR: ")
                    pps.lower()

                    if pps == "sair":
                        break
                    else:
                        pps = int(pps)
                    if pps < 0:
                        print("Um PPS não pode ser negativo")
                    elif pps <= 50:
                        print("Tráfego Normal")
                    elif pps <= 200:
                        print("Suspeito. Deve ser feita uma varredura")
                    elif pps <= 1000:
                        print("Anómalo. Possível ataque DDoS. Validação necessária")
                    else:
                        print("Crítico. Bloquear IP de Origem")
            case 3:
                def validar_email():
                    i = 0
                    for a in email:
                        if a == "@":
                            i = i + 1
                        elif i == 1 and a == ".":
                            i = i + 1
                                    
                    if i == 2:
                        return True
                    else:
                        return False
                                    
                email = input("Escreva um email: ")

                if validar_email():
                    print("Possivel email valido")
                else:
                    print("Email incorreto")
            case 4:
                def dados():
                    for _ in range(1, 11):
                        print(_, "º dado:", random.randint(1, 6))
                def dificuldade(diff):
                    match diff:
                        case 1:
                            return random.randint(1, 20)
                        case 2:
                            return random.randint(1, 50)
                        case 3:
                            return random.randint(1, 100)
                def adivinhar():
                    diff = int(input("Escolha uma dificuldade:\n" +
                             "1- Fácil\n"+
                             "2- Médio\n" +
                             "3- Hard\n" +
                             "Escolha: "))
                    
                    dado = dificuldade(diff)

                    trys = 0
                    while True:   
                        x = int(input("Digite um valor: "))
                        trys = trys + 1

                        if dado < x:
                            if x - 20 > dado:
                                print("O valor é muito menor.")
                            else:
                                print("O valor é menor.")
                        else:
                            if x + 20 < dado:
                                print("O valor é muito maior")
                            else:
                                print("O valor é maior")
                        
                        if dado == x:
                            print(f"Em cheio! Parabéns! O valor era {dado} e levou {trys} tentativas")
                            break
                def menu():
                    vali = int(input("1- Rodar 10 dados de 6 lados\n" +
                                 "2- Adivinhar Nº\n" +
                                 "Escolha: "))

                    match vali:
                        case 1:
                            dados()
                        case 2:
                            adivinhar()
                menu()            
            case 5:
                print("Programa finalizado")
                break
            case _:
                print("Escolhe um número que exista na lista")
    except ValueError:
        print("Escolhe um número da lista")