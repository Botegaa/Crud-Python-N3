def menu():
    while True:
        print("Escolha a opção:")
        print("1 - Cadastrar Dados")
        print("2 - Listar Dados")
        print("3 - Alterar Dados")
        print("4 - Excluir Dados")
        print("5 - Realizar Backup do arquivo")
        print("0 - Sair")
        opcao = input("Digite a sua opção: ")
        print("-"*50)
        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            alterar_dados()
        elif opcao == "4":
            excluir_dados()
        elif opcao == "5":
            backup_dados()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite um número válido.")
            print("-"*50)
def cadastrar_dados():
    try:
        with open("Dados.txt", "a") as arquivo:      # Abre o arquivo no modo de adicionar novos dados "a" append 
            nome=input("Digite o nome do atleta: ") 
            sexo=input("Digite o sexo do atleta: ") 
            dataNascimento=input("Insira o número do ano de nascimento do atleta (Ex. 28/04/2002): ") 
            cidade=input("Digite a cidade que o atleta reside: ") 
            estado=input("Digite a sigla do estado que o atleta reside(Ex. SC): ") 
            posicao=input("Digite a posição do atleta: ") 
            responsavel=input("Digite o nome do responsável pelo atleta: ")
      
            jogador = f"{nome},{sexo},{dataNascimento},{cidade},{estado},{posicao},{responsavel}\n"    # Formata os dados do jogador em uma string

            arquivo.write(jogador)    # Escreve a string no formato acima em dados no arquivo "Dados.txt"
             
            print("Dados do jogador cadastrados com sucesso!")
            print("-"*50)
    except Exception as e:
            print("Ocorreu um erro ao cadastrar os dados:", str(e))
            print("-"*50)
def listar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo: # Abrir o arquivo 'Dados.txt' em modo de leitura ('r')
            linhas = arquivo.readlines() # Ler todas as linhas do arquivo e armazená-las em uma lista
        if not linhas:   # if para caso as nao haja linha alguma no dados.txt
            print("Nenhum dado do jogador cadastrado.")
            print("-"*50)
        else:
            print("Dados do jogador cadastrados:") 
            print("-"*50)
            for linha in linhas:
                dados = linha.strip().split(',')# Dividir a linha em partes separadas por vírgula (',') e remover os espaços em branco

# Transforma as strings do txt em variaveis capturando elas pelo seus index
                nome = dados[0]
                sexo = dados[1]
                dataNascimento = dados[2]
                cidade = dados[3]
                estado = dados[4]
                posicao = dados[5]
                responsavel = dados[6]

                print("Nome do Jogador:", nome)
                print("Sexo:", sexo)
                print("Data de nascimento:", dataNascimento)
                print("Cidade:", cidade)
                print("Estado:", estado)
                print("Posição do Atleta:", posicao)
                print("Nome do Responsavel:", responsavel)
                print("-"*50)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
        print("-"*50)
    except Exception as e:
        print("Ocorreu um erro ao listar os dados:", str(e))
        print("-"*50)            


def alterar_dados(): 
    try:
        with open('Dados.txt', 'r') as arquivo: #abre arquivo Dados.txt no modo de leitura "r"
            linhas=arquivo.readlines() #lê todas as linhas do arquivo e as armazena em uma variavel chamada 'linhas'
        if not linhas: #verifica se tem elementos a lista linhas
            print("Nenhum dado foi cadastrado.")
            print("-"*50)
            
        nome=input("Digite o nome do atleta que deseja alterar os dados: ") 
        encontrado=False #variavel para verificar se o jogador foi encontrado

        with open("Dados.txt", "w") as arquivo: #abre arquivo Dados.txt no modo de escrita "w" para substituir os dados ja existentes
            for linha in linhas: #percorre todas as linhas do .txt
                dados=linha.strip().split(',') #.strip() remove espaços em branco no início e no final da linha e .split()separa os dados pela vírgula
                if dados[0]==nome: #verifica se o nome na linha corresponde ao nome digitado
                    novo_nome=input("Digite o novo nome do atleta: ") 
                    novo_sexo=input("Digite o novo sexo do atleta: ")
                    nova_dataNascimento=input("Insira o número do ano de nascimento do atleta: ")
                    nova_posicao=input("Digite a nova posição em que a atleta atua: ")
                    nova_cidade=input("Digite a nova cidade que o atleta reside: ")
                    novo_estado=input("Digite o novo estado que o atleta reside: ")
                    novo_responsavel=input("Digite o novo nome do(a) responsável pelo atleta: ")
                    jogador= f"{novo_nome}, {novo_sexo}, {nova_dataNascimento}, {nova_posicao}, {nova_cidade}, {novo_estado}, {novo_responsavel},\n" #cria uma nova linha com os 
                    
                    arquivo.write(jogador) #escreve a string alt_jogador no arquivo Dados.txt com os dados alterados
                    encontrado=True  #indicando que o jogador foi encontrado e os dados foram alterados
                    print("Dados alterados com sucesso!\n")
                    print("-"*50)
                else:
                    arquivo.write(linha) #escreve a linha origina no arquivo

        if not encontrado:
             print("Nome do(a) atleta não encontrada nos cadastros.")
             print("-"*50)
    except FileNotFoundError:
         print("Arquivo de dados não encontrado.")
         print("-"*50)
    except Exception as e: 
            print("Ocorreu um erro ao alterar os dados:", str(e))
            print("-"*50)

def backup_dados(): 
    try:
        with open("Dados.txt", "r") as arquivo_origem: #abre arquivo de origem Dados.txt no modo de leitura "r"
              with open("backup_Dados.txt", "w") as arquivo_backup: #abre o arquivo de backup Backup_Dados.txt no modo escrita "w"
                   conteudo = arquivo_origem.read() #lê todo o arquivo
                   arquivo_backup.write(conteudo)
                   print("Backup Realizado Com sucesso")
                   print("-"*50)
    except Exception as e: 
        print("Ocorreu um erro ao realizar o backup dos dados:", str(e))
        print("-"*50)

def excluir_dados(): 
  try:
    with open('Dados.txt', 'r') as arquivo: #abre arquivo Dados.txt no modo de leitura "r"
      linhas=arquivo.readlines() #lê todas as linhas do arquivo e as armazena em uma lista chamada 'linhas'
      if not linhas: #verifica se tem elementos a lista linhas
        print("Nenhum dado foi cadastrado.")
        print("-"*50)
        return 
    nome=input("Digite o nome do atleta que deseja excluir os dados: ")
    encontrado=False
    with open('Dados.txt','w') as arquivo: #abre arquivo Dados.txt no modo de escrita "w" para substituir os dados ja existentes
      for linha in linhas: #percorre todas as linhas do .txt
        dados=linha.strip().split(',') #.strip() remove espaços em branco no início e no final da linha e .split()separa os dados pela vírgula
        if dados[0]==nome: #verifica se o nome na linha corresponde ao nome digitado
          encontrado=True 
          print("Dados excluídos com sucesso!")
          print("-"*50)
        else:
          arquivo.write(linha) #escreve a linha no arquivo, retirando a do atleta a ser excluído.
    if not encontrado:
      print(f"O atleta '{nome}' não foi encontrado.")
      print("-" * 50)     
  except FileNotFoundError: 
    print("Arquivo de dados não encontrado.\n")
    print("-"*50)
  except Exception as e: 
    print("Ocorreu um erro ao alterar os dados: ", str(e))
    print("-"*50)        