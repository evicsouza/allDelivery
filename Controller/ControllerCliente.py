from Model.ClientePedido import ClientePedido
from Repositorio.RepositorioCliente import RepositorioCliente
class ControllerCliente():
    repCliente = RepositorioCliente()
    def cadastrarCliente(nome, email, senha, cpf, endereco):
        c = ClientePedido(nome, email, senha, cpf, endereco)
        self.repCliente.cadastrarCliente(c)
    def removerCliente(cpf):
        self.repCliente.desativarCliente(cpf)
    def alterarCliente(nome, email, senha, cpf, endereco):
        self.repCliente.atualizarDadosClientePedido(nome, email, senha, cpf, endereco)
    def realizarPedido():

    def simularPedido():