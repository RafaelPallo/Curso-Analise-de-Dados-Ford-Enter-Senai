numero1 = float(input("Insira o primeiro número: "))
tipo_conta = input("1 - Adição(+) \n 2 - Subtração (-)\n 3 - Divisao(/) \n 4 - Multiplicação(*) \n 5 - Resto (%) \n 6 - Exponenciação \n Insira a operação desejada:")
numero2 = float(input("\n Insira o segundo número: "))

if tipo_conta == "1":
    print(f"{numero1} + {numero2} = {numero1+numero2}")
elif (tipo_conta == "2"):
    print(f"{numero1} - {numero2} = {numero1-numero2}")
elif (tipo_conta == "3"):
    if numero2 != 0:
        print(f"{numero1} / {numero2} = {numero1/numero2}")
    else:
        print("Não é possível dividir por zero")
elif (tipo_conta == "4"):
    print(f"{numero1} x {numero2} = {numero1*numero2}")
elif (tipo_conta == "5"):
    print(f"O resto da divisão entre {numero1} e {numero2} é = {numero1%numero2}")
elif (tipo_conta == "6"):
    print(f"O número {numero1} elevado a {numero2} é = {numero1**numero2}")
else : 
    print("Opção Inválida")
