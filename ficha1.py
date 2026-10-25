while True:
    try:
        def porta(numero):
            if numero != 2:
                for i in range(2, numero):
                    if numero % i == 0:
                        return False
            
            return True    
        
        def NVogais(frase):
            fraseN = ("")
            for c in frase:
                if c.lower() not in "aeiou ":
                    fraseN = fraseN + c
            
            return fraseN
        
        def contar_intervalo():
                inicio = int(input("Digite um valor de inicio: "))
                fim = int(input("Digite um valor de fim: "))
                
                if inicio > fim:
                    inicio, fim = fim, inicio
                
                for res in range(fim, inicio, -1):
                    if res % 10 != 0:
                        print(res)
        
        def estatisticas_valores():
            lista = []
            cont = 0
            imp = 0
            some = 0

            while True:
                num = int(input("Digite um valor positivo ou negativo caso queira encerrar o programa: "))
                
                if num <= 0:
                    media(some, len(lista), cont, imp)
                    break
                
                cont = cont + 1

                if num % 2 == 0:
                    lista.append(num)
                    some = some + num
                else:
                    imp = imp + 1
        
        def media(soma, tamanho, cont, imp):
            media_f = soma/tamanho

            print("Valores digitados:", cont)
            print("Valores Impares:", imp)
            print("Valores Medio Positivos:", media_f)

        def contar_leds():
            num = input("Digite um valor: ")
            leds = 0
            for i in num:
                if i == "1":
                    leds = leds + 2
                elif i == "2, 3, 5":
                    leds = leds + 5
                elif i == "6, 9, 0":
                    leds = leds + 6
                elif i == "4":
                    leds = leds + 4
                elif i == "7":
                    leds = leds + 3
                else:
                    leds = leds + 7

            print("Leds Necessários:", leds)       

        def IP_VAL():
            ip_list = []
            ip = input("Digite o IP: ")
            ip_list = ip.split(".")
            cont = 0

            for i in ip_list:
                if not i.isdigit():
                    print("IP Inválido")
                IPV = int(ip_list[cont])
                if not (0 <= IPV <= 255):
                    print("IP Inválido")
                    break
                cont = cont + 1
            
            print("IP Válido")

        
        def menu():
            return int(input("1- Validação de Porta\n" + 
                        "2- Frases sem vogais\n" +
                        "3- Contar intervalo\n" +
                        "4- Contar Numeros\n" +
                        "5- Nº Leds\n" +
                        "6- IP Validation\n" +
                        "7- Break\n" +
                        "Escolha: "))
        match menu():
            case 1:
                while True:
                    primo = input("Digite o número da porta ou FIM: ").lower()

                    if primo == "fim":
                        break
                    else:
                        primo = int(primo)
                        val = porta(primo)
                    
                    if val == True:
                        print("A porta é um Nº Primo")
                    else:
                        print("A porta não é um Nº primo")
            case 2:
                while True:
                    frase = input("Digite uma frase ou FIM: ").lower()

                    if frase == "fim":
                        break
                    else:
                        frase_n = NVogais(frase)
                        print(frase_n)
            case 3:
                contar_intervalo()
            case 4:
                estatisticas_valores()
            case 5:
                contar_leds()
            case 6:
                IP_VAL()
            case 7:
                print("Programa finalizado")
                break
            case _:
                print("Escolhe um número que exista na lista")
    except ValueError:
        print("Escolhe um número da lista")