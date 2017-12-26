class Cliente:

    def __init__(self, nome, idade, n_cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = n_cpf


class Casas:

    def __init__(self, qt_comodos, area, local):
        self.comodos = qt_comodos
        self.area = area
        self.localizacao = local

class Funcionario:

    def __init__(self,nome,login,senha):
        self.name = nome
        self.login = login
        self.senha = senha

class Gerente:

    def __init__(self,nome,login,senha):
        self.name = nome
        self.login = login
        self.senha = senha