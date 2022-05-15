class pessoasEmpresaX():  
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionariosgeral(pessoasEmpresaX):

    def __init__(self):
        self.salario = None
    
    def fazer_login(self):
        self.login = None
        pass
# Pra nomear depois
f1 = Funcionariosgeral()
f1.nome = "Felipe"
print(f"o nome do Funcionario: {f1.nome}")
f1.salario = 1200
print(f"O salario do Funcionario: {f1.salario}")
#'''
# f1 = Aluno()
# f1.nome = "Pedro"
# print(f"o nome do Aluno: {f1.nome}")
# c1 = Aluno()
# c1.cpf = "111.111.111-11"
# print(f"O cpf do Aluno: {c1.cpf}\n") '''
