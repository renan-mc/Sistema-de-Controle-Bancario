from abc import ABC, abstractmethod, abstractproperty

class Transacao(ABC):
    @abstractmethod
    def registrar(self, Conta):
        pass

class Deposito(Transacao):
    def registrar(self, Conta, valor):
        pass
        #TODO implementar transação de depósito. valor deve ser privado

class Saque(Transacao):
    def registrar(self, Conta, valor):
        pass
        #TODO implementar transação de saque. valor deve ser privado

class Historico:
    def adicionar_transacao(self, Transacao):
        pass
        #TODO implementar histórico de transação



class Conta:
    def __init__(self, saldo, numero, agencia, cliente, Historico) -> None:
        self._saldo = saldo #float
        self._numero = numero #int
        self._agencia = agencia #str
        self._cliente = cliente #Cliente
        self._Historico = Historico #Historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        pass
        #TODO implementar função de criar nova conta

    def saldo(self) -> float:
        return self._saldo
    
    def sacar(self, valor) -> bool:
        pass
        #TODO implementar função de saque
    
    def depositar(self, valor) -> bool:
        pass
        #TODO implementar função de depósito
    
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        #_limite = float
        #_limite_saques = float
        pass
        #TODO implementar função de criar conta corrente



class Cliente:
    def __init__(self, endereco, contas) -> None:
        self._endereco = endereco
        self._contas = contas #lista que terá o tipo Conta

    def realizar_transacao(self, Conta, Transacao):
        pass

    def adicionar_conta(self, Conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento) -> None:
        super().__init__(endereco, contas)
        self._cpf = cpf #str
        self._nome = nome #str
        self._data_nascimento = data_nascimento #date


def main():
    pass

main()