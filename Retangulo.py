class Retangulo:
	def __init__(self, altura, largura, suaa, seup):
		self.altura = altura
		self.largura = largura
		self.suaa = suaa
		self.seup = seup
	def area(self):
		return f"a sua área é de: {self.suaa}"
	def perimetro(self):
		return f"seu perímetro é de: {self.seup}"

if __name__ == "__main__":
	retangulo1 = Retangulo("5", "10", "50", "30")

	print(retangulo1.area())
	print(retangulo1.perimetro())