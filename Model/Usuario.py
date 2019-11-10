class Usuario:
    def __init__(self, id, nome, email, senha, cpf):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setSenha(self, senha):
        self.senha = senha

    def getSenha(self):
        return self.senha

    def setCPF(self, cpf):
        self.cpf = cpf

    def getCPF(self):
        return self.cpf
