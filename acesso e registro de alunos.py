import time



#seperador
def linha():
    print("-------------------")
    
    
#função cadastro 
def cadastro(): # cadastro de alunos ao colégio
    
    print("COLETA DE DADOS NÃO SENSÍVEL")
    idade = int(input(f"{R} antes de mais nada,qual a sua idade ? \n"))
    if idade < 18:
        print("Perdão, apenas maiores de idade podem fazer esse cadastro.")
    else:
        nome = input("Informe o nome completo:\n")
        serie = input("Em qual série você esta? \n")
        tel = input("Tel:")
    
    linha()
    print("\t\t\t\tCarregando.......")
    time.sleep(3.0)
    print("\t\t\t\tCadastrado com sucesso!\n Agora aguarde o nosso contato para \ncomparecer ao escritório")
    print("\t\tDados fornecidos")
    print(f"\t\t\t\tNome:{nome} \n Idade:{idade} \n Série: {serie} \n Contato:{tel}")


#função acesso
def acesso():
    lista_acesso = ["Luna"]
    lista_senha = ["12345"]
    login = input("Login de aluno:")
    if login not in lista_acesso:
            print("\t\t\tACESSO NEGADO \n \t\t\tLogin incorreto")
    else:
            senha = input("inserir senha:")
            if senha not in lista_senha:
                print("Senha incorreta")
    

#------------------------   código primário  --------------------------
print("INICIANDO O SISTEMA,AGUARDE......")
time.sleep(5.0)

linha()
class pessoa:
    def __init__(self,nome,sexo):
        self.nome = nome
        self.sexo = sexo
        
    def saudação(self):
        print("Seja bem-vindo \t" + self.nome +" ao sistema aluno.\n")
        time.sleep(3.0)
        linha()
        
        
    def pergunta(self):
        info=input("É aluno? s ou n")
        if info == "s":
            print(f"Bem - vindo aluno {R}") 
            acesso()
        if info == "n":
            print("Faz cadastro")
            cadastro()

        
        
# -------------------------- código secundário ---------------------

        
R = input("Qual o seu nome")
S = input("Qual o sexo ")

Y=pessoa(R,S)
Y.saudação()
Y.pergunta()
