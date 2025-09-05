import sqlite3 #Importando a biblioteca sqlite3

#criando conexao com o banco de dados, no caso do sqlite3, um arquivo
conexao = sqlite3.connect("banco.db")

#criando variavel responsavel por executar querys(comandos sql). Chama-se cursor
cursor = conexao.cursor()

#chamar a funcao execute presente dentro da variavel cursor. Passando a query em formato
#de string
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY, nome TEXT, senha TEXT)")

while True:
    #menu com as opcoes disponiveis
    print()
    print("Escolha uma opcao a baixo: ")
    print("1) Inserir usuario")
    print("2) Listar usuarios")
    print("3) Sair")
    opcao = int(input("> "))

    if (opcao == 1):
        #pede ao usuario os valores de id, nome e senha do registro que quer adicionar
        #na tabela usuarios
        id = input("Digite o id do usuario: ")
        nome = input("Digite o nome do usuario: ")
        senha = input("Digite o senha do usuario: ")

        #execute a query de insert com os valores do usuario
        cursor.execute(f"INSERT INTO usuarios VALUES ({id}, '{nome}', '{senha}')")
        #salva as alteracoes feitas pelo insert
        conexao.commit()
    elif (opcao == 2):
        #Execute uma query de select e armazena o retorno da funcao execute na variavel resultado
        resultado = cursor.execute("SELECT * FROM usuarios")
        #chama a funcao fetchall presente dentro da variavel resultado. Mostra todas as linhas 
        #retornadas pela query executada acima
        print(resultado.fetchall())
    elif (opcao == 3):
        break
