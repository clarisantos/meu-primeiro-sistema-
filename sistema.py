menu = """

[D] Depositar
[S] Sacar 
[E] Extrato 
[X] Sair 

=> """

saldo = 0
limite = 500 
extrato = ""
numero_saque = 0 
LIMITE_SAQUE = 3 

while True: 

    opção = input(menu)

    if opção == "D":
        valor = float(input("Informe o valor de depósito:"))

        if valor > 0: 
           saldo += valor 
           extrato += f"Depósito: R$ {valor:.2f}\n"    

        else: 
         print("Operação falhou! O valor é inválido.")    
       

    elif opção == "S":
        valor = float(input("Informe o valor do saque:"))
    
        excedeu_saldo = valor > saldo 
    
        excedeu_limite = valor > limite 
     
        excedeu_saques = numero_saque >= LIMITE_SAQUE
    
        if excedeu_saldo: 
            print ("Operaçã falhou! Você não tem saldo suficiente")
       
        elif excedeu_limite:
             print("Operação falhou! O valor do saque excede o limite")
        
        elif excedeu_saques: 
              print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0: 
             saldo -= valor 
             extrato += f"saque: R${valor:.2f}\n"
             numero_saque += 1 
        
        else:  
               print("Operação falhou! O valor informado é inválido")


    elif opção == "E":
         print("\n======EXTRATO======")
         print("Não foram realizadas movimentações") if not extrato else extrato 
         print (f"\nSaldo: R${saldo:2F}")
         print("======================")
   
   
    elif opção == "X": 
        break 

    else: 
        print("Operação inávlida, por favor selecione novamente a operação desejada")