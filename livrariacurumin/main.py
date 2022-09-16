import PySimpleGUI as sg 
import janelas
import vendedores
import pickle
import clientes
import produtos

#confere se há algum arquivo pkl para carregar
try:
    with open('vendedores.pkl', 'rb') as p: #carrega o pkl com os dados dos vendedores
        vendedores.vendedores = pickle.load(p)
    with open('clientes.pkl', 'rb') as p:
        clientes.clientes = pickle.load(p)
    with open('produtos.pkl', 'rb') as p:
        produtos.produtos = pickle.load(p)
except:
    print("")    

janela1,janela2,janela3,janela4,janela5,janela6,janela7,janela8 = janelas.janela_vendedor(),None,None,None,None,None,None,None

while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        with open('vendedores.pkl', 'wb') as p:
            arqVendedores = pickle.dump(vendedores.vendedores, p)
        with open('clientes.pkl', 'wb') as p:
            arqClientes = pickle.dump(clientes.clientes, p)
        with open('produtos.pkl', 'wb') as p:
            arqProdutos = pickle.dump(produtos.produtos, p)
        break
    
    #============= janela 1 =================
    
    if window == janela1 and event == 'CADASTRE-SE':
        janela2 = janelas.janela_cadastro_vendedor()
        janela1.hide()
    
    if window == janela1 and event == 'ENTRAR':
        cpf = values['cpf']
        item = [True for x in vendedores.vendedores if x.cpf_vendedor == cpf]
        if True in item:
            janela3 = janelas.janela_sistema()
            janela1.hide()
        else:
            sg.Popup("Vendedor não cadastrado!")
            janela1.hide()
            janela1 = janelas.janela_vendedor()
            
    if window == janela1 and event == 'VISUALIZAR VENDEDORES':
        sg.Popup(vendedores.Vendedor.mostrarVendedores(vendedores.vendedores))
    
    #============= janela 2 =================
        
    if window == janela2 and event == 'VOLTAR':
        janela2.hide()
        janela1.un_hide()
        
    if window == janela2 and event == 'CADASTRAR':
        nome_vendedor = values['nome_vendedor']
        cpf_vendedor = values['cpf_vendedor']
        item = [True for x in vendedores.vendedores if x.cpf_vendedor == cpf_vendedor]
        if True in item:
            sg.Popup("Vendedor já Cadastrado")
            janela2.hide()
            janela1.un_hide()
        else:
            vendedores.vendedores.append(vendedores.Vendedor(nome_vendedor, cpf_vendedor))
            sg.Popup("Cadastro Realizado com Sucesso")
            janela2.hide()
            janela1 = janelas.janela_vendedor()
        
    #============= janela 3 =================
    
    if window == janela3 and event == 'VOLTAR':
        janela3.hide()
        janela1.un_hide()
    
    if window == janela3 and event == 'CADASTRAR CLIENTE':
        janela3.hide()
        janela4 = janelas.janela_cadastroCliente()
        
    if window == janela3 and event == "CADASTRAR PRODUTO":
        janela3.hide()
        janela5 = janelas.janela_cadastroProduto()
        
    if window == janela3 and event == 'VISUALIZAR PRODUTOS':
        sg.popup(produtos.Produto.mostrarProdutos(produtos.produtos))       
        
    #============= janela 4 =================
    if window == janela4 and event == 'CADASTRAR':
        nomeCliente = values['nomeCliente']
        cpfCliente = values['cpfCliente']
        item = [True for x in clientes.clientes if x.cpf_cliente == cpfCliente]
        if True in item:
            sg.Popup('Cliente já Cadastrado')
            janela4.hide()
            janela1 = janelas.janela_vendedor()
        else:
            clientes.clientes.append(clientes.Cliente(nomeCliente, cpfCliente))
            sg.Popup('Cadastro Realizado com Sucesso')
            janela4.hide()
            janela1 = janelas.janela_vendedor()
    
    if window == janela4 and event == "REMOVER CLIENTE":
        nomeCliente = values['nomeCliente']
        cpfCliente = values['cpfCliente']
        item = [True for x in clientes.clientes if x.cpf_cliente == cpfCliente]
        if True in item:
            numeroIndex = [clientes.clientes.index(x) for x in clientes.clientes if x.cpf_cliente == cpfCliente]
            sg.Popup(f'Cliente {clientes.clientes[numeroIndex[0]].nome_cliente} removido(a)!')
            del clientes.clientes[numeroIndex[0]]
            janela4.hide()
            janela1 = janelas.janela_vendedor()
        else:
            sg.Popup('Cliente não cadastrado!')
            janela4.hide()
            janela1 = janelas.janela_vendedor()
    
    if window == janela4 and event == "VOLTAR":
        janela4.hide()
        janela1 = janelas.janela_sistema()
        
    if window == janela4 and event == 'VISUALIZAR CLIENTES':
        sg.popup(clientes.Cliente.mostrarClientes(clientes.clientes))
        
    #============= janela 5 ==================================
    if window == janela5 and event == 'PAPELARIA':
        janela5.hide()
        janela6 = janelas.janela_cadastroPapelaria()
    
    if window == janela5 and event == 'LIVRO':
        janela5.hide()
        janela7 = janelas.janela_cadastrarLivro()
    
    if window == janela5 and event == 'LP/CD':
        janela5.hide()
        janela8 = janelas.janela_cadastrarLP_CD()
    
    if window == janela5 and event == 'VOLTAR':
        janela5.hide()
        janela4 = janelas.janela_sistema() 
    
    #============= janela 6 ======================================
    if window == janela6 and event == 'CADASTRAR':
        codigoPapelaria = values['codigoPapelaria']
        tipoPapelaria = values['tipoPapelaria']
        precoPapelaria = values['precoPapelaria']
        quantidadePapelaria = values['quantidadePapelaria']
        item = [True for x in produtos.produtos if x.codigo == codigoPapelaria]
        if True in item:
            sg.Popup('Produto já cadastrado!')
            janela6.hide()
            janela5 = janelas.janela_cadastroProduto()
        else:
            produtos.produtos.append(produtos.Produto(codigoPapelaria,tipoPapelaria,precoPapelaria,quantidadePapelaria))
            sg.Popup('Produto Cadastrado com Sucesso!')
            janela6.hide()
            janela5 = janelas.janela_cadastroProduto()
    
    if window == janela6 and event == 'VOLTAR':
        janela6.hide()
        janela5 = janelas.janela_sistema()
        
    #=============== janela 7 ====================================
    if window == janela7 and event == 'CADASTRAR':
        codigoLivro = values['codigoLivro']
        tipoLivro = values['tipoLivro']
        autorLivro = values['autorLivro']
        tituloLivro = values['tituloLivro']
        editoraLivro = values['editoraLivro']
        precoLivro = values['precoLivro']
        quantidadeLivro = values['quantidadeLivro']
        item = [True for x in produtos.produtos if x.codigo == codigoLivro]
        if True in item:
            sg.Popup('Livro já cadastrado!')
            janela7.hide()
            janela5 = janelas.janela_cadastroProduto()
        else:
            produtos.produtos.append(produtos.Livro(codigoLivro,tipoLivro,autorLivro,tituloLivro,editoraLivro,precoLivro,quantidadeLivro))
            sg.Popup('Livro Cadastrado com Sucesso!')
            janela7.hide()
            janela5 = janelas.janela_cadastroProduto()
        
        if window == janela7 and event == 'VOLTAR':
            janela7.hide()
            janela5 = janelas.janela_cadastroProduto()
    
        
        
