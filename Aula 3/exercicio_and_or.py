#Exercicio 1

idade = int(input("Insira a sua idade: "))
autorizacao = input("Você tem autorização? \nDigite 1 - Sim ou 2 - Não: ")

if (idade >= 18 or autorizacao == "1"):
    print("Acesso autorizado")
else:
    print("Acesso negado")

#Exercicio 2

nota_final = float(input("Insira a nota final: "))
frequencia = int(input("Insira a frequencia do aluno: "))

if(nota_final >= 7 or frequencia >= 75):
    print("Aprovado")
else:
    print("Reprovado")

#Exercicio 3

login = input("Login: ")
senha = input("Senha: ")

if(login == "admin" and senha == "1234"):
    print("Acesso Autorizado")
else:
    print("Acesso Negado")

#Exercicio 4

salario = float(input("Insira o valor do salario: "))
tempo = int(input("Insira o tempo de empresa (anos): "))

if(salario < 3000 and tempo >= 2):
    print("Bônus concedido!")
else:
    print("Não recebe bônus!")