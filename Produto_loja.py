class Produto_loja:
	def __init__(self, nome, preço, estoque, atual, lucro):
		self.nome = nome
		self.preço = preço
		self.estoque = estoque
		self.atual = atual
		self.lucro = lucro
	def atualizar(self):
		return f"atualizar o produto {self.nome} no estoque"
	def total(self):
		return f"{self.nome} no novo estoque: {self.atual}, tem um lucro de {self.lucro}"

if __name__ == "__main__":
	produto1 = Produto_loja("creme", "10", "5", "35", "350")

	print(produto1.atualizar())
	print(produto1.total())