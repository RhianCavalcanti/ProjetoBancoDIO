loop=0#variavel para iniciar o looping
saldo=10000
extrato=[]
nsaques=3
while loop==0:
    op =input("""Qual operação deseja realizar?(digite o número)
    1-Saque
    2-Depósito
    3-Visualizar Extrato 
    4-SAIR """)


    if op=='1':
        saque=int(input("Quanto deseja sacar?"))
        if saldo>=saque and saque<=500 and nsaques>0:
            saldo=saldo-saque
            nsaques=nsaques-1
            extrato.append(str(f"-R${saque:.2f}"))#formantando a string para vermos que é um saque no extrato
            print(f"Saque Realizado!! ({nsaques} restantes)")
        elif saque>500:
            print("Não foi possível realizar saque. Saque Limite de R$500!")
        elif nsaques<=0:
            print("Não foi possível realizar saque. Número máximo de saques diários atingido!!")
        else:
            print("Não foi possível realizar saque. Sem dinheiro suficiente!")

    elif op=='2':
        deposito=int(input("Quanto deseja depositar?"))#formantando a string para vermos que é um depósito no extrato
        saldo=saldo+deposito
        extrato.append(str(f"+R${deposito:.2f}"))
        print("Depósito Realizado!!")
    elif op =='3':
        print("EXTRATO")
        extrato.append(str(f"Seu saldo é: R${saldo:.2f}"))
        for i in extrato:
            print('|'+i+'|')#So para deixar bonitinho
        extrato.pop(-1)#removendo o saldo para não ocorrer de adicionar varias vezes
    elif op == '4':
        loop=1