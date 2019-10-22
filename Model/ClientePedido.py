from Usuario import Usuario
class ClientePedido(Usuario):
    def __init__(self, nome, email, senha, cpf, endereco):
        super().__init__(nome, email, senha, cpf)
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco
    def setEndereco(self, endereco):
        self.endereco = endereco