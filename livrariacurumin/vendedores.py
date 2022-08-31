vendedores = []
vendas = []

class Vendedor:
        
    def __init__(self, nome_vendedor, cpf_vendedor):
        self.nome_vendedor = nome_vendedor
        self.cpf_vendedor = cpf_vendedor
                
    def getNome(self):
        return self.nome_vendedor
    
    def getCPF(self):
        return self.cpf_vendedor
    
    def getVendedores(self):
        return vendedores
    
    def getVendas(self):
        return vendas
    
    def setNome(self, valor):
        self.nome_vendedor = valor
    
    def setCPF(self, valor):
        self.cpf_vendedor = valor
        
    def removeItem(self, valor):
        item = [vendas.index(x) for x in self.vendas if x.codigo == valor]
        if len(item) > 0:
            vendas.remove(self.vendas[item[0]])
        else:
            print("Não há este item em suas vendas!")
    
    def adicionarItem(self, valor):
        return vendas.append(valor)
    
    
