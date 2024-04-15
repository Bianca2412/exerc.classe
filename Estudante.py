class Estudante:
	def __init__(self, nome, idade, nota1, nota2, nota3, medias, statu):
		self.nome = nome
		self.idade = idade
		self.nota1 = nota1
		self.nota2 = nota2
		self.nota3 = nota3
		self.medias = medias
		self.statu = statu
	def media(self):
		return f"o aluno {self.nome} está com a média {self.medias}"
	def status(self):
		return f"o aluno está {self.statu}"

if __name__ == "__main__":
	aluno1 = Estudante("Pedro", "16", "10", "5", "7", "7,3", "Aprovado")

	print(aluno1.media())
	print(aluno1.status())