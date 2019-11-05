class Pedido:
    def __init__(self, idPedido, usuario, produto):
        self.idPedido = idPedido
        self.usuario = usuario
        self.produto = produto
    def getIdPedido(self):
        return self.idPedido

    def setIdPedido(self, idPedido):
        self.idPedido = idPedido
