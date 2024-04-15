class Pedido_restaurante:
	def __init__(self, pedido, totali, status_pedido, add, precoadd, totalf, statu):
		self.pedido = pedido
		self.totali = totali
		self.status_pedido = status_pedido
		self.add = add
		self.precoadd = precoadd
		self.totalf = totalf
		self.statu = statu
	def adicionar(self):
		return f"o seu pedido contém {self.pedido} no valor {self.totali}, porém você adicionou mais um item ao carrinho uma: {self.add}"
	def total(self):
		return f"o seu novo total a pagar é de {self.totalf}"
	def status(self):
		return f"seu status de pedido é {self.statu}"

if __name__ == "__main__":
	pedido1 = Pedido_restaurante("pizza", "30", "em processo", "H2O", "7", "37", "pago")

	print(pedido1.adicionar())
	print(pedido1.total())
	print(pedido1.status())