from Usuario import Usuario
from Produto import Produto


class Pedido:
    def __init__(self, idPedido, idUsuario, idProduto):
        self.idPedido = idPedido
        self.idUsuario = idUsuario
        self.idProduto = idProduto

    def getIdPedido(self):
        return self.idPedido

    def setIdPedido(self, idPedido):
        self.idPedido = idPedido
