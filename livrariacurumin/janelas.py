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
        [sg.Button('CADASTRE-SE')],
        [sg.Push()],
        [sg.Push()],
        [sg.Button('VISUALIZAR VENDEDORES')]
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
        [sg.Button('CADASTRAR CLIENTE'),sg.Button('CADASTRAR PRODUTO')],
        [sg.Push()],
        [sg.Button('VISUALIZAR PRODUTOS')]
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
        [sg.Button('REMOVER CLIENTE')],
        [sg.Push()],
        [sg.Button('VISUALIZAR CLIENTES')]
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
        [sg.Button('LP/CD')],
        [sg.Push()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('Cadastrar Produto', layout, element_justification='c', finalize=True)

#janela6
def janela_cadastroPapelaria():
    sg.theme('DarkBrown')
    layout = [
        [sg.Image('imagens/livraria2.png')],
        [sg.Text('Código:'), sg.Input(key='codigoPapelaria')],
        [sg.Text('Tipo:'), sg.Input(key='tipoPapelaria')],
        [sg.Text('Preço:'), sg.Input(key='precoPapelaria')],
        [sg.Text('Quantidade:'), sg.Input(key='quantidadePapelaria')],
        [sg.Button('CADASTRAR')],
        [sg.Push()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('Cadastrar Papelaria', layout, element_justification='center', finalize=True)

#janela7
def janela_cadastrarLivro():
    sg.theme('DarkBrown')
    layout = [
        [sg.Image('imagens/livraria2.png')],
        [sg.Text('Código:'),sg.Input(key='codigoLivro')],
        [sg.Text('Tipo:'),sg.Input(key='tipoLivro')],
        [sg.Text('Autor(a):'),sg.Input(key='autorLivro')],
        [sg.Text('Título:'),sg.Input(key='tituloLivro')],
        [sg.Text('Editora:'),sg.Input(key='editoraLivro')],
        [sg.Text('Preço:'),sg.Input(key='precoLivro')],
        [sg.Text('Quantidade:'), sg.Input(key='quantidadeLivro')],
        [sg.Button('CADASTRAR')],
        [sg.Push()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('Cadastrar Livro', layout, element_justification='center', finalize=True)

#janela8
def janela_cadastrarLP_CD():
    sg.theme('DarkBrown')
    layout = [
        [sg.Image('imagens/livraria2.png')],
        [sg.Text('Código:'),sg.Input(key='codigoLP')],
        [sg.Text('Tipo:'),sg.Input(key='tipoLP')],
        [sg.Text('Artista:'),sg.Input(key='artistaLP')],
        [sg.Text('Título:'),sg.Input(key='tituloLP')],
        [sg.Text('Gravadora:'),sg.Input(key='gravadoraLP')],
        [sg.Text('Preço:'),sg.Input(key='precoLP')],
        [sg.Text('Quantidade:'), sg.Input(key='quantidadeLP')],
        [sg.Button('CADASTRAR')],
        [sg.Push()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('Cadastrar LP / CD', layout, element_justification='center', finalize=True)