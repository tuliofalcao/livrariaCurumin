import PySimpleGUI as sg 


#janela1
def janela_vendedor():
    sg.theme('DarkBrown')
    layout = [
        [sg.Image('imagens/livraria2.png')],
        [sg.Push()],
        [sg.Text('MATRÍCULA/CPF: ')],
        [sg.Input(key='cpf')],
        [sg.Push()],
        [sg.Button('ENTRAR')],
        [sg.Push()],
        [sg.Push()],
        [sg.Push()],
        [sg.Text('Ainda não cadastrado?')],
        [sg.Button('CADASTRE-SE')]
    ]
    
    return sg.Window('Login', layout, element_justification='c',finalize=True)

#janela2
def janela_cadastro_vendedor():
    sg.theme('DarkBrown')
    layout = [
        [sg.Text('Preencha seus dados abaixo')],
        [sg.Push()],
        [sg.Push()],
        [sg.Text('Nome:')],
        [sg.Input(key='nome_vendedor')],
        [sg.Text('CPF:')],
        [sg.Input(key='cpf_vendedor')],
        [sg.Push()],
        [sg.Button('VOLTAR'), sg.Button('CADASTRAR')]
    ]
    
    return sg.Window('Cadastro - Vendedor', layout, element_justification='c', finalize=True)

#janela3
def janela_sistema():
    sg.theme('DarkBrown')
    layout = [
        [sg.Image('imagens/livraria2.png')],
        [sg.Push()],
        [sg.Text('Buscar produto')],
        [sg.Input(key='busca_produto')],
        [sg.Button('VOLTAR'),sg.Button('BUSCAR')],
        [sg.Button('CADASTRAR CLIENTE'),sg.Button('CADASTRAR PRODUTO')]
    ]
    
    return sg.Window('Sistema de Busca', layout, element_justification='c', finalize=True)

#janela4
def janela_cadastroCliente():
    sg.theme('DarkBrown')
    layout = [
        [sg.Text('Nome do cliente:')],
        [sg.Input(key='nomeCliente')],
        [sg.Text('CPF do Cliente:')],
        [sg.Input(key='cpfCliente')],
        [sg.Button('VOLTAR'), sg.Button('CADASTRAR')],
        [sg.Button('REMOVER CLIENTE')]
        ]
    return sg.Window('Cadastro de Cliente', layout, element_justification='c', finalize=True)

#janela5
def janela_cadastroProduto():
    sg.theme('DarkBrown')
    layout = [
        [sg.Image('imagens/livraria2.png')],
        [sg.Text('Qual produto você irá cadastrar?')],
        [sg.Button('PAPELARIA')],
        [sg.Button('LIVRO')],
        [sg.Button('LP/CD')]
    ]
    return sg.Window('Cadastrar Produto', layout, element_justification='c', finalize=True)

