clientes = []
compras = []

class Cliente():
    
    def __init__(self, nome_cliente, cpf_cliente):
        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        
    def getNomeCliente(self):
        return self.nome_cliente
    
    def getCpfCliente(self):
        return self.cpf_cliente
    
    def setNomeCliente(self, valor):
        self.nome_cliente = valor
        
    def setCpfCliente(self, valor):
        self.cpf_cliente = valor
    