import os.path
from Model.ClientePedido import ClientePedido
class RepositorioCliente:
    clientesPedido = []
    clientesEntrega = []
    separador = ';'
    def criaArquivo():
        if(!os.path.exists('dadosCliente.txt')):
            arquivo = open('dadosCliente.txt', w)
            arquivo.close()
    def cadastrarCliente(cliente):
        clientesPedido.append(cliente)
    def atualizarDadosClientePedido(nome, email, senha, cpf, endereco):
        client = recuperarCliente(cpf)
        client.setNome(nome)
        client.setEmail(email)
        client.setSenha(senha)
        client.setEndereco(endereco)
    def atualizarDadosClienteEntrega(nome, email, senha, cpf, reputacao, tipoVeiculo):

    def recuperarCliente(cpf):
        for i in range(len(clientesPedido)):
            if(clientesPedido[i].getCPF() == cpf):
                return clientesPedido[i]
    def recuperarTodosClientes():

    def verificaCPF(cpf):
        for i in range(len(clientesPedido)):
            if(clientesPedido[i].getCPF() == cpf):
                return True
        return False
    def desativarCliente(cpf):
        a = 0
    def salvarArquivo():
        arquivo = open('dadosCliente.txt')
        for i in range(len(clientesPedido)):
            arquivo.write(clientesPedido[i].toString()+'\n')

    
