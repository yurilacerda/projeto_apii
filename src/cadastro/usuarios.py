usuarios = []

def cadastrar(lista):
    nome = input()
    idade = input()
    usuario = [nome, idade]
    lista.append(usuario)

def listar(lista):
    for e in lista:
        print("Nome:",e[0])    
        print("Idade:",e[1])    

opcao = 1
while (opcao!=9):
    print("1 - cadastra")
    print("9 - sair")
    opcao = int(input("Opção:"))
    if (opcao==1):
        cadastrar(usuarios)
    elif (opcao==2):
        listar(usuarios)
