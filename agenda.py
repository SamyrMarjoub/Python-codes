AGENDA = {}


# AGENDA['guilherme'] = {
#     'telefone': '2222222',
#     'email': 'asdasdasd@gmail.com',
#     'endereco': 'Av.2',
# }

# AGENDA['Mario'] = {
#     'telefone': '111111',
#     'email': 'asdasdsad@gmail.com',
#     'endereco': 'Av.21',
# }


def BuscarContato(nome):
    try:
        print('Telefone:', AGENDA[nome]['telefone'])
        print('Email:', AGENDA[nome]['email'])
        print('Endereco:', AGENDA[nome]['endereco'])
        print('')
    except KeyError:
        print('Usuario não encontrado')
    except Exception as error:
        print('Erro desconhecido')


def MostrarAgenda():
    if len(AGENDA) == 0:
        print('Não há contatos atualmente')
    else:
        for pessoas in AGENDA:
            BuscarContato(pessoas)

    print('-----------------------')


def ExcluirContato(nome):
    try:
        AGENDA.pop(nome)
        print('Excluido com sucesso!')
        salvar()

    except KeyError:
        print('Usuario não encontrado')
    except Exception as error:
        print('Erro desconhecido')


def EditarContato(prevname, telefone, email, endereco):
    try:
        if telefone == '':
            telefone = AGENDA[prevname]['telefone']
        else:
            AGENDA[prevname]['telefone'] = telefone
        if email == '':
            email = AGENDA[prevname]['email']
        else:
            AGENDA[prevname]['email'] = email
        if endereco == '':
            endereco = AGENDA[prevname]['email']
        else:
            AGENDA[prevname]['endereco'] = endereco

        salvar()

    except KeyError:
        print('Usuario não encontrado')
    except Exception as error:
        print('Erro desconhecido')


def IncluirContato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone':  telefone,
        'email': email,
        'endereco': endereco
    }
    
    print('Nome {} incluido com sucesso'.format(nome))
    salvar()


def exportarcsv(nome_do_arquivo):
    # print('Exportando arquivos para csv')
    arquivo = open(nome_do_arquivo, 'w')
    for contatos in AGENDA:
        telefone = AGENDA[contatos]['telefone']
        email = AGENDA[contatos]['email']
        Endereco = AGENDA[contatos]['endereco']
        arquivo.write('{}, {}, {}, {} \n'.format(
            contatos, telefone, email, Endereco))
    arquivo.close()


def importarcsv(nome_do_arquivo):
    print('Importando contatos do banco de dados')
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                IncluirContato(nome, telefone, email, endereco)
                print('{} contatos carregados'.format(len(AGENDA)))
                
    except FileNotFoundError:
        print('arquivo não encontrado')
    except Exception as error:
        print('Erro desconhecido', error)


def salvar():
    exportarcsv('database.csv')


def carregar():
    importarcsv('database.csv')


def menu():
    print()
    print(('---------------------------------------'))
    print('1 - MOSTRA OS CONTATOS DA AGENDA')
    print('2 - BUSCAR CONTATO')
    print('3 - REMOVER CONTATO')
    print('4 - EDITAR CONTATO')
    print('5 - ADICIONAR CONTATO')
    print('6 - EXPORTAR CONTATOS')
    print('7 - IMPORTAR CONTATOS')
    print('0 - FECHAR SA PORRA')
    print(('---------------------------------------'))
    print()


carregar()
while True:
    menu()
    opc = input('Digite sua escolha: ')

    if opc == '1':
        MostrarAgenda()
    elif opc == '2':
        valor = input('Quem você quer buscar?? ')
        BuscarContato(valor)
    elif opc == '3':
        valor = input('Quem você quer excluir?? ')
        ExcluirContato(valor)

    elif opc == '4':
        valor = input('Quem você quer editar?? ')
        novoTel = input('Digite novo telefone ')
        novoEma = input('Digite novo email ')
        novoEnd = input('Digite novo endereco ')
        EditarContato(valor, novoTel, novoEma, novoEnd)

    elif opc == '5':
        Name = input('Digite o nome a ser incluido ')
        Telefone = input('Digite o Telefone a ser incluido ')
        Email = input('Digite o email a ser incluido ')
        Endereco = input('Digite o Endereco a ser incluido ')
        IncluirContato(Name, Telefone, Email, Endereco)
        BuscarContato(Name)
    elif opc == '6':
        print('Você tem certeza que quer importar? certifique-se que você esteja com todos os arquivos do csv localmente para evitar perda de dados.')
        confirmar = input('Digite 1 para continuar e 2 para cancelar ')

        if confirmar == '1':
            valor = input('Digite o nome do arquivo  ')
            exportarcsv(valor)
        elif confirmar == '2':
            pass

    elif opc == '7':
        valor = input('Digite o nome do arquivo ')
        importarcsv(valor)

    elif opc == '0':
        print('Fechando programa')
        break
