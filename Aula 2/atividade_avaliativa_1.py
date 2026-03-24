""" 
#Exercicio 1:
numero1= float(input("Insira o primeiro numero: "))
numero2= float(input("Insira o segundo numero: "))

if(numero1>numero2):
    print(f"O número {numero1} é maior do que o número {numero2}")
elif(numero1<numero2):
    print(f"O número {numero2} é maior do que o número {numero1}")
else:
    print("Os dois números são iguais!")

print("--------------------------------------------------------------------------------------------------------")

#Exercicio 2:
numero = int(input("Insira um numero inteiro: "))

if (numero%2 == 0):
    print(f"O número: {numero} é par!")
else:
    print(f"O número: {numero} é ímpar!")

print("--------------------------------------------------------------------------------------------------------")
"""
#Exercício 3:
estado_civil = input(" C - casado \n S - solteiro \n D - divociado \n V - viúvo \n O - outros \n Qual o seu estado civil: ").upper()

if (estado_civil == "C"):
    print("C - Casado")
elif (estado_civil == "S"):
    print("S - Solteiro")    
elif (estado_civil == "D"):
    print("D - Divorciado")
elif (estado_civil == "V"):
    print("V - Viúvo")
elif (estado_civil == "O"):
    print("O - Outros")
else:
    print("Opção Inválida!")