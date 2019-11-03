class Pedido:
    def __init__(self, idPedido, usuario, produto):
        self.idPedido = idPedido
        self.usuario = Usuario(nome, email, senha, cpf)
        self.produto = Produto(idProduto, categoria, descricao)

    def getIdPedido(self):
        return self.idPedido

    def setIdPedido(self, idPedido):
        self.idPedido = idPedido
