# -*- coding: utf-8 -*-
from controller import Controller
op = 55
control = Controller

master_log = "admin" # login padrão master, se mudada, vai ser importada na persistencia de arquivos
master_senha = 123

print "\n--------------- CondoPlus ---------------\n"
type_log = 0
log_sucess = False
cont = 0
while log_sucess == False:
    if cont == 0:
        cont += 1
        log = raw_input("Login: ")
    else:
        print "Login incorreto, tente novamente!"
        log = raw_input("Login: ")
    n = control.tamanho_func()
    for k in range(n):
        if control.lista_de_funcionarios[k].login == log:
            log_sucess = True
            type_log = 1
    if control.gerente.login == log:
        log_sucess = True
        type_log = 2
    if master_log == log:
        log_sucess = True
        type_log = 3
logsenha_sucess = False
cont = 0
while logsenha_sucess == False:
    if cont == 0:
        cont += 1
        log_senha = raw_input("Senha: ")
    else:
        if cont == 5:
            print "\nSenha incorreta\nLimite de tentativas excedido"
        else:
            cont += 1
            print "Senha incorreta, tente novamente!"
            log_senha = raw_input("Senha: ")
    n = control.tamanho_func()
    for k in range(n):
        if control.lista_de_funcionarios[k].login == log:
            if control.lista_de_funcionarios[k].senha == log_senha:
                logsenha_sucess == True
    if control.gerente.login == log:
        if control.gerente.senha == log_senha:
            logsenha_sucess == True
    if master_log == log:
        if master_senha == log_senha:
            logsenha_sucess == True
print "Login realizado com sucesso!"

'''while op != 7:
    print"1 - Cadastrar Casa\n" \
         "2 - Cadastrar Cliente\n" \
         "3 - Listar Casas Disponiveis\n" \
         "4 - Locação\n" \
         "5 - Pagamentos\n" \
         "6 - Listar Clientes\n" \
         "7 - Sair\n"
    op = int(raw_input())
    if op == 1:
        cs_com = int(raw_input("Digite a quantidade de comodos: "))
        cs_area = float(raw_input("Digite a área em metros quadrados: "))
        cs_loc = raw_input("Digite a localização: ")

        control.new_casa(cs_com,cs_area,cs_loc)
    if op == 2:
        cl_name = raw_input("Digite o nome do cliente: ")
        cl_idade = int(raw_input("Digite a idade do cliente: "))
        cl_cod = int(raw_input("Codigo do Cliente: "))
        control.new_cliente(cl_name,cl_idade,cl_cod)'''
