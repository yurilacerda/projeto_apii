clientes = []

def cadastrar(lista):
    nome = input()
    cpf = input()
    usuario = [nome, cpf]
    lista.append(usuario)

def listar(lista):
    for e in lista:
        print("Nome:",e[0])    
        print("cpf:",e[1])    

opcao = 1
while (opcao!=9):
    print("1 - cadastra")
    print("9 - sair")
    opcao = int(input("Opção:"))
    if (opcao==1):
        cadastrar(clientes)
    elif (opcao==2):
        listar(clientes)
