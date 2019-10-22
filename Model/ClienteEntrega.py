from Usuario import Usuario
class ClienteEntrega(Usuario):
    def __init__(self, nome, email, senha, cpf, reputacao, tipoVeiculo):
        super().__init__(nome, email, senha, cpf)
        self.reputacao = reputacao
        self.tipoVeiculo = tipoVeiculo

    def getReputacao(self):
        return self.reputacao
    def setEndereco(self, reputacao):
        self.reputacao = reputacao
    def getTipoVeiculo(self):
        return self.tipoVeiculo
    def setTipoVeiculo(self, tipoVeiculo):
        self.tipoVeiculo = tipoVeiculo