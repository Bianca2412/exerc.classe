class Livro:
	def __init__(self, titulo, autor, paginas, palavras, genero, ano, personagens):
		self.titulo = titulo
		self.autor = autor
		self.paginas = paginas
		self.palavras = palavras
		self.genero = genero
		self.ano = ano
		self.personagens = personagens
	def informacoes(self):
		return f"o livro {self.titulo} foi lançado em {self.ano} seu gênero é {self.genero} e seus personagens principais {self.personagens}"
	def total(self):
		return f"tem {self.paginas} páginas e tem aproximadamente {self.palavras} palavras"

if __name__ == "__main__":
	l1 = Livro("Eu e esse meu coração", "C. C. Hunter", "424", "150", "Ficção, Romance contemporâneo e Fantasia romântica", "2018", "Leah e Matt")

	print(l1.informacoes())
	print(l1.total())