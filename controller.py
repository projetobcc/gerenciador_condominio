from model import *

class Controller:

    def __init__(self):
        self.lista_de_clientes = []
        self.lista_de_casas = []
        self.lista_de_funcionarios = []
        self.gerente = 0

    def tamanho_func(self):
        n = len(self.lista_de_funcionarios)
        return n

    def new_cliente(self,name,id,cpf):
        nome = name
        idade = id
        cpfi = int(cpf)
        newclient = Cliente(nome,idade,cpfi)
        self.lista_de_clientes.append(newclient)

    def new_casa(self,cs_comodos,cs_area,cs_localizacao):
        comodos = int(cs_comodos)
        area = float(cs_area)
        localizacao = cs_localizacao
        newcasa = Casas(comodos,area,localizacao)
        self.lista_de_casas.append(newcasa)

