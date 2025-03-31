def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print(f"\nVuelto\n")
    Vuelto = money-expense
    Pesos = int(Vuelto)
    print("Pesos")
    print(Pesos)
    Centavos = int((Vuelto-Pesos)*100)
    print("Centavos")
    print(Centavos)
