class Produto:

    def __init__(self, idProduto, categoria, descricao):
        self.categoria = categoria
        self.descricao = descricao

    def getIdProduto(self):
        return self.idProduto

    def setIdProduto(self, idProduto):
        self.idProduto = idProduto

    def getCategoria(self):
        return self.categoria

    def getCategoria(self, categoria):
        self.categoria = categoria

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao
