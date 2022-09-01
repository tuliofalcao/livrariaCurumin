import PySimpleGUI as sg 
import janelas
import vendedores
import pickle
import clientes

#confere se há algum arquivo pkl para carregar
try:
    with open('vendedores.pkl', 'rb') as p: #carrega o pkl com os dados dos vendedores
        vendedores.vendedores = pickle.load(p)
    with open('clientes.pkl', 'rb') as p:
        clientes.clientes = pickle.load(p)
except:
    print("")    

janela1,janela2,janela3,janela4 = janelas.janela_vendedor(), None, None, None

while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        with open('vendedores.pkl', 'wb') as p:
            arqVendedores = pickle.dump(vendedores.vendedores, p)
        with open('clientes.pkl', 'wb') as p:
            arqClientes = pickle.dump(clientes.clientes, p)
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
        
        
