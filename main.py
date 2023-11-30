from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

LIMITE_POR_SAQUE = 500
LIMITE_DE_SAQUES = 3

def verificar_ponto_flutuante(valor):
    try:
        float(valor)
        return True
    except:
        return False

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_completa = conta.depositar(self.valor)

        if transacao_completa:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_completa = conta.sacar(self.valor)

        if transacao_completa:
            conta.historico.adicionar_transacao(self)

class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if verificar_ponto_flutuante(valor):
            valor = float(valor)
            if valor > 0.0:
                self._saldo += valor
                print('Depósito realizado com sucesso')
                return True
            else:
                print('O valor depositado não pode ser menor ou igual a zero')
                return False
        else:
            print('O valor depositado deve estar no formato numérico correto')
            return False
        
    def sacar(self, valor):
        if verificar_ponto_flutuante(valor):
            valor = float(valor)
            if self._saldo >= valor:
                self._saldo -= valor
                print('Saque realizado com sucesso')
                return True
            else:
                print('O valor do saque deve ser menor ou igual que o saldo em conta')
                return False
        else:
            print('O valor sacado deve estar no formato numérico correto')
            return False
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=LIMITE_POR_SAQUE, limite_saques=LIMITE_DE_SAQUES):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques_realizados = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        if saques_realizados <= self.limite_saques:
            if verificar_ponto_flutuante(valor):
                if float(valor) <= self.limite:
                    super().sacar(valor)
                else:
                    print('Valor maior do que o limite por saque estabelecido!')
        else:
            print('Limite máximo de saques por dia alcançado!')
            return False