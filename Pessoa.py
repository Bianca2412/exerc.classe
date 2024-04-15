class Pessoa:
	def __init__(self, nome, idade, altura, pergunta, pessoa):
		self.nome = nome
		self.idade = idade
		self.altura = altura
		self.pergunta = pergunta
		self.pessoa = pessoa
	def definir(self):
		return f"meu é {self.nome} tenho {self.idade}"
	def obter(self):
		return f"{self.pergunta}?"
	def cumprimentar(self, mensagem):
		return f"{self.nome} está falando com {self.pessoa}: {mensagem}"

if __name__ == "__main__":
	pessoa1 = Pessoa("Gabriel", "18", "1,79", "qual é o seu nome", "Caio")

	print(pessoa1.definir())
	print(pessoa1.obter())
	print(pessoa1.cumprimentar("prazer em conhecer você."))