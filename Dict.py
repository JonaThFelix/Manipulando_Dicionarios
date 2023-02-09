#Jonathan | Akenathon | @hiperbolante
#Code usado para manipulação de dados em dicionário com Python
#Exemplo foi usado um sistema de cadastro de pacientes em um hospital

usuarios = []
permanecer = True

def adicionar_usuarios(cpf, nome, doenca, agenda):
    usuario = {}
    usuario["cpf"] = cpf
    usuario["nome"] = nome
    usuario["doenca"] = doenca
    usuario["agenda"] = agenda
    print("\n")

    usuarios.append(usuario)
    print(f"Paciente {nome} incluído com sucesso ")

while permanecer == True:
    escolha = int(input("\n[0] - Sair < \n[1] - Cadastro < \n[2] - Consultas < \n[3] - Listar pacientes cadastrados < \n[4] - Deletar usuários < \n[5] - Alterar dados do usuário <\n "))
    print("\n") 

    if escolha == 0:
        print("Você decidiu Sair.")
        permanecer = False
        break #encerra o alg se for False

    elif escolha == 1: #cadastrar
        cpf = input("Insira o CPF: ") #cpf como string
        nome = input("Insira o nome do paciente: ")
        doenca = input("Insira a doença: ")
        agenda = input("Insira a agenda: ")

        adicionar_usuarios(cpf, nome, doenca, agenda)
        
    elif escolha == 2: #consultar
        print("Você escolheu realizar uma CONSULTA\n")
        usuario1 = input("Digite o CPF que deseja consultar: ")
        for i in usuarios:
            if (i['cpf'] == usuario1):
                print("Paciente encontrado foi: ","\n Nome: ",i["nome"],"\n Doença: ",i["doenca"], " \n Data: ",i["agenda"])
        break #quiser reiniciar o sistema apenas tirar o comando


    elif escolha == 3: #listar
        print("Você escolheu LISTAR os usuários\n")
        for i in usuarios:
            print("Fichario cadastrado: ", i["nome"], "| Doença: ", i["doenca"])
            
        

  
    elif escolha == 4: #exclusão
        print("Você escolheu EXCLUIR\n")
        usuario3 = input("Digite o cpf que deseja excluir: ")
        for i in usuarios:
            if(i['cpf'] == usuario3):
                del i["cpf"]
                del i["nome"]
                del i["doenca"]
                del i["agenda"]
                print("Usuário excluído" ,usuarios)
                print("Usuário exclucído não poderá realizar nenhuma operação, apenas um novo cadastro, Digite 1")
        
    elif escolha == 5: #alteração
        print("Você escolheu ALTERAR\n")
        usuario4 = input("Digite o cpf para podermos realizar a Alteração: ")
        for i in usuarios:
            if(i['cpf'] == usuario4):
                for key, value in i.items():
                    if key == "nome":
                        i[key] = input(f"Alterar nome de > {nome} < para: ")
                    elif key == "doenca":
                        i[key] = input(f"Alterar doença de > {doenca} < para: ")
                    elif key == "agenda":
                        i[key] = input("Informe nova data para consulta: ")
                        print("Fichario atualizado para : ",usuarios)
                        print("")
                        print(" ")