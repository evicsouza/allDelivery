from Model.Pedido import Pedido
from Model.Usuario import Usuario
from Model.Produto import Produto
from Repositorio.RepositorioPedidos import RepositorioPedidos

class ControllerPedido: 
    repPedidos = RepositorioPedidos()
    def realizaPedido(self, idPedido, Usuario, Produto):
        pedido = Pedido(idPedido, usuario, produto)
        

