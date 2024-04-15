class Conta_bancaria:
	def __init__(self, numero_conta, saldo, titular, depositar, tirar, atual):
		self.numero_conta = numero_conta
		self.saldo = saldo
		self.titular = titular
		self.depositar = depositar
		self.tirar = tirar
		self.atual = atual
		
	def deposito(self):
		return f"{self.titular} fez um depósito de valor {self.depositar} da conta"
	def sacar(self):
		return f"{self.titular} Fez um saque de valor total da conta {self.tirar}"
	def saldo_atual(self):
		return f"{self.titular} seu saldo atual é de {self.atual}"
	
if __name__ == "__main__":
	conta1 = Conta_bancaria("1010", "500", "Lucas", "100", "150", "250")

	print(conta1.deposito())
	print(conta1.sacar())
	print(conta1.saldo_atual())