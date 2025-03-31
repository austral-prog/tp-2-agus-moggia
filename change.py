def change():
    expense = 23.75
    money = 100
    print("ingresar gasto:")
    print(expense)
    print("dinero recibido")
    print(money)
    print(f"\n vuelto \n")
    vuelto = money-expense
    pesos = int(vuelto)
    print("Pesos")
    print(pesos)
    centavos = int((vuelto-pesos)*100)
    print("Centavos")
    print(centavos)
change() 
