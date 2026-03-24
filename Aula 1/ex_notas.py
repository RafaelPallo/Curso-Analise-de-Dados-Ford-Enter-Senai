nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))
nota4 = float(input("Insira a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if (media >=7):
    print(f"A sua média foi de: {media}. Parabéns você foi aprovado!!!")
elif(media>=5): 
    print(f"A sua média foi de: {media}. Você está de recuperação!")
else:
    print(f"A sua média foi de: {media}. Que triste...Você foi reprovado!")


    