from Usuario import Usuario


class Administrador(Usuario):
    def __init__(self, nome, senha, cpf, email, privilegio):
        super().__init__(nome, email, senha, cpf)
        self.privilegio = privilegio

    def getPrivilegio(self):
        return self.privilegio

    def setPrivilegio(self, privilegio):
        self.privilegio = privilegio
