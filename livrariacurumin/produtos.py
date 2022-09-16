produtos = []

class Produto:
    
    def __init__(self, codigo, tipo, preco, quantidade):
        self.codigo = codigo
        self.tipo = tipo
        self.preco = preco
        self.quantidade = quantidade
        
    def getCodigo(self):
        return self.codigo
    
    def getTipo(self):
        return self.tipo
    
    def getPreco(self):
        return self.preco
    
    def getQuantidade(self):
        return self.quantidade
    
    def setCodigo(self, valor):
        self.codigo = valor
    
    def setTipo(self, valor):
        self.tipo = valor
    
    def setPreco(self, preco):
        self.preco = preco
        
    def setQuantidade(self, valor):
        self.quantidade = valor
    
    def mostrarProdutos(self):
        m = '\n'.join([str((x.codigo, x.tipo)) for x in produtos])
        return m


class Livro(Produto):
    
    def __init__(self, codigo, tipo, autor, titulo, editora, preco, quantidade):
        super().__init__(codigo,tipo,preco,quantidade)
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        
    def getAutor(self):
        return self.autor
    
    def getTitulo(self):
        return self.titulo
    
    def getEditora(self):
        return self.editora
    
    def setAutor(valor):
        self.autor = valor
        
    def setTitulo(valor):
        self.titulo = valor
        
    def setEditora(valor):
        self.editora = valor


class Disco(Produto):
    
    def __init__(self, codigo, tipo, artista, titulo, gravadora, preco, quantidade):
        super().__init__(codigo, tipo, preco, quantidade)
        self.artista = artista
        self.titulo = titulo
        self.gravadora = gravadora
        
    def getArtista(self):
        return self.artista
    
    def getTitulo(self):
        return self.titulo
    
    def getGravadora(self):
        return self.gravadora
    
    def setArtista(self, valor):
        self.artista = valor
        
    def setTitulo(self, valor):
        self.titulo = valor
    
    def setGravadora(self, valor):
        self.gravadora = valor
        